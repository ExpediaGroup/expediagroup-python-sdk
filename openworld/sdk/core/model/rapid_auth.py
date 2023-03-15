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

import datetime
from dataclasses import dataclass
from multiprocessing import Lock

import requests
from requests.auth import AuthBase

from openworld.sdk.core.constant import constant, header


@dataclass
class RapidAuthHeader(AuthBase):
    __signature: str
    __api_key: str
    __timestamp: str

    def __init__(self, signature: str, api_key: str, timestamp: str):
        self.__signature = signature
        self.__api_key = api_key
        self.__timestamp = timestamp

    def __call__(self, request: requests.Request = None) -> requests.Request:
        request.headers[header.AUTHORIZATION] = str(self)
        return request

    def __str__(self) -> str:
        return f"{header.EAN} {header.API_KEY}={self.__api_key}," f"{header.SIGNATURE}={self.__signature}," f"{header.TIMESTAMP}={self.__timestamp}"


@dataclass
class RapidToken:
    """A model of an API response."""

    def __init__(self, auth_header: RapidAuthHeader):
        self.__auth_header = auth_header
        self.__expiration_time = datetime.datetime.now() + datetime.timedelta(seconds=constant.RAPID_TOKEN_LIFE_SPAN_IN_SECONDS)

        self.lock: Lock = Lock()

    def update(self, auth_header: RapidAuthHeader):
        self.__auth_header = auth_header
        self.__expiration_time = datetime.datetime.now() + datetime.timedelta(seconds=constant.RAPID_TOKEN_LIFE_SPAN_IN_SECONDS)

    def is_expired(self):
        return datetime.datetime.now() >= self.__expiration_time

    def is_about_expired(self):
        return datetime.datetime.now() + datetime.timedelta(seconds=constant.REFRESH_TOKEN_TIME_GAP_IN_SECONDS) >= self.__expiration_time

    @property
    def access_token(self):
        return str(self.__auth_header)

    @property
    def auth_header(self):
        return self.__auth_header
