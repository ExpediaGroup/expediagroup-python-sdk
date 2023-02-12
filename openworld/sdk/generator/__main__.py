from pathlib import Path
from typing import Any, Dict, List, Optional

import typer
from datamodel_code_generator import LiteralType, PythonVersion, chdir
from datamodel_code_generator.format import CodeFormatter
from fastapi_code_generator.__main__ import (MODEL_PATH,
                                             BUILTIN_TEMPLATE_DIR,
                                             dynamic_load_module,
                                             app
                                             )
from fastapi_code_generator.visitor import Visitor
from jinja2 import Environment, FileSystemLoader

from parser import OpenApiParser


def generate_code(
    input_name: str,
    input_text: str,
    output_dir: Path,
    template_dir: Optional[Path],
    model_path: Optional[Path] = None,
    enum_field_as_literal: Optional[str] = None,
    custom_visitors: Optional[List[Path]] = [],
) -> None:
    if not model_path:
        model_path = MODEL_PATH
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    if not template_dir:
        template_dir = BUILTIN_TEMPLATE_DIR
    if enum_field_as_literal:
        parser = OpenApiParser(input_text, enum_field_as_literal=enum_field_as_literal)
    else:
        parser = OpenApiParser(input_text)
    with chdir(output_dir):
        models = parser.parse()
    if not models:
        return
    elif isinstance(models, str):
        output = output_dir / model_path
        modules = {output: (models, input_name)}
    else:
        raise Exception('Modular references are not supported in this version')

    environment: Environment = Environment(
        loader=FileSystemLoader(
            template_dir if template_dir else f"{Path(__file__).parent}/template",
            encoding="utf8",
        ),
    )

    results: Dict[Path, str] = {}
    code_formatter = CodeFormatter(PythonVersion.PY_38, Path().resolve())

    template_vars: Dict[str, object] = {"info": parser.parse_info()}
    visitors: List[Visitor] = []

    # Load visitors
    BUILTIN_VISITOR_DIR = Path(__file__).parent / "visitors"
    builtin_visitors = BUILTIN_VISITOR_DIR.rglob("*.py")
    visitors_path = [*builtin_visitors, *(custom_visitors if custom_visitors else [])]
    for visitor_path in visitors_path:
        module = dynamic_load_module(visitor_path)
        if hasattr(module, "visit"):
            visitors.append(module.visit)
        else:
            raise Exception(f"{visitor_path.stem} does not have any visit function")

    # Call visitors to build template_vars
    for visitor in visitors:
        visitor_result = visitor(parser, model_path)
        template_vars = {**template_vars, **visitor_result}

    for target in template_dir.rglob("*"):
        relative_path = target.relative_to(template_dir)
        template = environment.get_template(str(relative_path))
        result = template.render(template_vars)
        results[relative_path] = code_formatter.format_code(result)

    for path, code in results.items():
        with output_dir.joinpath(path.with_suffix(".py")).open("wt") as file:
            print(code.rstrip(), file=file)

    for path, body_and_filename in modules.items():
        body, filename = body_and_filename
        if path is None:
            file = None
        else:
            if not path.parent.exists():
                path.parent.mkdir(parents=True)
            file = path.open('wt', encoding='utf8')

        if body:
            print('', file=file)
            print(body.rstrip(), file=file)

        if file is not None:
            file.close()


@app.command()
def main(
    input_file: typer.FileText = typer.Option(..., "--input", "-i"),
    output_dir: Path = typer.Option(..., "--output", "-o"),
    model_file: str = typer.Option(None, "--model-file", "-m"),
    template_dir: Optional[Path] = typer.Option(None, "--template-dir", "-t"),
    enum_field_as_literal: Optional[LiteralType] = typer.Option(
        None, "--enum-field-as-literal"
    ),
    custom_visitors: Optional[List[Path]] = typer.Option(
        None, "--custom-visitor", "-c"
    ),
) -> None:
    input_name: str = input_file.name
    input_text: str = input_file.read()
    if model_file:
        model_path = Path(model_file).with_suffix('.py')
    else:
        model_path = MODEL_PATH

    if enum_field_as_literal:
        return generate_code(
            input_name,
            input_text,
            output_dir,
            template_dir,
            model_path,
            enum_field_as_literal,
        )
    return generate_code(
        input_name,
        input_text,
        output_dir,
        template_dir,
        model_path,
        custom_visitors=custom_visitors,
    )


if __name__ == '__main__':
    typer.run(main)
