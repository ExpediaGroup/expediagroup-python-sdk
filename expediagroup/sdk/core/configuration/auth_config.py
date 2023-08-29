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

from dataclasses import dataclass

from expediagroup.sdk.core.constant import message
from expediagroup.sdk.core.constant.constant import EMPTY_STRING
from expediagroup.sdk.core.constant.url import AUTH_ENDPOINT
from expediagroup.sdk.core.model.authentication import Credentials
from expediagroup.sdk.core.model.exception import client as client_exception

DEFAULT_CREDENTIALS = Credentials(key=EMPTY_STRING, secret=EMPTY_STRING)


@dataclass
class AuthConfig:
    def __init__(
        self,
        credentials: Credentials = DEFAULT_CREDENTIALS,
        auth_endpoint: str = AUTH_ENDPOINT,
    ):
        r"""Holds authentication config data.

        :param credentials: Client's credentials.
        :param auth_endpoint: URL to use as a base for oauth token requests, has a default value of [ACCESS_TOKEN] if
                               not provided.
        """
        self.__credentials: Credentials = credentials
        self.__auth_endpoint: str = auth_endpoint

        self.__post_init__()

    def __post_init__(self):
        missing = list()

        for attribute in [
            ("Key", self.__credentials.key),
            ("Secret", self.__credentials.secret),
            ("Auth_Endpoint", self.__auth_endpoint),
        ]:
            if not attribute[1]:
                missing.append(attribute[0])

        if len(missing):
            raise client_exception.ExpediaGroupConfigurationException(message=message.NONE_VALUE_NOT_ALLOWED_FOR_MESSAGE_TEMPLATE.format(f"{missing}"))

    @property
    def credentials(self) -> Credentials:
        return self.__credentials

    @property
    def auth_endpoint(self) -> str:
        return self.__auth_endpoint
