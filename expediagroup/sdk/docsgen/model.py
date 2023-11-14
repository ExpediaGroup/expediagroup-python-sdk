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

from __future__ import annotations

import collections
import copy
from typing import Any, Union

import constant
import docspec
import docstring_parser
import util
from docstring_parser.parser import parse
from pydantic import BaseModel


class DocumentedObject(BaseModel):
    """
    Represents a base object with documentation attributes.

    Attributes:
        name (str): The name of the object.
        description (str | None): An optional description of the object.
    """

    class Config:
        smart_union = True

    name: str
    description: Union[str, None]


class Breadcrumbs(BaseModel):
    """
    Represents breadcrumbs for a documentation.

    Attributes:
        document_name (str): The name of the document.
        parent (Breadcrumbs | None): Reference to the parent breadcrumb.
        alias (str | None): Optional alias for the breadcrumb.
    """

    class Config:
        smart_union = True

    document_name: str
    parent: Union[Breadcrumbs, None]
    alias: Union[str, None] = None

    def __str__(self) -> str:
        """
        String representation of breadcrumbs.

        Returns:
            str: Full breadcrumb trail.
        """
        breadcrumbs: str = util.to_markdown_file_ref(self.document_name)

        node = self.parent
        while node:
            breadcrumbs = f"{util.to_markdown_file_ref(node.document_name)} / {breadcrumbs}"
            node = node.parent

        return breadcrumbs


class Document(DocumentedObject):
    """
    Represents a documentation entity.

    Attributes:
        breadcrumbs (Breadcrumbs | None): The breadcrumb trail for the document.
    """

    breadcrumbs: Union[Breadcrumbs, None]

    def init_breadcrumbs_from_parent(self, parent: Document) -> None:
        """
        Initializes breadcrumbs based on a parent document.

        Args:
            parent (Document): The parent document.
        """
        self.breadcrumbs = Breadcrumbs(document_name=self.name, parent=parent.breadcrumbs)


class Variable(DocumentedObject):
    """
    Represents a variable entity in the documentation.

    Attributes:
        value (str | None): The value of the variable.
    """

    value: Union[str, None] = None

    @staticmethod
    def from_(other: docspec.Variable) -> Variable:
        """
        Creates an instance from a docspec.Variable object.

        Args:
            other (docspec.Variable): A docspec variable instance.

        Returns:
            Variable: Initialized variable instance.
        """
        description: str = constant.NULL_DESCRIPTION
        if other.docstring:
            description = other.docstring.content

        return Variable(
            name=other.name,
            description=description,
            value=other.value,
        )


class Attribute(DocumentedObject):
    """
    Represents an attribute with type and default value details.

    Attributes:
        datatype (str): Data type of the attribute.
        is_optional (bool): Whether the attribute is optional.
        default_value (Any): The default value of the attribute.
    """

    datatype: str
    is_optional: bool
    default_value: Any

    @staticmethod
    def from_(other: docspec.Variable) -> Attribute:
        """
        Creates an Attribute instance from a docspec.Variable.

        Args:
            other (docspec.Variable): A docspec variable instance.

        Returns:
            Attribute: Initialized attribute instance.
        """
        if not other:
            raise ValueError(str(other))

        if not other.datatype:
            other.datatype = str(Any)

        return Attribute(
            name=other.name,
            datatype=other.datatype,
            is_optional=other.datatype.startswith(constant.OPTIONAL),
            default_value=other.value,
            description=other.docstring.content if other.docstring else constant.NULL_DESCRIPTION,
        )


class Argument(Attribute):
    """
    Represents an argument derived from methods in the documentation.
    """

    @staticmethod
    def from_method(method: docspec.Function) -> list[Argument]:
        """
        Creates a list of Arguments from a docspec.Function method.

        Args:
            method (docspec.Function): A docspec function instance.

        Returns:
            list[Argument]: List of initialized Argument instances.
        """
        arguments: list[Argument] = list()

        if not method.docstring:
            return arguments

        docstring_content: Union[str] = method.docstring.content

        docstring_object = parse(str(docstring_content), docstring_parser.Style.GOOGLE)
        description: str = max(
            docstring_object.long_description if docstring_object.long_description else constant.NULL_DESCRIPTION,
            docstring_object.short_description if docstring_object.short_description else constant.NULL_DESCRIPTION,
            key=len,
        )

        for param in docstring_object.params:
            arguments.append(
                Argument(name=param.arg_name, description=description, datatype=param.type_name, is_optional=param.is_optional, default_value=param.default)
            )

        return arguments


class Method(DocumentedObject):
    """
    Represents a method with return type and arguments.

    Attributes:
        return_type (str | None): The return type of the method.
        arguments (list[Argument | Attribute]): List of arguments of the method.
    """

    return_type: Union[str, None]
    arguments: list[Union[Argument, Attribute]]

    @staticmethod
    def from_(other: docspec.Function) -> Method:
        """
        Creates a Method instance from a docspec.Function.

        Args:
            other (docspec.Function): A docspec function instance.

        Returns:
            Method: Initialized method instance.
        """
        if not other:
            raise ValueError(str(other))

        docstring_content: Union[str, None] = None
        if other.docstring:
            docstring_content = other.docstring.content

        description = util.parse_method_description_docstrings(docstring_content)

        return Method(
            name=other.name,
            description=description,
            arguments=Argument.from_method(method=other),
            return_type=other.return_type,
        )


class Class(Document):
    """Represents a class entity in the documentation, extending the Document class.
    Contains detailed information about the class including its constructor, bases,
    attributes, and methods.

    Attributes:
        constructor (Method): The constructor method of the class.
        bases (list[str]): List of base classes that the class inherits from.
        attributes (list[Attribute]): List of attributes of the class.
        methods (list[Method]): List of methods defined in the class.
    """

    constructor: Method
    bases: list[str]
    attributes: list[Attribute]
    methods: list[Method]

    @staticmethod
    def from_(other: docspec.Class):
        """Creates an instance of the Class from a docspec.Class object.

        Args:
            other (docspec.Class): A docspec class instance.

        Returns:
            Class: A Class instance with details extracted from the docspec class instance.

        Raises:
            ValueError: If the input docspec class instance is None.
        """
        if not other:
            raise ValueError(str(other))

        description: str = constant.EMPTY_STRING
        if other.docstring:
            description = other.docstring.content

        methods = list(map(Method.from_, filter(lambda m: isinstance(m, docspec.Function), other.members)))
        attributes = list(map(Attribute.from_, filter(lambda i: isinstance(i, docspec.Variable), other.members)))
        constructor = None
        is_enum = "Enum" in other.bases

        for index, method in enumerate(list(map(Method.from_, filter(lambda m: isinstance(m, docspec.Function), other.members)))):
            if constant.INIT_METHOD in method.name:
                constructor = copy.deepcopy(method)
                constructor.name = other.name

                description = description + f"{constant.NEW_LINE}{method.description}" if method.description else description

                methods.pop(index)
                break

        if not constructor:
            constructor = Method(
                name=other.name,
                arguments=attributes if not is_enum else [],
                description="",
                return_type="",
            )

        attributes.sort(key=lambda a: a.name)

        return Class(
            name=other.name,
            methods=methods,
            attributes=attributes,
            constructor=constructor,
            description=description.content if isinstance(description, docspec.Docstring) else description,
            bases=list(other.bases),
            breadcrumbs=None,
        )


class Module(Document):
    """Represents a module entity in the documentation, extending the Document class.
    Contains detailed information about the module including its classes, variables,
    and submodules.

    Attributes:
        classes (list[Class]): List of classes defined in the module.
        variables (list[Variable]): List of variables defined in the module.
        submodules (list[Module]): List of submodules within the module.
    """

    classes: list[Class]
    variables: list[Variable]
    submodules: list[Module]

    # TODO: Add module level functions to `Module` attributes.

    def sync_submodules(self, modules: list[Module]) -> None:
        """Syncs the submodules within the current module instance by checking the
        names of modules from the input list.

        Args:
            modules (list[Module]): List of module instances to check for submodule relationships.
        """
        for module in modules:
            if module.name == self.name:
                continue

            if module.name.rsplit(sep=".", maxsplit=1).pop(0) == self.name:
                self.submodules.append(module)

    @staticmethod
    def from_(other: docspec.Module):
        r"""Creates an instance of the Module class from a docspec.Module object.

        Args:
            other (docspec.Module): A docspec module instance.

        Returns:
            Module: A Module instance with details extracted from the docspec module instance.

        Raises:
            ValueError: If the input docspec module instance is None.
        """
        if not other:
            raise ValueError(str(other))

        # classes = list(map(Class.from_, list(filter(lambda m: isinstance(m, docspec.Class), other.members))))
        return Module(
            name=other.name,
            description=other.docstring,
            classes=list(map(Class.from_, list(filter(lambda m: isinstance(m, docspec.Class), other.members)))),
            variables=list(map(Variable.from_, list(filter(lambda v: isinstance(v, docspec.Variable), other.members)))),
            submodules=list(),
            breadcrumbs=None,
        )


class Master(Document):
    """Represents the master document that consolidates modules, extending the Document class.

    Attributes:
        modules (list[Module]): List of modules to be included in the master document.
    """

    modules: list[Module]

    @staticmethod
    def from_modules(modules: list[Module]) -> Master:
        """Creates a Master instance from a list of module instances, organizing
        them appropriately for the master document.

        Args:
            modules (list[Module]): List of module instances to be included in the master document.

        Returns:
            Master: A Master instance with organized modules.
        """
        return Master(
            modules=Master.parse_master_modules(modules=modules),
            name=constant.DefaultNames.MASTER_FILE_NAME,
            breadcrumbs=Breadcrumbs(document_name=constant.DefaultNames.MASTER_FILE_NAME, parent=None),
            description="",
        )

    @staticmethod
    def parse_master_modules(modules: list[Module]) -> list[Module]:
        r"""Parses the modules to extract and organize modules to be included in the
        master document based on their parent-child relationships.

        Args:
            modules (list[Module]): List of module instances to be parsed.

        Returns:
            list[Module]: List of organized module instances for inclusion in the master document.
        """
        modules: dict[str, Union[Module, None]] = collections.defaultdict(lambda m: None, {module.name: module for module in modules})
        master_modules: list[Module] = list()
        has_parent: dict[str, bool] = collections.defaultdict(bool)

        for module_name in modules.keys():
            parent_module_name = module_name.rsplit(sep=".", maxsplit=1).pop(0)
            has_parent[module_name] = bool(modules.get(parent_module_name))

        for module_name, parent_does_exist in has_parent.items():
            if parent_does_exist:
                master_modules.append(modules[module_name])

        return master_modules
