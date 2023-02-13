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

import requests

from openworld.sdk.core.constant import header
from openworld.sdk.core.model.authentication import _TokenResponse, Token, HttpBearerAuth
from test.core.constant import authentication as auth_constant


class TokenTest(unittest.TestCase):
    def test_token_response_model(self):
        token_response: _TokenResponse = _TokenResponse.parse_obj(auth_constant.TOKEN_RESPONSE_DATA)

        self.assertIsNotNone(token_response)
        self.assertIsNotNone(token_response.expires_in)
        self.assertIsNotNone(token_response.id_token)
        self.assertIsNotNone(token_response.token_type)
        self.assertIsNotNone(token_response.refresh_token)
        self.assertIsNotNone(token_response.scope)

        self.assertEqual(token_response.access_token, auth_constant.ACCESS_TOKEN)
        self.assertEqual(token_response.expires_in, auth_constant.TOKEN_EXPIRES_IN_SECONDS)
        self.assertEqual(token_response.id_token, auth_constant.ID_TOKEN)
        self.assertEqual(token_response.token_type, auth_constant.TOKEN_TYPE)
        self.assertEqual(token_response.scope, auth_constant.SCOPE)

    def test_token_model(self):
        token = Token(auth_constant.TOKEN_RESPONSE_DATA)

        self.assertIsNotNone(token)
        self.assertIsNotNone(token.lock)
        self.assertIsNotNone(token.id_token)
        self.assertIsNotNone(token.refresh_token)
        self.assertIsNotNone(token.access_token)

        self.assertEqual(token.access_token, auth_constant.ACCESS_TOKEN)
        self.assertEqual(token.refresh_token, auth_constant.REFRESH_TOKEN)
        self.assertEqual(token.id_token, auth_constant.ID_TOKEN)

    def test_token_expiration_status(self):
        # Test non-expired token
        token = Token(auth_constant.TOKEN_RESPONSE_DATA)

        self.assertIsNotNone(token)
        self.assertFalse(token.is_about_expired())
        self.assertFalse(token.is_expired())

        # Test about expired token
        token_data = auth_constant.TOKEN_RESPONSE_DATA.copy()
        token_data[auth_constant.EXPIRES_IN] = 0.5
        token = Token(token_data)

        self.assertIsNotNone(token)
        self.assertTrue(token.is_about_expired())
        self.assertFalse(token.is_expired())

        # Test expired token
        time.sleep(0.5)
        self.assertTrue(token.is_about_expired())
        self.assertTrue(token.is_expired())


class HttpBearerAuthHeaderTest(unittest.TestCase):
    def test_http_bearer_auth_str(self):
        http_bearer_auth = HttpBearerAuth(auth_constant.ACCESS_TOKEN)
        expected_authorization_header_value = header.BEARER + auth_constant.ACCESS_TOKEN

        self.assertIsNotNone(http_bearer_auth)
        self.assertIsNotNone(str(http_bearer_auth))

        self.assertEqual(str(http_bearer_auth), expected_authorization_header_value)

    def test_http_bearer_auth_call(self):
        http_bearer_auth = HttpBearerAuth(auth_constant.ACCESS_TOKEN)
        request = http_bearer_auth(requests.Request())

        self.assertIsNotNone(http_bearer_auth)
        self.assertIsNotNone(request)
        self.assertIsNotNone(request.headers)

        auth_header = request.headers[header.AUTHORIZATION]
        self.assertEqual(auth_header, header.BEARER + auth_constant.ACCESS_TOKEN)

    def test_http_bearer_auth_missing_access_token(self):
        with self.assertRaises(TypeError) as missing_access_token_test:
            http_bearer_auth = HttpBearerAuth()


if __name__ == '__main__':
    unittest.main(verbosity=True, failfast=True)
