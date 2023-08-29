from pathlib import Path

import typer

from openworld.sdk.docsgen.generate import generate
from openworld.sdk.docsgen.models import Module
from openworld.sdk.docsgen.parse import parse

app = typer.Typer()


@app.command()
def main(
    namespace: str = typer.Option(..., "--namespace", "-n"),
    package: Path = typer.Option(..., "--package-path", "-p"),
    output: Path = typer.Option(Path("./documentation"), "--output-path", "-o"),
):
    modules: list[Module] = parse(package_path=package)
    generate(
        namespace=namespace,
        output=output,
        modules=modules,
    )


if __name__ == "__main__":
    main()
