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

from __future__ import annotations

import platform
from typing import Union
from uuid import UUID, uuid4

from furl import furl

from expediagroup.sdk.core.client.api import ApiClient
from expediagroup.sdk.core.client.expediagroup_auth_client import (
    _ExpediaGroupAuthClient,
)
from expediagroup.sdk.core.configuration.client_config import ClientConfig
from expediagroup.sdk.core.constant import header

from .model import (
    BadGatewayError,
    BadRequestError,
    ForbiddenError,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    OrderPurchaseScreenRequest,
    OrderPurchaseScreenResponse,
    OrderPurchaseUpdateNotFoundError,
    OrderPurchaseUpdateRequest,
    OrderPurchaseUpdateResponse,
    ServiceUnavailableError,
    TooManyRequestsError,
    UnauthorizedError,
)


class FraudPreventionV2Client:
    def __init__(self, client_config: ClientConfig):
        r"""Fraud Prevention V2 API Client.

        Args:
            client_config(ClientConfig): SDK Client Configurations Holder.
        """
        python_version = platform.python_version()
        os_name, os_version, *_ = platform.platform().split("-")
        sdk_metadata = "expediagroup-fraudpreventionv2-python-sdk/1.0.1"

        self.__api_client = ApiClient(client_config, _ExpediaGroupAuthClient)

        self.__user_agent = f"{sdk_metadata} (Python {python_version}; {os_name} {os_version})"

    def screen(
        self, transaction_id: UUID = uuid4(), body: OrderPurchaseScreenRequest = None
    ) -> Union[
        OrderPurchaseScreenResponse,
        BadRequestError,
        UnauthorizedError,
        ForbiddenError,
        NotFoundError,
        TooManyRequestsError,
        InternalServerError,
        BadGatewayError,
        ServiceUnavailableError,
        GatewayTimeoutError,
    ]:
        r"""The Order Purchase API gives a Fraud recommendation for a transaction. A recommendation can be Accept, Reject, or Review. A transaction is marked as Review whenever there are insufficient signals to recommend Accept or Reject. These incidents are manually reviewed, and a corrected recommendation is made asynchronously.
        Args:
           body(OrderPurchaseScreenRequest): ..."""
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
        }

        query = {key: value for key, value in {}.items() if value}

        request_url = furl(self.__api_client.endpoint)
        request_url /= "/fraud-prevention/v2/order/purchase/screen"
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(
            headers=headers,
            method="post",
            body=body,
            response_models=[
                OrderPurchaseScreenResponse,
                BadRequestError,
                UnauthorizedError,
                ForbiddenError,
                NotFoundError,
                TooManyRequestsError,
                InternalServerError,
                BadGatewayError,
                ServiceUnavailableError,
                GatewayTimeoutError,
            ],
            url=request_url,
        )

    def update(
        self, transaction_id: UUID = uuid4(), body: OrderPurchaseUpdateRequest = None
    ) -> Union[
        OrderPurchaseUpdateResponse,
        BadRequestError,
        UnauthorizedError,
        ForbiddenError,
        OrderPurchaseUpdateNotFoundError,
        TooManyRequestsError,
        InternalServerError,
        BadGatewayError,
        ServiceUnavailableError,
        GatewayTimeoutError,
    ]:
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
        request_url /= "/fraud-prevention/v2/order/purchase/update"
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(
            headers=headers,
            method="post",
            body=body,
            response_models=[
                OrderPurchaseUpdateResponse,
                BadRequestError,
                UnauthorizedError,
                ForbiddenError,
                OrderPurchaseUpdateNotFoundError,
                TooManyRequestsError,
                InternalServerError,
                BadGatewayError,
                ServiceUnavailableError,
                GatewayTimeoutError,
            ],
            url=request_url,
        )
