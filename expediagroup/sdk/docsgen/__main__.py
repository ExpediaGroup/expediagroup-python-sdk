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
import os
from pathlib import Path
from typing import Optional

import typer
from pydoc_markdown.contrib.loaders.python import PythonLoader
from pydoc_markdown.interfaces import Context

from generator import ExpediaGroupDocumentationGenerator

app = typer.Typer()


def main(
    package_name: str = typer.Option(..., "--package-name", "-n"),
    package_path: Path = typer.Option(..., "--package-path", "-p"),
    templates_path: Optional[Path] = typer.Option(None, "--templates-path", "-t"),
    output_path: Optional[Path] = typer.Option(Path(".."), "--output-path", "-o"),
):
    print(Path().absolute())
    print(os.listdir(Path()))
    context = Context(directory=str(package_path.absolute()))
    loader = PythonLoader(search_path=[str(package_path.absolute())])

    generator: ExpediaGroupDocumentationGenerator = ExpediaGroupDocumentationGenerator(
        context=context,
        loader=loader,
        templates_path=templates_path,
        package_name=package_name,
    )

    generator.generate(output_path=output_path)


if __name__ == "__main__":
    typer.run(main)
