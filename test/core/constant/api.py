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
import typing
from http import HTTPStatus

import orjson
import pydantic.schema
import requests

from openworld.sdk.core.model.error import Error
from test.core.constant import authentication as auth_constant

METHOD = 'post'

ENDPOINT = "https://www.example.com/"

HELLO_WORLD_MESSAGE: str = 'Hello, World!'

DATETIME_NOW: datetime.datetime = datetime.datetime.now()


class HelloWorldEnum(enum.Enum):
    HELLO_WORLD: str = HELLO_WORLD_MESSAGE


class HelloWorld(pydantic.BaseModel):
    time: typing.Optional[datetime.datetime] = pydantic.Field(default=DATETIME_NOW)
    message: typing.Optional[str] = pydantic.Field(default=HELLO_WORLD_MESSAGE)
    enum_value: typing.Optional[HelloWorldEnum] = pydantic.Field(default=HelloWorldEnum.HELLO_WORLD)


HELLO_WORLD_OBJECT: HelloWorld = HelloWorld()

ERROR_OBJECT = Error(type=ENDPOINT, detail='Test Error')


class MockResponse:
    @staticmethod
    def hello_world_response():
        response = requests.Response()
        response.status_code = HTTPStatus.OK
        response.url = auth_constant.AUTH_ENDPOINT
        response.code = 'ok'
        response._content = orjson.dumps(HELLO_WORLD_OBJECT, default=pydantic.schema.pydantic_encoder)
        return response

    @staticmethod
    def invalid_response():
        response = requests.Response()
        response.status_code = HTTPStatus.BAD_REQUEST
        response.url = auth_constant.AUTH_ENDPOINT
        response.code = 'Bad Request'
        response._content = orjson.dumps(ERROR_OBJECT, default=pydantic.schema.pydantic_encoder)
        return response
