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
from openworld.sdk.docsgen.util import replace_new_lines_with_br_tag


class CodeRepresentationElement:
    r"""A generic class that is a parent to all code representation classes.

    Args:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.

    Attributes:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
    """
    name: str
    docstrings: str

    def __init__(self, name: str = "", docstrings: str = ""):
        self.name = deepcopy(name)
        self.docstrings = deepcopy(docstrings)


class Attribute(CodeRepresentationElement):
    r"""A representation of an attribute, which belongs to a class.

    Args:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
        type_hint(str): Attribute type hint.
        optional(bool): True if attribute is nullable or not.

    Attributes:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
        type_hint(str): Attribute type hint.
        optional(bool): True if attribute is nullable or not.
    """
    type_hint: str
    optional: bool

    def __init__(self, name: str = "", docstrings: str = "", type_hint: str = "", optional: bool = False):
        super().__init__(name, docstrings)
        self.docstrings = replace_new_lines_with_br_tag(self.docstrings)
        self.type_hint = deepcopy(type_hint)
        self.optional = deepcopy(optional)

    @staticmethod
    def from_(param_docstrings: docstring_parser.DocstringParam):
        r"""A static method that creates an object of this class based on given arguments.

        Args:
            param_docstrings(docstring_parser.DocstringParam): Parsed docstrings of attribute.

        Returns:
            Attribute
        """
        return Attribute(
            name=param_docstrings.arg_name, docstrings=param_docstrings.description, type_hint=param_docstrings.type_name, optional=param_docstrings.is_optional
        )


class Argument(Attribute):
    r"""A representation of an attribute, which belongs to a class.

    Args:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
        type_hint(str): Attribute type hint.
        optional(bool): True if attribute is nullable or not.

    Attributes:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
        type_hint(str): Attribute type hint.
        optional(bool): True if attribute is nullable or not.
    """

    def __init__(self, name: str = "", docstrings: str = "", type_hint: str = "", optional: bool = False):
        super().__init__(name=name, docstrings=replace_new_lines_with_br_tag(docstrings), type_hint=type_hint, optional=optional)

    @staticmethod
    def from_(param_docstrings: docstring_parser.DocstringParam):
        r"""A static method that creates an object of this class based on given arguments.

        Args:
            param_docstrings(docstring_parser.DocstringParam): Parsed docstrings of argument.

        Returns:
            Argument
        """
        return Argument(
            name=param_docstrings.arg_name,
            docstrings=replace_new_lines_with_br_tag(param_docstrings.description),
            type_hint=param_docstrings.type_name,
            optional=param_docstrings.is_optional,
        )


class Method(CodeRepresentationElement):
    r"""A representation of a method, which belongs to a class.

    Args:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
        arguments(list[Argument]): List of method arguments representation.
        return_type(str): Return type of method.

    Attributes:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
        arguments(list[Argument]): List of method arguments representation.
        return_type(str): Return type of method.
    """

    arguments: list[Argument]
    return_type: str

    def __init__(self, name: str = "", docstrings: str = "", arguments: list[Argument] = [], return_type: str = ""):
        super().__init__(name, replace_new_lines_with_br_tag(docstrings))
        self.arguments = deepcopy(arguments)
        self.return_type = deepcopy(return_type)

    @staticmethod
    def from_function_def(definition: ast.FunctionDef):
        r"""A static method that creates an object of this class based from a function definition ast node.

        Args:
            definition(ast.FunctionDef): Parsed ast node of the methods' definition.

        Returns:
            Method
        """
        docstrings = docstring_parser.parse(ast.get_docstring(definition))

        description: str = "---"
        if docstrings.long_description:
            description = docstrings.long_description
        elif docstrings.short_description:
            description = docstrings.short_description

        description = replace_new_lines_with_br_tag(description)

        return Method(
            name=definition.name,
            docstrings=description,
            arguments=[Argument.from_(param_docstrings) for param_docstrings in docstrings.params],
        )

    @staticmethod
    def from_class_def(definition: ast.ClassDef):
        r"""A static method that creates an object of this class based from a class definition ast node.

        Args:
            definition(ast.FunctionDef): Parsed ast node of the classes' definition.

        Returns:
            list[Method]: List of methods representation parsed from a class.
        """
        ignore_methods = ["__str__", "__dict__"]

        methods: list[Method] = []
        for method in [definition for definition in ast.walk(definition) if isinstance(definition, ast.FunctionDef)]:
            docstrings = docstring_parser.parse(deepcopy(ast.get_docstring(method)), docstring_parser.Style.GOOGLE)

            if method.name in ignore_methods:
                continue

            method_docstrings = "---"
            if docstrings.long_description:
                method_docstrings = docstrings.long_description
            elif docstrings.short_description:
                method_docstrings = docstrings.short_description

            method_docstrings = replace_new_lines_with_br_tag(method_docstrings)

            methods.append(
                Method(
                    name=method.name,
                    docstrings=method_docstrings,
                    arguments=[Argument.from_(param_docstring) for param_docstring in docstrings.params],
                    return_type=astor.to_source(node=method.returns) if method.returns else None,
                )
            )

        return methods


class Function(Method):
    r"""A representation of a method, which belongs to a class.

    Args:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
        arguments(list[Argument]): List of method arguments representation.
        return_type(str): Return type of method.

    Attributes:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
        arguments(list[Argument]): List of method arguments representation.
        return_type(str): Return type of method.
    """

    def __init__(self, name: str = "", docstrings: str = "", arguments: list[Argument] = [], return_type: str = ""):
        super().__init__(name=name, docstrings=replace_new_lines_with_br_tag(docstrings), arguments=arguments, return_type=return_type)


class Class(CodeRepresentationElement):
    r"""A representation of a method, which belongs to a class.

    Args:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
        attributes(list[Attribute]): List of class attributes representation.
        bases(list[str]): List of base classes.
        methods(list[Method]): List of class methods.

    Attributes:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
        attributes(list[Attribute]): List of class attributes representation.
        bases(list[str]): List of base classes.
        methods(list[Method]): List of class methods.
    """

    attributes: list[Attribute]
    methods: list[Method]
    bases: list[str]

    def __init__(self, name: str = "", docstrings: str = str, attributes: list[Attribute] = [], methods: list[Method] = [], bases: list[str] = ["object"]):
        super().__init__(name=name, docstrings=docstrings)
        self.attributes = deepcopy(attributes)
        self.methods = deepcopy(methods)
        self.bases = deepcopy(bases)

    @staticmethod
    def from_class_def(definition: ast.ClassDef):
        r"""A static method that creates an object of this class based from a class definition ast node.

        Args:
            definition(ast.FunctionDef): Parsed ast node of the classes' definition.

        Returns:
            Class: Representation of a parsed class.
        """

        docstrings = docstring_parser.parse(ast.get_docstring(definition), docstring_parser.Style.GOOGLE)

        description = constant.EMPTY_DESCRIPTION_DOCSTRING
        if docstrings.long_description:
            description = docstrings.long_description
        elif docstrings.short_description and docstrings.short_description != "None":
            description = docstrings.short_description

        return Class(
            name=definition.name,
            docstrings=description,
            methods=Method.from_class_def(definition),
            bases=["object"] + [base.id for base in definition.bases] + [definition.name],
            attributes=[Attribute.from_(param) for param in docstrings.params],
        )


class Alias(CodeRepresentationElement):
    r"""A representation of a type alias, which belongs to a module.

    Args:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
        one_of(list[str]): List of types this alias is union of.

    Attributes:
        name(str): Name of the element (method name, class name, ...etc).
        docstrings(str): Parsed docstrings.
        one_of(list[str]): List of types this alias is union of.
    """
    one_of: list[str]

    def __init__(self, name: str = "", docstrings: str = "", one_of: list[str] = []):
        super().__init__(name, docstrings)
        self.one_of = one_of

    @staticmethod
    def from_assign(node: ast.Assign):
        r"""A static method that creates an object of this class based from a class definition ast node.

        Args:
            node(ast.Assign): Parsed ast node of the assigns' definition.

        Returns:
            Alias: Representation of a parsed alias.
        """
        text = astor.to_source(node)
        name, one_of = text.split("=")

        return Alias(name=name.strip(), docstrings="", one_of=[model.strip() for model in one_of.removeprefix("Union[").removesuffix("]").split(",")])


class Module:
    r"""A representation of a module.

    Args:
        name(str): Name of the element (method name, class name, ...etc).
        classes(list[Class]): List of classes in a module.
        functions(list[Function]): List of functions in a module.
        aliases(list[Alias]): List of aliases in a module.

    Attributes:
        name(str): Name of the element (method name, class name, ...etc).
        classes(list[Class]): List of classes in a module.
        functions(list[Function]): List of functions in a module.
        aliases(list[Alias]): List of aliases in a module.
        file(str): Markdown file of the rendered module.
    """
    name: str
    classes: list[Class]
    functions: list[Function]
    aliases: list[Alias]
    file: str

    def __init__(self, name: str = "", classes: list[Class] = [], functions: list[Function] = [], aliases: list[Alias] = []):
        self.name = deepcopy(name)
        self.classes = deepcopy(classes)
        self.functions = deepcopy(functions)
        self.aliases = aliases
        self.file = f"{self.name}{constant.MARKDOWN_SUFFIX}"
