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

import dataclasses
import datetime
import enum
import json
from http import HTTPStatus

import dataclasses_json
import requests
from dataclasses_json.mm import _IsoField

from openworld.sdk.core.client.api import ApiClient
from openworld.sdk.core.model.error import Error
from test.core.constant import authentication as auth_constant

METHOD = 'post'

ENDPOINT = "https://www.example.com/"

HELLO_WORLD_MESSAGE: str = 'Hello, World!'

DATETIME_NOW: datetime.datetime = datetime.datetime.now()


class HelloWorldEnum(enum.Enum):
    HELLO_WORLD: str = HELLO_WORLD_MESSAGE


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class HelloWorld:
    # TODO: Consider using the below approach instead of __serialization_helper in ApiClient (Generator Templates Work)
    time: datetime.datetime = dataclasses.field(
        default=DATETIME_NOW,
        metadata={'dataclasses_json': {
            'encoder': datetime.datetime.isoformat,
            'decoder': datetime.datetime.fromisoformat,
            'mm_field': _IsoField()
        }})
    message: str = HELLO_WORLD_MESSAGE
    enum_value: HelloWorldEnum = HelloWorldEnum.HELLO_WORLD


HELLO_WORLD_OBJECT: HelloWorld = HelloWorld()

ERROR_OBJECT = Error(type=ENDPOINT, detail='Test Error')


class MockResponse:
    @staticmethod
    def hello_world_response():
        response = requests.Response()
        response.status_code = HTTPStatus.OK
        response.url = auth_constant.AUTH_ENDPOINT
        response.code = 'ok'
        response._content = f"{HELLO_WORLD_OBJECT.to_json(default=ApiClient._ApiClient__serialization_helper)}".encode()
        return response

    @staticmethod
    def invalid_response():
        response = requests.Response()
        response.status_code = HTTPStatus.BAD_REQUEST
        response.url = auth_constant.AUTH_ENDPOINT
        response.code = 'Bad Request'
        response._content = f"{json.dumps(ERROR_OBJECT.to_json())}".encode()
        return response
