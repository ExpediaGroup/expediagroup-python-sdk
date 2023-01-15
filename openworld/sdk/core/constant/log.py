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
from textwrap import dedent

TOKEN_RENEWAL_IN_PROCESS: str = "Renewing token"

TOKEN_RENEWAL_SUCCESSFUL: str = "Token renewal successful"

TOKEN_EXPIRED: str = "Token expired or is about to expire, request will wait until token is renewed"

OPENWORLD_LOG_MESSAGE_TEMPLATE: str = "ExpediaSDK: {0}"

UNSUCCESSFUL_RESPONSE_MESSAGE_TEMPLATE: str = "Unsuccessful response [{0}]"

NEW_TOKEN_EXPIRATION_TEMPLATE: str = "New token expires in {0} seconds"

HTTP_HEADERS_LOG_MESSAGE_TEMPLATE: str = dedent(
    """\tHeaders:
    \t--- BEGIN ---
    {0}
    \t--- END ---
    """
)

HTTP_BODY_LOG_MESSAGE_TEMPLATE: str = dedent(
    """
    \tBody:
    \t--- BEGIN ---
    {0}
    \t--- END ---
    """
)
