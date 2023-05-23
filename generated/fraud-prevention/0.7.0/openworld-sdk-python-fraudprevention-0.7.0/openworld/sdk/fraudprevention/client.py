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

import platform
from typing import *
from uuid import UUID, uuid4

from furl import furl

from openworld.sdk.core.client.api import ApiClient
from openworld.sdk.core.client.openworld_auth_client import _OpenWorldAuthClient
from openworld.sdk.core.configuration.client_config import ClientConfig
from openworld.sdk.core.constant import header

from .model import *


class FraudPreventionClient:
    def __init__(self, client_config: ClientConfig):
        r"""Fraud Prevention API Client.

        Args:
            client_config(ClientConfig): SDK Client Configurations Holder.
        """
        python_version = platform.python_version()
        os_name, os_version, *_ = platform.platform().split('-')
        sdk_metadata = f'open-world-sdk-python-fraudprevention/0.7.0'

        self.__api_client = ApiClient(client_config, _OpenWorldAuthClient)

        self.__user_agent = f'{sdk_metadata} (Python {python_version}; {os_name} {os_version})'

    def screen(self, transaction_id: UUID = uuid4(), body: OrderPurchaseScreenRequest = None) -> Union[OrderPurchaseScreenResponse, ExtendedError, Error]:
        r"""The Order Purchase API gives a Fraud recommendation for a transaction. A recommendation can be Accept, Reject, or Review. A transaction is marked as Review whenever there are insufficient signals to recommend Accept or Reject. These incidents are manually reviewed, and a corrected recommendation is made asynchronously.
        Args:
           body(OrderPurchaseScreenRequest): ..."""
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
        }

        query = {key: value for key, value in {}.items() if value}

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/fraud-prevention/order/purchase/screen'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(
            headers=headers, method='post', body=body, response_models=[OrderPurchaseScreenResponse, ExtendedError, Error], url=request_url
        )

    def update(self, transaction_id: UUID = uuid4(), body: OrderPurchaseUpdateRequest = None) -> Union[None, ExtendedError, Error]:
        r"""The Order Purchase Update API is called when the status of the order has changed.

        For example, if the customer cancels the reservation, changes reservation in any way, or adds additional products or travelers to the reservation, the Order Purchase Update API is called to notify Expedia Group about the change.

        The Order Purchase Update API is also called when the merchant cancels or changes an order based on a Fraud recommendation.

        Args:
           body(OrderPurchaseUpdateRequest): An OrderPurchaseUpdate request may be of one of the following types `ORDER_UPDATE`, `CHARGEBACK_FEEDBACK`, `INSULT_FEEDBACK`, `REFUND_UPDATE`, `PAYMENT_UPDATE`.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
        }

        query = {key: value for key, value in {}.items() if value}

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/fraud-prevention/order/purchase/update'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='post', body=body, response_models=[None, ExtendedError, Error], url=request_url)
