from enum import Enum
from fastapi_code_generator import parser as fastapi_code_generator_parser


class ParamTypes(Enum):
    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"
    body = "body"


class Argument(fastapi_code_generator_parser.Argument):
    in_: ParamTypes = None
    alias: str = ""


class Operation(fastapi_code_generator_parser.Operation):
    arguments_list: list[Argument] = []
    snake_case_arguments_list: list[Argument] = []
