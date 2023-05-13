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

import ast
from pathlib import Path

import astor

from openworld.sdk.docsgen.constant import IGNORE_MODULES, PYTHON_SUFFIX
from openworld.sdk.docsgen.models import *


def parse_modules_paths(path: Path) -> list[Path]:
    """Parses modules present in a given directory for one depth level.

    :param path: A path of where modules are present.
    :type path: pathlib.Path
    """

    modules_paths: list[Path] = list()
    for module in path.rglob("*.py"):
        modules_paths.append(module)

    return modules_paths


def parse_module(definitions: list[ast.AST], name: str) -> Module:
    """Parses classes and methods in an AST.

    :param name: Name of module.
    :type name: str

    :param definitions: Root node in the AST.
    :type definitions: ast.AST
    """
    module: Module = Module(name=name)
    for node in definitions:
        if isinstance(node, ast.ClassDef):
            module.classes.append(Class.from_(node))

        if isinstance(node, ast.FunctionDef):
            module.functions.append(Method.from_function_def(node))

        if isinstance(node, ast.Assign):
            value = astor.to_source(node).strip().replace(" ", "").split("=")
            if len(value) < 2:
                continue

            if not value[1].startswith("Union["):
                continue

            module.aliases.append(Alias.from_assign(node))

    return module


def parse_modules(modules_paths: list[Path]) -> list[Module]:
    modules: list[Module] = []
    for path in modules_paths:
        if path.name.removesuffix(PYTHON_SUFFIX) in IGNORE_MODULES:
            continue

        ast_root = ast.parse(source=path.read_text())

        for node in ast.walk(ast_root):
            if isinstance(node, ast.Module):
                module = parse_module(list(node.body), path.name.removesuffix(PYTHON_SUFFIX))
                modules.append(module)

    return modules


def parse(package_path: Path) -> list[Module]:
    return parse_modules(parse_modules_paths(package_path))
