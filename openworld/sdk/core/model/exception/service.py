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

from http import HTTPStatus
from typing import Optional

from openworld.sdk.core.model.error import Error
from openworld.sdk.core.model.exception.openworld import OpenWorldException


class OpenWorldServiceException(OpenWorldException):
    def __init__(self, message: str, cause: Optional[BaseException] = None):
        super().__init__(message, cause)

    @staticmethod
    def of(error: Error, error_code: HTTPStatus):
        return OpenWorldServiceException(message=f"[{error_code.value}] {error}")


class OpenWorldAuthException(OpenWorldServiceException):
    def __init__(self, error_code: HTTPStatus, message: str):
        super().__init__(message=f"[{error_code.value}] {message}")
