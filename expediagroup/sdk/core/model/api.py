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

import json
from typing import Any

from pydantic import BaseModel, Field


class RequestHeaders(BaseModel):
    """
    RequestHeaders class represents the headers of an HTTP request.

    Attributes:
        headers (Any): The HTTP request headers. It can be of any type.
    """

    headers: Any = Field(default=None)

    def unwrap(self) -> dict[str, Any]:
        """
        Unwraps the headers from the model.

        Returns:
            A dictionary containing the headers.

        Example:
            >>> headers = RequestHeaders()
            >>> headers.unwrap()
            {'Content-Type': 'application/json', 'Authorization': 'Bearer token'}
        """
        if not self.headers:
            return dict()

        return json.loads(self.model_dump_json()).get("headers")
