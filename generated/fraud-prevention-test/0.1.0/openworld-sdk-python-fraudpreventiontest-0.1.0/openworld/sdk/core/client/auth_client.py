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

import abc
import logging

LOG = logging.getLogger(__name__)


class AuthClient(abc.ABC):
    @abc.abstractmethod
    def refresh_token(self):
        pass

    @property
    @abc.abstractmethod
    def access_token(self):
        return None

    @property
    @abc.abstractmethod
    def auth_header(self):
        return None

    @property
    @abc.abstractmethod
    def is_token_expired(self):
        return None

    @property
    @abc.abstractmethod
    def is_token_about_expired(self):
        return None
