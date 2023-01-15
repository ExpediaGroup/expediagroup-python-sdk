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

MINIMUM_REQUIRED_COVERAGE_PERCENTAGE: int = 90
FAILURE_MESSAGE_TEMPLATE: str = 'Coverage Validation Failed!\n' \
                                'Minimum Required Coverage Percentage: {0}%\n' \
                                'Current Coverage Percentage: {1}%'
SUCCESS_MESSAGE_TEMPLATE: str = 'Coverage Validation Succeed!\n' \
                                'Current Coverage Percentage: {0}%'


def validate_test_coverage(report: dict):
    data: dict = report['totals']
    current_coverage_percentage: int = math.ceil(int(data['percent_covered']))

    if current_coverage_percentage < MINIMUM_REQUIRED_COVERAGE_PERCENTAGE:
        message: str = FAILURE_MESSAGE_TEMPLATE.format(
            MINIMUM_REQUIRED_COVERAGE_PERCENTAGE,
            int(data['percent_covered'])
        )
        raise Exception(message)

    else:
        print(SUCCESS_MESSAGE_TEMPLATE.format(current_coverage_percentage))


with open('coverage.json', 'r') as coverage_json_report:
    coverage_report = json.load(coverage_json_report)
    validate_test_coverage(coverage_report)
