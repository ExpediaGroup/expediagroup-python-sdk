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
import logging
from dataclasses import dataclass
from multiprocessing import Lock
from typing import Optional

import pydantic.schema
import requests
from requests.auth import AuthBase

from openworld.sdk.core.constant import header, log
from openworld.sdk.core.constant.constant import REFRESH_TOKEN_TIME_GAP_IN_SECONDS

LOG = logging.getLogger(__name__)


@dataclass
class Credentials:
    """A pair of client key and secret."""

    key: str
    secret: str


class _TokenResponse(pydantic.BaseModel):
    """A model of an API response."""

    access_token: str
    expires_in: int
    scope: str
    token_type: str
    id_token: Optional[str] = None
    refresh_token: Optional[str] = None


class Token:
    def __init__(self, data: dict):
        r"""Represents a token model.

        :param data: token data
        """
        self.__token: _TokenResponse = _TokenResponse.parse_obj(data)
        self.lock = Lock()
        self.__expiration_time = datetime.datetime.now() + datetime.timedelta(seconds=self.__token.expires_in)
        self.__auth_header = HttpBearerAuth(self.__token.access_token)

        LOG.info(log.OPENWORLD_LOG_MESSAGE_TEMPLATE.format(log.NEW_TOKEN_EXPIRATION_TEMPLATE.format(str(self.__token.expires_in))))

    @property
    def refresh_token(self) -> str:
        return self.__token.refresh_token

    @property
    def access_token(self) -> str:
        return self.__token.access_token

    @property
    def id_token(self) -> str:
        return self.__token.id_token

    @property
    def auth_header(self) -> AuthBase:
        return self.__auth_header

    def is_expired(self):
        return datetime.datetime.now() >= self.__expiration_time

    def is_about_expired(self):
        return datetime.datetime.now() + datetime.timedelta(seconds=REFRESH_TOKEN_TIME_GAP_IN_SECONDS) >= self.__expiration_time

    def update(self, data: dict):
        self.__token = _TokenResponse.parse_obj(data)
        self.__expiration_time = datetime.datetime.now() + datetime.timedelta(seconds=self.__token.expires_in)


class HttpBearerAuth(AuthBase):
    r"""Holds Bearer access token."""

    __access_token: str

    def __init__(self, access_token):
        self.__access_token = access_token

    def __call__(self, request: requests.Request = None) -> requests.Request:
        request.headers[header.AUTHORIZATION] = header.BEARER + self.__access_token
        return request

    def __str__(self) -> str:
        return header.BEARER + self.__access_token
