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
from copy import deepcopy
from http import HTTPStatus
from typing import Any, Optional

import requests
from pydantic import BaseModel, TypeAdapter

from expediagroup.sdk.core.client.auth_client import AuthClient
from expediagroup.sdk.core.configuration.client_config import ClientConfig
from expediagroup.sdk.core.constant import header as header_constant
from expediagroup.sdk.core.constant import log as log_constant
from expediagroup.sdk.core.constant.constant import OK_STATUS_CODES_RANGE
from expediagroup.sdk.core.model.api import RequestHeaders
from expediagroup.sdk.core.model.error import Error
from expediagroup.sdk.core.model.exception import service as service_exception
from expediagroup.sdk.core.util import log as log_util

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
    def __build_response(
        response: requests.Response,
        response_models: list[type],
        error_responses: dict[int, Any],
    ):
        if response.status_code not in OK_STATUS_CODES_RANGE:
            exception: service_exception.ExpediaGroupApiException

            if response.status_code in error_responses.keys():
                error_object = error_responses[response.status_code].model.model_validate(response.json())
                exception = error_responses[response.status_code].exception.of(error=error_object, error_code=HTTPStatus(response.status_code))
            else:
                exception = service_exception.ExpediaGroupApiException.of(
                    error=Error.model_validate(response.json()),
                    error_code=HTTPStatus(response.status_code),
                )

            raise exception

        response_object = None
        for model in response_models:
            if not model:
                continue
            try:
                response_object = TypeAdapter(model).validate_python(response.json())
                return response_object
            except Exception:
                continue

        return response_object

    def call(
        self,
        method: str,
        url: str,
        body: BaseModel,
        headers: RequestHeaders = RequestHeaders(),  # noqa
        response_models: Optional[list[Any]] = list(),  # noqa
        error_responses: dict[int, Any] = dict(),  # noqa
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

        if not body:
            response = requests.request(
                method=method.upper(),
                url=str(url),
                headers=request_headers,
                auth=self.__auth_client.auth_header,
                timeout=self.request_timeout,
            )
        else:
            request_body = body.model_dump_json(exclude_none=True)
            response = requests.request(
                method=method.upper(),
                url=url,
                headers=request_headers,
                data=request_body,
                auth=self.__auth_client.auth_header,
                timeout=self.request_timeout,
            )

        logged_body: dict[str, Any] = dict() if not body else body.model_dump()

        request_log_message = log_util.request_log(
            headers=request_headers,
            body=str(logged_body),
            endpoint=url,
            method=method,
            response=response,
        )

        LOG.info(log_constant.EXPEDIAGROUP_LOG_MESSAGE_TEMPLATE.format(request_log_message))

        result = ApiClient.__build_response(
            response=response,
            response_models=response_models,
            error_responses=error_responses,
        )

        return result

    @staticmethod
    def __fill_request_headers(request_headers: dict):
        if not request_headers:
            return header_constant.API_REQUEST

        headers: dict = deepcopy(header_constant.API_REQUEST)
        headers.update(request_headers)

        return headers

    @staticmethod
    def __prepare_request_headers(headers: RequestHeaders) -> dict:
        request_headers: dict = headers.unwrap()

        return ApiClient.__fill_request_headers(request_headers)
