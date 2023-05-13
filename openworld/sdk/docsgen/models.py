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
from copy import deepcopy

import astor
import docstring_parser

from openworld.sdk.docsgen import constant
from openworld.sdk.docsgen.util import process_new_lines


class Definition:
    name: str
    docstrings: str

    def __init__(self, name: str = "", docstrings: str = ""):
        self.name = deepcopy(name)
        self.docstrings = deepcopy(docstrings)


class Attribute(Definition):
    type_hint: str
    optional: bool

    def __init__(
        self,
        name: str = "",
        docstrings: str = "",
        type_hint: str = "",
        optional: bool = False
    ):
        super().__init__(name, docstrings)
        self.docstrings = process_new_lines(self.docstrings)
        self.type_hint = deepcopy(type_hint)
        self.optional = deepcopy(optional)

    @staticmethod
    def from_(param_docstrings: docstring_parser.DocstringParam):
        return Attribute(
            name=param_docstrings.arg_name,
            docstrings=param_docstrings.description,
            type_hint=param_docstrings.type_name,
            optional=param_docstrings.is_optional
        )


class Argument(Attribute):
    def __init__(
        self,
        name: str = "",
        docstrings: str = "",
        type_hint: str = "",
        optional: bool = False
    ):
        super().__init__(
            name=name,
            docstrings=process_new_lines(docstrings),
            type_hint=type_hint,
            optional=optional
        )

    @staticmethod
    def from_(param_docstrings: docstring_parser.DocstringParam):
        return Argument(
            name=param_docstrings.arg_name,
            docstrings=process_new_lines(param_docstrings.description),
            type_hint=param_docstrings.type_name,
            optional=param_docstrings.is_optional
        )


class Method(Definition):
    arguments: list[Argument]
    return_type: str

    def __init__(
        self,
        name: str = "",
        docstrings: str = "",
        arguments: list[Argument] = [],
        return_type: str = ""
    ):
        super().__init__(name, process_new_lines(docstrings))
        self.arguments = deepcopy(arguments)
        self.return_type = deepcopy(return_type)

    @staticmethod
    def from_function_def(definition: ast.FunctionDef):
        docstrings = docstring_parser.parse(
            ast.get_docstring(definition)
        )

        description: str = "---"
        if docstrings.long_description:
            description = docstrings.long_description
        elif docstrings.short_description:
            description = docstrings.short_description

        description = process_new_lines(description)

        return Method(
            name=definition.name,
            docstrings=description,
            arguments=[
                Argument.from_(param_docstrings)
                for param_docstrings in docstrings.params
            ],

        )

    @staticmethod
    def from_class_def(definition: ast.ClassDef):
        ignore_methods = [
            "__str__",
            "__dict__"
        ]

        methods: list[Method] = []
        for method in [definition for definition in ast.walk(definition) if isinstance(definition, ast.FunctionDef)]:
            docstrings = docstring_parser.parse(
                deepcopy(ast.get_docstring(method)),
                docstring_parser.Style.GOOGLE
            )

            if method.name in ignore_methods:
                continue

            method_docstrings = "---"
            if docstrings.long_description:
                method_docstrings = docstrings.long_description
            elif docstrings.short_description:
                method_docstrings = docstrings.short_description

            method_docstrings = process_new_lines(method_docstrings)

            methods.append(
                Method(
                    name=method.name,
                    docstrings=method_docstrings,
                    arguments=[
                        Argument.from_(param_docstring) for param_docstring in docstrings.params
                    ],
                    return_type=astor.to_source(node=method.returns) if method.returns else None
                )
            )

        return methods


class Function(Method):
    def __init__(
        self,
        name: str = "",
        docstrings: str = "",
        arguments: list[Argument] = [],
        return_type: str = ""
    ):
        super().__init__(
            name=name,
            docstrings=process_new_lines(docstrings),
            arguments=arguments,
            return_type=return_type
        )


class Class(Definition):
    attributes: list[Attribute]
    methods: list[Method]
    bases: list[str]

    def __init__(
        self,
        name: str = "",
        docstrings: str = str,
        attributes: list[Attribute] = [],
        methods: list[Method] = [],
        bases: list[str] = ["object"]
    ):
        super().__init__(name=name, docstrings=docstrings)
        self.attributes = deepcopy(attributes)
        self.methods = deepcopy(methods)
        self.bases = deepcopy(bases)

    @staticmethod
    def from_(definition: ast.ClassDef):
        docstrings = docstring_parser.parse(
            ast.get_docstring(definition),
            docstring_parser.Style.GOOGLE
        )

        print(docstrings.meta)

        description = constant.EMPTY_DESCRIPTION_DOCSTRING
        if docstrings.long_description:
            description = docstrings.long_description
        elif docstrings.short_description and docstrings.short_description != "None":
            description = docstrings.short_description

        # description = process_new_lines(description)

        return Class(
            name=definition.name,
            docstrings=description,
            methods=Method.from_class_def(definition),
            bases=["object"] + [base.id for base in definition.bases] + [definition.name],
            attributes=[Attribute.from_(param) for param in docstrings.params]
        )


class Alias(Definition):
    one_of: list[str]

    def __init__(self, name: str = "", docstrings: str = "", one_of: list[str] = []):
        super().__init__(name, docstrings)
        self.one_of = one_of

    @staticmethod
    def from_assign(node: ast.Assign):
        text = astor.to_source(node)
        name, one_of = text.split("=")

        return Alias(
            name=name.strip(),
            docstrings="",
            one_of=[model.strip() for model in one_of.removeprefix('Union[').removesuffix(']').split(',')]
        )


class Module:
    name: str
    classes: list[Class]
    functions: list[Function]
    aliases: list[Alias]
    file: str

    def __init__(
        self,
        name: str = "",
        classes: list[Class] = [],
        functions: list[Function] = [],
        aliases: list[Alias] = []
    ):
        self.name = deepcopy(name)
        self.classes = deepcopy(classes)
        self.functions = deepcopy(functions)
        self.aliases = aliases
        self.file = f"{self.name}{constant.MARKDOWN_SUFFIX}"
