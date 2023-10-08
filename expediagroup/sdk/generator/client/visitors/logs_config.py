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
import collections
from pathlib import Path

from fastapi_code_generator.parser import OpenAPIParser
from fastapi_code_generator.visitor import Visitor


def get_omitted_log_fields() -> collections.defaultdict[str, list[str]]:
    r"""Returns a static dict mapping of models and attributes to omit when serializing objects for logging.

    Returns:
        dict[str, list[str]]
    """
    return collections.defaultdict(
        list,
        {
            "CreditCard": [
                "card_number",
                "card_cvv_response",
                "card_avs_response",
            ],
            "GiftCard": [
                "pin",
            ],
            "DirectDebit": [
                "account_number",
            ],
        },
    )


def get_logs_config(parser: OpenAPIParser, model_path: Path) -> dict[str, object]:
    return {"omitted_log_fields": get_omitted_log_fields()}


visit: Visitor = get_logs_config
