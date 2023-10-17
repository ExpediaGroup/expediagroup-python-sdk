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

from datetime import datetime
from enum import Enum
from typing import Any, Literal, Optional, Union

from pydantic import BaseModel, EmailStr, Extra, Field, constr
from pydantic.dataclasses import dataclass

from expediagroup.sdk.core.model.exception.service import ExpediaGroupApiException


class Code(
    Enum,
):
    r"""pydantic model Code: Snake cased all caps error code interpreted from the HTTP status code that can programmatically be acted upon."""

    UNAUTHORIZED: Any = "UNAUTHORIZED"
    FORBIDDEN: Any = "FORBIDDEN"
    NOT_FOUND: Any = "NOT_FOUND"
    ORDER_PURCHASE_UPDATE_NOT_FOUND: Any = "ORDER_PURCHASE_UPDATE_NOT_FOUND"
    TOO_MANY_REQUESTS: Any = "TOO_MANY_REQUESTS"
    INTERNAL_SERVER_ERROR: Any = "INTERNAL_SERVER_ERROR"
    BAD_GATEWAY: Any = "BAD_GATEWAY"
    RETRYABLE_ORDER_PURCHASE_SCREEN_FAILURE: Any = "RETRYABLE_ORDER_PURCHASE_SCREEN_FAILURE"
    RETRYABLE_ORDER_PURCHASE_UPDATE_FAILURE: Any = "RETRYABLE_ORDER_PURCHASE_UPDATE_FAILURE"
    GATEWAY_TIMEOUT: Any = "GATEWAY_TIMEOUT"
    BAD_REQUEST: Any = "BAD_REQUEST"


class Error(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Error: The object used to describe an error, containing both human-readable and machine-readable information."""

    code: Code = Field(..., example="BAD_REQUEST")
    """
    Snake cased all caps error code interpreted from the HTTP status code that can programmatically be acted upon.
    """
    message: str = Field(..., example="An input validation error was encountered. Please see causes for more details.")
    """
    A human-readable explanation of the error, specific to this error occurrence.
    """


class UnauthorizedError(
    Error,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model UnauthorizedError: Indicates that the token sent in the 'Authorization' header is either invalid or missing. Please check the value in the token field along with the token expiration time before retrying."""

    pass


class OrderPurchaseUpdateNotFoundError(
    Error,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model OrderPurchaseUpdateNotFoundError: Indicates that the API cannot find the resource that is either being requested or against which the operation is being performed."""

    pass


class RetryableOrderPurchaseScreenFailure(
    Error,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model RetryableOrderPurchaseScreenFailure: Indicates that the API is either down for maintenance or overloaded and cannot fulfill the request at the current time. This is a temporary error and retrying the same request after a certain delay could eventually result in success.
    There will be a Retry-After HTTP header in API response specifying how long to wait to retry the request. If there is no Retry-After HTTP header then retry can happen immediately. If the error persists after retrying with delay, please reach out to <support team>."

    """

    pass


class RetryableOrderPurchaseUpdateFailure(
    Error,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model RetryableOrderPurchaseUpdateFailure: Indicates that the API is either down for maintenance or overloaded and cannot fulfill the request at the current time. This is a temporary error and retrying the same request after a certain delay could eventually result in success.
    There will be a Retry-After HTTP header in API response specifying how long to wait to retry the request. If there is no Retry-After HTTP header then retry can happen immediately. If the error persists after retrying with delay, please reach out to <support team>."

    """

    pass


class Code1(
    Enum,
):
    r"""pydantic model Code1"""

    MISSING_MANDATORY_PARAM: Any = "MISSING_MANDATORY_PARAM"
    INVALID_PARAM: Any = "INVALID_PARAM"
    INVALID_FORMAT: Any = "INVALID_FORMAT"


class Cause(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Cause"""

    code: Optional[Code1] = Field(None, example="MISSING_MANDATORY_PARAM")
    field: Optional[str] = Field(None, example="$.transaction.customer_account.account_type")
    """
    A JSON Path expression indicating which field, in the request body, caused the error.
    """
    message: Optional[str] = Field(None, example="The value of a field should not be null.")


class BadRequestError(
    Error,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model BadRequestError: Indicates that a bad request occurred. Typically it is an invalid parameter."""

    causes: Optional[list[Cause]] = None


class UpdateType(
    Enum,
):
    r"""pydantic model UpdateType: Transaction type associated with the update event."""

    ORDER_UPDATE: Any = "ORDER_UPDATE"
    CHARGEBACK_FEEDBACK: Any = "CHARGEBACK_FEEDBACK"
    INSULT_FEEDBACK: Any = "INSULT_FEEDBACK"
    REFUND_UPDATE: Any = "REFUND_UPDATE"
    PAYMENT_UPDATE: Any = "PAYMENT_UPDATE"


class CancellationReason(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model CancellationReason: Reason of order update cancellation."""

    primary_reason_code: Optional[constr(max_length=200)] = None
    """
    Primary cancellation reason code.
    """
    sub_reason_code: Optional[constr(max_length=200)] = None
    """
    Substitute cancellation reason code.
    """
    primary_reason_description: Optional[constr(max_length=200)] = None
    """
    Primary cancellation reason code. Required if `order_status = CANCELLED`.
    """
    sub_reason_description: Optional[constr(max_length=200)] = None
    """
    Substitute cancellation reason description.
    """


class RefundStatus(
    Enum,
):
    r"""pydantic model RefundStatus: Identifies the refund status. Possible values are:
    -`ISSUED` - The refund was issued.
    -`SETTLED` - The refund was settled.

    """

    ISSUED: Any = "ISSUED"
    SETTLED: Any = "SETTLED"


class ChargebackStatus(
    Enum,
):
    r"""pydantic model ChargebackStatus: Identifies the chargeback status. Possible values are:
    -`RECEIVED` - The chargeback was received.
    -`REVERSAL` - The chargeback reversal was received.

    """

    RECEIVED: Any = "RECEIVED"
    REVERSAL: Any = "REVERSAL"


class ChargebackReason(
    Enum,
):
    r"""pydantic model ChargebackReason: Reason for chargeback which can be `Fraud` or `Non Fraud`."""

    FRAUD: Any = "FRAUD"
    NON_FRAUD: Any = "NON_FRAUD"


class InsultDetail(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model InsultDetail: Details related to the insult."""

    insult_reported_date_time: Optional[datetime] = None
    """
    Date and time when the insult was reported to the partner, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """


class Status(
    Enum,
):
    r"""pydantic model Status: Defines the current state of the Order.
    Generally, OrderPurchaseScreenRequest is followed by an OrderUpdate reflecting the change in current order status. From `IN_PROGRESS` to any of below possible values:
    * `COMPLETED` is used when the order has been processed fully. For example, inventory has been reserved, and the payment has been settled.
    * `CHANGE_COMPLETED` is like `COMPLETED` but on a changed order.
    * `CANCELLED` is used when the order is cancelled. This could be acustomer initiated cancel or based on Fraud recommendation.
    * `FAILED` is used when order failed due to any errors on Partner system. This could be followed by another OrderUpdate call with any `order_status` once the order is recovered, abandoned, or cancelled.
    * `CHANGE_FAILED` is like `FAILED` but on a changed order.
    *
    * `CHANGE_COMPLETED` or `CHANGE_FAILED` are applicable if OrderPurchaseScreen Fraud API was called via a change in order which is through `transaction.transaction_details.order_type` = `CHANGE`
    * `COMPLETED` or `CANCELLED` order status indicates the completion of lifecycle on an order.

    """

    COMPLETED: Any = "COMPLETED"
    CHANGE_COMPLETED: Any = "CHANGE_COMPLETED"
    CANCELLED: Any = "CANCELLED"
    FAILED: Any = "FAILED"
    CHANGE_FAILED: Any = "CHANGE_FAILED"


class OrderPurchaseUpdateResponse(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model OrderPurchaseUpdateResponse"""

    risk_id: Optional[constr(max_length=200)] = Field(None, example="1234567")
    """
    Unique identifier of transaction that was updated.
    """


class FraudDecision(
    Enum,
):
    r"""pydantic model FraudDecision"""

    ACCEPT: Any = "ACCEPT"
    REVIEW: Any = "REVIEW"
    REJECT: Any = "REJECT"


class SiteInfo(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model SiteInfo"""

    country_code: constr(regex=r"^[A-Z]{3}$") = Field(..., example="USA")
    """
    The alpha-3 ISO code that represents a country name.
    """
    agent_assisted: bool = None
    """
    Identifies if an agent assisted in booking travel for the customer. `False` if the order was directly booked by customer.
    """


class DeviceDetails(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model DeviceDetails"""

    source: Optional[constr(max_length=50)] = None
    """
    Source of the device_box. Default value is `TrustWidget`.
    """
    device_box: Optional[constr(max_length=16000)] = None
    """
    Device related information retrieved from TrustWidget.
    """
    ip_address: constr(
        regex=r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$"
    ) = Field(..., example="192.168.32.48")
    """
    IP address of the device used for booking.
    """


class CurrentOrderStatus(
    Enum,
):
    r"""pydantic model CurrentOrderStatus: Status of the order:
    * `IN_PROGRESS` is used when order has not processed fully. For example, inventory has not yet been reserved, or payment has not yet been settled.
    * `COMPLETED` is used when an order has been processed fully. For example, inventory has been reserved, and the payment has been settled.

    """

    IN_PROGRESS: Any = "IN_PROGRESS"
    COMPLETED: Any = "COMPLETED"


class OrderType(
    Enum,
):
    r"""pydantic model OrderType: Type of order. Possible `order_types`.

    `CREATE` - Initial type of a brand new order.

    `CHANGE` - If a `OrderPurchaseScreenRequest` has already been submitted for the initial booking with `order_type = CREATE`, but has now been modified and partner wishes to resubmit for Fraud screening then the `order_type = CHANGE`. Examples of changes that are supported are changes made to `check-in/checkout dates` or `price of a TravelProduct`.

    """

    CREATE: Any = "CREATE"
    CHANGE: Any = "CHANGE"


class AccountType(
    Enum,
):
    r"""pydantic model AccountType: Identifies if the customer account is known to the client. Possible values are:

    -`GUEST` - Applicable if the partner maintains record to distinguish whether the transaction was booked via a guest account.

    -`STANDARD` - Default account type.

    """

    GUEST: Any = "GUEST"
    STANDARD: Any = "STANDARD"


class AddressType(
    Enum,
):
    r"""pydantic model AddressType"""

    HOME: Any = "HOME"
    WORK: Any = "WORK"


class Address(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Address"""

    address_type: Optional[AddressType] = None
    address_line1: Optional[constr(max_length=200)] = None
    """
    Address line 1 of the address provided.
    """
    address_line2: Optional[constr(max_length=200)] = None
    """
    Address line 2 of the address provided.
    """
    city: Optional[constr(max_length=200)] = None
    """
    City of the address provided.
    """
    state: Optional[constr(regex=r"^[A-Z]{2}$")] = None
    """
    The two-characters ISO code for the state or province of the address.
    """
    zip_code: Optional[constr(max_length=20)] = None
    """
    Zip code of the address provided.
    """
    country_code: Optional[constr(regex=r"^[A-Z]{3}$")] = None
    """
    ISO alpha-3 country code of the address provided.
    """


class InventorySource(
    Enum,
):
    r"""pydantic model InventorySource: Identifies the business model through which the supply is being sold. Merchant/Agency.
    * `MERCHANT` is used when Partner is the merchant of record for this order.
    * `AGENCY` is used when this order is through an agency booking.

    """

    MERCHANT: Any = "MERCHANT"
    AGENCY: Any = "AGENCY"


class TravelersReference(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model TravelersReference"""

    __root__: constr(max_length=50) = None


class RouteType(
    Enum,
):
    r"""pydantic model RouteType: The type of route or itinerary for the Rail product, indicating the travel arrangement and pattern. Possible values are:
    - `MULTIPLE_DESTINATIONS` - The Rail product includes multiple destinations in its itinerary.
    - `ONE_WAY` - The Rail product represents a one-way journey.
    - `ROUNDTRIP` - The Rail product represents a roundtrip journey.

    """

    MULTIPLE_DESTINATIONS: Any = "MULTIPLE_DESTINATIONS"
    ONE_WAY: Any = "ONE_WAY"
    ROUND_TRIP: Any = "ROUND_TRIP"


class TransportationMethod(
    Enum,
):
    r"""pydantic model TransportationMethod: This attribute represents the specific transportation method by which the passenger is traveling. It captures the mode of transportation used during the Rail product journey, Possible values are:
    - `BUS` - The Rail product includes bus transportation for certain segments of the itinerary.
    - `FERRY` - The Rail product involves ferry transportation as part of the journey.
    - `PUBLIC_TRANSPORT` - The Rail product represents the use of public transportation modes for the journey.
    - `TRAM` - The Rail product includes tram transportation as part of the journey.
    - `RAIL` - The Rail product specifically utilizes train transportation for the journey.
    - `TRANSFER` - The Rail product involves transfers between different modes of transportation.
    - `OTHER` - The Rail product utilizes transportation methods not covered by the aforementioned categories.

    """

    BUS: Any = "BUS"
    FERRY: Any = "FERRY"
    PUBLIC_TRANSPORT: Any = "PUBLIC_TRANSPORT"
    RAIL: Any = "RAIL"
    TRAM: Any = "TRAM"
    TRANSFER: Any = "TRANSFER"
    OTHERS: Any = "OTHERS"


class OperatingCompany(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model OperatingCompany: This attribute captures the name or identifier of the company responsible for operating the Rail product. It represents the specific operating entity, such as Amtrak, British Railways, or a bus company."""

    marketing_name: Optional[constr(max_length=200)] = None
    """
    The name used by the transportation carrier for marketing purposes in the travel segment. Example: ARX, AMTRAC, ARRIVA
    """


class Type(
    Enum,
):
    r"""pydantic model Type: This attribute provides information about the specific classification assigned to the rail station. It helps differentiate between different types of stations, such as major stations (STATION) or stations located within a city (city)."""

    STATION: Any = "STATION"
    CITY: Any = "CITY"


class RailwayStationDetails(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model RailwayStationDetails"""

    name: constr(max_length=200) = Field(..., example="Grand Central Terminal")
    """
    The popularly known name or title by which the railway station is identified.
    """
    type: Optional[Type] = Field(None, example="STATION")
    """
    This attribute provides information about the specific classification assigned to the rail station. It helps differentiate between different types of stations, such as major stations (STATION) or stations located within a city (city).
    """
    station_code: constr(max_length=200) = Field(..., example="GCT")
    """
    The unique identifier or code assigned to an individual rail station or a pseudo-station representing all the stations within a specific city, from which rail travel originates.
    """
    address: Address = None
    timezone: Optional[constr(max_length=200)] = Field(None, example="America/New_York")
    """
    The timezone associated with the location of the station, specifying the local time offset from Coordinated Universal Time (UTC).
    """


class FlightType(
    Enum,
):
    r"""pydantic model FlightType: Identifies the type of air trip based on the air destinations."""

    ROUNDTRIP: Any = "ROUNDTRIP"
    ONEWAY: Any = "ONEWAY"
    MULTIPLE_DESTINATION: Any = "MULTIPLE_DESTINATION"


class AirSegment(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AirSegment"""

    airline_code: constr(max_length=10) = None
    """
    Airline code of the trip segment
    """
    departure_airport_code: constr(max_length=10) = None
    """
    Departure airport of the trip segment
    """
    arrival_airport_code: constr(max_length=10) = None
    """
    Arrival airport of the trip segment
    """
    departure_time: Optional[datetime] = None
    """
    Local date and time of departure from departure location, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    arrival_time: Optional[datetime] = None
    """
    Local date and time of arrival to destination location, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """


class HotelAddress(
    Address,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model HotelAddress: Address of a hotel."""

    pass


class Brand(
    Enum,
):
    r"""pydantic model Brand: The `brand` field value is the payment brand used for payment on this transaction.
    For credit card payment method ensure attributes mentioned in dictionary below are set to corresponding values only.
    Ensure to comply with the naming standards provided in below dictionary. For example, some Payment processors use “Japan Credit Bureau” but “JCB” should be used when calling Fraud API.
    Incorrect `brand` - `card_type` combination will result in data quality issues and result in degraded risk recommendation.
    'brand' is an enum value with the following mapping with CreditCard 'card_type' attribute:
    *       brand                 :      card_type
    * -------------------------------------------------------
    * `AMERICAN_EXPRESS`          : `AMERICAN_EXPRESS`
    * `DINERS_CLUB_INTERNATIONAL` : `DINERS_CLUB`
    * `BC_CARD`                   : `DINERS_CLUB`
    * `DISCOVER`                  : `DISCOVER`
    * `BC_CARD`                   : `DISCOVER`
    * `DINERS_CLUB_INTERNATIONAL` : `DISCOVER`
    * `JCB`                       : `DISCOVER`
    * `JCB`                       : `JCB`
    * `MASTER_CARD`               : `MASTER_CARD`
    * `MAESTRO`                   : `MASTER_CARD`
    * `POSTEPAY_MASTERCARD`       : `MASTER_CARD`
    * `SOLO`                      : `SOLO`
    * `SWITCH`                    : `SWITCH`
    * `MAESTRO`                   : `MAESTRO`
    * `CHINA_UNION_PAY`           : `CHINA_UNION_PAY`
    * `VISA`                      : `VISA`
    * `VISA_DELTA`                : `VISA`
    * `VISA_ELECTRON`             : `VISA`
    * `CARTA_SI`                  : `VISA`
    * `CARTE_BLEUE`               : `VISA`
    * `VISA_DANKORT`              : `VISA`
    * `POSTEPAY_VISA_ELECTRON`    : `VISA`
    * `PAYPAL`                    :

    'brand' with 'Points' payment_type is an enum value with following:
    * `EXPEDIA_REWARDS`
    * `AMEX_POINTS`
    * `BANK_OF_AMERICA_REWARDS`
    * `DISCOVER_POINTS`
    * `MASTER_CARD_POINTS`
    * `CITI_THANK_YOU_POINTS`
    * `MERRILL_LYNCH_REWARDS`
    * `WELLS_FARGO_POINTS`
    * `DELTA_SKY_MILES`
    * `UNITED_POINTS`
    * `DISCOVER_MILES`
    * `ALASKA_MILES`
    * `RBC_REWARDS`
    * `BILT_REWARDS`
    * `ORBUCKS`
    * `CHEAP_CASH`
    * `BONUS_PLUS`
    * `ULTIMATE_REWARDS`
    * `UATP`
    * `UATP_SUPPLY`
    * `AIR_PLUS`
    * `US_PASS_PLUS`

    'brand' with 'GiftCard' payment_type is an enum value with following:
    * `GIFT_CARD`

    'brand' with 'InternetBankPayment' payment_type is an enum value with following:
    * `IBP`
    * `LOCAL_DEBIT_CARD`
    * `SOFORT`
    * `YANDEX`
    * `WEB_MONEY`
    * `QIWI`
    * `BITCOIN`

    'brand' with 'DirectDebit' payment_type is an enum value with following:
    * `ELV`
    * `INTER_COMPANY`

    """

    AMERICAN_EXPRESS: Any = "AMERICAN_EXPRESS"
    DINERS_CLUB_INTERNATIONAL: Any = "DINERS_CLUB_INTERNATIONAL"
    BC_CARD: Any = "BC_CARD"
    DISCOVER: Any = "DISCOVER"
    JCB: Any = "JCB"
    MASTER_CARD: Any = "MASTER_CARD"
    MAESTRO: Any = "MAESTRO"
    POSTEPAY_MASTERCARD: Any = "POSTEPAY_MASTERCARD"
    SOLO: Any = "SOLO"
    SWITCH: Any = "SWITCH"
    CHINA_UNION_PAY: Any = "CHINA_UNION_PAY"
    VISA: Any = "VISA"
    VISA_DELTA: Any = "VISA_DELTA"
    VISA_ELECTRON: Any = "VISA_ELECTRON"
    CARTA_SI: Any = "CARTA_SI"
    CARTE_BLEUE: Any = "CARTE_BLEUE"
    VISA_DANKORT: Any = "VISA_DANKORT"
    POSTEPAY_VISA_ELECTRON: Any = "POSTEPAY_VISA_ELECTRON"
    PAYPAL: Any = "PAYPAL"
    EXPEDIA_REWARDS: Any = "EXPEDIA_REWARDS"
    AMEX_POINTS: Any = "AMEX_POINTS"
    BANK_OF_AMERICA_REWARDS: Any = "BANK_OF_AMERICA_REWARDS"
    DISCOVER_POINTS: Any = "DISCOVER_POINTS"
    MASTER_CARD_POINTS: Any = "MASTER_CARD_POINTS"
    CITI_THANK_YOU_POINTS: Any = "CITI_THANK_YOU_POINTS"
    MERRILL_LYNCH_REWARDS: Any = "MERRILL_LYNCH_REWARDS"
    WELLS_FARGO_POINTS: Any = "WELLS_FARGO_POINTS"
    DELTA_SKY_MILES: Any = "DELTA_SKY_MILES"
    UNITED_POINTS: Any = "UNITED_POINTS"
    DISCOVER_MILES: Any = "DISCOVER_MILES"
    ALASKA_MILES: Any = "ALASKA_MILES"
    RBC_REWARDS: Any = "RBC_REWARDS"
    BILT_REWARDS: Any = "BILT_REWARDS"
    ORBUCKS: Any = "ORBUCKS"
    CHEAP_CASH: Any = "CHEAP_CASH"
    BONUS_PLUS: Any = "BONUS_PLUS"
    ULTIMATE_REWARDS: Any = "ULTIMATE_REWARDS"
    UATP: Any = "UATP"
    UATP_SUPPLY: Any = "UATP_SUPPLY"
    AIR_PLUS: Any = "AIR_PLUS"
    US_PASS_PLUS: Any = "US_PASS_PLUS"
    GIFT_CARD: Any = "GIFT_CARD"
    IBP: Any = "IBP"
    LOCAL_DEBIT_CARD: Any = "LOCAL_DEBIT_CARD"
    SOFORT: Any = "SOFORT"
    YANDEX: Any = "YANDEX"
    WEB_MONEY: Any = "WEB_MONEY"
    QIWI: Any = "QIWI"
    BITCOIN: Any = "BITCOIN"
    ELV: Any = "ELV"
    INTER_COMPANY: Any = "INTER_COMPANY"


class PaymentThreeDSCriteria(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model PaymentThreeDSCriteria: Payment ThreeDS criteria attributes."""

    probable_flag: Optional[bool] = None
    """
    This is a flag passed that indicates that this transaction could potentially go through 3DS.
    """
    transaction_model: Optional[constr(max_length=200)] = None
    """
    Model used to process payment transaction.
    """


class PaymentReason(
    Enum,
):
    r"""pydantic model PaymentReason: The reason of payment. Possible values:
    - `FULL` - If the amount is paid i full for the order
    - `DEPOSIT` - The initial payment. Amount to be paid up front.
    - `SCHEDULED` - The amount to be payment based on a schedule for the remaining portion of the booking amount.
    - `SUBSEQUENT` - An additional amount paid that was not originally scheduled.
    - `DEFERRED`

    """

    FULL: Any = "FULL"
    DEPOSIT: Any = "DEPOSIT"
    SCHEDULED: Any = "SCHEDULED"
    SUBSEQUENT: Any = "SUBSEQUENT"
    DEFERRED: Any = "DEFERRED"


class VerificationType(
    Enum,
):
    r"""pydantic model VerificationType: The type of the verification used to verify the instrument. If the Card Verfication Value was provided to verify the credit card used for the transaction, `type = CVV`."""

    CVV: Any = "CVV"
    field_3DS: Any = "3DS"


class PaymentStatus(
    Enum,
):
    r"""pydantic model PaymentStatus: The status of the payment operation."""

    COMPLETED: Any = "COMPLETED"
    FAILED: Any = "FAILED"


class PaymentMethod(
    Enum,
):
    r"""pydantic model PaymentMethod: The payment method used at the time of purchase for the transaction. Supported `method`'s are: `CREDIT_CARD`, `PAYPAL`, `POINTS`, `GIFT_CARD`, `INTERNET_BANK_PAYMENT`, `DIRECT_DEBIT`."""

    CREDIT_CARD: Any = "CREDIT_CARD"
    PAYPAL: Any = "PAYPAL"
    POINTS: Any = "POINTS"
    GIFT_CARD: Any = "GIFT_CARD"
    INTERNET_BANK_PAYMENT: Any = "INTERNET_BANK_PAYMENT"
    DIRECT_DEBIT: Any = "DIRECT_DEBIT"


class TravelProductType(
    Enum,
):
    r"""pydantic model TravelProductType: Type of product."""

    CRUISE: Any = "CRUISE"
    AIR: Any = "AIR"
    CAR: Any = "CAR"
    INSURANCE: Any = "INSURANCE"
    HOTEL: Any = "HOTEL"
    RAIL: Any = "RAIL"


class CardType(
    Enum,
):
    r"""pydantic model CardType: The 'card_type' field value is an enum value which is associated with the payment method of the specific payment instrument.
    For credit card payment method ensure attributes mentioned in dictionary below are set to corresponding values only.
    Ensure to comply with the naming standards provided in below dictionary. For example, some Payment processors use “Japan Credit Bureau” but “JCB” should be used when calling Fraud API.
    Incorrect `card_type` - `brand` combination will result in data quality issues and result in degraded risk recommendation.
    'card_type' is an enum value with the following mapping with Payment `brand` attribute:
    *       card_type            :          brand
    * --------------------------------------------------------
    * `AMERICAN_EXPRESS`         : `AMERICAN_EXPRESS`
    * `DINERS_CLUB`              : `DINERS_CLUB_INTERNATIONAL`
    * `DINERS_CLUB`              : `BC_CARD`
    * `DISCOVER`                 : `DISCOVER`
    * `DISCOVER`                 : `BC_CARD`
    * `DISCOVER`                 : `DINERS_CLUB_INTERNATIONAL`
    * `DISCOVER`                 : `JCB`
    * `JCB`                      : `JCB`
    * `MASTER_CARD`              : `MASTER_CARD`
    * `MASTER_CARD`              : `MAESTRO`
    * `MASTER_CARD`              : `POSTEPAY_MASTERCARD`
    * `SOLO`                     : `SOLO`
    * `SWITCH`                   : `SWITCH`
    * `MAESTRO`                  : `MAESTRO`
    * `CHINA_UNION_PAY`          : `CHINA_UNION_PAY`
    * `VISA`                     : `VISA`
    * `VISA`                     : `VISA_DELTA`
    * `VISA`                     : `VISA_ELECTRON`
    * `VISA`                     : `CARTA_SI`
    * `VISA`                     : `CARTE_BLEUE`
    * `VISA`                     : `VISA_DANKORT`
    * `VISA`                     : `POSTEPAY_VISA_ELECTRON`

    """

    AMERICAN_EXPRESS: Any = "AMERICAN_EXPRESS"
    DINERS_CLUB: Any = "DINERS_CLUB"
    DISCOVER: Any = "DISCOVER"
    JCB: Any = "JCB"
    MASTER_CARD: Any = "MASTER_CARD"
    SOLO: Any = "SOLO"
    SWITCH: Any = "SWITCH"
    MAESTRO: Any = "MAESTRO"
    CHINA_UNION_PAY: Any = "CHINA_UNION_PAY"
    VISA: Any = "VISA"


class Name(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Name: Group of attributes intended to hold information about a customer or traveler's name for the order."""

    last_name: constr(max_length=200) = None
    """
    Surname, or last name, of the person.
    """
    first_name: constr(max_length=200) = None
    """
    Given, or first name, of the person.
    """
    middle_name: Optional[constr(max_length=200)] = None
    """
    Middle name of the person.
    """
    title: Optional[constr(max_length=200)] = None
    """
    Title of the person for name (e.g. Mr., Ms. etc).
    """
    suffix: Optional[constr(max_length=50)] = None
    """
    Generational designations (e.g. Sr, Jr, III) or values that indicate the individual holds a position, educational degree, accreditation, office, or honor (e.g. PhD, CCNA, OBE).
    """


class TelephoneType(
    Enum,
):
    r"""pydantic model TelephoneType: Classification of the phone (e.g. `Home`, `Mobile`)."""

    HOME: Any = "HOME"
    MOBILE: Any = "MOBILE"
    BUSINESS: Any = "BUSINESS"
    FAX: Any = "FAX"
    OTHER: Any = "OTHER"


class TelephonePlatformType(
    Enum,
):
    r"""pydantic model TelephonePlatformType: Classification of the phone platform."""

    MOBILE: Any = "MOBILE"
    LANDLINE: Any = "LANDLINE"
    VOIP: Any = "VOIP"


class Email(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Email: Group of attributes intended to hold information about email address associated with the transaction."""

    email_address: Optional[EmailStr] = None
    """
    Full email address including the alias, @ symbol, domain, and root domain.
    """


class Amount(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Amount"""

    value: float = None
    """
    The amount required in payment for the product/order in local currency (including any taxes and fees).
    """
    currency_code: constr(regex=r"^[A-Z]{3}$", max_length=3) = None
    """
    The ISO  alpha-3 country code for the amount currency.
    """


class Code2(
    Enum,
):
    r"""pydantic model Code2: Snake cased all caps error code interpreted from the HTTP status code that can programmatically be acted upon."""

    UNAUTHORIZED: Any = "UNAUTHORIZED"
    FORBIDDEN: Any = "FORBIDDEN"
    NOT_FOUND: Any = "NOT_FOUND"
    ACCOUNT_UPDATE_NOT_FOUND: Any = "ACCOUNT_UPDATE_NOT_FOUND"
    TOO_MANY_REQUESTS: Any = "TOO_MANY_REQUESTS"
    INTERNAL_SERVER_ERROR: Any = "INTERNAL_SERVER_ERROR"
    BAD_GATEWAY: Any = "BAD_GATEWAY"
    RETRYABLE_ACCOUNT_SCREEN_FAILURE: Any = "RETRYABLE_ACCOUNT_SCREEN_FAILURE"
    RETRYABLE_ACCOUNT_UPDATE_FAILURE: Any = "RETRYABLE_ACCOUNT_UPDATE_FAILURE"
    GATEWAY_TIMEOUT: Any = "GATEWAY_TIMEOUT"
    BAD_REQUEST: Any = "BAD_REQUEST"


class AccountTakeoverError(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountTakeoverError: The object used to describe an error, containing both human-readable and machine-readable information."""

    code: Code2 = Field(..., example="BAD_REQUEST")
    """
    Snake cased all caps error code interpreted from the HTTP status code that can programmatically be acted upon.
    """
    message: str = Field(..., example="An input validation error was encountered. Please see causes for more details.")
    """
    A human-readable explanation of the error, specific to this error occurrence.
    """


class AccountTakeoverUnauthorizedError(
    AccountTakeoverError,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountTakeoverUnauthorizedError: Indicates that the token sent in the 'Authorization' header is either invalid or missing. Please check the value in the token field along with the token expiration time before retrying."""

    pass


class AccountUpdateNotFoundError(
    AccountTakeoverError,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountUpdateNotFoundError: Indicates that the API cannot find the resource that is either being requested or against which the operation is being performed."""

    pass


class ServiceUnavailableError(
    AccountTakeoverError,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model ServiceUnavailableError: Indicates that the API is either down for maintenance or overloaded and cannot fulfill the request at the current time. This is a temporary error and retrying the same request after a certain delay could eventually result in success.
    There will be a Retry-After HTTP header in API response specifying how long to wait to retry the request. If there is no Retry-After HTTP header then retry can happen immediately. If the error persists after retrying with delay, please reach out to <support team>."

    """

    pass


class Code3(
    Enum,
):
    r"""pydantic model Code3"""

    MISSING_MANDATORY_PARAM: Any = "MISSING_MANDATORY_PARAM"
    INVALID_PARAM: Any = "INVALID_PARAM"
    INVALID_FORMAT: Any = "INVALID_FORMAT"


class Cause1(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Cause1"""

    code: Optional[Code3] = Field(None, example="MISSING_MANDATORY_PARAM")
    field: Optional[str] = Field(None, example="$.transaction.device_details.device_box")
    """
    A JSON Path expression indicating which field, in the request body, caused the error.
    """
    message: Optional[str] = Field(None, example="The value of a field was missed or not valid.")


class AccountTakeoverBadRequestError(
    AccountTakeoverError,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountTakeoverBadRequestError: Indicates that a bad request occurred. Typically it is an invalid parameter."""

    causes: Optional[list[Cause1]] = None


class Type1(
    Enum,
):
    r"""pydantic model Type1: The categorized type of account update event from the Partner's system."""

    MULTI_FACTOR_AUTHENTICATION_UPDATE: Any = "MULTI_FACTOR_AUTHENTICATION_UPDATE"
    REMEDIATION_UPDATE: Any = "REMEDIATION_UPDATE"


class AccountUpdateRequestGeneric(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountUpdateRequest: The `type` field value is used as a discriminator, with the following mapping:
    * `MULTI_FACTOR_AUTHENTICATION_UPDATE`: `MultiFactorAuthenticationUpdate`
    * `REMEDIATION_UPDATE`: `RemediationUpdate`

    """

    type: Type1 = None
    """
    The categorized type of account update event from the Partner's system.
    """
    risk_id: constr(max_length=200) = Field(..., example="123456789")
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `AccountScreenResponse`.
    """


class DeliveryMethod(
    Enum,
):
    r"""pydantic model DeliveryMethod: The delivery method of the Multi-Factor Authentication to a user."""

    EMAIL: Any = "EMAIL"
    SMS: Any = "SMS"
    VOICE: Any = "VOICE"
    PUSH: Any = "PUSH"


class Status1(
    Enum,
):
    r"""pydantic model Status1: The status of a user''s response to the Multi-Factor Authentication initiated by the Partner''s system to the user.'
    - `SUCCESS` - Applicable if the user successfully passed the challenge.
    - `ABANDON` - Applicable if the user did not complete the challenge.
    - `FAILED` - Applicable if the user failed the challenge.

    """

    SUCCESS: Any = "SUCCESS"
    ABANDON: Any = "ABANDON"
    FAILED: Any = "FAILED"


class ActionName(
    Enum,
):
    r"""pydantic model ActionName: The categorized remediation action initiated by the Partner''s system to a user. Possible values are:
    - `PASSWORD_RESET` - Applicable if this event is the result of a password reset by the Partner''s system.
    - `DISABLE_ACCOUNT` - Applicable if this event is the result of disabling an account by the Partner''s system.
    - `TERMINATE_ALL_SESSIONS` - Applicable if this event is the result of terminating all active user sessions of an account by the Partner''s system.

    """

    PASSWORD_RESET: Any = "PASSWORD_RESET"
    DISABLE_ACCOUNT: Any = "DISABLE_ACCOUNT"
    TERMINATE_ALL_SESSIONS: Any = "TERMINATE_ALL_SESSIONS"


class Status2(
    Enum,
):
    r"""pydantic model Status2: The status of the remediation action.
    - `SUCCESS` - Applicable if the Partner''s system was successfully able to perform the remediation action.
    - `FAILED` - Applicable if the Partner''s system failed to perform the remediation action.

    """

    SUCCESS: Any = "SUCCESS"
    FAILED: Any = "FAILED"


class RemediationUpdateAction(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model RemediationUpdateAction: Information specific to the remediation action initiated by the Partner's system to a user."""

    action_name: ActionName = None
    """
    The categorized remediation action initiated by the Partner''s system to a user. Possible values are:
    - `PASSWORD_RESET` - Applicable if this event is the result of a password reset by the Partner''s system.
    - `DISABLE_ACCOUNT` - Applicable if this event is the result of disabling an account by the Partner''s system.
    - `TERMINATE_ALL_SESSIONS` - Applicable if this event is the result of terminating all active user sessions of an account by the Partner''s system.

    """
    status: Status2 = None
    """
    The status of the remediation action.
      - `SUCCESS` - Applicable if the Partner''s system was successfully able to perform the remediation action.
      - `FAILED` - Applicable if the Partner''s system failed to perform the remediation action.

    """
    update_end_date_time: Optional[datetime] = None
    """
    The local date and time the remediation action to a user ended in the Partner's system, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """


class AccountUpdateResponse(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountUpdateResponse"""

    risk_id: Optional[constr(max_length=200)] = Field(None, example="1234567")
    """
    Unique identifier of transaction that was updated.
    """


class AccountTakeoverFraudDecision(
    Enum,
):
    r"""pydantic model AccountTakeoverFraudDecision: Fraud recommendation for an account transaction. A recommendation can be ACCEPT, CHALLENGE, or REJECT.
    - `ACCEPT` - Represents an account transaction where the user’’s account activity is accepted.
    - `CHALLENGE` - Represents an account transaction that requires additional verification or challenges the user’’s identity (example: CAPTCHA, MULTI_FACTOR_AUTHENTICATION, etc).
    - `REJECT` - Represents a suspicious account transaction where the user’’s credentials or their behavior requires us to block the account activity.

    """

    ACCEPT: Any = "ACCEPT"
    CHALLENGE: Any = "CHALLENGE"
    REJECT: Any = "REJECT"


class PlacementName(
    Enum,
):
    r"""pydantic model PlacementName: The categorized name of the page where a user initiated event is being evaluated.
    - `LOGIN` - Applicable if the user initiated this account event from a login web page.
    - `PASSWORD_RESET` - Applicable if the user initiated this account event from a password reset web page.

    """

    LOGIN: Any = "LOGIN"
    PASSWORD_RESET: Any = "PASSWORD_RESET"


class AccountTakeoverSiteInfo(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountTakeoverSiteInfo: Information specific to the Partner's website through which a transaction was made."""

    locale: Optional[constr(regex=r"^([a-z]{2}-[A-Z]{2})$")] = Field(None, example="en-US")
    """
    The locale of the website a user is accessing, which is separate from the user configured browser locale, in ISO 639-2 language code format and in ISO 3166-1 country code format.
    """
    name: Optional[constr(max_length=200)] = Field(None, example="expedia.com")
    """
    Name of the website from which the event is generated.
    """
    brand_name: constr(max_length=200) = None
    """
    The trademark brand name that is displayed to a user on the website.
    """
    placement_name: Optional[PlacementName] = None
    """
    The categorized name of the page where a user initiated event is being evaluated.
    - `LOGIN` - Applicable if the user initiated this account event from a login web page.
    - `PASSWORD_RESET` - Applicable if the user initiated this account event from a password reset web page.

    """


class Type2(
    Enum,
):
    r"""pydantic model Type2: The categorized type of device used by a user. Possible values are:
    - `WEBSITE` - Applicable if the user initiated this event from a web browser on a desktop computer.
    - `PHONE_WEB` - Applicable if the user initiated this event from a web browser on a phone.
    - `TABLET_WEB` - Applicable if the user initiated this event from a web browser on a tablet.
    - `PHONE_APP` - Applicable if the user initiated this event from an app on a phone.
    - `TABLET_APP` - Applicable if the user initiated this event from an app on a tablet.

    """

    WEBSITE: Any = "WEBSITE"
    PHONE_WEB: Any = "PHONE_WEB"
    TABLET_WEB: Any = "TABLET_WEB"
    PHONE_APP: Any = "PHONE_APP"
    TABLET_APP: Any = "TABLET_APP"


class AccountTakeoverDeviceDetails(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountTakeoverDeviceDetails: Information specific to the Partner's device through which a transaction was made."""

    source: Optional[constr(max_length=50)] = None
    """
    Source of the device_box. Default value is `TrustWidget`.
    """
    device_box: constr(max_length=16000) = None
    """
    Device related information retrieved from TrustWidget.
    """
    ip_address: constr(
        regex=r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$"
    ) = Field(..., example="192.168.32.48")
    """
    IP address of the device used for this event.
    """
    user_agent: constr(max_length=200) = Field(
        ..., example="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    )
    """
    The application type, operating system, software vendor, or software version of the originating request.
    """
    type: Optional[Type2] = None
    """
    The categorized type of device used by a user. Possible values are:
    - `WEBSITE` - Applicable if the user initiated this event from a web browser on a desktop computer.
    - `PHONE_WEB` - Applicable if the user initiated this event from a web browser on a phone.
    - `TABLET_WEB` - Applicable if the user initiated this event from a web browser on a tablet.
    - `PHONE_APP` - Applicable if the user initiated this event from an app on a phone.
    - `TABLET_APP` - Applicable if the user initiated this event from an app on a tablet.

    """


class AccountType1(
    Enum,
):
    r"""pydantic model AccountType1: Identifies the account type of a user''s account. Possible values are:
    - `INDIVIDUAL` - Applicable if this account is for an individual traveler.
    - `BUSINESS` - Applicable if this account is for a business or organization account used by suppliers or Partners.

    """

    INDIVIDUAL: Any = "INDIVIDUAL"
    BUSINESS: Any = "BUSINESS"


class AccountRole(
    Enum,
):
    r"""pydantic model AccountRole: Identifies the account role and associated permissions of a user''s account. Possible values are:
    - `USER`: Basic account with no special privileges.
    - `MANAGER`: Account with additional privileges, such as the ability to make bookings for others.
    - `ADMIN`: Account with higher privileges than a manager, including the ability to grant manager access to other users.

    """

    USER: Any = "USER"
    MANAGER: Any = "MANAGER"
    ADMIN: Any = "ADMIN"


class AccountTakeoverName(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountTakeoverName: Group of attributes intended to hold information about a customer or traveler''s name for the account."""

    last_name: constr(max_length=200) = None
    """
    Surname, or last name, of the person.
    """
    first_name: constr(max_length=200) = None
    """
    Given, or first name, of the person.
    """
    middle_name: Optional[constr(max_length=200)] = None
    """
    Middle name of the person.
    """
    title: Optional[constr(max_length=200)] = None
    """
    Title of the person for name (e.g. Mr., Ms. etc).
    """
    suffix: Optional[constr(max_length=50)] = None
    """
    Generational designations (e.g. Sr, Jr, III) or values indicate that the individual holds a position, educational degree, accreditation, office, or honor (e.g. PhD, CCNA, OBE).
    """


class Type3(
    Enum,
):
    r"""pydantic model Type3: The categorized type of account event related to a user's action."""

    LOGIN: Any = "LOGIN"


class AuthenticationType(
    Enum,
):
    r"""pydantic model AuthenticationType: The type of login authentication method used by a user.
    For `authentication_type` ensure attributes mentioned in dictionary below are set to corresponding values only.
    `authentication_type` is an enum value with the following mapping with `authentication_sub_type` attribute:
    *       authentication_type       :     authentication_sub_type
    * -------------------------------------------------------------------------------
    * `CREDENTIALS`                         : `EMAIL`
    * `CREDENTIALS`                         :
    * `PASSWORD_RESET`                      : `EMAIL`
    * `SINGLE_SIGN_ON`                      : `EMAIL`
    * `MULTI_FACTOR_AUTHENTICATION`         : `EMAIL`
    * `MULTI_FACTOR_AUTHENTICATION`         : `PHONE`
    * `SOCIAL`                              : `GOOGLE`
    * `SOCIAL`                              : `FACEBOOK`
    * `SOCIAL`                              : `APPLE`

    """

    CREDENTIALS: Any = "CREDENTIALS"
    PASSWORD_RESET: Any = "PASSWORD_RESET"
    SOCIAL: Any = "SOCIAL"
    SINGLE_SIGN_ON: Any = "SINGLE_SIGN_ON"
    MULTI_FACTOR_AUTHENTICATION: Any = "MULTI_FACTOR_AUTHENTICATION"


class AuthenticationSubType(
    Enum,
):
    r"""pydantic model AuthenticationSubType: The sub type of login authentication method used by a user.
    For `authentication_sub_type` ensure attributes mentioned in dictionary below are set to corresponding values only.
    `authentication_sub_type` is an enum value with the following mapping with `authentication_type` attribute:
    *       authentication_sub_type   :     authentication_type
    * -------------------------------------------------------------------------------
    * `EMAIL`                               : `CREDENTIALS`
    * `EMAIL`                               : `PASSWORD_RESET`
    * `EMAIL`                               : `SINGLE_SIGN_ON`
    * `EMAIL`                               : `MULTI_FACTOR_AUTHENTICATION`
    * `PHONE`                               : `MULTI_FACTOR_AUTHENTICATION`
    * `GOOGLE`                              : `SOCIAL`
    * `FACEBOOK`                            : `SOCIAL`
    * `APPLE`                               : `SOCIAL`
    *                                       : `CREDENTIALS`

    """

    EMAIL: Any = "EMAIL"
    PHONE: Any = "PHONE"
    GOOGLE: Any = "GOOGLE"
    FACEBOOK: Any = "FACEBOOK"
    APPLE: Any = "APPLE"


class FailedLoginReason(
    Enum,
):
    r"""pydantic model FailedLoginReason: The reason for the failed login attempt in the Partner''s system, related to user failure or Partner''s system failure.
    - `INVALID_CREDENTIALS` - Applicable if the user provided invalid login credentials for this login attempt.
    - `ACCOUNT_NOT_FOUND` - Applicable if the user attempted to login to an account that doesn't exist.
    - `VERIFICATION_FAILED` - Applicable if the user failed the verification for this login, or any authentication exception occured in the Partner system for this login attempt.
    - `ACCOUNT_LOCKED` - Applicable if the user attempted to login to an account that is locked.

    """

    INVALID_CREDENTIALS: Any = "INVALID_CREDENTIALS"
    ACCOUNT_NOT_FOUND: Any = "ACCOUNT_NOT_FOUND"
    VERIFICATION_FAILED: Any = "VERIFICATION_FAILED"
    ACCOUNT_LOCKED: Any = "ACCOUNT_LOCKED"


class Type4(
    Enum,
):
    r"""pydantic model Type4: The kind of challenge served by the Partner''s system to a user prior to calling Expedia''s Fraud Prevention Service.
    - `CAPTCHA` - Applicable if the challenge served by the Partner''s system was a Captcha challenge.
    - `TWO_FACTOR` - Applicable if the challenge served by the Partner''s system was a two-factor challenge including (Email verification, One Time Password, Okta, etc).

    """

    CAPTCHA: Any = "CAPTCHA"
    TWO_FACTOR: Any = "TWO_FACTOR"


class Status3(
    Enum,
):
    r"""pydantic model Status3: The status of the challenge served by the Partner''s system to a user before calling Expedia''s Fraud Prevention Service.
    - `SUCCESS` - Applicable if the user successfully passed the challenge.
    - `FAILED` - Applicable if the user failed the challenge.

    """

    SUCCESS: Any = "SUCCESS"
    FAILED: Any = "FAILED"


class ChallengeDetail(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model ChallengeDetail: Information related to challenges initiated by the Partner's system to a user before calling Expedia's Fraud Prevention Service."""

    displayed_flag: bool = None
    """
    Indicates that there was a challenge initiated by the Partner's system to a user before calling Expedia's Fraud Prevention Service.
    """
    type: Type4 = None
    """
    The kind of challenge served by the Partner''s system to a user prior to calling Expedia''s Fraud Prevention Service.
    - `CAPTCHA` - Applicable if the challenge served by the Partner''s system was a Captcha challenge.
    - `TWO_FACTOR` - Applicable if the challenge served by the Partner''s system was a two-factor challenge including (Email verification, One Time Password, Okta, etc).

    """
    status: Status3 = None
    """
    The status of the challenge served by the Partner''s system to a user before calling Expedia''s Fraud Prevention Service.
    - `SUCCESS` - Applicable if the user successfully passed the challenge.
    - `FAILED` - Applicable if the user failed the challenge.

    """


class ForbiddenError(
    AccountTakeoverError,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model ForbiddenError: Indicates that the API cannot fulfill the request because while the client is correctly authenticated, the client doesn't have the permission to execute the specified operation. This error type does not imply that the request is valid, or that the resource against which the operation being performed exists or satisfies other pre-conditions."""

    pass


class NotFoundError(
    AccountTakeoverError,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model NotFoundError: Indicates that the API cannot find the resource that is either being requested or against which the operation is being performed. Please check the request again to make sure that the request is valid."""

    pass


class TooManyRequestsError(
    AccountTakeoverError,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model TooManyRequestsError: Indicates that the API cannot fulfill the request because server resources have been exhausted. Perhaps the client has sent too many requests in a given amount of time or has reached some specific quota. Please check the rate limits for the product and adjust as necessary before retries. If you believe the rate limit was incorrect or if you need a different rate limit, please reach out to the <support team> regarding the next steps."""

    pass


class InternalServerError(
    AccountTakeoverError,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model InternalServerError: Indicates that the API encountered an unexpected condition that prevented it from fulfilling the request. Sometimes used as a generic catch-allerror type when no other error types can be used. Retrying the same request will usually result in the same error. Please reach out to support team as next step for this error resolution."""

    pass


class BadGatewayError(
    AccountTakeoverError,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model BadGatewayError: Indicates that the server received an invalid response from the upstream server. Causes could be incorrectly configured target server at gateway, EOF exception, incorrectly configured keep-alive timeouts. Please reach out to support team as next step for this error resolution."""

    pass


class GatewayTimeoutError(
    AccountTakeoverError,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model GatewayTimeoutError: Indicates that the API gateway has issues completing the request on time. Request can be retried if it is idempotent, If the issue persists, please reach out to support. For non-idempotent requests, please reach out to <support team> to know the status of your request before attempting retries."""

    pass


class OrderPurchaseUpdateRequestGeneric(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model OrderPurchaseUpdateRequest: The `type` field value is used as a discriminator, with the following mapping:
    * `ORDER_UPDATE`: `OrderUpdate`
    * `CHARGEBACK_FEEDBACK`: `ChargebackFeedback`
    * `INSULT_FEEDBACK`: `InsultFeedback`
    * `REFUND_UPDATE`: `RefundUpdate`
    * `PAYMENT_UPDATE`: `PaymentUpdate`

    """

    type: UpdateType = None
    risk_id: constr(max_length=200) = Field(..., example="123456789")
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """


class OrderUpdate(
    OrderPurchaseUpdateRequestGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model OrderUpdate: Order related data that should be updated."""

    order_status: Status = None
    acquirer_reference_number: Optional[constr(max_length=200)] = None
    """
    A unique number that tags a credit or debit card transaction when it goes from the merchant's bank through to the cardholder's bank.
    `acquirer_reference_number` is a required field only if `order_status` = `COMPLETED`
    Typically, merchants can get this number from their payment processors.
    This number is used when dealing with disputes/chargebacks on original transactions.

    """
    cancellation_reason: Optional[CancellationReason] = None
    type: Literal["ORDER_UPDATE"] = "ORDER_UPDATE"


class InsultFeedback(
    OrderPurchaseUpdateRequestGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model InsultFeedback: Feedback from EG external partners regarding a false positive recommendation that from Fraud Prevention system gave for their customer."""

    insult_detail: Optional[InsultDetail] = None
    type: Literal["INSULT_FEEDBACK"] = "INSULT_FEEDBACK"


class RefundUpdateGeneric(
    OrderPurchaseUpdateRequestGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model RefundUpdate: Refund related data. Update should be sent when refund is issued or settled. Amounts should include all fees and taxes."""

    refund_status: RefundStatus = None
    """
    Identifies the refund status. Possible values are:
    -`ISSUED` - The refund was issued.
    -`SETTLED` - The refund was settled.

    """
    type: Literal["REFUND_UPDATE"] = "REFUND_UPDATE"


class IssuedRefundUpdateDetails(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model IssuedRefundUpdateDetails: Data that describes issued refund that should be updated."""

    refund_issued_date_time: datetime = None
    """
    Date and time when the 3rd party payment processor confirmed that a previously submitted payment refund has issued at the participating financial institutions.
    """
    refund_issued_amount: Amount = None


class SettledRefundUpdateDetails(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model SettledRefundUpdateDetails: Data that describes settled refund that should be updated."""

    refund_settlement_date_time: datetime = None
    """
    Date and time when the 3rd party payment processor confirmed that a previously submitted payment refund has settled at the participating financial institutions.
    """
    refund_deposit_date_time: datetime = None
    """
    Date and time when the refund was deposited to the original form of payment.
    """
    acquirer_reference_number: constr(max_length=200) = None
    """
    A unique number that tags a credit or debit card transaction when it goes from the merchant's bank through to the cardholder's bank.
    Typically, merchants can get this number from their payment processors.
    This number is used when dealing with disputes/chargebacks on original transactions.

    """
    settlement_id: constr(max_length=200) = None
    """
    Unique settlement identifier specific to the payment processor for the settlement transaction generated for a previously submitted payment refund.
    """
    refund_settled_amount: Amount = None


class PaymentUpdate(
    OrderPurchaseUpdateRequestGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model PaymentUpdate: Payment related data that should be updated."""

    merchant_order_code: constr(max_length=200) = None
    """
    Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.
    """
    type: Literal["PAYMENT_UPDATE"] = "PAYMENT_UPDATE"


class ChargebackDetail(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model ChargebackDetail: Details related to the chargeback."""

    chargeback_status: ChargebackStatus = None
    """
    Identifies the chargeback status. Possible values are:
    -`RECEIVED` - The chargeback was received.
    -`REVERSAL` - The chargeback reversal was received.

    """
    chargeback_reason: ChargebackReason = None
    """
    Reason for chargeback which can be `Fraud` or `Non Fraud`.
    """
    chargeback_amount: Amount = None
    bank_reason_code: Optional[constr(max_length=200)] = None
    """
    Unique code provided by the acquiring bank for the category of fraud.
    """
    chargeback_reported_date_time: Optional[datetime] = None
    """
    Date and time when the chargeback was reported to the partner, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """


class OrderPurchaseScreenResponse(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model OrderPurchaseScreenResponse"""

    risk_id: Optional[constr(max_length=200)] = Field(None, example="1234567")
    """
    Unique identifier assigned to the transaction by Expedia's Fraud Prevention Service.
    """
    decision: Optional[FraudDecision] = None


class TravelProductGeneric(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model TravelProduct: The `type` field value is used as a discriminator, with the following mapping:
    * `CRUISE`: `Cruise`
    * `AIR`: `Air`
    * `CAR`: `Car`
    * `INSURANCE`: `Insurance`
    * `HOTEL`: `Hotel`
    * `RAIL`: `Rail`

    """

    price: Amount = None
    type: TravelProductType = None
    inventory_type: constr(max_length=30) = None
    """
    Type of inventory.
    Ensure attributes mentioned in dictionary below are set to corresponding values only.
    `inventory_type` has the following mapping with TravelProduct `type` attribute:
    *       inventory_type            :      type
    * ------------------------------------------------------
    *  `Cruise`                       : `CRUISE`
    *  `Air`                          : `AIR`
    *  `Car`                          : `CAR`
    *  `Insurance`                    : `INSURANCE`
    *  `Hotel`                        : `HOTEL`
    *  `Rail`                         :  `RAIL`

    """
    inventory_source: InventorySource = None
    """
    Identifies the business model through which the supply is being sold. Merchant/Agency.
    * `MERCHANT` is used when Partner is the merchant of record for this order.
    * `AGENCY` is used when this order is through an agency booking.

    """
    travelers_references: Optional[list[constr(max_length=50)]] = Field(None, maxItems=40, minItems=1)
    """
    List of travelerGuids who are part of the traveling party on the order for the product.
    Information for each product and its required travelers should be provided in the API request.
    If the product booking does not require accompanying quest information then that does not need to be provided in the API request.
    Example:
    * For Air products, all travelers' details are required to complete the booking.
    * For Hotel products, typically the details on the person checking-in is required.
    * For Car products, typically only the primary driver information is required.
    If multiple traveler details are in the itinerary, this structure allows to fill up traveler details once in the `travelers` section, and then associate individual products to the respective travelers.
    This association is made using `traveler_id` field. A GUID can be generated for each object in the `travelers` section. The same GUID can be provided in the `traveler_references` below.
    The `travelers` array should have at least one `traveler` object, and each `traveler` object should have a `traveler_id` which is not necessarily an account id.
    Example:
    *   Travelers
    * ------------
    *  A - GUID1
    *  B - GUID2
    *  C - GUID3
    *
    *   Products
    * ------------
    * Air
    *   [GUID1, GUID2, GUID3]
    * Hotel
    *   [GUID1]
    * Car
    *   [GUID3]
    * Rail
    *   [GUID2]
    * The example above demonstrates the association of travelers with various products.
    * All three travelers (A, B, and C) are associated with the Air product.
    * Traveler A is associated with the Hotel.
    * Traveler C is associated with the Car product.
    * Traveler B is associated with the Rail product.

    """
    pay_later: Optional[bool] = None
    """
    The attribute serves as a boolean indicator that significantly influences the handling of payment information during the fraud prevention process:
    * When 'pay_later' is set to 'true':
      - This configuration signals that payment information is optional for the booking. Travelers are given the choice to defer payment until they arrive at the rental counter following the completion of the booking.
      - It is imperative for partners to explicitly set this attribute to 'true' when payment information can be optional for a particular booking scenario.
    * When 'pay_later' is set to 'false':
      - In this mode, the attribute mandates the inclusion of payment information during the order purchase screen request. Travelers are required to provide payment details.
      - Partners must exercise caution and ensure they supply the necessary payment information, as failure to do so in cases where 'pay_later' is set to 'false' will result in a 'Bad Request' error. This error helps maintain the consistency and accuracy of the fraud prevention process and payment handling.

    """


class RailSegments(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model RailSegments"""

    departure_time: datetime = None
    """
    The local date and time of the scheduled departure from the departure station, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    arrival_time: datetime = None
    """
    The local date and time of the scheduled arrival at the destination station, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    departure_station: RailwayStationDetails = None
    arrival_station: RailwayStationDetails = None
    transportation_method: TransportationMethod = None
    """
    This attribute represents the specific transportation method by which the passenger is traveling. It captures the mode of transportation used during the Rail product journey, Possible values are:
        - `BUS` - The Rail product includes bus transportation for certain segments of the itinerary.
        - `FERRY` - The Rail product involves ferry transportation as part of the journey.
        - `PUBLIC_TRANSPORT` - The Rail product represents the use of public transportation modes for the journey.
        - `TRAM` - The Rail product includes tram transportation as part of the journey.
        - `RAIL` - The Rail product specifically utilizes train transportation for the journey.
        - `TRANSFER` - The Rail product involves transfers between different modes of transportation.
        - `OTHER` - The Rail product utilizes transportation methods not covered by the aforementioned categories.

    """
    operating_company: Optional[OperatingCompany] = None
    """
    This attribute captures the name or identifier of the company responsible for operating the Rail product. It represents the specific operating entity, such as Amtrak, British Railways, or a bus company.
    """


class Air(
    TravelProductGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Air"""

    departure_time: datetime = None
    """
    Local date and time of departure from original departure location, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    arrival_time: datetime = None
    """
    Local date and time of arrival to final destination location, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    air_segments: list[AirSegment] = Field(..., maxItems=30, minItems=1)
    """
    Additional airline and flight details for each of the trip segments.
    """
    flight_type: Optional[FlightType] = None
    """
    Identifies the type of air trip based on the air destinations.
    """
    passenger_name_record: Optional[constr(max_length=100)] = None
    """
    Airline booking confirmation code for the trip.
    """
    global_distribution_system_type: Optional[constr(max_length=100)] = None
    """
    Associated with Passenger Name Record (PNR).
    """
    type: Literal["AIR"] = "AIR"


class Cruise(
    TravelProductGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Cruise"""

    departure_time: datetime = None
    """
    Local date and time of departure from original departure location, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    arrival_time: datetime = None
    """
    Local date and time of arrival from original arrival location, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    embarkation_port: constr(max_length=200) = None
    """
    Location from where cruise will depart.
    """
    disembarkation_port: constr(max_length=200) = None
    """
    The cruise's final destination.
    """
    ship_name: constr(max_length=200) = None
    """
    Name of the cruise ship.
    """
    type: Literal["CRUISE"] = "CRUISE"


class Car(
    TravelProductGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Car"""

    pick_up_location: constr(max_length=200) = None
    """
    Location where the automobile will be picked up.
    """
    drop_off_location: constr(max_length=200) = None
    """
    Location at which the automobile will be returned.
    """
    pickup_time: datetime = None
    """
    Local date and time the automobile will be picked-up, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    return_time: datetime = None
    """
    Local date and time the automobile will be returned, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    type: Literal["CAR"] = "CAR"


class Hotel(
    TravelProductGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Hotel"""

    hotel_id: constr(max_length=200) = Field(..., example="8883333999221")
    """
    Unique hotel identifier assigned by the partner.
    """
    price_withheld: Optional[bool] = None
    """
    Identifies if the product price was withheld from the customer during the booking process.
    """
    hotel_name: constr(max_length=200) = Field(..., example="Hotel Expedia")
    """
    Name of the hotel.
    """
    room_count: Optional[int] = None
    """
    Total number of rooms booked within the hotel product collection.
    """
    address: HotelAddress = None
    checkin_time: datetime = None
    """
    Local date and time of the hotel check-in, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    checkout_time: datetime = None
    """
    Local date and time of the hotel check-out, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    type: Literal["HOTEL"] = "HOTEL"


class PaymentOutcome(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model PaymentOutcome"""

    status: Optional[PaymentStatus] = None
    code: Optional[constr(max_length=200)] = None
    """
    A mnemonic code for the payment processing.
    """
    description: Optional[constr(max_length=200)] = None
    """
    A short description providing additional explanation regarding the mnemonic code.
    """


class Insurance(
    TravelProductGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Insurance"""

    type: Literal["INSURANCE"] = "INSURANCE"


class Telephone(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Telephone: Group of attributes intended to hold information about phone number associated with the transaction.  A user can have one to many phone numbers (home, work, mobile, etc.)."""

    type: Optional[TelephoneType] = None
    platform_type: Optional[TelephonePlatformType] = None
    country_access_code: constr(regex=r"^[0-9]{1,3}$", max_length=3) = Field(..., example="1")
    """
    Numeric digit between 1 to 3 characters used to represent the country code for international dialing.  Does not include symbols, spaces, or leading zeros.
    """
    area_code: constr(regex=r"^[0-9]{1,20}$", max_length=20) = Field(..., example="1")
    """
    A number prefixed to an individual telephone number: used in making long-distance calls.  Does not include symbols, spaces, or leading zeros.
    """
    phone_number: constr(regex=r"^[0-9]{1,50}$", max_length=50) = Field(..., example="1234567")
    """
    A number that is dialed on a telephone, without the country or area codes, to reach a particular person, business, etc.  Does not include symbols, spaces, or leading zeros.
    """
    extension_number: Optional[constr(regex=r"^[0-9]{1,20}$", max_length=20)] = Field(None, example="89")
    """
    The number used to reach an individual once a phone connection is established.  Does not include symbols, spaces, or leading zeros.
    """
    preference_rank: Optional[float] = None
    """
    Ranking of order of user preference for contact via text (if type is Mobile) or voice.  `0` means no preference.  `1` is the primary phone, `2` is the secondary phone, etc.
    """
    last_verified_date_time: Optional[datetime] = None
    """
    Local date and time user validated possession of their phone number via a text or voice multi factor authentication challenge, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    verified_flag: Optional[bool] = None
    """
    Flag indicating whether user passed validation of possession of their phone number via a text or voice multi factor authentication challenge.
    """


class MultiFactorAuthenticationAttempt(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model MultiFactorAuthenticationAttempt: Information specific to the update event by a user."""

    delivery_method: DeliveryMethod = None
    """
    The delivery method of the Multi-Factor Authentication to a user.
    """
    status: Status1 = None
    """
    The status of a user''s response to the Multi-Factor Authentication initiated by the Partner''s system to the user.'
    - `SUCCESS` - Applicable if the user successfully passed the challenge.
    - `ABANDON` - Applicable if the user did not complete the challenge.
    - `FAILED` - Applicable if the user failed the challenge.

    """
    reference_id: constr(max_length=200) = None
    """
    The identifier related to a Multi-Factor Authentication attempt by the Partner's system to the Multi-Factor Authentication provider.
    """
    provider_name: constr(max_length=200) = None
    """
    The vendor providing the Multi-Factor Authentication verification.
    """
    attempt_count: float = None
    """
    The number of attempts a user tried for this Multi-Factor Authentication.
    """
    update_start_date_time: Optional[datetime] = None
    """
    The local date and time the Multi-Factor Authentication was initiated to a user from the Partner's system, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    update_end_date_time: Optional[datetime] = None
    """
    The local date and time the Multi-Factor Authentication to a user ended in the Partner's system, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    telephone: Optional[Telephone] = None
    email_address: Optional[EmailStr] = None
    """
    Email address used for the Multi-Factor Authentication by a user.
    """


class RemediationUpdate(
    AccountUpdateRequestGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model RemediationUpdate: Information specific to remediation actions initiated by the Partner's system to a user as a result of a fraud recommendation."""

    remediation_update_actions: list[RemediationUpdateAction] = Field(..., maxItems=20, minItems=1)
    type: Literal["REMEDIATION_UPDATE"] = "REMEDIATION_UPDATE"
    """
    The categorized type of account update event from the Partner's system.
    """


class AccountScreenResponse(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountScreenResponse: Response for an account transaction provided by Expedia's Fraud Prevention Service."""

    risk_id: Optional[constr(max_length=200)] = Field(None, example="1234567")
    """
    Unique identifier assigned to the transaction by Expedia's Fraud Prevention Service.
    """
    decision: Optional[AccountTakeoverFraudDecision] = None


class AccountTakeoverCustomerAccount(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountTakeoverCustomerAccount: Information about a user's account."""

    user_id: constr(max_length=200) = None
    """
    Unique account identifier provided by the Partner's Identity Provider/System assigned to the account owner by the partner. `user_id` is specific to the Partner's namespace. Used to track repeat account activity by the same user.
    """
    account_type: AccountType1 = None
    """
    Identifies the account type of a user''s account. Possible values are:
    - `INDIVIDUAL` - Applicable if this account is for an individual traveler.
    - `BUSINESS` - Applicable if this account is for a business or organization account used by suppliers or Partners.

    """
    account_role: Optional[AccountRole] = None
    """
    Identifies the account role and associated permissions of a user''s account. Possible values are:
    - `USER`: Basic account with no special privileges.
    - `MANAGER`: Account with additional privileges, such as the ability to make bookings for others.
    - `ADMIN`: Account with higher privileges than a manager, including the ability to grant manager access to other users.

    """
    name: Optional[AccountTakeoverName] = None
    username: constr(max_length=200) = None
    """
    Username of the account.
    """
    email_address: EmailStr = None
    """
    Email address for the account owner.
    """
    telephones: Optional[list[Telephone]] = Field(None, maxItems=20)
    address: Optional[Address] = None
    registered_time: datetime = None
    """
    The local date and time that the customer first registered on the Partner's site, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    active_flag: bool = None
    """
    Indicator for if this account is an active account or not.
    """
    loyalty_member_id: Optional[constr(max_length=200)] = None
    """
    Unique loyalty identifier for a user.
    """


class CurrentUserSession(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model CurrentUserSession: The current user session prior to this transaction, which contains details related to any challenge initiated by the Partner''s system to a user before calling Expedia''s Fraud Prevention Service.
    An example is if the Partner''s system sent a Captcha challenge to the user before calling Expedia''s Fraud Prevention Service.

    """

    session_id: Optional[constr(max_length=200)] = None
    """
    Unique identifier for a user's session on their device
    """
    start_date_time: Optional[datetime] = None
    """
    The local date and time a user's session started, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    challenge_detail: Optional[ChallengeDetail] = None


class ChargebackFeedback(
    OrderPurchaseUpdateRequestGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model ChargebackFeedback: Feedback from EG external partners if they receive a chargeback for a false negative recommendation from Fraud Prevention system."""

    chargeback_detail: Optional[ChargebackDetail] = None
    type: Literal["CHARGEBACK_FEEDBACK"] = "CHARGEBACK_FEEDBACK"


class IssuedRefundUpdate(
    RefundUpdateGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model IssuedRefundUpdate: Data related to the issued refund that should be updated."""

    refund_details: Optional[IssuedRefundUpdateDetails] = None
    refund_status: Literal["ISSUED"] = "ISSUED"
    """
    Identifies the refund status. Possible values are:
    -`ISSUED` - The refund was issued.
    -`SETTLED` - The refund was settled.

    """


class SettledRefundUpdate(
    RefundUpdateGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model SettledRefundUpdate: Data related to the settled refund that should be updated."""

    refund_details: Optional[SettledRefundUpdateDetails] = None
    refund_status: Literal["SETTLED"] = "SETTLED"
    """
    Identifies the refund status. Possible values are:
    -`ISSUED` - The refund was issued.
    -`SETTLED` - The refund was settled.

    """


class CustomerAccount(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model CustomerAccount"""

    user_id: Optional[str] = None
    """
    Unique account identifier provided by the partner's Identity Provider/System assigned to the account owner by the partner. `user_id` is specific to the partner namespace. Used to track repeat purchases by the same user.
    """
    account_type: AccountType = Field(..., example="STANDARD")
    """
    Identifies if the customer account is known to the client. Possible values are:

    -`GUEST` - Applicable if the partner maintains record to distinguish whether the transaction was booked via a guest account.

    -`STANDARD` - Default account type.

    """
    name: Name = None
    email_address: EmailStr = None
    """
    Email address for the account owner.
    """
    telephones: Optional[list[Telephone]] = None
    address: Optional[Address] = None
    registered_time: Optional[datetime] = None
    """
    The local date and time that the customer first registered on the client site, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """


class Traveler(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Traveler"""

    traveler_name: Name = None
    email_address: Optional[EmailStr] = None
    """
    Email address associated with the traveler as supplied by the partner system.
    """
    telephones: Optional[list[Telephone]] = Field(None, maxItems=250, minItems=1)
    primary: bool = None
    """
    Indicator for one of the travelers who is the primary traveler. One traveler in each itinerary item must be listed as primary. By default, for a single traveler this should be set to `true`.
    """
    age: Optional[float] = None
    """
    Age of the traveler.
    """
    birth_date: Optional[datetime] = None
    """
    Date of birth for traveler, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    citizenship_country_code: Optional[constr(regex=r"^[A-Z]{3}$", min_length=3, max_length=3)] = None
    """
    The alpha-3 ISO country code of the traveler's nationality.
    """
    traveler_id: Optional[constr(max_length=100)] = None
    """
    A unique identifier for travelers in the transaction.
    """


class Rail(
    TravelProductGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Rail"""

    route_type: RouteType = None
    """
    The type of route or itinerary for the Rail product, indicating the travel arrangement and pattern. Possible values are:
    - `MULTIPLE_DESTINATIONS` - The Rail product includes multiple destinations in its itinerary.
    - `ONE_WAY` - The Rail product represents a one-way journey.
    - `ROUNDTRIP` - The Rail product represents a roundtrip journey.

    """
    rail_segments: list[RailSegments] = Field(..., maxItems=20, minItems=1)
    type: Literal["RAIL"] = "RAIL"


class PaymentOperation(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model PaymentOperation"""

    id: Optional[constr(max_length=200)] = None
    amount: Optional[Amount] = None
    outcome: Optional[PaymentOutcome] = None


class MultiFactorAuthenticationUpdate(
    AccountUpdateRequestGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model MultiFactorAuthenticationUpdate: Information specific to a user's response to a Multi-Factor Authentication initiated by the Partner's system as a result of a fraud recommendation."""

    multi_factor_authentication_attempts: list[MultiFactorAuthenticationAttempt] = Field(..., maxItems=20, minItems=1)
    type: Literal["MULTI_FACTOR_AUTHENTICATION_UPDATE"] = "MULTI_FACTOR_AUTHENTICATION_UPDATE"
    """
    The categorized type of account update event from the Partner's system.
    """


class AccountTakeoverTransactionDetailsGeneric(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountTakeoverTransactionDetails: The `transaction_type` field value is used as a discriminator, with the following mapping:
    * `LOGIN`: `LoginTransactionDetails`

    """

    type: Type3 = None
    """
    The categorized type of account event related to a user's action.
    """
    transaction_date_time: datetime = None
    """
    The local date and time the transaction occured in the Partner's system, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    transaction_id: constr(max_length=200) = None
    """
    Unique identifier to identify a transaction attempt in the Partner's system.
    """
    current_user_session: Optional[CurrentUserSession] = None


class LoginTransactionDetails(
    AccountTakeoverTransactionDetailsGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model LoginTransactionDetails"""

    authentication_type: AuthenticationType = None
    """
    The type of login authentication method used by a user.
    For `authentication_type` ensure attributes mentioned in dictionary below are set to corresponding values only.
    `authentication_type` is an enum value with the following mapping with `authentication_sub_type` attribute:
    *       authentication_type       :     authentication_sub_type
    * -------------------------------------------------------------------------------
    * `CREDENTIALS`                         : `EMAIL`
    * `CREDENTIALS`                         :
    * `PASSWORD_RESET`                      : `EMAIL`
    * `SINGLE_SIGN_ON`                      : `EMAIL`
    * `MULTI_FACTOR_AUTHENTICATION`         : `EMAIL`
    * `MULTI_FACTOR_AUTHENTICATION`         : `PHONE`
    * `SOCIAL`                              : `GOOGLE`
    * `SOCIAL`                              : `FACEBOOK`
    * `SOCIAL`                              : `APPLE`

    """
    authentication_sub_type: Optional[AuthenticationSubType] = None
    """
    The sub type of login authentication method used by a user.
    For `authentication_sub_type` ensure attributes mentioned in dictionary below are set to corresponding values only.
    `authentication_sub_type` is an enum value with the following mapping with `authentication_type` attribute:
    *       authentication_sub_type   :     authentication_type
    * -------------------------------------------------------------------------------
    * `EMAIL`                               : `CREDENTIALS`
    * `EMAIL`                               : `PASSWORD_RESET`
    * `EMAIL`                               : `SINGLE_SIGN_ON`
    * `EMAIL`                               : `MULTI_FACTOR_AUTHENTICATION`
    * `PHONE`                               : `MULTI_FACTOR_AUTHENTICATION`
    * `GOOGLE`                              : `SOCIAL`
    * `FACEBOOK`                            : `SOCIAL`
    * `APPLE`                               : `SOCIAL`
    *                                       : `CREDENTIALS`

    """
    successful_login_flag: bool = None
    """
    Identifies if a login attempt by a user was successful or not.
    """
    failed_login_reason: Optional[FailedLoginReason] = None
    """
    The reason for the failed login attempt in the Partner''s system, related to user failure or Partner''s system failure.
    - `INVALID_CREDENTIALS` - Applicable if the user provided invalid login credentials for this login attempt.
    - `ACCOUNT_NOT_FOUND` - Applicable if the user attempted to login to an account that doesn't exist.
    - `VERIFICATION_FAILED` - Applicable if the user failed the verification for this login, or any authentication exception occured in the Partner system for this login attempt.
    - `ACCOUNT_LOCKED` - Applicable if the user attempted to login to an account that is locked.

    """
    type: Literal["LOGIN"] = "LOGIN"
    """
    The categorized type of account event related to a user's action.
    """


class Verify(
    PaymentOperation,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Verify: A verify operation represents the intent to verify the payment associated with this transaction."""

    type: Optional[VerificationType] = None


class Authorize(
    PaymentOperation,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Authorize: Authorize operation on the payment. An authorize operation represents placing the funds on hold with the specified form of payment."""

    pass


class AuthorizeReversal(
    PaymentOperation,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AuthorizeReversal: Authorize Reversal operation on the payment. An authorize reversal operation represents a notification received usually from a 3rd party payment processor to indicate that an authorization hold should be released as a result of a sale being partially or completely cancelled."""

    pass


class Capture(
    PaymentOperation,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Capture: Capture operation on the payment. A capture operation represents a notification received usually from a 3rd party payment processor to indicate that the funds placed on hold will be captured and the funds transfer process will occur from the customer's funds to the merchant's funds."""

    pass


class Refund(
    PaymentOperation,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Refund: Refund operation on the payment. A refund operation represents the intent to refund a previous charge."""

    pass


class AccountTransaction(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountTransaction: Information for an account transaction."""

    site_info: AccountTakeoverSiteInfo = None
    device_details: AccountTakeoverDeviceDetails = None
    customer_account: AccountTakeoverCustomerAccount = None
    transaction_details: AccountTakeoverTransactionDetails = None


class Operations(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Operations: All operations related to a payment throughout its lifespan. An operation represents an event external to Fraud Prevention Service that specifies to perform a payment operation. Possible operation types include:

    - `Verify`

    - `Authorize`

    - `AuthorizeReversal`

    - `Capture`

    - `Refund`

    """

    verify: Optional[Verify] = None
    authorize: Optional[Authorize] = None
    authorize_reversal: Optional[AuthorizeReversal] = None
    capture: Optional[Capture] = None
    refunds: Optional[list[Refund]] = Field(None, maxItems=20)


class AccountScreenRequest(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model AccountScreenRequest: Information for account screening by Expedia's Fraud Prevention Service."""

    transaction: AccountTransaction = None


class PaymentGeneric(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Payment: The `method` field value is used as a discriminator, with the following mapping:
    * `CREDIT_CARD`: `CreditCard`
    * `PAYPAL`: `PayPal`
    * `POINTS`: `Points`
    * `GIFT_CARD`: `GiftCard`
    * `INTERNET_BANK_PAYMENT`: `InternetBankPayment`
    * `DIRECT_DEBIT`: `DirectDebit`

    """

    brand: Brand = None
    """
    The `brand` field value is the payment brand used for payment on this transaction.
    For credit card payment method ensure attributes mentioned in dictionary below are set to corresponding values only.
    Ensure to comply with the naming standards provided in below dictionary. For example, some Payment processors use “Japan Credit Bureau” but “JCB” should be used when calling Fraud API.
    Incorrect `brand` - `card_type` combination will result in data quality issues and result in degraded risk recommendation.
    'brand' is an enum value with the following mapping with CreditCard 'card_type' attribute:
    *       brand                 :      card_type
    * -------------------------------------------------------
    * `AMERICAN_EXPRESS`          : `AMERICAN_EXPRESS`
    * `DINERS_CLUB_INTERNATIONAL` : `DINERS_CLUB`
    * `BC_CARD`                   : `DINERS_CLUB`
    * `DISCOVER`                  : `DISCOVER`
    * `BC_CARD`                   : `DISCOVER`
    * `DINERS_CLUB_INTERNATIONAL` : `DISCOVER`
    * `JCB`                       : `DISCOVER`
    * `JCB`                       : `JCB`
    * `MASTER_CARD`               : `MASTER_CARD`
    * `MAESTRO`                   : `MASTER_CARD`
    * `POSTEPAY_MASTERCARD`       : `MASTER_CARD`
    * `SOLO`                      : `SOLO`
    * `SWITCH`                    : `SWITCH`
    * `MAESTRO`                   : `MAESTRO`
    * `CHINA_UNION_PAY`           : `CHINA_UNION_PAY`
    * `VISA`                      : `VISA`
    * `VISA_DELTA`                : `VISA`
    * `VISA_ELECTRON`             : `VISA`
    * `CARTA_SI`                  : `VISA`
    * `CARTE_BLEUE`               : `VISA`
    * `VISA_DANKORT`              : `VISA`
    * `POSTEPAY_VISA_ELECTRON`    : `VISA`
    * `PAYPAL`                    :

    'brand' with 'Points' payment_type is an enum value with following:
    * `EXPEDIA_REWARDS`
    * `AMEX_POINTS`
    * `BANK_OF_AMERICA_REWARDS`
    * `DISCOVER_POINTS`
    * `MASTER_CARD_POINTS`
    * `CITI_THANK_YOU_POINTS`
    * `MERRILL_LYNCH_REWARDS`
    * `WELLS_FARGO_POINTS`
    * `DELTA_SKY_MILES`
    * `UNITED_POINTS`
    * `DISCOVER_MILES`
    * `ALASKA_MILES`
    * `RBC_REWARDS`
    * `BILT_REWARDS`
    * `ORBUCKS`
    * `CHEAP_CASH`
    * `BONUS_PLUS`
    * `ULTIMATE_REWARDS`
    * `UATP`
    * `UATP_SUPPLY`
    * `AIR_PLUS`
    * `US_PASS_PLUS`

    'brand' with 'GiftCard' payment_type is an enum value with following:
    * `GIFT_CARD`

    'brand' with 'InternetBankPayment' payment_type is an enum value with following:
    * `IBP`
    * `LOCAL_DEBIT_CARD`
    * `SOFORT`
    * `YANDEX`
    * `WEB_MONEY`
    * `QIWI`
    * `BITCOIN`

    'brand' with 'DirectDebit' payment_type is an enum value with following:
    * `ELV`
    * `INTER_COMPANY`

    """
    method: PaymentMethod = None
    reason: Optional[PaymentReason] = None
    billing_name: Name = None
    billing_address: Address = None
    billing_email_address: EmailStr = None
    """
    Email address associated with the payment.
    """
    authorized_amount: Optional[Amount] = None
    verified_amount: Optional[Amount] = None
    three_digits_secure_criteria: Optional[PaymentThreeDSCriteria] = None
    operations: Optional[Operations] = None


class CreditCard(
    PaymentGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model CreditCard"""

    def dict(self, **kwargs):
        omitted_fields = ["card_number", "card_cvv_response", "card_avs_response"]

        dictionary = super().dict(**kwargs)
        dictionary.update([(attribute, "<-- omitted -->") for attribute in omitted_fields])

        return dictionary

    card_type: CardType = None
    """
    The 'card_type' field value is an enum value which is associated with the payment method of the specific payment instrument.
    For credit card payment method ensure attributes mentioned in dictionary below are set to corresponding values only.
    Ensure to comply with the naming standards provided in below dictionary. For example, some Payment processors use “Japan Credit Bureau” but “JCB” should be used when calling Fraud API.
    Incorrect `card_type` - `brand` combination will result in data quality issues and result in degraded risk recommendation.
    'card_type' is an enum value with the following mapping with Payment `brand` attribute:
    *       card_type            :          brand
    * --------------------------------------------------------
    * `AMERICAN_EXPRESS`         : `AMERICAN_EXPRESS`
    * `DINERS_CLUB`              : `DINERS_CLUB_INTERNATIONAL`
    * `DINERS_CLUB`              : `BC_CARD`
    * `DISCOVER`                 : `DISCOVER`
    * `DISCOVER`                 : `BC_CARD`
    * `DISCOVER`                 : `DINERS_CLUB_INTERNATIONAL`
    * `DISCOVER`                 : `JCB`
    * `JCB`                      : `JCB`
    * `MASTER_CARD`              : `MASTER_CARD`
    * `MASTER_CARD`              : `MAESTRO`
    * `MASTER_CARD`              : `POSTEPAY_MASTERCARD`
    * `SOLO`                     : `SOLO`
    * `SWITCH`                   : `SWITCH`
    * `MAESTRO`                  : `MAESTRO`
    * `CHINA_UNION_PAY`          : `CHINA_UNION_PAY`
    * `VISA`                     : `VISA`
    * `VISA`                     : `VISA_DELTA`
    * `VISA`                     : `VISA_ELECTRON`
    * `VISA`                     : `CARTA_SI`
    * `VISA`                     : `CARTE_BLEUE`
    * `VISA`                     : `VISA_DANKORT`
    * `VISA`                     : `POSTEPAY_VISA_ELECTRON`

    """
    card_number: constr(max_length=200) = None
    """
    All the digits (unencrypted) of the credit card number associated with the payment.
    """
    expiry_date: datetime = None
    """
    Expiration date of the credit card used for payment, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    electronic_commerce_indicator: Optional[constr(max_length=200)] = None
    """
    Electronic Commerce Indicator, a two or three digit number usually returned by a 3rd party payment processor in regards to the authentication used when gathering the cardholder's payment credentials.
    """
    virtual_credit_card_flag: Optional[bool] = None
    """
    A flag to indicate that the bank card being used for the charge is a virtual credit card.
    """
    wallet_type: Optional[constr(max_length=200)] = None
    """
    If a virtual/digital form of payment was used, the type of digital wallet should be specified here. Possible `wallet_type`'s include: `Google` or `ApplePay`.
    """
    card_avs_response: Optional[constr(max_length=50)] = None
    """
    A field used to confirm if the address provided at the time of purchase matches what the bank has on file for the Credit Card.
    """
    card_cvv_response: Optional[constr(max_length=20)] = None
    """
    A field used to confirm the Card Verification Value on the Credit Card matches the Credit Card used at the time of purchase.
    """
    telephones: list[Telephone] = Field(..., maxItems=20, minItems=1)
    """
    Telephone(s) associated with card holder and credit card.
    """
    merchant_order_code: Optional[constr(max_length=200)] = None
    """
    Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.
    """
    card_authentication_failure_count: Optional[int] = None
    """
    Total authentication failure count for given card.
    """
    method: Literal["CREDIT_CARD"] = "CREDIT_CARD"


class PayPal(
    PaymentGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model PayPal"""

    payer_id: constr(max_length=200) = None
    """
    Unique PayPal Customer Account identification number.
    """
    transaction_id: constr(max_length=200) = None
    """
    Unique transaction number to identify Auth calls at PayPal.
    """
    merchant_order_code: Optional[constr(max_length=200)] = None
    """
    Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.
    """
    method: Literal["PAYPAL"] = "PAYPAL"


class Points(
    PaymentGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model Points"""

    account_id: constr(max_length=200) = None
    """
    Points account id.
    """
    method: Literal["POINTS"] = "POINTS"


class GiftCard(
    PaymentGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model GiftCard"""

    def dict(self, **kwargs):
        omitted_fields = ["pin"]

        dictionary = super().dict(**kwargs)
        dictionary.update([(attribute, "<-- omitted -->") for attribute in omitted_fields])

        return dictionary

    card_number: constr(regex=r"^[0-9A-Za-z]{4,16}$", max_length=16) = Field(..., example="123456ABCDabcd")
    """
    Gift card number.
    """
    card_holder_name: constr(max_length=200) = None
    """
    The name of gift card holder.
    """
    pin: constr(regex=r"^[0-9]{4,8}$", max_length=8) = Field(..., example="123456")
    """
    The PIN of gift card.
    """
    method: Literal["GIFT_CARD"] = "GIFT_CARD"


class InternetBankPayment(
    PaymentGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model InternetBankPayment"""

    bank_id: constr(max_length=15) = None
    """
    The bank_id provided by the internet bank payment(IBP) provider (DRWP aka NetGiro) for the bank used for processing the payment.
    """
    bank_branch_code: constr(max_length=15) = None
    """
    A code that identifies the bank branch for internet bank payment(IBP).
    """
    telephones: list[Telephone] = Field(..., maxItems=20, minItems=1)
    """
    Telephone(s) associated with internet bank payment(IBP) provider.
    """
    method: Literal["INTERNET_BANK_PAYMENT"] = "INTERNET_BANK_PAYMENT"


class DirectDebit(
    PaymentGeneric,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model DirectDebit"""

    def dict(self, **kwargs):
        omitted_fields = ["account_number"]

        dictionary = super().dict(**kwargs)
        dictionary.update([(attribute, "<-- omitted -->") for attribute in omitted_fields])

        return dictionary

    routing_number: constr(max_length=15) = Field(..., example="100000000")
    """
    A code that identifies the financial institution for a specific bank account.
    """
    account_number: constr(max_length=100) = None
    """
    Cleartext (unencrypted) DirectDebit bank account number associated with the payment instrument.
    """
    telephones: list[Telephone] = Field(..., maxItems=20, minItems=1)
    """
    Telephone(s) associated with direct debit payment provider.
    """
    method: Literal["DIRECT_DEBIT"] = "DIRECT_DEBIT"


class TransactionDetails(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model TransactionDetails"""

    order_id: constr(max_length=50) = Field(..., example="1000000234")
    """
    Unique identifier assigned to the order by the partner. `order_id` is specific to the partner namespace.
    """
    current_order_status: CurrentOrderStatus = None
    """
    Status of the order:
    * `IN_PROGRESS` is used when order has not processed fully. For example, inventory has not yet been reserved, or payment has not yet been settled.
    * `COMPLETED` is used when an order has been processed fully. For example, inventory has been reserved, and the payment has been settled.

    """
    order_type: OrderType = Field(..., example="CREATE")
    """
    Type of order. Possible `order_types`.

    `CREATE` - Initial type of a brand new order.

    `CHANGE` - If a `OrderPurchaseScreenRequest` has already been submitted for the initial booking with `order_type = CREATE`, but has now been modified and partner wishes to resubmit for Fraud screening then the `order_type = CHANGE`. Examples of changes that are supported are changes made to `check-in/checkout dates` or `price of a TravelProduct`.

    """
    travel_products: list[TravelProduct] = Field(..., maxItems=20, minItems=1)
    travelers: list[Traveler] = Field(..., maxItems=30, minItems=1)
    """
    Individuals who are part of the travel party for the order. At minimum there must be at least `1` traveler.
    """
    payments: Optional[list[Payment]] = Field(None, maxItems=30, minItems=1)
    """
    List of the form(s) of payment being used to purchase the order.  One or more forms of payment can be used within an order. Information gathered will be specific to the form of payment.
    """


class OrderPurchaseTransaction(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model OrderPurchaseTransaction"""

    site_info: SiteInfo = None
    device_details: DeviceDetails = None
    customer_account: CustomerAccount = None
    transaction_details: TransactionDetails = None


class OrderPurchaseScreenRequest(
    BaseModel,
    smart_union=True,
    extra=Extra.forbid,
):
    r"""pydantic model OrderPurchaseScreenRequest"""

    transaction: OrderPurchaseTransaction = None


RefundUpdate = Union[IssuedRefundUpdate, SettledRefundUpdate, RefundUpdateGeneric]

OrderPurchaseUpdateRequest = Union[OrderUpdate, ChargebackFeedback, InsultFeedback, RefundUpdate, PaymentUpdate, OrderPurchaseUpdateRequestGeneric]

TravelProduct = Union[Rail, Air, Cruise, Car, Hotel, Insurance, TravelProductGeneric]

Payment = Union[CreditCard, PayPal, Points, GiftCard, InternetBankPayment, DirectDebit, PaymentGeneric]

AccountUpdateRequest = Union[MultiFactorAuthenticationUpdate, RemediationUpdate, AccountUpdateRequestGeneric]

AccountTakeoverTransactionDetails = Union[LoginTransactionDetails, AccountTakeoverTransactionDetailsGeneric]


Error.update_forward_refs()


UnauthorizedError.update_forward_refs()


OrderPurchaseUpdateNotFoundError.update_forward_refs()


RetryableOrderPurchaseScreenFailure.update_forward_refs()


RetryableOrderPurchaseUpdateFailure.update_forward_refs()


Cause.update_forward_refs()


BadRequestError.update_forward_refs()


CancellationReason.update_forward_refs()


InsultDetail.update_forward_refs()


OrderPurchaseUpdateResponse.update_forward_refs()


SiteInfo.update_forward_refs()


DeviceDetails.update_forward_refs()


Address.update_forward_refs()


TravelersReference.update_forward_refs()


OperatingCompany.update_forward_refs()


RailwayStationDetails.update_forward_refs()


AirSegment.update_forward_refs()


HotelAddress.update_forward_refs()


PaymentThreeDSCriteria.update_forward_refs()


Name.update_forward_refs()


Email.update_forward_refs()


Amount.update_forward_refs()


AccountTakeoverError.update_forward_refs()


AccountTakeoverUnauthorizedError.update_forward_refs()


AccountUpdateNotFoundError.update_forward_refs()


ServiceUnavailableError.update_forward_refs()


Cause1.update_forward_refs()


AccountTakeoverBadRequestError.update_forward_refs()


RemediationUpdateAction.update_forward_refs()


AccountUpdateResponse.update_forward_refs()


AccountTakeoverSiteInfo.update_forward_refs()


AccountTakeoverDeviceDetails.update_forward_refs()


AccountTakeoverName.update_forward_refs()


ChallengeDetail.update_forward_refs()


ForbiddenError.update_forward_refs()


NotFoundError.update_forward_refs()


TooManyRequestsError.update_forward_refs()


InternalServerError.update_forward_refs()


BadGatewayError.update_forward_refs()


GatewayTimeoutError.update_forward_refs()


OrderUpdate.update_forward_refs()


InsultFeedback.update_forward_refs()


IssuedRefundUpdateDetails.update_forward_refs()


SettledRefundUpdateDetails.update_forward_refs()


PaymentUpdate.update_forward_refs()


ChargebackDetail.update_forward_refs()


OrderPurchaseScreenResponse.update_forward_refs()


RailSegments.update_forward_refs()


Air.update_forward_refs()


Cruise.update_forward_refs()


Car.update_forward_refs()


Hotel.update_forward_refs()


PaymentOutcome.update_forward_refs()


Insurance.update_forward_refs()


Telephone.update_forward_refs()


MultiFactorAuthenticationAttempt.update_forward_refs()


RemediationUpdate.update_forward_refs()


AccountScreenResponse.update_forward_refs()


AccountTakeoverCustomerAccount.update_forward_refs()


CurrentUserSession.update_forward_refs()


ChargebackFeedback.update_forward_refs()


IssuedRefundUpdate.update_forward_refs()


SettledRefundUpdate.update_forward_refs()


CustomerAccount.update_forward_refs()


Traveler.update_forward_refs()


Rail.update_forward_refs()


PaymentOperation.update_forward_refs()


MultiFactorAuthenticationUpdate.update_forward_refs()


LoginTransactionDetails.update_forward_refs()


Verify.update_forward_refs()


Authorize.update_forward_refs()


AuthorizeReversal.update_forward_refs()


Capture.update_forward_refs()


Refund.update_forward_refs()


AccountTransaction.update_forward_refs()


Operations.update_forward_refs()


AccountScreenRequest.update_forward_refs()


CreditCard.update_forward_refs()


PayPal.update_forward_refs()


Points.update_forward_refs()


GiftCard.update_forward_refs()


InternetBankPayment.update_forward_refs()


DirectDebit.update_forward_refs()


TransactionDetails.update_forward_refs()


OrderPurchaseTransaction.update_forward_refs()


OrderPurchaseScreenRequest.update_forward_refs()


class ExpediaGroupForbiddenErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a ForbiddenError object."""
    pass


class ExpediaGroupNotFoundErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a NotFoundError object."""
    pass


class ExpediaGroupTooManyRequestsErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a TooManyRequestsError object."""
    pass


class ExpediaGroupBadRequestErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a BadRequestError object."""
    pass


class ExpediaGroupRetryableOrderPurchaseUpdateFailureException(ExpediaGroupApiException):
    r"""Exception wrapping a RetryableOrderPurchaseUpdateFailure object."""
    pass


class ExpediaGroupBadGatewayErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a BadGatewayError object."""
    pass


class ExpediaGroupServiceUnavailableErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a ServiceUnavailableError object."""
    pass


class ExpediaGroupAccountUpdateNotFoundErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a AccountUpdateNotFoundError object."""
    pass


class ExpediaGroupAccountTakeoverUnauthorizedErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a AccountTakeoverUnauthorizedError object."""
    pass


class ExpediaGroupRetryableOrderPurchaseScreenFailureException(ExpediaGroupApiException):
    r"""Exception wrapping a RetryableOrderPurchaseScreenFailure object."""
    pass


class ExpediaGroupUnauthorizedErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a UnauthorizedError object."""
    pass


class ExpediaGroupInternalServerErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a InternalServerError object."""
    pass


class ExpediaGroupAccountTakeoverBadRequestErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a AccountTakeoverBadRequestError object."""
    pass


class ExpediaGroupOrderPurchaseUpdateNotFoundErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a OrderPurchaseUpdateNotFoundError object."""
    pass


class ExpediaGroupGatewayTimeoutErrorException(ExpediaGroupApiException):
    r"""Exception wrapping a GatewayTimeoutError object."""
    pass


@dataclass
class ForbiddenErrorDeserializationContract:
    exception: type = ExpediaGroupForbiddenErrorException
    model: type = ForbiddenError


@dataclass
class NotFoundErrorDeserializationContract:
    exception: type = ExpediaGroupNotFoundErrorException
    model: type = NotFoundError


@dataclass
class TooManyRequestsErrorDeserializationContract:
    exception: type = ExpediaGroupTooManyRequestsErrorException
    model: type = TooManyRequestsError


@dataclass
class BadRequestErrorDeserializationContract:
    exception: type = ExpediaGroupBadRequestErrorException
    model: type = BadRequestError


@dataclass
class RetryableOrderPurchaseUpdateFailureDeserializationContract:
    exception: type = ExpediaGroupRetryableOrderPurchaseUpdateFailureException
    model: type = RetryableOrderPurchaseUpdateFailure


@dataclass
class BadGatewayErrorDeserializationContract:
    exception: type = ExpediaGroupBadGatewayErrorException
    model: type = BadGatewayError


@dataclass
class ServiceUnavailableErrorDeserializationContract:
    exception: type = ExpediaGroupServiceUnavailableErrorException
    model: type = ServiceUnavailableError


@dataclass
class AccountUpdateNotFoundErrorDeserializationContract:
    exception: type = ExpediaGroupAccountUpdateNotFoundErrorException
    model: type = AccountUpdateNotFoundError


@dataclass
class AccountTakeoverUnauthorizedErrorDeserializationContract:
    exception: type = ExpediaGroupAccountTakeoverUnauthorizedErrorException
    model: type = AccountTakeoverUnauthorizedError


@dataclass
class RetryableOrderPurchaseScreenFailureDeserializationContract:
    exception: type = ExpediaGroupRetryableOrderPurchaseScreenFailureException
    model: type = RetryableOrderPurchaseScreenFailure


@dataclass
class UnauthorizedErrorDeserializationContract:
    exception: type = ExpediaGroupUnauthorizedErrorException
    model: type = UnauthorizedError


@dataclass
class InternalServerErrorDeserializationContract:
    exception: type = ExpediaGroupInternalServerErrorException
    model: type = InternalServerError


@dataclass
class AccountTakeoverBadRequestErrorDeserializationContract:
    exception: type = ExpediaGroupAccountTakeoverBadRequestErrorException
    model: type = AccountTakeoverBadRequestError


@dataclass
class OrderPurchaseUpdateNotFoundErrorDeserializationContract:
    exception: type = ExpediaGroupOrderPurchaseUpdateNotFoundErrorException
    model: type = OrderPurchaseUpdateNotFoundError


@dataclass
class GatewayTimeoutErrorDeserializationContract:
    exception: type = ExpediaGroupGatewayTimeoutErrorException
    model: type = GatewayTimeoutError
