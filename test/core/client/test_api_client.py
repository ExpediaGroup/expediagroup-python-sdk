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
import time
import unittest
from test.core.constant import api as api_constant
from test.core.constant import authentication as auth_constant
from unittest import mock
from unittest.mock import Mock

from openworld.sdk.core.client.api import ApiClient
from openworld.sdk.core.client.openworld_auth_client import _OpenWorldAuthClient
from openworld.sdk.core.configuration.client_config import ClientConfig
from openworld.sdk.core.constant import header as header_constant
from openworld.sdk.core.model.exception import service as service_exception


class Mocks:
    authorized_retrieve_token_mock = Mock(return_value=auth_constant.MockResponse.default_token_response())

    hello_world_request_response_mock = Mock(return_value=api_constant.MockResponse.hello_world_response())

    invalid_request_response_mock = Mock(return_value=api_constant.MockResponse.invalid_response())


class Configs:
    client_config = ClientConfig(
        key=auth_constant.VALID_KEY, secret=auth_constant.VALID_SECRET, endpoint=api_constant.ENDPOINT,
        auth_endpoint=auth_constant.AUTH_ENDPOINT, request_timeout_milliseconds=10_000
    )


class ApiClientTest(unittest.TestCase):
    def test_fill_header_request(self):
        headers = ApiClient._ApiClient__fill_request_headers(dict())

        self.assertIsNotNone(headers)
        self.assertEqual(headers, header_constant.API_REQUEST)

        headers: dict = ApiClient._ApiClient__fill_request_headers(None)

        self.assertIsNotNone(headers)
        self.assertEqual(headers, header_constant.API_REQUEST)

    @mock.patch.object(_OpenWorldAuthClient, "_OpenWorldAuthClient__retrieve_token", authorized_retrieve_token_mock)
    def test_api_client(self):
        api_client = ApiClient(Configs.client_config)

        self.assertIsNotNone(api_client)

    def test_missing_client_config(self):
        with self.assertRaises(TypeError) as missing_client_config_test:
            api_client = ApiClient()

    @mock.patch.object(_OpenWorldAuthClient, "_OpenWorldAuthClient__retrieve_token", authorized_retrieve_token_mock)
    @mock.patch("openworld.sdk.core.client.api.requests.request", hello_world_request_response_mock)
    def test_api_client_call(self):
        api_client = ApiClient(Configs.client_config)

        response_obj: api_constant.HelloWorld = api_client.call(
            method=api_constant.METHOD,
            body=api_constant.HELLO_WORLD_OBJECT,
            response_models=[api_constant.HelloWorld],
            url=api_constant.ENDPOINT,
            headers=dict(),
        )

        self.assertEqual(response_obj.message, api_constant.HELLO_WORLD_MESSAGE)
        self.assertEqual(response_obj.time, api_constant.DATETIME_NOW)
        self.assertEqual(response_obj.enum_value, api_constant.HelloWorldEnum.HELLO_WORLD)

    @mock.patch.object(_OpenWorldAuthClient, "_OpenWorldAuthClient__retrieve_token", authorized_retrieve_token_mock)
    @mock.patch("openworld.sdk.core.client.api.requests.request", hello_world_request_response_mock)
    def test_api_client_call_missing_headers(self):
        api_client = ApiClient(Configs.client_config)

        response_obj: api_constant.HelloWorld = api_client.call(
            method=api_constant.METHOD, body=api_constant.HELLO_WORLD_OBJECT, response_models=[api_constant.HelloWorld],
            url=api_constant.ENDPOINT
        )

        self.assertEqual(response_obj.message, api_constant.HELLO_WORLD_MESSAGE)
        self.assertEqual(response_obj.time, api_constant.DATETIME_NOW)
        self.assertEqual(response_obj.enum_value, api_constant.HelloWorldEnum.HELLO_WORLD)

    @mock.patch.object(_OpenWorldAuthClient, "_OpenWorldAuthClient__retrieve_token", authorized_retrieve_token_mock)
    def test_api_client_call_missing_url(self):
        api_client = ApiClient(Configs.client_config)

        with self.assertRaises(Exception) as call_missing_url_test:
            api_client.call(body=api_constant.HELLO_WORLD_OBJECT, method=api_constant.METHOD,
                            response_models=[api_constant.HelloWorld], headers=dict())

    @mock.patch.object(_OpenWorldAuthClient, "_OpenWorldAuthClient__retrieve_token", authorized_retrieve_token_mock)
    @mock.patch("openworld.sdk.core.client.api.requests.request", hello_world_request_response_mock)
    def test_api_client_call_default_response_model(self):
        api_client = ApiClient(Configs.client_config)

        response_obj: api_constant.HelloWorld = api_client.call(
            method=api_constant.METHOD, body=api_constant.HELLO_WORLD_OBJECT, url=api_constant.ENDPOINT, headers=dict()
        )

        self.assertIsNone(response_obj)

    @mock.patch.object(_OpenWorldAuthClient, "_OpenWorldAuthClient__retrieve_token", authorized_retrieve_token_mock)
    def test_api_client_call_missing_obj(self):
        api_client = ApiClient(Configs.client_config)

        with self.assertRaises(Exception) as call_missing_obj_test:
            api_client.call(method=api_constant.METHOD, url=api_constant.ENDPOINT,
                            response_models=[api_constant.HelloWorld], headers=dict())

    @mock.patch.object(_OpenWorldAuthClient, "_OpenWorldAuthClient__retrieve_token", authorized_retrieve_token_mock)
    @mock.patch("openworld.sdk.core.client.api.requests.request", invalid_request_response_mock)
    def test_error_response(self):
        api_client = ApiClient(Configs.client_config)

        with self.assertRaises(service_exception.OpenWorldServiceException) as call_error_response:
            api_client.call(
                body=api_constant.HELLO_WORLD_OBJECT,
                method=api_constant.METHOD,
                url=api_constant.ENDPOINT,
                response_models=[api_constant.HelloWorld],
                headers=dict(),
            )

    @mock.patch.object(_OpenWorldAuthClient, "_OpenWorldAuthClient__retrieve_token", authorized_retrieve_token_mock)
    def test_api_client_call_missing_method(self):
        api_client = ApiClient(Configs.client_config)

        with self.assertRaises(TypeError) as call_missing_method_test:
            api_client.call(
                body=api_constant.HELLO_WORLD_OBJECT,
                url=api_constant.ENDPOINT,
                response_models=[api_constant.HelloWorld],
                headers=dict(),
            )

    @mock.patch.object(_OpenWorldAuthClient, "_OpenWorldAuthClient__retrieve_token", authorized_retrieve_token_mock)
    @mock.patch("openworld.sdk.core.client.api.requests.request", hello_world_request_response_mock)
    def test_api_client_call_none_body(self):
        api_client = ApiClient(Configs.client_config)

        response_obj: api_constant.HelloWorld = api_client.call(
            method=api_constant.METHOD, response_models=[api_constant.HelloWorld], url=api_constant.ENDPOINT,
            headers=dict(), body=None
        )

        self.assertEqual(response_obj.message, api_constant.HELLO_WORLD_MESSAGE)
        self.assertEqual(response_obj.time, api_constant.DATETIME_NOW)
        self.assertEqual(response_obj.enum_value, api_constant.HelloWorldEnum.HELLO_WORLD)


if __name__ == "__main__":
    unittest.main(verbosity=True, failfast=True)
