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
import ast
import re
import typing
from pathlib import Path

from openworld.sdk.docsgen.constant import CONSTR, MARKDOWN_SUFFIX


def process_new_lines(text: str) -> str:
    # TODO: Improve to which lines and how the <br> tag is added.
    text = text.strip()
    while "\n\n" in text:
        text = text.replace("\n\n", "\n")
    return text.replace("\n", "<br/>")


def __remove_constr(datatype: str):
    """TODO: Cases the algorithm fails on:
    - Union[constr(...), Dict[Model, constr(...)]]: This will remove the `Model` alongside the right constr.
    """
    if CONSTR not in datatype:
        return datatype

    left_index, right_index = datatype.find(CONSTR + "("), len(datatype) - 1

    while datatype[right_index] != ")" and right_index > left_index:
        right_index -= 1

    if left_index == right_index:
        return datatype

    return datatype.replace(datatype[left_index : right_index + 1], "")


def has_class_definition(type_hint: str):
    for index, char in enumerate(type_hint):
        if char.isupper() and index + 3 < len(type_hint) and type_hint[index : index + 4] != "None":
            return True
    return False


def remove_builtin_type_aliases(datatype: str) -> list[str]:
    builtin_type_aliases = [
        "Optional",
        "Union",
        "Set",
        "Dict",
        "List",
        "ChainMap",
        "Counter",
        "DefaultDict",
        "OrderedDict",
        "FrozenSet",
        "NamedTuple",
        "TypedDict",
        "Generator",
        "Literal",
    ]
    generic_datatypes = ["None", "Any", "AnyUrl", "Enum", "BaseModel", "ClientConfig"]

    datatype = datatype.strip().replace(" ", "")

    has_type_alias = True
    while has_type_alias:
        has_type_alias = False

        for type_alias in builtin_type_aliases:
            if datatype.startswith(type_alias + "["):
                has_type_alias = True
                datatype = datatype.removeprefix(type_alias + "[")

            elif datatype.endswith("]"):
                while datatype.endswith("]"):
                    datatype = datatype.removesuffix("]")

    if "constr" in datatype:
        datatype = __remove_constr(datatype)

    result: list[str] = []
    if "," in datatype:
        datatype = datatype.split(",")
        for index, value in enumerate(datatype):
            processed_datatype = remove_builtin_type_aliases(value)
            datatype[index] = processed_datatype[0] if processed_datatype else ""

        for _, value in enumerate(datatype):
            if value and value not in generic_datatypes and value[0].isupper():
                result.append(value)

    else:
        result = [datatype] if datatype and datatype not in generic_datatypes and datatype[0].isupper() else []

    return result


def add_reference_to_datatype(datatype: str, to_add_reference: str):
    reference = f"[{to_add_reference}]({to_add_reference}{MARKDOWN_SUFFIX})"
    length = len(to_add_reference)

    if len(datatype) == length:
        return reference

    for index in [word.start() for word in re.finditer(to_add_reference, datatype)]:
        if index == 0 and not datatype[length].isalpha():
            return reference + datatype[length::]
        elif index + length == len(datatype) and not datatype[index - 1].isalpha():
            return datatype[:index] + reference
        elif not datatype[index - 1].isalpha() and not datatype[index + length].isalpha():
            return datatype[:index] + reference + datatype[index + length :]
    return datatype


def get_datatype_reference(datatype: str) -> typing.Union[None, str]:
    if not datatype:
        return

    processed_datatype = remove_builtin_type_aliases(datatype)
    if not processed_datatype:
        return datatype

    for _, type_hint in enumerate(processed_datatype):
        # TODO: Find a more decent way to add reference instead of string replacement.

        datatype = add_reference_to_datatype(datatype, type_hint)

    return datatype


def extract_types(node) -> list[ast.Name]:
    if isinstance(node, ast.Constant):
        return []

    if isinstance(node, ast.Name):
        return [node]

    result = []
    if isinstance(node, ast.Tuple):
        for item in node.elts:
            result += extract_types(item)

    if isinstance(node, ast.Subscript):
        result += extract_types(node.value)
        result += extract_types(node.slice)

    return result


def write_file(path: Path, content: str):
    path.touch(exist_ok=True)
    with open(path, "w") as file:
        file.write(content)


def header1(content: str):
    return "# " + content


def header2(content: str):
    return "## " + content


def header3(content: str):
    return "### " + content


def header4(content: str):
    return "#### " + content


def bullet_points(points: list[str]):
    return "\n".join([f"+ {point}" for point in points])
