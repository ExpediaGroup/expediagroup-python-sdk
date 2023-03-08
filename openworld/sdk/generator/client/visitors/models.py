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
from collections import OrderedDict
from pathlib import Path

from datamodel_code_generator.imports import Import, Imports
from datamodel_code_generator.model.base import DataModel
from datamodel_code_generator.parser.base import sort_data_models
from fastapi_code_generator.parser import OpenAPIParser
from fastapi_code_generator.visitor import Visitor


def collect_imports(sorted_models, parser):
    models = OrderedDict()
    model_imports = Imports()

    imports = Imports()
    imports.update(parser.imports)

    for model in sorted_models.values():
        models[model.class_name] = model

    for model in sorted_models.values():
        for import_ in model.imports:
            imports.append(import_)
            for field in model.fields:
                for field_import in field.imports:
                    imports.append(field_import)

    for import_ in model_imports:
        if isinstance(import_, Import):
            imports.append(import_)

    return imports


def get_operations(parser: OpenAPIParser, model_path: Path) -> dict[str, object]:
    _, sorted_models, __ = sort_data_models(unsorted_data_models=[_ for _ in parser.results if isinstance(_, DataModel)])

    return {"models": sorted_models.values(), "model_imports": collect_imports(sorted_models, parser)}


visit: Visitor = get_operations
