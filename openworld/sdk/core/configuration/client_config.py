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
from typing import Optional

from openworld.sdk.core.configuration.auth_config import AuthConfig
from openworld.sdk.core.constant import constant, message, url
from openworld.sdk.core.model.authentication import Credentials
from openworld.sdk.core.model.exception import client as client_exception


@dataclass
class ClientConfig:
    __auth_config: AuthConfig = None

    def __init__(
        self,
        key: str,
        secret: str,
        endpoint: Optional[str] = url.ENDPOINT,
        request_timeout_milliseconds: Optional[float] = constant.TEN_SECONDS_MILLISECONDS,
        auth_endpoint: Optional[str] = url.AUTH_ENDPOINT,
    ):
        r"""SDK Client Configurations Holder.

        :param key: The API key to use for authentication.
        :param secret: The API secret to use for authentication.
        :param endpoint: An optional API endpoint to use for requests.
        :param request_timeout_milliseconds: Request timeout to be used in milliseconds.
        :param auth_endpoint: An optional API endpoint to use for authentication.
        """
        self.__auth_config = AuthConfig(Credentials(key, secret), auth_endpoint)
        self.__endpoint = endpoint
        self.__request_timeout = float(request_timeout_milliseconds / 1000)

        self.__post_init__()

    def __post_init__(self):
        if not self.__endpoint:
            raise client_exception.OpenWorldConfigurationException(message.NONE_VALUE_NOT_ALLOWED_FOR_MESSAGE_TEMPLATE.format(self.__endpoint))

    @property
    def auth_config(self) -> AuthConfig:
        return self.__auth_config

    @property
    def endpoint(self) -> str:
        return self.__endpoint

    @property
    def request_timeout(self) -> float:
        return self.__request_timeout
