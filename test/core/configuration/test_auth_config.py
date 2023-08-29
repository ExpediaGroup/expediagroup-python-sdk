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
from test.core.constant import authentication as auth_constant

from expediagroup.sdk.core.configuration.auth_config import AuthConfig
from expediagroup.sdk.core.constant import url
from expediagroup.sdk.core.model.exception import client as client_exception


class AuthConfigTest(unittest.TestCase):
    def test_auth_config(self):
        auth_config = AuthConfig(credentials=auth_constant.VALID_CREDENTIALS, auth_endpoint=auth_constant.AUTH_ENDPOINT)
        self.assertIsNotNone(auth_config)
        self.assertIsNotNone(auth_config.credentials)
        self.assertIsNotNone(auth_config.credentials.key)
        self.assertIsNotNone(auth_config.credentials.secret)
        self.assertIsNotNone(auth_config.auth_endpoint)

        self.assertEqual(auth_config.credentials.key, auth_constant.VALID_KEY)
        self.assertEqual(auth_config.credentials.secret, auth_constant.VALID_SECRET)
        self.assertEqual(auth_config.auth_endpoint, auth_constant.AUTH_ENDPOINT)

    def test_auth_config_missing_credentials(self):
        with self.assertRaises(client_exception.ExpediaGroupConfigurationException) as missing_credentials_test:
            auth_config = AuthConfig()

    def test_default_auth_endpoint(self):
        auth_config = AuthConfig(credentials=auth_constant.VALID_CREDENTIALS)
        self.assertIsNotNone(auth_config)
        self.assertIsNotNone(auth_config.auth_endpoint)
        self.assertEqual(auth_config.auth_endpoint, url.AUTH_ENDPOINT)


if __name__ == "__main__":
    unittest.main(verbosity=True, failfast=True)
