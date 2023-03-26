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
from pathlib import Path

from datamodel_code_generator.model import DataModel
from datamodel_code_generator.model.pydantic import CustomRootType
from fastapi_code_generator.parser import OpenAPIParser, Operation
from fastapi_code_generator.visitor import Visitor


def parse_non_schema_models(parser: OpenAPIParser):
    models: list[DataModel] = list(
        {
            result
            for result in parser.results
            if isinstance(result, DataModel)
            and result.reference.path.startswith("#/paths/")
            and not result.class_name.endswith("Response")
            and not result.class_name.endswith("Request")
        }
    )

    models_classnames = [model.class_name for model in models]
    for index in range(len(models) - 1, -1, -1):
        model = models[index]
        if model.class_name[-1].isdigit() or f"{model.class_name}1" in models_classnames:
            continue
        models.pop(index)
        index += 1

    return models


def clean_unused_models(parser: OpenAPIParser, unused_models_classnames: list[str]):
    indices_stack = list()
    for index, result in enumerate(parser.results):
        if isinstance(result, DataModel) and result.class_name in unused_models_classnames:
            indices_stack.append(index)

    while len(indices_stack):
        parser.results.pop(indices_stack.pop())


def update_classname_by_operation_id(operation_id: str, classname: str):
    if not operation_id:
        return classname

    if not classname:
        classname = ""

    operation_id = list(operation_id)
    operation_id[0] = operation_id[0].upper()

    return "".join(operation_id) + re.sub(r"\d+$", "", classname)


def clean_root_models_from_operations_return_type(parser: OpenAPIParser, models: dict[str, DataModel]) -> list[Operation]:
    sorted_operations: list[Operation] = []
    for operation in sorted(parser.operations.values(), key=lambda m: m.path):
        if (operation.response is not None) and (operation.response in models.keys()):
            model = models[operation.response]

            source = model.reference.source
            if isinstance(source, CustomRootType):
                for field in source.fields:
                    operation.return_type = operation.return_type.replace(source.name, field.type_hint)

            for field in source.fields:
                for import_ in field.imports:
                    operation.imports.append(import_)

        sorted_operations.append(operation)

    return sorted_operations


def clean_non_schema_parameter_models(operations, non_schema_models, models_classnames_to_update):
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

        operations[operation_index].snake_case_arguments = ", ".join(argument.argument for argument in operations[operation_index].snake_case_arguments_list)
    return operations


def update_non_schema_models_names(parser: OpenAPIParser, models_classnames_to_update):
    for model_index, model in enumerate(parser.results):
        if isinstance(model, DataModel):
            if models_classnames_to_update[model.class_name]:
                parser.results[model_index].class_name = models_classnames_to_update[model.class_name]


def post_process_operations(parser: OpenAPIParser):
    models = {model.class_name: model for model in parser.results if isinstance(model, DataModel)}

    non_schema_models = sorted(parse_non_schema_models(parser), key=lambda m: len(m.class_name), reverse=True)
    models_classnames_to_update = collections.defaultdict(lambda: None)

    sorted_operations = clean_non_schema_parameter_models(
        clean_root_models_from_operations_return_type(parser, models), non_schema_models, models_classnames_to_update
    )

    update_non_schema_models_names(parser, models_classnames_to_update)

    models_classnames_to_update = {key: value for key, value in models_classnames_to_update.items() if value}

    clean_unused_models(
        parser,
        [model.class_name for model in non_schema_models if model.class_name not in models_classnames_to_update.keys() and model.class_name[-1].isdigit()],
    )

    return sorted_operations


def get_operations(parser: OpenAPIParser, model_path: Path) -> dict[str, object]:
    return {"operations": post_process_operations(parser)}


order: int = 1
visit: Visitor = get_operations
