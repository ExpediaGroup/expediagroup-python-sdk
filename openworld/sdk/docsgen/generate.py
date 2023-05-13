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

from openworld.sdk.docsgen.docs import *


def generate(namespace: str, output: Path, modules: list[Module]):
    output.mkdir(exist_ok=True)
    index_component = IndexComponent(namespace=namespace, modules=modules)
    classes_components = []
    aliases_components = []

    for module_component in index_component.modules:
        module = module_component.module
        for class_ in module.classes:
            classes_components.append(ClassComponent(class_=class_, parent_breadcrumb=module_component.breadcrumbs))
        for alias in module.aliases:
            aliases_components.append(AliasComponent(alias, module_component.breadcrumbs))

    index_component.render(output)
    for module in index_component.modules:
        module.render(output)
    for class_ in classes_components:
        class_.render(output)
    for alias in aliases_components:
        alias.render(output)
