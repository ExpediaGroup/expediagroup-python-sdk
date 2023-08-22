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
import typing
from enum import Enum

from datamodel_code_generator.types import DataType
from fastapi_code_generator import parser as fastapi_code_generator_parser


# expediagroup: new models to add more attributes for SDK generation.
class ParamTypes(Enum):
    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"
    body = "body"


class Argument(fastapi_code_generator_parser.Argument):
    in_: ParamTypes = None
    alias: str = ""
    description: str = ""
    datatype: typing.Optional[DataType] = None

    # Replace `cached property` with a normal `property` in order to take effect on change.
    @property
    def argument(self) -> str:
        if self.default is None and self.required:
            return f"{self.name}: {self.type_hint}"
        return f"{self.name}: {self.type_hint} = {self.default}"


class Operation(fastapi_code_generator_parser.Operation):
    arguments_list: list[Argument] = []
    snake_case_arguments_list: list[Argument] = []
