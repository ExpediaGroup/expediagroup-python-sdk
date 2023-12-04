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
import time
from hashlib import sha512
from http import HTTPStatus

import pydantic.schema
import requests

from expediagroup.sdk.core.constant import constant
from expediagroup.sdk.core.model.authentication import Credentials
from expediagroup.sdk.core.model.rapid_auth import RapidAuthHeader, RapidToken

VALID_KEY: str = "valid_key"

VALID_SECRET: str = "valid_secret"

VALID_CREDENTIALS: Credentials = Credentials(key=VALID_KEY, secret=VALID_SECRET)

INVALID_KEY: str = "invalid_key"

INVALID_SECRET: str = "invalid_secret"

INVALID_CREDENTIALS: Credentials = Credentials(key=INVALID_KEY, secret=INVALID_SECRET)

AUTH_ENDPOINT = "https://auth.example.com/"

ENDPOINT = "https://www.example.com/"

ACCESS_TOKEN = "access_token"

EXPIRES_IN = "expires_in"

SCOPE = "scope"

TOKEN_TYPE = "token_type"

ID_TOKEN = "id_token"

REFRESH_TOKEN = "refresh_token"

TOKEN_EXPIRES_IN_SECONDS = 30 * 60

TOKEN_RESPONSE_DATA = {
    ACCESS_TOKEN: ACCESS_TOKEN,
    EXPIRES_IN: TOKEN_EXPIRES_IN_SECONDS,
    SCOPE: SCOPE,
    TOKEN_TYPE: TOKEN_TYPE,
    ID_TOKEN: ID_TOKEN,
    REFRESH_TOKEN: REFRESH_TOKEN,
}

TIMESTAMP = str(int(time.time()))

SIGNATURE: str = sha512(f"{VALID_KEY}{VALID_SECRET}{TIMESTAMP}".encode(encoding=constant.UTF8)).hexdigest()

RAPID_AUTH_HEADER_OBJECT = RapidAuthHeader(signature=SIGNATURE, api_key=VALID_KEY, timestamp=TIMESTAMP)

RAPID_TOKEN_OBJECT = RapidToken(RAPID_AUTH_HEADER_OBJECT)


class MockResponse:
    @staticmethod
    def default_token_response():
        response = requests.Response()

        response.status_code = HTTPStatus.OK
        response.url = AUTH_ENDPOINT
        response.code = "ok"
        response._content = json.dumps(TOKEN_RESPONSE_DATA.copy()).encode()

        return response

    @staticmethod
    def eleven_seconds_expiration_token_response():
        response = requests.Response()
        response.status_code = HTTPStatus.OK
        response.url = AUTH_ENDPOINT
        response.code = "ok"

        content = TOKEN_RESPONSE_DATA.copy()
        content[EXPIRES_IN] = 11
        response._content = json.dumps(content).encode()
        return response

    @staticmethod
    def unauthorized_token_response() -> requests.Response:
        response = requests.Response()
        response.status_code = HTTPStatus.UNAUTHORIZED
        response.url = AUTH_ENDPOINT
        response.code = "Unauthorized"
        response._content = "Unauthorized".encode()
        return response
