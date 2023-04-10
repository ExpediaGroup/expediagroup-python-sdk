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

import hashlib
import logging
import time

from openworld.sdk.core.client.openworld_auth_client import AuthClient
from openworld.sdk.core.constant import constant
from openworld.sdk.core.constant import log as log_constant
from openworld.sdk.core.model.authentication import Credentials
from openworld.sdk.core.model.rapid_auth import RapidAuthHeader, RapidToken

LOG = logging.getLogger(__name__)


class _RapidAuthClient(AuthClient):
    def __init__(self, credentials: Credentials, *args, **kwargs):
        r"""Manages user authentication process.

        :param credentials: Client key and secret pair
        """
        self.__credentials: Credentials = credentials
        self.__token: RapidToken = self.__retrieve_token()

    def __retrieve_token(self):
        LOG.info(log_constant.OPENWORLD_LOG_MESSAGE_TEMPLATE.format(log_constant.TOKEN_RENEWAL_IN_PROCESS))
        timestamp = str(int(time.time()))
        signature: str = hashlib.sha512(f"{self.__credentials.key}{self.__credentials.secret}{timestamp}".encode(encoding=constant.UTF8)).hexdigest()

        return RapidToken(RapidAuthHeader(signature=signature, api_key=self.__credentials.key, timestamp=timestamp))

    def refresh_token(self) -> None:
        r"""Refreshes access token."""
        if not self.__token.is_about_expired():
            return

        if self.__token.lock.acquire(block=True):
            if self.__token.is_about_expired():
                LOG.info(log_constant.OPENWORLD_LOG_MESSAGE_TEMPLATE.format(log_constant.TOKEN_EXPIRED))
                self.__token = self.__retrieve_token()
                LOG.info(log_constant.OPENWORLD_LOG_MESSAGE_TEMPLATE.format(log_constant.TOKEN_RENEWAL_SUCCESSFUL))
            self.__token.lock.release()

    @property
    def access_token(self):
        r"""Gets the access token value.

        :return: the access token value.
        :rtype: str
        """
        return self.__token.access_token

    @property
    def auth_header(self):
        return self.__token.auth_header

    @property
    def is_token_expired(self):
        r"""Returns true if token is expired, false otherwise.

        :rtype: bool
        """
        return self.__token.is_expired()

    @property
    def is_token_about_expired(self):
        r"""Returns true if token is about expired, false otherwise.

        :rtype: bool
        """
        return self.__token.is_about_expired()
