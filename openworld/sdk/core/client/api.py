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
from typing import Any, Optional

import orjson
import pydantic
import pydantic.schema
import requests
from furl import furl

from openworld.sdk.core.client.auth_client import _AuthClient
from openworld.sdk.core.configuration.client_config import ClientConfig
from openworld.sdk.core.constant import header as header_constant
from openworld.sdk.core.constant import log as log_constant
from openworld.sdk.core.constant.constant import OK_STATUS_CODES_RANGE
from openworld.sdk.core.model.authentication import HttpBearerAuth
from openworld.sdk.core.model.error import Error
from openworld.sdk.core.model.exception import service as service_exception
from openworld.sdk.core.util import log as log_util

LOG = logging.getLogger(__name__)


class ApiClient:
    def __init__(self, config: ClientConfig):
        r"""Sends requests to API.

        :param config: Client Configuration Wrapper
        """
        self.__auth_client: _AuthClient = _AuthClient(
            credentials=config.auth_config.credentials,
            auth_endpoint=config.auth_config.auth_endpoint,
        )

        self.endpoint = config.endpoint

    @staticmethod
    def __build_response(response: requests.Response, response_models: list[pydantic.BaseModel]):
        if response.status_code not in OK_STATUS_CODES_RANGE:
            raise service_exception.OpenWorldServiceException.of(
                error=Error.parse_obj(response.json()),
                error_code=HTTPStatus(response.status_code),
            )

        response_object = None
        for model in response_models:
            if not model:
                continue
            try:
                response_object = pydantic.parse_obj_as(model, response.json())
                return response_object
            except Exception:
                continue

        return response_object

    def call(
        self,
        method: str,
        url: furl,
        body: pydantic.BaseModel,
        headers: dict = dict(), # noqa
        response_models: Optional[list[Any]] = [None], # noqa
    ) -> Any:
        r"""Sends HTTP request to API.

        :param method: Http request method.
        :param body: Object that holds request data.
        :param response_models: Model to fetch the response data into.
        :param url: URL used to send the request.
        :param headers: Request headers.

        :return: response as object
        :rtype: Any
        """
        self.__auth_client.refresh_token()
        request_headers = ApiClient.__prepare_request_headers(headers)
        auth_bearer = HttpBearerAuth(access_token=self.__auth_client.access_token)
        request_body = dict()

        if not body:
            response = requests.request(
                method=method.upper(),
                url=str(url),
                headers=request_headers,
                auth=auth_bearer,
            )
        else:
            request_body = body.json(exclude_none=True, exclude_unset=True)
            response = requests.request(
                method=method.upper(),
                url=str(url),
                headers=request_headers,
                data=request_body,
                auth=auth_bearer,
            )

        request_log_message = log_util.request_log(
            headers=request_headers,
            body=str(request_body),
            endpoint=str(url),
            method=method,
            response=response,
        )

        LOG.info(log_constant.OPENWORLD_LOG_MESSAGE_TEMPLATE.format(request_log_message))

        result = ApiClient.__build_response(response=response, response_models=response_models)
        return result

    @staticmethod
    def __fill_request_headers(request_headers: dict):
        if not request_headers:
            request_headers = dict()

        request_header_keys = request_headers.keys()
        for key in header_constant.API_REQUEST.keys():
            if key in request_header_keys:
                continue

            request_headers[key] = header_constant.API_REQUEST[key]

        return request_headers

    @staticmethod
    def __prepare_request_headers(headers: dict) -> dict:
        request_headers = dict()
        for header_key, header_value in headers.items():
            if not header_value:
                continue
            request_headers[header_key] = orjson.dumps(header_value, default=pydantic.schema.pydantic_encoder)

        return ApiClient.__fill_request_headers(request_headers)
