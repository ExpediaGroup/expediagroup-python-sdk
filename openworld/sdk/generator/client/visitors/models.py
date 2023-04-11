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
import dataclasses
from pathlib import Path

from datamodel_code_generator.imports import Imports
from datamodel_code_generator.model import DataModel
from datamodel_code_generator.model.pydantic import CustomRootType
from datamodel_code_generator.parser.base import sort_data_models
from datamodel_code_generator.types import DataType
from fastapi_code_generator.parser import OpenAPIParser
from fastapi_code_generator.visitor import Visitor


@dataclasses.dataclass
class Alias:
    r"""A dataclass representing an Alias datatype.

    Attributes:
        parent_classname(str): Classname of a model that is a parent to a list of children models.
        children_classnames(list[str]): A list of models that are children of a given parent model.
        order(int): A value used in sorting alias position among other aliases, depending on its position in the
        inheritance hierarchy.
    """
    parent_classname: str
    children_classnames: list[str]
    order: int = 1

    def __str__(self):
        return f"{self.parent_classname} = Union[{','.join(self.children_classnames)}]"


def collect_imports(sorted_models: dict[str, DataModel], parser: OpenAPIParser) -> Imports:
    r"""Collects any needed imports for models that are missing.

    Args:
        sorted_models(dict[str, DataModel]): Models sorted depending on their dependency on each other.
        parser(OpenApiParser): The parser holding parsed results.

    Returns:
        Imports: Missing imports needed to add after postprocessing.
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


def parse_children(models: dict[str, DataModel]) -> dict[str, list[DataModel]]:
    r"""Parses models that have parents other than `Enum` and `BaseModel`.

    Args:
        models(dict[str, DataModel]): All models parsed from the `OpenApiParser`.

    Returns:
        dict[str, list[DataModel]]: A dictionary of models which are children to other models.
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

    Args:
        parser(OpenAPIParser): The OpenApiParser which holds all the results.
    """
    models: collections.defaultdict[str, DataModel] = collections.defaultdict(lambda: None)

    for model in [result for result in parser.results if isinstance(result, DataModel)]:
        if (not model) or (not model.class_name) or (not model.base_class):
            continue
        models[model.class_name] = model
    return models


def copy_parent_fields_to_child(parent: DataModel, child: DataModel) -> DataModel:
    r"""Copies all fields present in a parent model to a child, except for the fields `type` and `__root__`. Also adds
    any needed `__root__` field and `Literal` type

    Args:
        parent(DataModel): Parent model.
        child(DataModel): Child model.

    Returns:
        DataModel: Child model with its parent's attributes added to its attributes.
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

    Args:
        parent(DataModel): The parent model.
        children(list[DataModel]): Children of a given parent model.

    Returns:
        DataModel: Refactored parent model.
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
    r"""Checks if a model has a `type` attribute.

    Args:
        model(DataModel): Model to be checked.

    Returns:
        bool: rue if model has a `type` attribute, False otherwise.
    """
    for field in model.fields:
        if field.name == "type":
            return True
    return False


def is_parent_processed(parent: DataModel, children: list[DataModel]) -> bool:
    """Checks if a parent model has been post processed before, in other words, it has children models, and one `__root__` field.

    Args:
        parent(DataModel): A model that is a parent for a set of children models by inheritance.
        children(list[DataModel]): Children of a given parent model.

    Returns:
        bool: True if parent is processed, False otherwise.
    """

    return (
        len(parent.fields) == 1
        and (parent.fields[0].name == "__root__" or isinstance(parent, CustomRootType))
        and len([child.class_name for child in children if child.class_name in parent.fields[0].type_hint])
    )


def get_flattened_children(parent: DataModel, parent_children: dict[str, list[DataModel]]) -> list[DataModel]:
    r"""If a parent has a `type` attribute, it will be considered as discriminator,and parent attributes will be copied to child.

    Args:
        parent(DataModel): Parent model in inheritance relationship.
        parent_children(dict[str, list[DataModel]): Mapping of parent classname to its children models.

    Returns:
        list[DataModel]]: Flattened child, a child that holds all its parent's attributes, and now has no need to inherit from its parent.
    """

    flattened_children = []

    for child in parent_children[parent.class_name]:
        flattened_children += (
            get_flattened_children(parent=copy_parent_fields_to_child(parent, child), parent_children=parent_children) + [child]
            if parent_children[child.class_name]
            else [copy_parent_fields_to_child(parent, child)]
        )

    return flattened_children


def get_child_parent_classnames(parent_children: dict[str, list[DataModel]]) -> dict[str, str]:
    r"""Generates a mapping of child-parent classnames.

    Args:
        parent_children(dict[str, list[DataModel]): Mapping of parent classname to its children models.

    Returns:
        dict[str, str]: A mapping of child-parent classnames
    """
    child_parent_classnames: dict[str, str] = collections.defaultdict(str)

    for parent_classname, children in parent_children.items():
        for child in children:
            if child.class_name != parent_classname:
                child_parent_classnames[child.class_name] = parent_classname

    return child_parent_classnames


def get_highest_ancestor_classname(model_classname: str, child_parent_classnames: dict[str, str]) -> str:
    r"""Parses the highest ancestor classname of a model.

    Args:
        model_classname(str): Model's classname.
        child_parent_classnames(dict[str, str]): A mapping of classnames for any child and its parent.

    Returns:
        str: Highest ancestor classname.
    """
    highest_ancestor_classname = model_classname
    while bool(child_parent_classnames[highest_ancestor_classname]):
        highest_ancestor_classname = child_parent_classnames[highest_ancestor_classname]
    return highest_ancestor_classname


def flatten_inheritance_hierarchy_tree(
    models: dict[str, DataModel], parent_children: dict[str, list[DataModel]]
) -> tuple[dict[str, DataModel], dict[str, list[DataModel]]]:
    r"""Flattens inheritance relationship in the inheritance tree of models, by taking every non-leaf node
    (aka model that is a child, and is parent to no children), and transforming each one into an alias.

    Transformation into an alias includes processing each non-leaf model by transforming it into a `__root__` model,
    then, each will be parsed as aliases in `get_sorted_aliases` method.

    Args:
        models(dict[str, DataModel]): A mapping of classnames and parsed models.
        parent_children(dict[str, list[DataModel]): Mapping of parent classname to its children models.

    Returns:
        tuple[dict[str, DataModel], dict[str, list[DataModel]]]: Same params are returned after the inheritance
        hierarchy tree have been flattened.
    """
    flattened_parent_children: dict[str, list[DataModel]] = collections.defaultdict(list)
    is_model_processed: dict[str, bool] = collections.defaultdict(bool)
    child_parent_classnames: dict[str, str] = get_child_parent_classnames(parent_children)

    for parent_classname in list(parent_children.keys()):
        highest_ancestor_classname = get_highest_ancestor_classname(parent_classname, child_parent_classnames)
        highest_ancestor = models[highest_ancestor_classname]

        # If parent has no `type` attribute, then there is no discriminator.
        if not has_type_attribute(highest_ancestor):
            # Skip model due to lack of discriminator, this also covers for __root__ model case.
            continue

        if is_model_processed[highest_ancestor_classname]:
            if parent_children[parent_classname]:
                models[parent_classname] = refactor_parent(models[parent_classname], parent_children[parent_classname])
            continue

        flattened_parent_children[highest_ancestor_classname] = get_flattened_children(highest_ancestor, parent_children)

        models[highest_ancestor_classname] = refactor_parent(highest_ancestor, parent_children[highest_ancestor_classname])

        for child in flattened_parent_children[highest_ancestor_classname]:
            if child.base_classes != highest_ancestor_classname and parent_children[child.base_class]:
                models[child.base_class] = refactor_parent(models[child.base_class], parent_children[child.base_class])

        is_model_processed[highest_ancestor_classname] = True

        for child_index, child in enumerate(flattened_parent_children[highest_ancestor_classname]):
            is_model_processed[child.class_name] = True
            flattened_parent_children[highest_ancestor_classname][child_index] = child

            models[child.class_name] = child
            models[highest_ancestor_classname] = refactor_parent(highest_ancestor, flattened_parent_children[highest_ancestor_classname])

    return models, flattened_parent_children


def post_process_models_parent_children(parser: OpenAPIParser):
    r"""Method to post process models whenever `type` attribute is present, move parent model attributes to children,
    add one `__root__` attribute in each parent, and replace type hint of `type` with Literal type-hint.

    Args:
        parser(OpenAPIParser): The OpenApiParser which holds all the results.
    """

    models = parse_datamodels(parser)

    models, parent_children = flatten_inheritance_hierarchy_tree(models=models, parent_children=parse_children(models))

    for index, model in enumerate(parser.results):
        if isinstance(parser.results[index], DataModel):
            if not model or not model.class_name or not model.base_class:
                continue

            parser.results[index] = models[model.class_name]


def parse_processed_parent_children_classnames(models: dict[str, DataModel]) -> dict[str, list[str]]:
    r"""Parses processed children and their parents

    Args:
        models(dict[str, DataModel]): A mapping of classnames and parsed models.

    Returns:
        dict[str, list[str]]: A mapping of processed parent classname, and its children classnames.
    """
    processed_parent_children_classnames: dict[str, list[str]] = collections.defaultdict(list)

    for parent_classname, children in parse_children(models).items():
        parent = models[parent_classname]
        if is_parent_processed(parent, children):
            processed_parent_children_classnames[parent_classname] += [child.class_name for child in children]

    return processed_parent_children_classnames


def get_sorted_aliases(processed_parent_children_classnames: dict[str, list[str]]) -> list[Alias]:
    r"""Generates a list of aliases, sorted based on their dependency/inheritance tree.

    Args:
        processed_parent_children_classnames(dict[str, list[str]]): A mapping for processed parent models classnames,
        and their children classnames.

    Returns:
        list[Alias]: A list of aliases, sorted based on their dependency/inheritance tree.
    """
    aliases: list[Alias] = []

    # A memo to record/remember the order of aliases
    alias_order: dict[str, int] = collections.defaultdict(int)

    is_aliased: dict[str, bool] = collections.defaultdict(bool)

    current_order = 1
    for parent_classname, children_classnames in processed_parent_children_classnames.items():
        is_aliased[parent_classname] = True

        # If the current parent being aliased has been encountered before (as a child),
        # then the order of the current alias should come before any other alias that
        # depends on it.
        order = current_order if not alias_order[parent_classname] else min(current_order - 1, -current_order)

        alias = Alias(parent_classname=parent_classname, children_classnames=children_classnames, order=order)
        aliases.append(alias)

        alias_order.update(
            [(child_classname, alias.order) for child_classname in alias.children_classnames if not alias_order[child_classname]]
            + [(parent_classname, alias.order)]
        )

        current_order += 1

    return sorted(aliases, key=lambda a: a.order)


def get_models(parser: OpenAPIParser, model_path: Path) -> dict[str, object]:
    r"""A visitor that exposes models and related data to `jinja2` templates.

    Args:
        parser(OpenAPIParser): The OpenApiParser which holds all the results.
        model_path(Path): Models path.

    Returns:
        dict[str, object]: Data to be exposed to `jinja2` templates.
    """

    post_process_models_parent_children(parser)
    _, sorted_models, __ = sort_data_models(unsorted_data_models=[result for result in parser.results if isinstance(result, DataModel)])

    processed_parent_children_classnames = parse_processed_parent_children_classnames(parse_datamodels(parser))

    is_aliased: dict[str, bool] = collections.defaultdict(bool, {parent_classname: True for parent_classname in processed_parent_children_classnames.keys()})

    return {
        "models": sorted_models.values(),
        "model_imports": collect_imports(sorted_models, parser),
        "aliases": get_sorted_aliases(processed_parent_children_classnames),
        "is_aliased": is_aliased,
    }


visit: Visitor = get_models
