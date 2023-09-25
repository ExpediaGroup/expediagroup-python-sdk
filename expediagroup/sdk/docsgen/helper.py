from typing import Any

from markdown_prettytable import PrettyTable


def table(field_names: list[str], rows: list[list[str]]):
    r"""Generates a markdown table using PrettyTable.

    Args:
        field_names (list[str]): The list of field names (column names) for the table.
        rows (list[list[str]]): A list of lists where each inner list contains values for a row in the table.

    Returns:
        PrettyTable: An instance of PrettyTable initialized with the field names and rows.
    """
    markdown_table: PrettyTable = PrettyTable(field_names=field_names)
    for row in rows:
        markdown_table.add_row(row)
    return markdown_table


helpers: dict[str, Any] = {"table": table}
