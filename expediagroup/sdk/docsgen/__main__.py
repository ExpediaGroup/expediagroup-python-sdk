from pathlib import Path
from typing import Optional

import typer
from pydoc_markdown.contrib.loaders.python import PythonLoader
from pydoc_markdown.interfaces import Context

from expediagroup.sdk.docsgen.generator import ExpediaGroupDocumentationGenerator

app = typer.Typer()


def main(
    package_path: Path = typer.Option(..., "--package-path", "-p"),
    templates_path: Optional[Path] = typer.Option(None, "--templates-path", "-t"),
    output_path: Optional[Path] = typer.Option(Path(".."), "--output-path", "-o")
):
    context = Context(directory=str(package_path.absolute()))
    loader = PythonLoader(search_path=[str(package_path.absolute())])

    generator: ExpediaGroupDocumentationGenerator = ExpediaGroupDocumentationGenerator(
        context=context,
        loader=loader,
        templates_path=templates_path,
    )

    generator.generate(output_path=output_path)


if __name__ == '__main__':
    typer.run(main)
