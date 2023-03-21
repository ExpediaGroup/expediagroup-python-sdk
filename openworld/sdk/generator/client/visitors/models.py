# Copyright 2022 Expedia, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import collections
from pathlib import Path

from datamodel_code_generator.imports import Imports
from datamodel_code_generator.model import DataModel
from datamodel_code_generator.model.pydantic import CustomRootType
from datamodel_code_generator.parser.base import sort_data_models
from datamodel_code_generator.types import DataType
from fastapi_code_generator.parser import OpenAPIParser
from fastapi_code_generator.visitor import Visitor


def collect_imports(sorted_models: dict[str, DataModel], parser: OpenAPIParser) -> Imports:
    r"""Collects any needed imports for models that are missing.

    :param sorted_models: Models sorted depending on their dependency on each other.
    :type sorted_models: dict[str, DataModel]

    :param parser: The parser holding parsed results.
    :type parser: OpenAPIParser

    :returns: Missing imports needed to add after postprocessing.
    :rtype: Imports
    """
    imports = Imports()
    imports.update(parser.imports)

    for model in sorted_models.values():
        for import_ in model.imports:
            imports.append(import_)
        for field in model.fields:
            for field_import in field.imports:
                imports.append(field_import)

    return imports


def parse_children(models: dict[str, DataModel]) -> collections.defaultdict[str, list[DataModel]]:
    r"""Parses models that have parents other than `Enum` and `BaseModel`.

    :param models: All models parsed from the `OpenApiParser`.
    :type models: defaultdict[str, DataModel]

    :returns: A dictionary of models which are children to other models.
    :rtype: defaultdict[str, list[DataModel]]
    """
    parent_children: collections.defaultdict[str, list[DataModel]] = collections.defaultdict(list)
    ignore_parents = ["BaseModel", "Enum"]
    for model in models.values():
        if model.base_class in ignore_parents:
            continue

        parent = models[model.base_class]
        parent_children[parent.class_name].append(model)

    return parent_children


def parse_datamodels(parser: OpenAPIParser) -> collections.defaultdict[str, DataModel]:
    r"""Parses all models that are of type `DataModel`.

    :param parser: The parser holding parsed results.
    :type parser: OpenAPIParser
    """
    models: collections.defaultdict[str, DataModel] = collections.defaultdict(lambda: None)

    for model in [result for result in parser.results if isinstance(result, DataModel)]:
        if (not model) or (not model.class_name) or (not model.base_class):
            continue
        models[model.class_name] = model
    return models


def copy_parent_fields_to_child(parent: DataModel, child: DataModel):
    r"""Copies all fields present in a parent model to a child, except for the fields `type` and `__root__`. Also adds
    any needed `__root__` field and `Literal` type

    :param parent: Parent model.
    :type parent: DataModel.

    :param child: Child model.
    :type child: DataModel
    """
    type_exists_in_child = bool([field for field in child.fields if field.name == "type"])

    type_attribute_in_parent = [field for field in parent.fields if field.name == "type"]
    if type_attribute_in_parent:
        type_attribute_in_parent = type_attribute_in_parent[0].copy()

    parent_fields = [field for field in parent.fields if field.name != "type" and field.name != "__root__"]

    if not type_exists_in_child:
        child.fields.append(type_attribute_in_parent)
    child.fields = parent_fields + child.fields

    for field in child.fields:
        if field.name != "type":
            continue

        literal = DataType(type=f'Literal["{child.class_name}"]')

        field.data_type = DataType(data_types=[literal])
        break

    return child


def refactor_parent(parent: DataModel, children: list[DataModel]) -> DataModel:
    r"""Finds if parent has type attribute, removes all fields from it, and replaces them with one `__root__` attribute.

    :param parent: The parent model.
    :type parent: DataModel.

    :param children: Children of a given parent model.
    :type children: list[DataModel].

    :returns: Refactored parent model.
    :rtype: DataModel.
    """
    type_field = [field for field in parent.fields if field.name == "type"]
    if not type_field:
        return parent

    type_field = type_field[0]

    parent.fields.clear()

    type_field.name = "__root__"

    data_types = [DataType(type=child.class_name, reference=child.reference) for child in children]

    type_field.data_type = DataType(data_types=data_types)

    type_field.default = "Field(None, discriminator='type')"
    type_field.required = True
    type_field.use_field_description = False

    parent.fields.append(type_field)
    return parent


def has_type_attribute(model: DataModel) -> bool:
    for field in model.fields:
        if field.name == "type":
            return True
    return False


def is_parent_processed(parent: DataModel, children: list[DataModel]):
    """Checks if a parent model has been post processed before, in other words, it has children models, and one `__root__` field.

    :param parent: Parent model.
    :type parent: DataModel.

    :param children: Children of a given parent model.
    :type children: list[DataModel].
    """
    return (
        len(parent.fields) == 1
        and (parent.fields[0].name == "__root__" or isinstance(parent, CustomRootType))
        and len([child.class_name for child in children if child.class_name in parent.fields[0].type_hint]) == len(children)
    )


def post_process_models_parent_children(parser: OpenAPIParser):
    r"""Method to post process models whenever `type` attribute is present, move parent model attributes to children,
    add one `__root__` attribute in each parent, and replace type hint of `type` with Literal type-hint.

    :param parser: The OpenApiParser which holds all the results.
    """

    models = parse_datamodels(parser)
    parent_children = parse_children(models)

    for parent, children in parent_children.items():
        parent = models[parent]

        # If parent has no `type` attribute, then there is no discriminator.
        if not has_type_attribute(parent):
            # Skip model due to lack of discriminator, this also covers for __root__ model case.
            continue

        for child_index in range(len(children)):
            child = copy_parent_fields_to_child(parent=parent, child=parent_children[parent.class_name][child_index])
            models[child.class_name] = child

        parent = refactor_parent(parent, parent_children[parent.class_name])
        models[parent.class_name] = parent

    for index, model in enumerate(parser.results):
        if isinstance(parser.results[index], DataModel):
            if not model or not model.class_name or not model.base_class:
                continue

            parser.results[index] = models[model.class_name]


def parse_processed_parent_children_classnames(models: dict[str, DataModel]) -> dict[str, list[str]]:
    r"""Parses processed children and their parents

    :param models: Parsed datamodels.
    :type models: dict[str, DataModel].
    """
    processed_parent_children_classnames: dict[str, list[str]] = collections.defaultdict(list)

    for parent_classname, children in parse_children(models).items():
        parent = models[parent_classname]
        if is_parent_processed(parent, children):
            processed_parent_children_classnames[parent_classname] = [child.class_name for child in children]

    return processed_parent_children_classnames


def get_models(parser: OpenAPIParser, model_path: Path) -> dict[str, object]:
    r"""A visitor that exposes models and related data to `jinja2` templates.

    :param parser: The parser holding results of parsing the OpenApi specification file.
    :type parser: OpenAPIParser

    :param model_path: Models path.
    :type model_path: Path

    :returns: Data to be exposed to `jinja2` templates.
    :rtype: dict[str, object]
    """
    # TODO: Do the same post-processing to operations `return-type`
    post_process_models_parent_children(parser)
    _, sorted_models, __ = sort_data_models(unsorted_data_models=[result for result in parser.results if isinstance(result, DataModel)])
    processed_parent_children_classnames = parse_processed_parent_children_classnames(parse_datamodels(parser))

    is_rendered: dict[str, bool] = dict()
    for parent_classname, children_classnames in processed_parent_children_classnames.items():
        is_rendered[parent_classname] = False
        for child_classname in children_classnames:
            is_rendered[child_classname] = False

    return {
        "models": sorted_models.values(),
        "model_imports": collect_imports(sorted_models, parser),
        "processed_parent_children_classnames": processed_parent_children_classnames,
        "is_rendered": is_rendered,
        "all_children_rendered_helper": collections.defaultdict(bool),
    }


visit: Visitor = get_models
