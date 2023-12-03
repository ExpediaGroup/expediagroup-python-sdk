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
from collections.abc import Callable
from pathlib import Path
from typing import Any

from datamodel_code_generator.imports import Imports
from datamodel_code_generator.model import DataModel
from datamodel_code_generator.parser.base import sort_data_models
from datamodel_code_generator.types import DataType
from fastapi_code_generator.parser import OpenAPIParser, Operation
from fastapi_code_generator.visitor import Visitor
from pydantic import BaseModel, Extra, Field, parse_obj_as

GENERIC_TYPES: list[str] = ["BaseModel", "Enum"]
DISCRIMINATOR: str = "discriminator"


class Discriminator(BaseModel, extra=Extra.forbid, smart_union=True):
    property_name: str = Field(alias="propertyName")
    mapping: dict[str, str] = Field(default=None)
    owner: str = Field(default=None)


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


def parse_children_classnames(parent_classname: str, models: dict[str, DataModel]) -> list[str]:
    r"""Parses children classnames of a given parent.

    Args:
        parent_classname(str): Parent model classname.
        models(dict[str, DataModel]): A mapping for models, and their classnames as keys.

    Returns:

    """
    children = list(filter(lambda model: model.base_class == parent_classname, models.values()))
    return [child.class_name for child in children]


def parse_raw_discriminator(owner: str, raw_discriminator: dict[str, str], models: dict[str, DataModel]) -> Discriminator:
    r"""Parses discriminator object from its raw representation parsed from the spec.

    Args:
        owner(str): Owner model of the discriminator, aka parent.
        raw_discriminator(dict[str, str]): Raw discriminator object.
        models(dict[str, DataModel]): A mapping for models, and their classnames as keys.

    Returns:

    """
    discriminator: Discriminator = parse_obj_as(Discriminator, {**raw_discriminator, "owner": owner})

    if not discriminator.mapping:
        discriminator.mapping = {
            child_classname: child_classname for child_classname in parse_children_classnames(parent_classname=discriminator.owner, models=models)
        }

    return discriminator


def parse_discriminators(parser: OpenAPIParser, models: dict[str, DataModel]) -> list[Discriminator]:
    r"""Parses `Discriminator` objects from specs.

    Args:
        parser(OpenAPIParser): The OpenApiParser which holds all the results.
        models(dict[str, DataModel]): A mapping for models, and their classnames as keys.

    Returns:

    """
    discriminators: list[Discriminator] = []

    for model in models.values():
        if not (model.reference and model.reference.path and parse_children_classnames(parent_classname=model.class_name, models=models)):
            continue

        raw_model = parser.get_ref_model(model.reference.path)

        if not raw_model or DISCRIMINATOR not in raw_model.keys():
            continue

        discriminator: Discriminator = parse_raw_discriminator(owner=model.class_name, raw_discriminator=raw_model[DISCRIMINATOR], models=models)

        for key, value in discriminator.mapping.items():
            # This might happen in case a reference to the model in schemas section is
            # used instead of the classname of the model itself.
            # Example: `#/components/schemas/Hotel` instead of just `Hotel`.
            if value.strip().startswith("#/"):
                discriminator.mapping[key] = value.rsplit("/", 1).pop()

        discriminator.owner = model.class_name

        discriminators.append(discriminator)

    return discriminators


def apply_discriminators_to_models(discriminators: list[Discriminator], models: dict[str, DataModel]) -> None:
    r"""Adds discriminator attributes & constraints to all models that inherit a discriminator from their parent.

    Args:
        discriminators(list[Discriminator]): List of parsed discriminator objects.
        models(dict[str, DataModel]): A mapping for models, and their classnames as keys.
    """
    for discriminator in discriminators:
        parent: DataModel = models[discriminator.owner]

        for discriminator_value, discriminated_model_classname in discriminator.mapping.items():
            discriminator_field = list(filter(lambda f: f.name == discriminator.property_name, parent.fields))

            if len(discriminator_field) != 1:
                continue

            cloned_discriminator_field = discriminator_field.pop().copy()
            literal = DataType(type=f"Literal['{discriminator_value}']")

            cloned_discriminator_field.default = f"'{discriminator_value}'"
            cloned_discriminator_field.required = True
            cloned_discriminator_field.has_default = True
            cloned_discriminator_field.data_type = DataType(data_types=[literal])

            models[discriminated_model_classname].fields.append(cloned_discriminator_field)


def parse_sorted_aliases(models: dict[str, DataModel], discriminators: list[Discriminator]) -> list[Alias]:
    r"""Generates a list of aliases, sorted based on their dependency.

    Args:
        discriminators(list[Discriminator]): List of parsed discriminator objects.
        models(dict[str, DataModel]): A mapping for models, and their classnames as keys.

    Returns:
        list[Alias]: A list of aliases, sorted based on their dependency/inheritance tree.
    """
    aliases: list[Alias] = []

    # A memo to record/remember the order of aliases
    alias_order: dict[str, int] = collections.defaultdict(int)
    current_order: int = 1

    for parent_classname in [discriminator.owner for discriminator in discriminators]:
        # If the current parent being aliased has been encountered before (as a child),
        # then the order of the current alias should come before any other alias that
        # depends on it.
        order = current_order if not alias_order[parent_classname] else min(current_order - 1, -current_order)

        alias: Alias = Alias(
            parent_classname=parent_classname, children_classnames=parse_children_classnames(parent_classname=parent_classname, models=models), order=order
        )
        alias.children_classnames.append(f"{alias.parent_classname}Generic")

        aliases.append(alias)

        alias_order.update(
            [(child_classname, alias.order) for child_classname in alias.children_classnames if not alias_order[child_classname]]
            + [(parent_classname, alias.order)]
        )

        current_order += 1

    return sorted(aliases, key=lambda alias_: alias_.order)


def set_other_responses_models(operations: list[Operation]):
    ok_status_code_range = [code for code in range(200, 300)]
    for index, operation in enumerate(operations):
        error_responses: dict[int, Any] = {
            int(code): response for code, response in operation.additional_responses.items() if int(code) not in ok_status_code_range
        }

        operations[index].error_responses = error_responses


def get_error_models(parser: OpenAPIParser) -> list:
    error_models: set[str] = set()
    for response in list(map(lambda operation: operation.error_responses, parser.operations.values())):
        for model in response.values():
            error_models.add(model["model"])
    return list(error_models)


def delete_root_models(models: dict[str, DataModel]):
    """
    Deletes root models from a dictionary of DataModel objects.

    Args:
        models (dict[str, DataModel]): A dictionary containing DataModel objects, where the keys are the class names.

    """
    is_root_model: Callable = lambda model: len(model.fields) == 1 and not model.fields[0].name
    root_models_classnames: list[str] = list(map(lambda model: model.class_name, filter(is_root_model, models.values())))

    for root_model_classname in root_models_classnames:
        models.pop(root_model_classname)


def get_models(parser: OpenAPIParser, model_path: Path) -> dict[str, object]:
    r"""A visitor that exposes models and related data to `jinja2` templates.

    Args:
        parser(OpenAPIParser): The OpenApiParser which holds all the results.
        model_path(Path): Models path.

    Returns:
        dict[str, object]: Data to be exposed to `jinja2` templates.
    """
    models: dict[str, DataModel] = parse_datamodels(parser)
    delete_root_models(models)

    _, sorted_models, __ = sort_data_models(unsorted_data_models=list(models.values()))

    discriminators: list[Discriminator] = parse_discriminators(parser=parser, models=models)

    set_other_responses_models([operation for operation in parser.operations.values()])
    apply_discriminators_to_models(discriminators=discriminators, models=models)

    aliases: list[Alias] = parse_sorted_aliases(models=models, discriminators=discriminators)
    is_aliased: collections.defaultdict[str, bool] = collections.defaultdict(bool, {alias.parent_classname: True for alias in aliases})

    return {
        "models": sorted_models.values(),
        "model_imports": collect_imports(sorted_models, parser),
        "aliases": aliases,
        "is_aliased": is_aliased,
        "error_responses_models": get_error_models(parser),
    }


order: int = 2
visit: Visitor = get_models
