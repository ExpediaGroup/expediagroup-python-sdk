from pathlib import Path
from typing import Dict, Optional

from datamodel_code_generator.imports import Import, Imports
from datamodel_code_generator.reference import Reference
from datamodel_code_generator.types import DataType

from fastapi_code_generator.parser import OpenAPIParser
from fastapi_code_generator.visitor import Visitor


def _get_most_of_reference(data_type: DataType) -> Optional[Reference]:
    if data_type.reference:
        return data_type.reference
    for data_type in data_type.data_types:
        reference = _get_most_of_reference(data_type)
        if reference:
            return reference
    return None


def get_imports(parser: OpenAPIParser, model_path: Path) -> Dict[str, object]:
    imports = Imports()

    imports.update(parser.imports)
    for data_type in parser.data_types:
        reference = _get_most_of_reference(data_type)
        if reference:
            imports.append(data_type.all_imports)
            imports.append(
                Import.from_full_path(f'.{model_path.stem}.{reference.name}')
            )
    # openworld: refactor fastapi_imports to parameter_imports.
    for from_, imports_ in parser.parameter_imports.items():
        imports[from_].update(imports_)
    return {'imports': imports}


visit: Visitor = get_imports
