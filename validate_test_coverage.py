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

import json
import math
from textwrap import dedent

from prettytable import PrettyTable

MINIMUM_REQUIRED_COVERAGE_PERCENTAGE: int = 90
FAILURE_MESSAGE_TEMPLATE: str = dedent(
    """
    > Coverage Validation Failed!
    >> Minimum Required Total Coverage Percentage: {0}%
    >> Current Total Coverage Percentage: {1}%
    >>> Full Coverage Report:
    {2}
    """
)
SUCCESS_MESSAGE_TEMPLATE: str = dedent(
    """
    > Coverage Validation Succeed!
    >> Current Total Coverage Percentage: {0}%
    >>> Full Coverage Report:
    {1}
    """
)


def validate_test_coverage(report: dict):
    data: dict = report["totals"]
    current_coverage_percentage: int = int(data["percent_covered_display"])

    data["covered_branches_percentage"] = f"{math.ceil(100 * (data['covered_branches'] / data['num_branches']))}%"
    full_coverage_report_table = PrettyTable(field_names=["Property", "Value"])

    full_coverage_report_table.add_rows([[key, value] for key, value in data.items()])

    if current_coverage_percentage < MINIMUM_REQUIRED_COVERAGE_PERCENTAGE:
        message: str = FAILURE_MESSAGE_TEMPLATE.format(MINIMUM_REQUIRED_COVERAGE_PERCENTAGE, data["percent_covered_display"], str(full_coverage_report_table))
        raise Exception(message)

    else:
        print(SUCCESS_MESSAGE_TEMPLATE.format(current_coverage_percentage, full_coverage_report_table))


with open("coverage.json", "r") as coverage_json_report:
    coverage_report = json.load(coverage_json_report)
    validate_test_coverage(coverage_report)
