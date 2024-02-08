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
from expediagroup.sdk.core.model.api import RequestHeaders

from .model import (
    AccountScreenRequest,
    AccountScreenResponse,
    AccountTakeoverBadRequestError,
    AccountTakeoverBadRequestErrorDeserializationContract,
    AccountTakeoverUnauthorizedError,
    AccountTakeoverUnauthorizedErrorDeserializationContract,
    AccountUpdateNotFoundError,
    AccountUpdateNotFoundErrorDeserializationContract,
    AccountUpdateRequest,
    AccountUpdateResponse,
    BadGatewayError,
    BadGatewayErrorDeserializationContract,
    BadRequestError,
    BadRequestErrorDeserializationContract,
    ForbiddenError,
    ForbiddenErrorDeserializationContract,
    GatewayTimeoutError,
    GatewayTimeoutErrorDeserializationContract,
    InternalServerError,
    InternalServerErrorDeserializationContract,
    NotFoundError,
    NotFoundErrorDeserializationContract,
    OrderPurchaseScreenRequest,
    OrderPurchaseScreenResponse,
    OrderPurchaseUpdateNotFoundError,
    OrderPurchaseUpdateNotFoundErrorDeserializationContract,
    OrderPurchaseUpdateRequest,
    OrderPurchaseUpdateResponse,
    RetryableOrderPurchaseScreenFailure,
    RetryableOrderPurchaseScreenFailureDeserializationContract,
    RetryableOrderPurchaseUpdateFailure,
    RetryableOrderPurchaseUpdateFailureDeserializationContract,
    ServiceUnavailableError,
    ServiceUnavailableErrorDeserializationContract,
    TooManyRequestsError,
    TooManyRequestsErrorDeserializationContract,
    UnauthorizedError,
    UnauthorizedErrorDeserializationContract,
)


class FraudPreventionV2Client:
    def __init__(self, client_config: ClientConfig):
        r"""
        Fraud Prevention V2 API Client.

        Args:
            client_config(ClientConfig): SDK Client Configurations Holder.

        """
        python_version = platform.python_version()
        os_name, os_version, *_ = platform.platform().split("-")
        sdk_metadata = "expediagroup-fraudpreventionv2-python-sdk/3.4.0"

        self.__api_client = ApiClient(client_config, _ExpediaGroupAuthClient)

        self.__user_agent = f"{sdk_metadata} (Python {python_version}; {os_name} {os_version})"

    def screen_account(
        self, transaction_id: UUID = uuid4(), body: AccountScreenRequest = None
    ) -> Union[
        AccountScreenResponse,
        AccountTakeoverBadRequestError,
        AccountTakeoverUnauthorizedError,
        ForbiddenError,
        NotFoundError,
        TooManyRequestsError,
        InternalServerError,
        BadGatewayError,
        ServiceUnavailableError,
        GatewayTimeoutError,
    ]:
        r"""
        The Account Screen API gives a Fraud recommendation for an account transaction.

        A recommendation can be ACCEPT, CHALLENGE, or REJECT. A transaction is marked as CHALLENGE whenever there are insufficient signals to recommend ACCEPT or REJECT. These CHALLENGE incidents are manually reviewed, and a corrected recommendation is made asynchronously.
        Args:
           body(AccountScreenRequest): ...

        """
        headers = RequestHeaders(
            headers={
                header.TRANSACTION_ID: transaction_id,
                header.USER_AGENT: self.__user_agent,
            }
        )

        query = {key: value for key, value in {}.items() if value}

        request_url = furl(self.__api_client.endpoint)
        request_url /= "/fraud-prevention/v2/account/screen"
        request_url.query.set(query)
        request_url.path.normalize()

        error_responses = {
            400: AccountTakeoverBadRequestErrorDeserializationContract,
            401: AccountTakeoverUnauthorizedErrorDeserializationContract,
            403: ForbiddenErrorDeserializationContract,
            404: NotFoundErrorDeserializationContract,
            429: TooManyRequestsErrorDeserializationContract,
            500: InternalServerErrorDeserializationContract,
            502: BadGatewayErrorDeserializationContract,
            503: ServiceUnavailableErrorDeserializationContract,
            504: GatewayTimeoutErrorDeserializationContract,
        }

        return self.__api_client.call(
            headers=headers,
            method="post",
            body=body,
            response_models=[
                AccountScreenResponse,
                AccountTakeoverBadRequestError,
                AccountTakeoverUnauthorizedError,
                ForbiddenError,
                NotFoundError,
                TooManyRequestsError,
                InternalServerError,
                BadGatewayError,
                ServiceUnavailableError,
                GatewayTimeoutError,
            ],
            url=request_url,
            error_responses=error_responses,
        )

    def notify_with_account_update(
        self, transaction_id: UUID = uuid4(), body: AccountUpdateRequest = None
    ) -> Union[
        AccountUpdateResponse,
        AccountTakeoverBadRequestError,
        AccountTakeoverUnauthorizedError,
        ForbiddenError,
        AccountUpdateNotFoundError,
        TooManyRequestsError,
        InternalServerError,
        BadGatewayError,
        ServiceUnavailableError,
        GatewayTimeoutError,
    ]:
        r"""
        The Account Update API is called when there is an account lifecycle transition
        such as a challenge outcome, account restoration, or remediation action
        completion.

        For example, if a user's account is disabled, deleted, or restored, the Account Update API is called to notify Expedia Group about the change. The Account Update API is also called when a user responds to a login Multi-Factor Authentication based on a Fraud recommendation.
        Args:
           body(AccountUpdateRequest): An AccountUpdate request may be of one of the following types `MULTI_FACTOR_AUTHENTICATION_UPDATE`, `REMEDIATION_UPDATE`.

        """
        headers = RequestHeaders(
            headers={
                header.TRANSACTION_ID: transaction_id,
                header.USER_AGENT: self.__user_agent,
            }
        )

        query = {key: value for key, value in {}.items() if value}

        request_url = furl(self.__api_client.endpoint)
        request_url /= "/fraud-prevention/v2/account/update"
        request_url.query.set(query)
        request_url.path.normalize()

        error_responses = {
            400: AccountTakeoverBadRequestErrorDeserializationContract,
            401: AccountTakeoverUnauthorizedErrorDeserializationContract,
            403: ForbiddenErrorDeserializationContract,
            404: AccountUpdateNotFoundErrorDeserializationContract,
            429: TooManyRequestsErrorDeserializationContract,
            500: InternalServerErrorDeserializationContract,
            502: BadGatewayErrorDeserializationContract,
            503: ServiceUnavailableErrorDeserializationContract,
            504: GatewayTimeoutErrorDeserializationContract,
        }

        return self.__api_client.call(
            headers=headers,
            method="post",
            body=body,
            response_models=[
                AccountUpdateResponse,
                AccountTakeoverBadRequestError,
                AccountTakeoverUnauthorizedError,
                ForbiddenError,
                AccountUpdateNotFoundError,
                TooManyRequestsError,
                InternalServerError,
                BadGatewayError,
                ServiceUnavailableError,
                GatewayTimeoutError,
            ],
            url=request_url,
            error_responses=error_responses,
        )

    def screen_order(
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
        RetryableOrderPurchaseScreenFailure,
        GatewayTimeoutError,
    ]:
        r"""
        The Order Purchase API gives a Fraud recommendation for a transaction.

        A recommendation can be Accept, Reject, or Review. A transaction is marked as Review whenever there are insufficient signals to recommend Accept or Reject. These incidents are manually reviewed, and a corrected recommendation is made asynchronously.
        Args:
           body(OrderPurchaseScreenRequest): ...

        """
        headers = RequestHeaders(
            headers={
                header.TRANSACTION_ID: transaction_id,
                header.USER_AGENT: self.__user_agent,
            }
        )

        query = {key: value for key, value in {}.items() if value}

        request_url = furl(self.__api_client.endpoint)
        request_url /= "/fraud-prevention/v2/order/purchase/screen"
        request_url.query.set(query)
        request_url.path.normalize()

        error_responses = {
            400: BadRequestErrorDeserializationContract,
            401: UnauthorizedErrorDeserializationContract,
            403: ForbiddenErrorDeserializationContract,
            404: NotFoundErrorDeserializationContract,
            429: TooManyRequestsErrorDeserializationContract,
            500: InternalServerErrorDeserializationContract,
            502: BadGatewayErrorDeserializationContract,
            503: RetryableOrderPurchaseScreenFailureDeserializationContract,
            504: GatewayTimeoutErrorDeserializationContract,
        }

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
                RetryableOrderPurchaseScreenFailure,
                GatewayTimeoutError,
            ],
            url=request_url,
            error_responses=error_responses,
        )

    def notify_with_order_update(
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
        RetryableOrderPurchaseUpdateFailure,
        GatewayTimeoutError,
    ]:
        r"""
        The Order Purchase Update API is called when the status of the order has
        changed.

        For example, if the customer cancels the reservation, changes reservation in any way, or adds additional products or travelers to the reservation, the Order Purchase Update API is called to notify Expedia Group about the change.

        The Order Purchase Update API is also called when the merchant cancels or changes an order based on a Fraud recommendation.

        Args:
           body(OrderPurchaseUpdateRequest): An OrderPurchaseUpdate request may be of one of the following types `ORDER_UPDATE`, `CHARGEBACK_FEEDBACK`, `INSULT_FEEDBACK`, `REFUND_UPDATE`, `PAYMENT_UPDATE`.

        """
        headers = RequestHeaders(
            headers={
                header.TRANSACTION_ID: transaction_id,
                header.USER_AGENT: self.__user_agent,
            }
        )

        query = {key: value for key, value in {}.items() if value}

        request_url = furl(self.__api_client.endpoint)
        request_url /= "/fraud-prevention/v2/order/purchase/update"
        request_url.query.set(query)
        request_url.path.normalize()

        error_responses = {
            400: BadRequestErrorDeserializationContract,
            401: UnauthorizedErrorDeserializationContract,
            403: ForbiddenErrorDeserializationContract,
            404: OrderPurchaseUpdateNotFoundErrorDeserializationContract,
            429: TooManyRequestsErrorDeserializationContract,
            500: InternalServerErrorDeserializationContract,
            502: BadGatewayErrorDeserializationContract,
            503: RetryableOrderPurchaseUpdateFailureDeserializationContract,
            504: GatewayTimeoutErrorDeserializationContract,
        }

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
                RetryableOrderPurchaseUpdateFailure,
                GatewayTimeoutError,
            ],
            url=request_url,
            error_responses=error_responses,
        )
