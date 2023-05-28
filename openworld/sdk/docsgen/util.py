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


def replace_new_lines_with_br_tag(text: str) -> str:
    r"""Replaces new lines in a text with `<br/>` tag.

    Args:
        text(str): Text to replace new lines with tags in.

    Returns:

    """
    # TODO: Improve to which lines and how the <br/> tag is added.
    text = text.strip()
    while "\n\n" in text:
        text = text.replace("\n\n", "\n")
    return text.replace("\n", "<br/>")


def __remove_constr(datatype: str):
    r"""

    Args:
        datatype:

    Returns:

    """
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


def remove_builtin_type_aliases(type_hint: str) -> list[str]:
    r"""Removes builtin types and those included in the `typing` library from a given type hint.

    Args:
        type_hint(str): Type hint to remove builtin types from.

    Returns:
        str: Cleaned type hint.
    """
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

    type_hint = type_hint.strip().replace(" ", "")

    has_type_alias = True
    while has_type_alias:
        has_type_alias = False

        for type_alias in builtin_type_aliases:
            if type_hint.startswith(type_alias + "["):
                has_type_alias = True
                type_hint = type_hint.removeprefix(type_alias + "[")

            elif type_hint.endswith("]"):
                while type_hint.endswith("]"):
                    type_hint = type_hint.removesuffix("]")

    if "constr" in type_hint:
        type_hint = __remove_constr(type_hint)

    result: list[str] = []
    if "," in type_hint:
        type_hint = type_hint.split(",")
        for index, value in enumerate(type_hint):
            processed_datatype = remove_builtin_type_aliases(value)
            type_hint[index] = processed_datatype[0] if processed_datatype else ""

        for _, value in enumerate(type_hint):
            if value and value not in generic_datatypes and value[0].isupper():
                result.append(value)

    else:
        result = [type_hint] if type_hint and type_hint not in generic_datatypes and type_hint[0].isupper() else []

    return result


def add_markdown_reference_to_datatype(type_hint: str, referenced_datatype: str) -> str:
    r"""Replaces all datatype occurrences in a type hint, with a markdown reference to a file with the same name as
    `referenced_datatype`.

    Examples:
        1. SomeModel -> [SomeModel](SomeModel.md)
        2. Union[SomeModel, str] -> Union[[SomeModel](SomeModel.md), str]
        3. dict[list[SomeModel], dict[int, Any]] -> dict[list[[SomeModel](SomeModel.md)], dict[int, Any]]

    Args:
        type_hint(str): Original type hint to process.
        referenced_datatype(str): Data type to be referenced in markdown.

    Returns:
        str: Processed type hint.
    """
    reference = f"[{referenced_datatype}]({referenced_datatype}{MARKDOWN_SUFFIX})"
    length = len(referenced_datatype)

    if len(type_hint) == length:
        return reference

    for index in [word.start() for word in re.finditer(referenced_datatype, type_hint)]:
        if index == 0 and not type_hint[length].isalpha():
            return reference + type_hint[length::]
        elif index + length == len(type_hint) and not type_hint[index - 1].isalpha():
            return type_hint[:index] + reference
        elif not type_hint[index - 1].isalpha() and not type_hint[index + length].isalpha():
            return type_hint[:index] + reference + type_hint[index + length:]
    return type_hint


def get_datatype_reference(datatype: str) -> typing.Union[None, str]:
    r"""Gets the datatype markdown reference string if it has one.

    Args:
        datatype(str): Given datatype.

    Returns:
        str | None: Datatype string referencing a markdown file, or the datatype itself in case it has no documented
            representation.
    """
    if not datatype:
        return

    processed_datatype = remove_builtin_type_aliases(datatype)
    if not processed_datatype:
        return datatype

    for _, type_hint in enumerate(processed_datatype):
        # TODO: Find a more decent way to add reference instead of string replacement.
        # TODO: Keep track of parsed classes & aliases, and add reference if they exist.

        datatype = add_markdown_reference_to_datatype(datatype, type_hint)

    return datatype


def extract_types(node: ast.AST) -> list[ast.Name]:
    r"""Extracts all type hints (datatypes) from an AST node.

    Args:
        node(ast.AST): Parsed `AST` node.

    Returns:
        list[ast.Name]: List of `ast.Name` nodes representing type hints.
    """
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
    r"""Writes a text content into a file with a given path. A new file is created in case its non-existent.

    Args:
        path(Path): Path of file to write into.
        content(str): Text content to write into a file.
    """
    path.touch(exist_ok=True)
    with open(path, "w") as file:
        file.write(content)


def header1(text: str):
    r"""Converts a given text into Markdown heading level 1.

    Args:
        text(str): Given text to convert.

    Returns:
        str: Text as a Markdown header.
    """
    return "# " + text


def header2(text: str):
    r"""Converts a given text into Markdown heading level 2.

    Args:
        text(str): Given text to convert.

    Returns:
        str: Text as a Markdown header.
    """
    return "## " + text


def header3(text: str):
    r"""Converts a given text into Markdown heading level 3.

    Args:
        text(str): Given text to convert.

    Returns:
        str: Text as a Markdown header.
    """
    return "### " + text


def header4(text: str):
    r"""Converts a given text into Markdown heading level 4.

    Args:
        text(str): Given text to convert.

    Returns:
        str: Text as a Markdown header.
    """
    return "#### " + text


def bullet_points(points: list[str]):
    r"""Formats a list of strings into a Markdown bullet points list.

    Args:
        points(list[str]): List of strings to format.

    Returns:
        str: Markdown formatted bullet points.
    """
    return "\n".join([f"+ {point}" for point in points])
