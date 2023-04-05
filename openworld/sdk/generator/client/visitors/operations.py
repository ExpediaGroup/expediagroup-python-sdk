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
import re
import typing
from pathlib import Path

from datamodel_code_generator.model import DataModel
from datamodel_code_generator.model.pydantic import CustomRootType
from fastapi_code_generator.parser import Argument, OpenAPIParser, Operation
from fastapi_code_generator.visitor import Visitor


class NonSchemaModelUtil:
    @staticmethod
    def is_non_schema_model(model: typing.Any) -> bool:
        r"""Checks if a model is a non-schema model or not.

        Args:
            model(Any): Model to be checked.

        Returns:
            bool
        """
        if not isinstance(model, DataModel):
            return False
        return model.reference.path.startswith("#/paths/") and not model.class_name.endswith(("Request", "Response"))

    @staticmethod
    def parse_non_schema_models(parser: OpenAPIParser) -> list[DataModel]:
        r"""Parses non-schema models from parser.

        Args:
            parser(OpenAPIParser): The parser holding results.

        Returns:
            list[DataModel]
        """
        models: list[DataModel] = list(set(filter(NonSchemaModelUtil.is_non_schema_model, parser.results)))

        models_classnames = [model.class_name for model in models]
        for index in range(len(models) - 1, -1, -1):
            model = models[index]
            if model.class_name[-1].isdigit() or f"{model.class_name}1" in models_classnames:
                continue
            models.pop(index)
            index += 1

        return models


class UnusedModelsUtil:
    @staticmethod
    def clean_unused_models(parser: OpenAPIParser, unused_models_classnames: list[str]):
        r"""Removes unused models from parser results.

        Args:
            parser(OpenAPIParser): The parser holding results.
            unused_models_classnames(list[str]): A list of models class names which are to be removed.
        """
        indices_stack = list()
        for index, result in enumerate(parser.results):
            if isinstance(result, DataModel) and result.class_name in unused_models_classnames:
                indices_stack.append(index)

        while len(indices_stack):
            parser.results.pop(indices_stack.pop())


def update_classname_by_operation_id(operation_id: str, classname: str) -> str:
    r"""Updates a class name by adding camel-case operation ID as a prefix.

    Args:
        operation_id(str): Camel-Case operation ID.
        classname(str): Class name to be updated.

    Returns:
        str
    """
    if not operation_id:
        return classname

    if not classname:
        classname = ""

    operation_id = list(operation_id)
    operation_id[0] = operation_id[0].upper()

    return "".join(operation_id) + re.sub(r"\d+$", "", classname)


class RootModelsUtil:
    @staticmethod
    def clean_root_models_from_operations_return_type(parser: OpenAPIParser, models: dict[str, DataModel]) -> list[Operation]:
        r"""Replaces any root model from any operation return type with the type-hint of `__root__`.

        Args:
            parser(OpenAPIParser): The parser holding results.
            models(dict[str, DataModel]): A dictionary of classnames as keys, and models as values.

        Returns:
            list[Operation]
        """
        sorted_operations: list[Operation] = []
        for operation in sorted(parser.operations.values(), key=lambda m: m.path):
            if (operation.response is not None) and (operation.response in models.keys()):
                model = models[operation.response]

                source = model.reference.source
                if isinstance(source, CustomRootType):
                    for field in source.fields:
                        operation.return_type = operation.return_type.replace(source.name, field.type_hint)

                for field in source.fields:
                    operation.imports += field.imports

            sorted_operations.append(operation)

        return sorted_operations


class OperationParamUtils:
    @staticmethod
    def clean_non_schema_parameter_models(operations: list[Operation], non_schema_models: list[DataModel], models_classnames_to_update: dict[str, str]):
        r"""For each operation's set of params, replaces a param's type-hint using `update_classname_by_operation_id`, removes any uneeded header, and rebuilds the value of `operation.snake_case_arguments`.

        Args:
            operations(list[Operation]): List of operations to be processed.
            non_schema_models(list[DataModel]): List of non-schema models to be replaced for each operation's param type-hint.
            models_classnames_to_update(dict[str, DataModel]): An empty dictionary to be filled with old classnames as keys, and new classnames as values.

        Returns:
             list[Operation]
        """
        for operation_index, operation in enumerate(operations):
            for arg_index, arg in enumerate(operation.snake_case_arguments_list):
                if arg.name == "body":
                    continue

                for model_index, model in enumerate(non_schema_models):
                    # TODO: Do processing using a `DataType`` object instead of `type_hint`
                    if model.class_name in arg.type_hint:
                        new_classname = update_classname_by_operation_id(operation.operationId, model.class_name)
                        models_classnames_to_update[model.class_name] = new_classname

                        operations[operation_index].snake_case_arguments_list[arg_index].type_hint = arg.type_hint.replace(model.class_name, new_classname)

                        non_schema_models[model_index].class_name = new_classname
                        break

            operations[operation_index].snake_case_arguments_list = OperationParamUtils.clean_unwanted_headers(
                operations[operation_index].snake_case_arguments_list
            )

            operations[operation_index].snake_case_arguments = ", ".join(
                argument.argument for argument in operations[operation_index].snake_case_arguments_list
            )

        return operations

    @staticmethod
    def update_non_schema_models_names(parser: OpenAPIParser, models_classnames_to_update: dict[str, str]):
        r"""Updates non-schema models classnames with new classnames

        Args:
            parser(OpenAPIParser): The parser holding results.
            models_classnames_to_update(dict[str, DataModel]): A dictionary of old classnames as keys, and new classnames as values.
        """
        for model_index, model in enumerate(parser.results):
            if isinstance(model, DataModel):
                if models_classnames_to_update[model.class_name]:
                    parser.results[model_index].class_name = models_classnames_to_update[model.class_name]

    @staticmethod
    def clean_unwanted_headers(snake_case_arguments: list[Argument]):
        r"""Removes unwanted headers from arguments list.

        Args:
            snake_case_arguments(list[Argument]): List of operation's snake case arguments.

        Returns:
            list[Argument]
        """
        unwanted_headers = ["accept", "accept-encoding", "user-agent", "authorization", "content-type"]
        return list(filter(lambda arg: arg.alias.lower() not in unwanted_headers, snake_case_arguments))


def post_process_operations(parser: OpenAPIParser):
    r"""Entry point to any post-processing required.

    Args:
        parser(OpenAPIParser): The parser holding results.

    Returns:
        list[Operation]
    """
    models = {model.class_name: model for model in parser.results if isinstance(model, DataModel)}

    non_schema_models = sorted(NonSchemaModelUtil.parse_non_schema_models(parser), key=lambda m: len(m.class_name), reverse=True)
    models_classnames_to_update: dict[str, str] = collections.defaultdict(lambda: None)

    sorted_operations = OperationParamUtils.clean_non_schema_parameter_models(
        RootModelsUtil.clean_root_models_from_operations_return_type(parser, models), non_schema_models, models_classnames_to_update
    )

    OperationParamUtils.update_non_schema_models_names(parser, models_classnames_to_update)

    models_classnames_to_update = {key: value for key, value in models_classnames_to_update.items() if value}

    UnusedModelsUtil.clean_unused_models(
        parser,
        [model.class_name for model in non_schema_models if model.class_name not in models_classnames_to_update.keys() and model.class_name[-1].isdigit()],
    )

    return sorted_operations


def get_operations(parser: OpenAPIParser, model_path: Path) -> dict[str, object]:
    r"""A visitor to expose operations to Jinja2 templates."""
    return {"operations": post_process_operations(parser)}


order: int = 1
visit: Visitor = get_operations
