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

CONSTR: str = 'constr'

MARKDOWN_SUFFIX: str = ".md"

PYTHON_SUFFIX: str = ".py"

MARKDOWN_CODE_BLOCK_PREFIX: str = "```python "

MARKDOWN_CODE_BLOCK_SUFFIX: str = "```"

OPENING_PARANTHESIS: str = "("

CLOSING_PARANTHESIS: str = ")"

TABLE_OF_CONTENT: str = "Table of Content"

CLASSES: str = "Classes"

CLASS: str = "Class"

MODEL: str = "Model"

FUNCTIONS: str = "Functions"

FUNCTION: str = "Function"

METHODS: str = "Methods"

METHOD: str = "Method"

PARAMETERS: str = "Parameters"

ATTRIBUTES: str = "Attributes"

__INIT__: str = "__init__"

EMPTY_DESCRIPTION_DOCSTRING: str = "---"

ENUM: str = "Enum"

DESCRIPTION: str = "Description"

NEW_LINE: str = "___"

INHERITANCE: str = "Inheritance"

ALIAS_DOCSTRINGS: str = "An alias datatype, can be one of:"

IGNORE_TYPES: list[str] = [
    str(datatype) for datatype in typing.__all__
] + ["BaseModel", "Enum"]

IGNORE_MODULES: list[str] = [
    "__init__",
    "setup"
]

CLASS_ATTRIBUTES_TABLE_FIELDS: list[str] = [
    "Name",
    "Type",
    "Required",
    "Description"
]

METHOD_TABLE_FIELDS: list[str] = [
    "Param",
    "Type",
    "Required",
    "Description"
]
