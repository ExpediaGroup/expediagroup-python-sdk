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

import unittest
from test.core.client.test_api_client import Configs
from test.core.client.test_api_client import Mocks as ApiClientTestMocks
from test.core.constant import api as api_constant
from unittest import mock

import requests.exceptions

from openworld.sdk.core.client.api import ApiClient
from openworld.sdk.core.client.pagination import PageLinkExtractionStrategy, Paginator
from openworld.sdk.core.client.rapid_auth_client import _RapidAuthClient
from openworld.sdk.core.model.api import Response


class Mocks:
    paginated_hello_world_request_response = mock.Mock(return_value=api_constant.MockResponse.hello_world_paginated_response())

    paginated_hello_world_request_response_call_with_response = mock.Mock(
        return_value=Response(raw=api_constant.MockResponse.hello_world_paginated_response(), body=api_constant.HELLO_WORLD_OBJECT)
    )


class PageLinkExtractionStrategyTest(unittest.TestCase):
    def test_default_strategy(self):
        default_strategy: PageLinkExtractionStrategy = PageLinkExtractionStrategy.DEFAULT

        self.assertIsNotNone(default_strategy)

        self.assertEqual(default_strategy(api_constant.MockResponse.hello_world_paginated_response().headers), api_constant.EXTRACTED_PAGINATED_LINK)


class PaginatorTest(unittest.TestCase):
    @mock.patch("openworld.sdk.core.client.api.requests.request", Mocks.paginated_hello_world_request_response)
    def test_paginator(self):
        api_client = ApiClient(Configs.client_config, _RapidAuthClient)

        paginator = Paginator(
            api_client=api_client,
            endpoint=api_constant.PAGINATED_ENDPOINT,
            response_models=[api_constant.HelloWorld],
        )

        self.assertIsNotNone(api_client)
        self.assertIsNotNone(paginator)
        self.assertIsNotNone(paginator.last_response_headers)
        self.assertIsNotNone(paginator.endpoint)
        self.assertIsNotNone(paginator.request_headers)
        self.assertIsNotNone(paginator.first_page)

        self.assertEqual(paginator.last_response_headers, api_constant.MockResponse.hello_world_paginated_response().headers)
        self.assertEqual(paginator.endpoint, api_constant.PAGINATED_ENDPOINT)  # next-page endpoint
        self.assertEqual(paginator.first_page, api_constant.HELLO_WORLD_OBJECT)

    def test_paginator_null_api_client(self):
        with self.assertRaises(Exception):
            Paginator(
                api_client=None,
                endpoint=api_constant.PAGINATED_ENDPOINT,
                response_models=[api_constant.HelloWorld],
            )

    def test_paginator_null_endpoint(self):
        api_client = ApiClient(Configs.client_config, _RapidAuthClient)

        with self.assertRaises(requests.exceptions.MissingSchema):
            Paginator(
                api_client=api_client,
                endpoint=None,
                response_models=[api_constant.HelloWorld],
            )

    @mock.patch("openworld.sdk.core.client.api.requests.request", Mocks.paginated_hello_world_request_response)
    def test_response_models_default_params(self):
        api_client = ApiClient(Configs.client_config, _RapidAuthClient)

        paginator = Paginator(
            api_client=api_client,
            endpoint=api_constant.PAGINATED_ENDPOINT,
        )

        self.assertIsNotNone(api_client)
        self.assertIsNotNone(paginator)
        self.assertIsNotNone(paginator.response_models)
        self.assertGreaterEqual(len(paginator.response_models), 1)
        self.assertIsNone(paginator.response_models[0])

    @mock.patch("openworld.sdk.core.client.api.requests.request", Mocks.paginated_hello_world_request_response)
    def test_response_models_params(self):
        api_client = ApiClient(Configs.client_config, _RapidAuthClient)

        paginator = Paginator(api_client=api_client, endpoint=api_constant.PAGINATED_ENDPOINT, response_models=[api_constant.HelloWorld, ApiClient])

        self.assertIsNotNone(api_client)
        self.assertIsNotNone(paginator)
        self.assertIsNotNone(paginator.response_models)
        self.assertGreaterEqual(len(paginator.response_models), 1)
        self.assertEqual(len(paginator.response_models), 2)
        self.assertIsNotNone(paginator.response_models[0])
        self.assertIsNotNone(paginator.response_models[1])

        self.assertEqual(paginator.response_models[0], api_constant.HelloWorld)
        self.assertEqual(paginator.response_models[1], ApiClient)

    @mock.patch("openworld.sdk.core.client.api.requests.request", ApiClientTestMocks.hello_world_request_response_mock)
    @mock.patch(
        "openworld.sdk.core.client.pagination.Paginator._Paginator__get_first_page_response", Mocks.paginated_hello_world_request_response_call_with_response
    )
    def test_paginator_get_pages(self):
        api_client = ApiClient(Configs.client_config, _RapidAuthClient)

        # Two pages response paginator
        paginator = Paginator(api_client=api_client, endpoint=api_constant.PAGINATED_ENDPOINT, response_models=[api_constant.HelloWorld])

        self.assertIsNotNone(paginator.first_page)
