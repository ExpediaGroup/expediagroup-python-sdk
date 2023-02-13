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

import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from test.core.constant import authentication as auth_constant
from unittest import mock
from unittest.mock import Mock

from openworld.sdk.core.client.auth_client import _AuthClient
from openworld.sdk.core.model.exception import service as service_exception


class AuthClientTest(unittest.TestCase):
    authorized_retrieve_token_mock = Mock(return_value=auth_constant.MockResponse.default_token_response())

    unauthorized_auth_request_mock = Mock(return_value=auth_constant.MockResponse.unauthorized_token_response())

    eleven_seconds_expiration_token_mock = Mock(return_value=auth_constant.MockResponse.eleven_seconds_expiration_token_response())

    @mock.patch("openworld.sdk.core.client.auth_client.post", authorized_retrieve_token_mock)
    def test_auth_client(self, mocked=authorized_retrieve_token_mock):
        auth_client = _AuthClient(auth_constant.VALID_CREDENTIALS, auth_constant.AUTH_ENDPOINT)

        self.assertIsNotNone(auth_client.access_token)

        self.assertEqual(auth_client.access_token, auth_constant.ACCESS_TOKEN)

        self.assertFalse(auth_client.is_token_expired())
        self.assertFalse(auth_client.is_token_about_expired())

        mocked.assert_called_once()

    @mock.patch("openworld.sdk.core.client.auth_client.post", authorized_retrieve_token_mock)
    def test_default_auth_endpoint(self, mocked=authorized_retrieve_token_mock):
        auth_client = _AuthClient(auth_constant.VALID_CREDENTIALS)

        self.assertIsNotNone(auth_client.access_token)

        self.assertEqual(auth_client.access_token, auth_constant.ACCESS_TOKEN)

        self.assertFalse(auth_client.is_token_expired())
        self.assertFalse(auth_client.is_token_about_expired())
        mocked.assert_called_once()

    def test_auth_client_missing_credentials(self):
        with self.assertRaises(TypeError) as missing_credentials_test:
            auth_client = _AuthClient(auth_endpoint=auth_constant.AUTH_ENDPOINT)

    @mock.patch("openworld.sdk.core.client.auth_client.post", unauthorized_auth_request_mock)
    def test_auth_client_invalid_credentials(self):
        with self.assertRaises(expected_exception=service_exception.OpenWorldAuthException) as invalid_credentials_test:
            auth_client = _AuthClient(auth_constant.INVALID_CREDENTIALS)

    @mock.patch("openworld.sdk.core.client.auth_client.post", eleven_seconds_expiration_token_mock)
    def test_refresh_token(self, mocked=eleven_seconds_expiration_token_mock):
        auth_client = _AuthClient(auth_constant.VALID_CREDENTIALS, auth_constant.AUTH_ENDPOINT)
        self.assertIsNotNone(auth_client)

        # Test refresh token on AuthClient initialization
        mocked.assert_called_once()

        # Test refresh token not being executed cause the token is not about expired yet
        thread_pool_executor = ThreadPoolExecutor()

        thread_pool_executor.submit(auth_client.refresh_token())
        mocked.assert_called_once()

        # Test refresh token when the token is about expired
        time.sleep(1)
        thread_pool_executor.submit(auth_client.refresh_token())
        self.assertEqual(len(mocked.mock_calls), 2)

        # Verify that after refresh, there will not be anymore calls
        thread_pool_executor.submit(auth_client.refresh_token())
        self.assertEqual(len(mocked.mock_calls), 2)

    def tearDown(self) -> None:
        AuthClientTest.authorized_retrieve_token_mock.reset_mock()
        AuthClientTest.eleven_seconds_expiration_token_mock.reset_mock()
        AuthClientTest.unauthorized_auth_request_mock.reset_mock()
        super().tearDown()


if __name__ == "__main__":
    unittest.main(verbosity=True, failfast=True)
