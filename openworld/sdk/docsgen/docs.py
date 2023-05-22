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

from openworld.sdk.docsgen import constant
from openworld.sdk.docsgen.models import Alias, Attribute, Class, Method, Module, Argument
from openworld.sdk.docsgen.prettytable import PrettyTable
from openworld.sdk.docsgen.util import *


class Breadcrumbs:
    r"""Breadcrumbs component.

    Args:
        current(str): Current element/level in breadcrumbs.
        previous(str): Parent element/level in breadcrumbs.
    """
    breadcrumbs: str = ""
    namespace: str = ""

    def __init__(self, current: str = "", previous: list[str] = []):
        self.breadcrumbs = " / ".join(previous + [current])

    def __str__(self):
        return self.breadcrumbs


class ConstructorComponent:
    r"""Constructor component, that renders a Markdown code description of the constructor to a class.

    Args:
        params(list[Argument]): List of params/args the constructor needs to create an object.
        classname(str): Name of the class of which the represented constructor creates an object of.
    """
    params: list[Argument]
    classname: str

    def __init__(self, classname: str, params: list[Argument]):
        self.classname = classname
        self.params = params

    def __str__(self):
        constructor_docs = (
            [constant.MARKDOWN_CODE_BLOCK_PREFIX, self.classname + constant.OPENING_PARANTHESIS]
            + [f"\t{param.name}: {param.type_hint}," for param in self.params]
            + [constant.CLOSING_PARANTHESIS, constant.MARKDOWN_CODE_BLOCK_SUFFIX]
            if self.params
            else [
                constant.MARKDOWN_CODE_BLOCK_PREFIX,
                f"{self.classname}{constant.OPENING_PARANTHESIS}{constant.CLOSING_PARANTHESIS}",
                constant.MARKDOWN_CODE_BLOCK_SUFFIX,
            ]
        )

        return "\n".join(constructor_docs)


class MethodComponent:
    r"""Method component, that renders a Markdown method representation, including description, arguments & their
    datatypes. Rendered output contains the following elements:
    - Method name and params code block.
    - Method description.
    - Table of params and their data types, referenced through Markdown reference links.
    - Method return data types, referenced through Markdown reference links.

    Args:
        method(Method): Method representation to be used in rendering.
    """
    method: Method

    def __init__(self, method: Method):
        self.method = method

    def __str__(self):
        method_params: PrettyTable = PrettyTable(field_names=constant.CLASS_ATTRIBUTES_TABLE_FIELDS)
        argument_count = 0

        for argument in self.method.arguments:
            argument_count += 1
            method_params.add_row([argument.name, get_datatype_reference(argument.type_hint), not argument.optional, argument.docstrings])

        method_header = (
            "\n".join(
                [
                    constant.MARKDOWN_CODE_BLOCK_PREFIX,
                    self.method.name + constant.OPENING_PARANTHESIS,
                ]
                + ["\t" + f"{arg.name}: {arg.type_hint}," for arg in self.method.arguments]
                + [constant.CLOSING_PARANTHESIS, constant.MARKDOWN_CODE_BLOCK_SUFFIX]
            )
            if self.method.arguments
            else "\n".join(
                [
                    constant.MARKDOWN_CODE_BLOCK_PREFIX,
                    f"{self.method.name}{constant.OPENING_PARANTHESIS}{constant.CLOSING_PARANTHESIS}",
                    constant.MARKDOWN_CODE_BLOCK_SUFFIX,
                ]
            )
        )

        return "\n".join(
            [
                f"{header4(self.method.name)}",
                method_header,
                self.method.docstrings,
                header4(constant.PARAMETERS),
                str(method_params) if argument_count else "",
                header4("Returns"),
                bullet_points([get_datatype_reference(self.method.return_type)]),
            ]
        )


class ClassComponent:
    name: str
    constructor: ConstructorComponent
    breadcrumbs: Breadcrumbs
    file: str
    class_: Class

    def __init__(self, class_: Class, parent_breadcrumb: Breadcrumbs):
        self.class_ = class_
        self.name = class_.name
        self.file = f"{self.name}{constant.MARKDOWN_SUFFIX}"
        self.breadcrumbs = Breadcrumbs(current=f"[{self.name}](./{self.file})", previous=[parent_breadcrumb.breadcrumbs])

        init = [(index, method) for index, method in enumerate(class_.methods) if method.name == constant.__INIT__]
        params = init[0][1].arguments if init else class_.attributes

        self.constructor = ConstructorComponent(classname=self.name, params=params)

        if constant.ENUM in class_.bases:
            self.constructor = ConstructorComponent(classname=class_.name, params=[])

        if init and init[0][1].docstrings and (self.class_.docstrings == constant.EMPTY_DESCRIPTION_DOCSTRING or not self.class_.docstrings):
            self.class_.docstrings = init[0][1].docstrings

    def __str__(self):
        attributes_toc: PrettyTable = PrettyTable(field_names=constant.CLASS_ATTRIBUTES_TABLE_FIELDS)

        methods_components: list[MethodComponent] = [MethodComponent(method) for method in self.class_.methods]

        methods = ("\n" + constant.NEW_LINE + "\n").join(
            [str(method_component) for method_component in methods_components if method_component.method.name != constant.__INIT__]
        )

        for attribute in self.class_.attributes:
            attributes_toc.add_row([attribute.name, get_datatype_reference(attribute.type_hint), not attribute.optional, attribute.docstrings])

        return "\n".join(
            [
                str(self.breadcrumbs),
                header1(f"{constant.CLASS} {self.name}"),
                str(self.constructor),
                self.class_.docstrings,
                header2(constant.ATTRIBUTES) if self.class_.attributes else "",
                str(attributes_toc) if self.class_.attributes else "",
                header2(constant.METHODS) if methods else "",
                methods if methods else "",
                header2(constant.INHERITANCE),
                " > ".join(get_datatype_reference(base) if base != self.class_.name else base for base in self.class_.bases),
            ]
        )

    def render(self, output: Path):
        write_file(output / self.file, str(self))


class ModuleComponent:
    module: Module
    breadcrumbs: Breadcrumbs
    file: str

    def __init__(self, module, parent_breadcrumb: Breadcrumbs):
        self.module = module
        self.breadcrumbs = Breadcrumbs(current=f"[{module.name}](./{module.file})", previous=[parent_breadcrumb.breadcrumbs])

    def __str__(self):
        classes_toc: PrettyTable = PrettyTable(field_names=[constant.CLASSES, constant.DESCRIPTION])
        self.module.classes.sort(key=lambda c: c.name)
        for class_ in self.module.classes:
            classes_toc.add_row([f"[{class_.name}]({class_.name}.md)", class_.docstrings])

        return "\n".join(
            [
                str(self.breadcrumbs),
                header1(self.module.name),
                constant.NEW_LINE,
                header2(f"{constant.CLASSES}:"),
                str(classes_toc),
            ]
        )

    def render(self, output_path):
        write_file(output_path / self.module.file, str(self))


class IndexComponent:
    file: str
    namespace: str
    modules: list[ModuleComponent]
    breadcrumbs: Breadcrumbs

    def __init__(self, modules: list[Module] = [], namespace: str = ""):
        self.file = f"index{constant.MARKDOWN_SUFFIX}"
        self.namespace = namespace
        self.breadcrumbs = Breadcrumbs(current=f"[openworld.sdk.{self.namespace}](./{self.file})")
        self.modules = [ModuleComponent(module, self.breadcrumbs) for module in modules]

    def __str__(self):
        toc = PrettyTable(field_names=["Table of Content"])

        for module_doc_page in self.modules:
            toc.add_row([f"[{module_doc_page.module.name}](./{module_doc_page.module.file})"])

        return "\n".join(
            [
                str(self.breadcrumbs),
                header1(f"openworld.sdk.{self.namespace}"),
                f"API documentation for [openworld.sdk.{self.namespace}](https://pypi.org/project/openworld-sdk-python-{self.namespace}/) package",
                header2("Modules"),
                str(toc),
            ]
        )

    def render(self, output_path: Path):
        write_file(output_path / self.file, str(self))


class AliasComponent:
    alias: Alias
    name: str
    file: str
    breadcrumbs: Breadcrumbs

    def __init__(self, alias: Alias, parent_breadcrumbs: Breadcrumbs):
        self.alias = alias
        self.file = f"{self.alias.name}{MARKDOWN_SUFFIX}"
        self.breadcrumbs = self.breadcrumbs = Breadcrumbs(current=f"[{self.alias.name}](./{self.file})", previous=[parent_breadcrumbs.breadcrumbs])
        self.name = self.alias.name

    def __str__(self):
        one_of_table = PrettyTable(field_names=["Types"])
        for type_name in self.alias.one_of:
            one_of_table.add_row([get_datatype_reference(type_name.strip().removeprefix("Union[").removesuffix("]"))])
        return "\n".join([str(self.breadcrumbs), header1(f"Alias {self.alias.name}"), constant.NEW_LINE, constant.ALIAS_DOCSTRINGS, str(one_of_table)])

    def render(self, output_path: Path):
        write_file(output_path / self.file, str(self))


class Documentation:
    index_component: IndexComponent
    modules_components: list[ModuleComponent]
    classes_components: list[ClassComponent]
    alias_components: list[AliasComponent]
    output: Path = Path("./output")

    def __init__(
        self,
        index_component: IndexComponent,
        modules_components: list[ModuleComponent],
        classes_components: list[ClassComponent],
        alias_components: list[AliasComponent],
    ):
        self.index_component = index_component
        self.classes_components = classes_components
        self.modules_components = modules_components
        self.alias_components = alias_components

    def render(self):
        self.index_component.render(self.output)
        for module in self.modules_components:
            module.render(self.output)
        for class_ in self.classes_components:
            class_.render(self.output)
        for alias in self.alias_components:
            alias.render(self.output)