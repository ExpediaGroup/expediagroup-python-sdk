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

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import constant
from jinja2 import Environment, FileSystemLoader, Template
from model import Breadcrumbs, Document, DocumentedObject, Master, Module
from util import write_markdown_file


@dataclass
class MarkdownRenderer:
    r"""A renderer class for generating markdown documentation from module, class and master instances.

    Attributes:
        master (Master): A Master object that contains the master documentation details.
        modules (list[Module]): A list of Module objects representing the modules to be documented.
        environment (Environment): A Jinja2 environment instance to manage templates.
        helpers (dict[str, Any]): A dictionary of helper functions to assist in rendering.
        resolvers (dict[str, Any]): A dictionary of resolver functions to assist in rendering.
        master_filename (str): The filename for the master documentation file.
    """

    master: Master
    modules: list[Module]
    environment: Environment
    helpers: dict[str, Any]
    resolvers: dict[str, Any]
    master_filename: str
    package_name: str

    def __init__(
        self,
        modules: list[Module],
        master: Master,
        package_name: str,
        master_filename: str,
        templates_path: Path = Path(__file__).parent / constant.TEMPLATES_DIR,
        helpers: dict[str, Any] = dict(),  # noqa
        resolvers: dict[str, Any] = dict(),  # noqa
    ):
        """Initializes the MarkdownRenderer instance with the given parameters.

        Args:
            modules (list[Module]): List of modules to be documented.
            master (Master): The master documentation instance.
            master_filename (str): The filename for the master documentation file.
            templates_path (Path): The path to the directory containing Jinja2 templates.
            helpers (dict[str, Any]): Dictionary of helper functions to assist in rendering.
            resolvers (dict[str, Any]): Dictionary of resolver functions to assist in rendering.
        """
        self.package_name = package_name
        self.master = master
        self.master_filename = master_filename.removesuffix(constant.FileExtensions.MARKDOWN)

        self.modules = modules
        self.helpers = helpers
        self.resolvers = resolvers
        self.environment = Environment(loader=FileSystemLoader(searchpath=templates_path, encoding=constant.UTF8))

        self.__post_init__()

    def __post_init__(self):
        """Called after the object is initialized to setup additional initial configurations."""
        self.__init_breadcrumbs()

    def render(self, output_path: Path):
        """Renders the documentation to markdown files and writes them to the specified output path.

        Args:
            output_path (Path): The path where the rendered markdown files should be saved.
        """
        output_path.mkdir(exist_ok=True)

        for name, documentation in self.render_modules().items():
            write_markdown_file(path=output_path, filename=name, content=documentation)

        for name, documentation in self.render_classes().items():
            write_markdown_file(path=output_path, filename=name, content=documentation)

        write_markdown_file(path=output_path, filename=self.master_filename, content=self.render_master())

    def render_modules(self) -> dict[str, str]:
        """Renders the documentation for each module to markdown.

        Returns:
            dict[str, str]: A dictionary mapping module names to their rendered markdown content.
        """
        template: Template = self.environment.get_template(constant.TemplateFileNames.MODULE)
        rendered_modules: dict[str, str] = dict()

        for module in self.modules:
            environment_args: dict[str, Any] = {
                constant.Jinja2EnvironmentVariables.MODULE: module,
                constant.Jinja2EnvironmentVariables.BREADCRUMBS: module.breadcrumbs,
            }
            self.setup_jinja_environment_arguments(environment_arguments=environment_args)

            rendered_modules[module.name] = template.render(environment_args)

        return rendered_modules

    def render_classes(self) -> dict[str, str]:
        """Renders the documentation for each class in each module to markdown.

        Returns:
            dict[str, str]: A dictionary mapping class names to their rendered markdown content.
        """
        template: Template = self.environment.get_template(constant.TemplateFileNames.CLASS)
        rendered_classes: dict[str, str] = dict()

        for module in self.modules:
            if not module.classes:
                continue

            for class_ in module.classes:
                environment_args: dict[str, DocumentedObject] = {
                    constant.Jinja2EnvironmentVariables.MODULE: module,
                    constant.Jinja2EnvironmentVariables.CLASS: class_,
                    constant.Jinja2EnvironmentVariables.BREADCRUMBS: class_.breadcrumbs,
                }
                self.setup_jinja_environment_arguments(environment_arguments=environment_args)

                rendered_classes[class_.name] = template.render(environment_args)

        return rendered_classes

    def render_master(self) -> str:
        """Renders the master documentation to markdown.

        Returns:
            str: The rendered markdown content for the master documentation.
        """
        template: Template = self.environment.get_template(constant.TemplateFileNames.MASTER)

        environment_args: dict[str, DocumentedObject] = {
            constant.Jinja2EnvironmentVariables.MODULES: self.master.modules,
            constant.Jinja2EnvironmentVariables.BREADCRUMBS: self.master.breadcrumbs,
            constant.Jinja2EnvironmentVariables.PACKAGE: self.package_name,
        }
        self.setup_jinja_environment_arguments(environment_arguments=environment_args)

        return template.render(environment_args)

    def setup_jinja_environment_arguments(self, environment_arguments: dict[str, Any]) -> None:
        """Sets up additional arguments for the Jinja2 environment before rendering.

        Args:
            environment_arguments (dict[str, Any]): Dictionary of arguments to be passed to the Jinja2 environment.
        """
        environment_arguments.update(self.helpers)
        environment_arguments.update(self.resolvers)

    def __init_breadcrumbs(self):
        """Initializes breadcrumb structures for modules and classes to facilitate navigation in the documentation."""
        dfs_stack: list = list()
        current_parent: Document = self.master

        for module in Master.parse_master_modules(modules=self.modules):
            module.breadcrumbs = Breadcrumbs(document_name=module.name, parent=current_parent.breadcrumbs)
            dfs_stack.append(module)

        while dfs_stack:
            module = dfs_stack.pop()
            for submodule in module.submodules:
                submodule.breadcrumbs = Breadcrumbs(document_name=submodule.name, parent=module.breadcrumbs)

            for class_ in module.classes:
                class_.breadcrumbs = Breadcrumbs(document_name=class_.name, parent=module.breadcrumbs)
