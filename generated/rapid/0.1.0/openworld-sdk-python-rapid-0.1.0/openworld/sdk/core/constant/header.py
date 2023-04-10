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

BEARER: str = "Bearer "

AUTHORIZATION: str = "Authorization"

GRANT_TYPE: str = "grant_type"

CLIENT_CREDENTIALS: str = "client_credentials"

CONTENT_TYPE: str = "Content-type"

JSON_CONTENT_TYPE: str = "application/json"

ACCEPT: str = "Accept"

ACCEPT_ENCODING: str = "Accept-Encoding"

GZIP: str = "gzip"

TRANSACTION_ID: str = "transaction-id"

USER_AGENT: str = "User-agent"

OPENWORLD_SDK_PYTHON: str = "open-world-sdk-python/"

API_REQUEST: dict = {CONTENT_TYPE: JSON_CONTENT_TYPE, ACCEPT: JSON_CONTENT_TYPE, ACCEPT_ENCODING: GZIP}

EAN: str = "EAN"

API_KEY: str = "APIKey"

SIGNATURE: str = "Signature"

TIMESTAMP: str = "timestamp"
