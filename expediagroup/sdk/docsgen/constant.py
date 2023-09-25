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

OPTIONAL: str = "Optional"

ARGS_DOCSTRINGS_HEADER: str = "Args:"

INIT_METHOD: str = "__init__"

TEMPLATES_DIR: str = "templates"

UTF8: str = "utf8"

NULL_DESCRIPTION: str = "..."

EMPTY_STRING: str = ""

NEW_LINE: str = "\n"


class TemplateFileNames:
    CLASS: str = "class.jinja2"
    MASTER: str = "master.jinja2"
    MODULE: str = "module.jinja2"


class DefaultNames:
    MASTER_FILE_NAME: str = "index"


class Jinja2EnvironmentVariables:
    CLASS: str = "class"
    MODULE: str = "module"
    MODULES: str = "modules"
    BREADCRUMBS: str = "breadcrumbs"


class FileExtensions:
    MARKDOWN: str = ".md"
