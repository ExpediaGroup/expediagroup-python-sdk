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

import requests

from openworld.sdk.core.constant import constant, log


def response_log(response: requests.Response):
    headers: dict = response.headers
    headers_log: str = constant.EMPTY_STRING

    for key, value in headers.items():
        headers_log += f"\t\t{key}: {value}\n"

    if not headers_log.endswith("\n"):
        headers_log += "\n"

    result: str = (
        "\nResponse:\n" + log.HTTP_HEADERS_LOG_MESSAGE_TEMPLATE.format(headers_log) + log.HTTP_BODY_LOG_MESSAGE_TEMPLATE.format("\t\t" + response.text + "\n")
    )

    return result


def request_log(headers: dict, body: str, endpoint: str, method: str, response: requests.Response):
    headers_log: str = constant.EMPTY_STRING

    for key, value in headers.items():
        headers_log += f"\t\t{key}: {value}\n"

    if not headers_log.endswith("\n"):
        headers_log += "\n"

    result = f"\nRequest: {endpoint}\n" f"Method: {method.upper()}\n" + log.HTTP_HEADERS_LOG_MESSAGE_TEMPLATE.format(
        headers_log
    ) + log.HTTP_BODY_LOG_MESSAGE_TEMPLATE.format("\t\t" + body + "\n") + response_log(response)

    return result


def filter_credentials(data: dict):
    new_data = dict()
    filter_keys = ["key", "secret", "username", "password"]
    for key, value in data.items():
        for word in filter_keys:
            if word.lower() in key.lower():
                new_data[key] = "<-- omitted -->"
                break
            new_data[key] = value
    return new_data
