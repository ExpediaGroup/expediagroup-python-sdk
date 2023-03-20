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
from pathlib import Path

from datamodel_code_generator.model.pydantic import CustomRootType
from fastapi_code_generator.parser import OpenAPIParser, Operation
from fastapi_code_generator.visitor import Visitor


def get_operations(parser: OpenAPIParser, model_path: Path) -> dict[str, object]:
    sorted_operations: list[Operation] = []

    models = dict()

    for model in parser.results:
        models[model.name] = model

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

    return {"operations": sorted_operations}


visit: Visitor = get_operations
