import re
from pathlib import Path

import docstring_parser
from docstring_parser.parser import parse


def to_markdown_file_ref(filename: str) -> str:
    """Converts a filename to a markdown file reference.

    Args:
        filename (str): The name of the file (without the extension).

    Returns:
        str: A markdown link referencing the file.
    """
    return "[{0}]({0}.md)".format(filename)


def parse_method_description_docstrings(description: str | None) -> str:
    """Parses the description docstring and extracts the longest description between short and long description.

    Args:
        description (str | None): The description docstring to be parsed. It can be None.

    Returns:
        str: The longest description parsed from the docstring, or an empty string if description is None or empty.
    """
    if not description:
        return ""

    docstring = parse(str(description), docstring_parser.Style.GOOGLE)
    return max(
        docstring.long_description if docstring.long_description else "",
        docstring.short_description if docstring.short_description else "",
        key=len
    )


def write_markdown_file(path: Path, filename: str, content: str) -> None:
    """Writes content to a markdown file in the specified path with the given filename.

    Args:
        path (Path): The path where the file will be created.
        filename (str): The name of the file (without the extension).
        content (str): The content to write to the file.
    """
    file = f"{str(path.absolute())}/{filename}.md"
    with open(file, "w+") as markdown_file:
        markdown_file.write(content)


def replace_word(text: str, word: str, replacement: str) -> str:
    """Replaces occurrences of a word in a text with the specified replacement, considering word boundaries.

    Args:
        text (str): The original text.
        word (str): The word to replace.
        replacement (str): The word to replace the original word with.

    Returns:
        str: The modified text with the word replaced.
    """
    if len(word) > len(text):
        return text

    index_change_value: int = 0
    index_change_ratio: int = len(replacement) - len(word)

    for index in [w.start() for w in re.finditer(word, text)]:
        index += index_change_value
        if index == 0 and not text[len(word)].isalnum():
            text = replacement + text[len(word)::]
            index_change_value += index_change_ratio

        elif index + len(word) == len(text) and not text[index - 1].isalnum():
            text = text[:index] + replacement
            index_change_value += index_change_ratio

        elif not text[index - 1].isalpha() and not text[index + len(word)].isalnum():
            text = text[:index] + replacement + text[index + len(word):]
            index_change_value += index_change_ratio

    return text
