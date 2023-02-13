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
from test.core.constant import api as api_constant
from test.core.constant import authentication as auth_constant

from openworld.sdk.core.configuration.client_config import ClientConfig
from openworld.sdk.core.constant import url


class ClientConfigTest(unittest.TestCase):
    def test_client_configuration(self):
        client_config = ClientConfig(
            key=auth_constant.VALID_KEY, secret=auth_constant.VALID_SECRET, endpoint=api_constant.ENDPOINT, auth_endpoint=auth_constant.AUTH_ENDPOINT
        )

        self.assertIsNotNone(client_config)
        self.assertIsNotNone(client_config.endpoint)

        self.assertIsNotNone(client_config.auth_config)
        self.assertIsNotNone(client_config.auth_config.auth_endpoint)
        self.assertIsNotNone(client_config.auth_config.credentials)
        self.assertIsNotNone(client_config.auth_config.credentials.key)
        self.assertIsNotNone(client_config.auth_config.credentials.secret)

        self.assertEqual(client_config.endpoint, api_constant.ENDPOINT)

        self.assertEqual(client_config.auth_config.auth_endpoint, auth_constant.AUTH_ENDPOINT)
        self.assertEqual(client_config.auth_config.credentials.key, auth_constant.VALID_KEY)
        self.assertEqual(client_config.auth_config.credentials.secret, auth_constant.VALID_SECRET)

    def test_missing_credentials(self):
        with self.assertRaises(TypeError) as missing_key_test:
            client_config = ClientConfig(secret=auth_constant.VALID_SECRET, endpoint=api_constant.ENDPOINT, auth_endpoint=auth_constant.AUTH_ENDPOINT)

        with self.assertRaises(TypeError) as missing_secret_test:
            client_config = ClientConfig(key=auth_constant.VALID_KEY, endpoint=api_constant.ENDPOINT, auth_endpoint=auth_constant.AUTH_ENDPOINT)

        with self.assertRaises(TypeError) as missing_key_and_secret_test:
            client_config = ClientConfig(endpoint=api_constant.ENDPOINT, auth_endpoint=auth_constant.AUTH_ENDPOINT)

    def test_with_default_auth_endpoint(self):
        client_config = ClientConfig(key=auth_constant.VALID_KEY, secret=auth_constant.VALID_SECRET, auth_endpoint=auth_constant.AUTH_ENDPOINT)

        self.assertIsNotNone(client_config)
        self.assertIsNotNone(client_config.endpoint)

        self.assertIsNotNone(client_config.auth_config)
        self.assertIsNotNone(client_config.auth_config.auth_endpoint)
        self.assertIsNotNone(client_config.auth_config.credentials)
        self.assertIsNotNone(client_config.auth_config.credentials.key)
        self.assertIsNotNone(client_config.auth_config.credentials.secret)

        self.assertEqual(client_config.endpoint, url.ENDPOINT)

        self.assertEqual(client_config.auth_config.auth_endpoint, auth_constant.AUTH_ENDPOINT)
        self.assertEqual(client_config.auth_config.credentials.key, auth_constant.VALID_KEY)
        self.assertEqual(client_config.auth_config.credentials.secret, auth_constant.VALID_SECRET)

    def test_with_default_endpoint(self):
        client_config = ClientConfig(key=auth_constant.VALID_KEY, secret=auth_constant.VALID_SECRET, endpoint=api_constant.ENDPOINT)

        self.assertIsNotNone(client_config)
        self.assertIsNotNone(client_config.endpoint)

        self.assertIsNotNone(client_config.auth_config)
        self.assertIsNotNone(client_config.auth_config.auth_endpoint)
        self.assertIsNotNone(client_config.auth_config.credentials)
        self.assertIsNotNone(client_config.auth_config.credentials.key)
        self.assertIsNotNone(client_config.auth_config.credentials.secret)

        self.assertEqual(client_config.endpoint, api_constant.ENDPOINT)

        self.assertEqual(client_config.auth_config.auth_endpoint, url.AUTH_ENDPOINT)
        self.assertEqual(client_config.auth_config.credentials.key, auth_constant.VALID_KEY)
        self.assertEqual(client_config.auth_config.credentials.secret, auth_constant.VALID_SECRET)


if __name__ == "__main__":
    unittest.main(verbosity=True, failfast=True)
