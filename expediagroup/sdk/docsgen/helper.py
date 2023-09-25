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
