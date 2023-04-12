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
import enum
import json
import logging
import uuid
from http import HTTPStatus
from typing import Any, Optional

import pydantic
import pydantic.schema
import requests
from pydantic import BaseModel

from openworld.sdk.core.client.auth_client import AuthClient
from openworld.sdk.core.configuration.client_config import ClientConfig
from openworld.sdk.core.constant import header as header_constant
from openworld.sdk.core.constant import log as log_constant
from openworld.sdk.core.constant.constant import OK_STATUS_CODES_RANGE
from openworld.sdk.core.model.error import Error
from openworld.sdk.core.model.exception import service as service_exception
from openworld.sdk.core.util import log as log_util

LOG = logging.getLogger(__name__)


class ApiClient:
    def __init__(self, config: ClientConfig, auth_client_cls):
        r"""Sends requests to API.

        :param config: Client Configuration Wrapper
        """
        self.__auth_client: AuthClient = auth_client_cls(
            credentials=config.auth_config.credentials,
            auth_endpoint=config.auth_config.auth_endpoint,
        )

        self.endpoint = config.endpoint
        self.request_timeout = config.request_timeout

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
        url: str,
        body: pydantic.BaseModel,
        headers: dict = dict(),  # noqa
        response_models: Optional[list[Any]] = [None],  # noqa
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
        request_body = dict()

        if not body:
            response = requests.request(
                method=method.upper(),
                url=str(url),
                headers=request_headers,
                auth=self.__auth_client.auth_header,
                timeout=self.request_timeout,
            )
        else:
            request_body = body.json(exclude_none=True, exclude_unset=True)
            response = requests.request(
                method=method.upper(),
                url=url,
                headers=request_headers,
                data=request_body,
                auth=self.__auth_client.auth_header,
                timeout=self.request_timeout,
            )

        request_log_message = log_util.request_log(
            headers=request_headers,
            body=str(request_body),
            endpoint=url,
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
        for key, value in header_constant.API_REQUEST.items():
            if key in request_header_keys:
                continue

            request_headers[key] = value

        return request_headers

    @staticmethod
    def __prepare_request_headers(headers: dict) -> dict:
        request_headers = dict()
        for header_key, header_value in headers.items():
            if not header_value:
                continue
            needs_serialization: bool = isinstance(header_value, BaseModel) or isinstance(header_value, enum.Enum) or isinstance(header_value, uuid.UUID)
            request_headers[header_key] = json.dumps(header_value, default=pydantic.schema.pydantic_encoder) if needs_serialization else header_value

        return ApiClient.__fill_request_headers(request_headers)
