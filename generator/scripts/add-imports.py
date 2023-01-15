#!/bin/env python3

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


"""Add imports to all generated models."""

import ast
import pathlib
import sys


def prepend(filename: str, line: str) -> None:
    """
    Prepend a line to a file.

    :param filename: the file to prepend to
    :param line: the line to prepend
    :return: none
    """
    with open(filename, "r+") as file_to_update:
        content = file_to_update.read()
        file_to_update.seek(0, 0)
        file_to_update.write(line.rstrip("\r\n") + "\n" + content)


def get_class_definition(text: str):
    text = text.strip().removeprefix("class").removesuffix(":").strip()

    if "(" in text:
        text = text.rsplit("(")
        text = text[0].strip()

    return text


if len(sys.argv) != 2:
    print("Usage: >> python3 add-imports.py <path to directory>")
    exit(1)

files = list(pathlib.Path(sys.argv[1]).glob("*.py"))

imports = {
    "List": "from typing import List",
    "Optional": "from typing import Optional",
    "Union": "from typing import Union",
    "field": "from dataclasses import field",
    "dataclass": "from dataclasses import dataclass",
    "dataclass_json": "from dataclasses_json import dataclass_json",
    "config": "from dataclasses_json import config",
    "datetime": "from datetime import datetime",
    "platform": "import platform",
    "header": "from openworld.sdk.core.constant import header",
}

for file in files:
    with open(file) as f:
        p = ast.parse(f.read())
        classes = [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
        for c in classes:
            imports[c] = f"from .{str(file.name)[:-3]} import {c}"

for file in files:
    file_path = str(file)
    with open(file) as f:
        contents = pathlib.Path(file).read_text()
        prepend(file_path, "\n\n\n")
        for k in imports.keys():
            is_class_definition = (f"class {k}" in contents) and (k == get_class_definition(contents))
            if k in contents and not is_class_definition:
                print(f">> Adding import {k} to {file.name}")
                prepend(file_path, imports[k])
