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

import logging
from http import HTTPStatus

from requests import Response, post
from requests.auth import HTTPBasicAuth

from openworld.sdk.core.client.auth_client import AuthClient
from openworld.sdk.core.constant import body as body_constant
from openworld.sdk.core.constant import log as log_constant
from openworld.sdk.core.constant import url as url_constant
from openworld.sdk.core.constant.constant import OK_STATUS_CODES_RANGE
from openworld.sdk.core.constant.message import UNABLE_TO_AUTHENTICATE
from openworld.sdk.core.model.authentication import Credentials, Token
from openworld.sdk.core.model.exception import service as service_exception
from openworld.sdk.core.util import log as log_util

LOG = logging.getLogger(__name__)


class _OpenWorldAuthClient(AuthClient):
    def __init__(self, credentials: Credentials, auth_endpoint: str = url_constant.AUTH_ENDPOINT, *args, **kwargs):
        r"""Manages user authentication process.

        :param credentials: Client key and secret pair
        """
        self.__credentials: Credentials = credentials
        self.__auth_endpoint: str = auth_endpoint

        token_response = self.__retrieve_token(auth_endpoint=self.__auth_endpoint).json()
        self.__token: Token = Token(token_response)

    def __retrieve_token(self, auth_endpoint: str = url_constant.AUTH_ENDPOINT) -> Response:
        LOG.info(log_constant.OPENWORLD_LOG_MESSAGE_TEMPLATE.format(log_constant.TOKEN_RENEWAL_IN_PROCESS))

        auth_method = HTTPBasicAuth(username=self.__credentials.key, password=self.__credentials.secret)

        response = post(url=auth_endpoint, auth=auth_method, data=body_constant.TOKEN_REQUEST)

        if response.status_code not in OK_STATUS_CODES_RANGE:
            raise service_exception.OpenWorldAuthException(
                message=UNABLE_TO_AUTHENTICATE,
                error_code=HTTPStatus(response.status_code),
            )

        request_log_message = log_util.request_log(
            headers=log_util.filter_credentials(auth_method.__dict__),
            body=str(body_constant.TOKEN_REQUEST),
            endpoint=auth_endpoint,
            method="post",
            response=response,
        )

        LOG.info(log_constant.OPENWORLD_LOG_MESSAGE_TEMPLATE.format(request_log_message))
        return response

    def refresh_token(self) -> None:
        r"""Refreshes access token.

        :return: the new token.
        :rtype: requests.Response
        """
        if not self.__token.is_about_expired():
            return

        if self.__token.lock.acquire(block=True):
            if self.__token.is_about_expired():
                LOG.info(log_constant.OPENWORLD_LOG_MESSAGE_TEMPLATE.format(log_constant.TOKEN_EXPIRED))
                response = self.__retrieve_token(auth_endpoint=self.__auth_endpoint)
                self.__token.update(data=response.json())
                LOG.info(log_constant.OPENWORLD_LOG_MESSAGE_TEMPLATE.format(log_constant.TOKEN_RENEWAL_SUCCESSFUL))
            self.__token.lock.release()

    @property
    def access_token(self) -> str:
        r"""Gets the access token value.

        :return: the access token value.
        :rtype: str
        """
        return self.__token.access_token

    def is_token_expired(self):
        return self.__token.is_expired()

    def is_token_about_expired(self):
        return self.__token.is_about_expired()

    @property
    def auth_header(self):
        return self.__token.auth_header
