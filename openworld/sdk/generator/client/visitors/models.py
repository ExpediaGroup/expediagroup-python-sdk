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
from datamodel_code_generator.parser.base import sort_data_models
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


def parse_highest_ancestor(model: DataModel, models: dict[str, DataModel]) -> DataModel:
    current_model = model
    while current_model.base_class not in ["BaseModel", "Enum"]:
        current_model = models[current_model.base_class]
    return current_model


def get_is_parent_model_helper(models: dict[str, DataModel]) -> dict[str, bool]:
    ignore_parents = ["BaseModel", "Enum"]

    return collections.defaultdict(
        bool,
        {model.base_class: (model.base_class not in ignore_parents) and has_type_attribute(parse_highest_ancestor(model, models)) for model in models.values()},
    )


def get_is_highest_parent_helper(models: dict[str, DataModel]) -> dict[str, bool]:
    is_parent_model = get_is_parent_model_helper(models)

    return collections.defaultdict(
        bool, {model.class_name: not is_parent_model[model.base_class] and is_parent_model[model.class_name] for model in models.values()}
    )


def parse_descendants_classnames(highest_parent_classname: str, models: dict[str, DataModel]) -> list[str]:
    children: list[str] = []

    dfs_stack = [highest_parent_classname]
    # Simple iterative depth-first search to get all descendants of a given parent.
    while dfs_stack:
        classname = dfs_stack.pop()

        if classname != highest_parent_classname:
            children.append(classname)

        dfs_stack += [model.class_name for model in models.values() if model.base_class == classname]

    return children


def parse_aliases(models: dict[str, DataModel]) -> list[Alias]:
    r"""Generates a list of aliases, sorted based on their dependency/inheritance tree.

    Args:
        processed_parent_children_classnames(dict[str, list[str]]): A mapping for processed parent models classnames,
        and their children classnames.

    Returns:
        list[Alias]: A list of aliases, sorted based on their dependency/inheritance tree.
    """
    aliases: list[Alias] = []
    is_highest_parent: dict[str, bool] = get_is_highest_parent_helper(models)

    for key, value in is_highest_parent.items():
        if not value:
            continue

        aliases.append(Alias(parent_classname=key, children_classnames=parse_descendants_classnames(key, models)))

    return aliases


def get_models(parser: OpenAPIParser, model_path: Path) -> dict[str, object]:
    r"""A visitor that exposes models and related data to `jinja2` templates.

    Args:
        parser(OpenAPIParser): The OpenApiParser which holds all the results.
        model_path(Path): Models path.

    Returns:
        dict[str, object]: Data to be exposed to `jinja2` templates.
    """

    _, sorted_models, __ = sort_data_models(unsorted_data_models=[result for result in parser.results if isinstance(result, DataModel)])

    models: dict[str, DataModel] = parse_datamodels(parser)

    aliases = parse_aliases(models)

    for alias in aliases:
        print(alias.parent_classname, alias.children_classnames)

    is_aliased = collections.defaultdict(bool, {alias.parent_classname: True for alias in aliases})

    highest_parent: dict[str, str] = dict()
    for alias in aliases:
        for child in alias.children_classnames:
            highest_parent[child] = alias.parent_classname
    print(f"Parent Models Are: {get_is_parent_model_helper(models)}")
    return {
        "models": sorted_models.values(),
        "model_imports": collect_imports(sorted_models, parser),
        "aliases": aliases,
        "is_aliased": is_aliased,
        "is_parent_model": get_is_parent_model_helper(models),
        "is_highest_parent": get_is_highest_parent_helper(models),
        "highest_parent": highest_parent,
    }


order: int = 2
visit: Visitor = get_models
