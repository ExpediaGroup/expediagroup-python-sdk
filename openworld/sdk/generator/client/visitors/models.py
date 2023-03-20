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
from collections import OrderedDict
from pathlib import Path
from typing import Union

from datamodel_code_generator.imports import Imports
from datamodel_code_generator.model import DataModel, DataModelFieldBase
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
def collect_imports(sorted_models, parser):
    imports = Imports()
    imports.update(parser.imports)

    for model in sorted_models.values():
        for import_ in model.imports:
            imports.append(import_)
        for field in model.fields:
            for field_import in field.imports:
                imports.append(field_import)

    return imports


def parse_children(models: collections.defaultdict[str, DataModel]) -> collections.defaultdict[str, list[DataModel]]:
    r"""Parses models that have parents other than `Enum` and `BaseModel`.

    :param models: All models parsed from the `OpenApiParser`.
    :type models: defaultdict[str, DataModel]

    :returns: A dictionary of models which are children to other models.
    :rtype: defaultdict[str, list[DataModel]]
    """
    children: collections.defaultdict[str, list[DataModel]] = collections.defaultdict(list)
    ignore_parents = ["BaseModel", "Enum"]
    for model_key in models.keys():
        model = models[model_key]

        if model.base_class in ignore_parents:
            continue

        parent = models[model.base_class]
        children[parent.class_name].append(model)

    return children


def set_datatype(old: Union[DataType, str], current: DataType, new: DataType) -> DataType:
    r"""Takes a datatype object, and converts it into another datatype.

    :param old: The original datatype.
    :type old: Union[DataType, str].

    :param current: The current datatype.
    :type current: DataType.

    :param new: The new datatype to use.
    :type new: DataType

    :returns: The new datatype after transformation.
    :rtype: DataType
    """
    if isinstance(old, DataType):
        old = old.type_hint

    if bool(len(current.data_types)):
        for index, datatype in enumerate(current.data_types):
            if datatype.type_hint == old:
                current.data_types[index] = new

    else:
        type_hint = current.type_hint
        if current.is_optional:
            type_hint = type_hint.removeprefix("Optional[").removesuffix("]")
        if type_hint == old:
            new.is_dict = current.is_dict
            new.is_list = current.is_list
            new.is_optional = current.is_optional
            current = new

    return current


def update_field_datatype(field: DataModelFieldBase, old_type_datamodel: DataModel, new_datatype: DataType) -> DataModelFieldBase:
    r"""Updates the datatype of a field.

    :param field: The field to update its datatype.
    :type field: DataModelFieldBase.

    :param old_type_datamodel: The original field datatype model.
    :type old_type_datamodel: DataModel.

    :param new_datatype: The new datatype to use for the field.
    :type new_datatype: DataType.

    :returns: The field with updated datatype.
    :rtype: DataModelFieldBase
    """
    if field.type_hint and old_type_datamodel.class_name in field.type_hint:
        if bool(len(field.data_type.data_types)):
            for index in range(len(field.data_type.data_types)):
                datatype = field.data_type.data_types[index]
                field.data_type.data_types[index] = set_datatype(old=old_type_datamodel.class_name, current=datatype, new=new_datatype)
        else:
            field.data_type = set_datatype(old_type_datamodel.class_name, field.data_type, new_datatype)

    return field


def cleanup_root_models(models: collections.defaultdict[str, DataModel]):
    root_models = [
        models[model_key]
        for model_key in models.keys()
        if ((len(models[model_key].fields) == 1) and models[model_key].fields[0].name == "__root__") or isinstance(models[model_key], CustomRootType)
    ]

    for root_model in root_models:
        root_data_type = root_model.fields[0].data_type

        for model_key in models.keys():
            model = models[model_key]
            if model.class_name == root_model.class_name:
                continue
            for field_index in range(len(models[model_key].fields)):
                models[model_key].fields[field_index] = update_field_datatype(
                    field=models[model_key].fields[field_index], old_type_datamodel=root_model, new_datatype=root_data_type
                )
    return models


def parse_datamodels(parser: OpenAPIParser) -> collections.defaultdict[str, DataModel]:
    r"""Parses all models that are of type `DataModel`.

    :param parser: The parser holding parsed results.
    :type parser: OpenAPIParser
    """
    models: collections.defaultdict[str, DataModel] = collections.defaultdict(lambda: None)

    for model in [_ for _ in parser.results if isinstance(_, DataModel)]:
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
    type_does_exist = bool(len([_ for _ in child.fields if _.name == "type"]))
    type_attribute = [_ for _ in parent.fields if _.name == "type"][0].copy()
    parent_fields = [_ for _ in parent.fields if _.name != "type" and _.name != "__root__"]

    if not type_does_exist:
        child.fields.append(type_attribute)
    child.fields = parent_fields + child.fields

    for field in child.fields:
        if field.name != "type":
            continue

        literal = DataType(type=f'Literal["{child.class_name}"')

        field.data_type = DataType(data_types=[literal])
        break

    return child


def refactor_child(child: DataModel, models: collections.defaultdict[str, DataModel]):
    child = copy_parent_fields_to_child(parent=models[child.base_class], child=child)
    child.base_classes.clear()
    child.set_base_class()
    return child


def refactor_parent(parent: DataModel, children: list[DataModel]) -> DataModel:
    type_field = [_ for _ in parent.fields if _.name == "type"][0]
    parent.fields.clear()

    type_field.name = "__root__"

    data_types = [DataType(type=child.class_name, reference=child.reference) for child in children]

    type_field.data_type = DataType(data_types=data_types)

    type_field.default = "Field(None, discriminator='type')"
    type_field.required = True
    type_field.use_field_description = False

    parent.fields.append(type_field)
    return parent


def post_process_models_parent_children(parser: OpenAPIParser):
    r"""Method to post process models whenever `type` attribute is present, move parent model attributes to children,
    add one `__root__` attribute in each parent, and replace type hint of `type` with Literal type-hint.

    :param parser: The OpenApiParser which holds all the results.
    """

    models = parse_datamodels(parser)
    children = parse_children(models)

    for parent_key in children.keys():
        parent = models[parent_key]

        # If parent has no `type` attribute, then there is no discriminator.
        has_type_attribute = False
        for field in parent.fields:
            has_type_attribute = has_type_attribute or field.name == "type"
        if not has_type_attribute:
            # Skip model due to lack of discriminator, this also covers for __root__ model case.
            continue

        for child_index in range(len(children[parent.class_name])):
            child = refactor_child(child=children[parent.class_name][child_index], models=models)
            models[child.class_name] = child

        parent = refactor_parent(parent, children[parent.class_name])
        models[parent.class_name] = parent

    models = cleanup_root_models(cleanup_root_models(models))
    for model_index in range(len(parser.results)):
        if isinstance(parser.results[model_index], DataModel):
            model = parser.results[model_index]

            if not model or not model.class_name or not model.base_class:
                continue

            parser.results[model_index] = models[model.class_name]


def get_models(parser: OpenAPIParser, model_path: Path) -> dict[str, object]:
    # TODO: Do the same post-processing to operations `return-type`
    post_process_models_parent_children(parser)
    _, sorted_models, __ = sort_data_models(unsorted_data_models=[_ for _ in parser.results if isinstance(_, DataModel)])

    return {"models": sorted_models.values(), "model_imports": collect_imports(sorted_models, parser)}


visit: Visitor = get_models
