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
from typing import Any, List, Literal, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr


class UpdateType(Enum):
    r"""pydantic model UpdateType: Transaction type associated with the update event.
    Attributes:
        ORDER_UPDATE(Any): --
        CHARGEBACK_FEEDBACK(Any): --
        INSULT_FEEDBACK(Any): --
        REFUND_UPDATE(Any): --
        PAYMENT_UPDATE(Any): --

    """
    ORDER_UPDATE: Any = 'ORDER_UPDATE'
    CHARGEBACK_FEEDBACK: Any = 'CHARGEBACK_FEEDBACK'
    INSULT_FEEDBACK: Any = 'INSULT_FEEDBACK'
    REFUND_UPDATE: Any = 'REFUND_UPDATE'
    PAYMENT_UPDATE: Any = 'PAYMENT_UPDATE'


class CancellationReason(BaseModel):
    r"""pydantic model CancellationReason: Reason of order update cancellation.
    Attributes:
        primary_reason_code(Optional[constr(max_length=200)], optional): Primary cancellation reason code.
        sub_reason_code(Optional[constr(max_length=200)], optional): Substitute cancellation reason code.
        primary_reason_description(constr(max_length=200)): Primary cancellation reason code. Required if `order_status = CANCELLED`.
        sub_reason_description(Optional[constr(max_length=200)], optional): Substitute cancellation reason description.

    """
    primary_reason_code: Optional[constr(max_length=200)] = None
    """
    Primary cancellation reason code.
    """
    sub_reason_code: Optional[constr(max_length=200)] = None
    """
    Substitute cancellation reason code.
    """
    primary_reason_description: constr(max_length=200)
    """
    Primary cancellation reason code. Required if `order_status = CANCELLED`.
    """
    sub_reason_description: Optional[constr(max_length=200)] = None
    """
    Substitute cancellation reason description.
    """


class RefundStatus(Enum):
    r"""pydantic model RefundStatus: Identifies the refund status. Possible values are:
    -`ISSUED` - The refund was issued.
    -`SETTLED` - The refund was settled.

    Attributes:
        ISSUED(Any): --
        SETTLED(Any): --

    """
    ISSUED: Any = 'ISSUED'
    SETTLED: Any = 'SETTLED'


class ChargebackStatus(Enum):
    r"""pydantic model ChargebackStatus: Identifies the chargeback status. Possible values are:

    -`RECEIVED` - The chargeback was received.

    -`REVERSAL` - The chargeback reversal was received.

    Attributes:
        RECEIVED(Any): --
        REVERSAL(Any): --

    """
    RECEIVED: Any = 'RECEIVED'
    REVERSAL: Any = 'REVERSAL'


class ChargebackReason(Enum):
    r"""pydantic model ChargebackReason: Reason for chargeback which can be `Fraud` or `Non Fraud`.
    Attributes:
        FRAUD(Any): --
        NON_FRAUD(Any): --

    """
    FRAUD: Any = 'FRAUD'
    NON_FRAUD: Any = 'NON_FRAUD'


class InsultDetail(BaseModel):
    r"""pydantic model InsultDetail: Details related to the insult.
    Attributes:
        insult_reported_date_time(Optional[datetime], optional): Date and time when the insult was reported to the partner, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

    """
    insult_reported_date_time: Optional[datetime] = None
    """
    Date and time when the insult was reported to the partner, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """


class Status(Enum):
    r"""pydantic model Status: Defines the current state of the Order.
    Attributes:
        COMPLETED(Any): --
        CHANGE_COMPLETED(Any): --
        CANCELLED(Any): --
        FAILED(Any): --
        CHANGE_FAILED(Any): --

    """
    COMPLETED: Any = 'COMPLETED'
    CHANGE_COMPLETED: Any = 'CHANGE_COMPLETED'
    CANCELLED: Any = 'CANCELLED'
    FAILED: Any = 'FAILED'
    CHANGE_FAILED: Any = 'CHANGE_FAILED'


class OrderPurchaseUpdateResponse(BaseModel):
    r"""pydantic model OrderPurchaseUpdateResponse
    Attributes:
        risk_id(Optional[constr(max_length=200)], optional): Unique identifier of transaction that was updated.

    """
    risk_id: Optional[constr(max_length=200)] = Field(None, example='1234567')
    """
    Unique identifier of transaction that was updated.
    """


class FraudDecision(Enum):
    r"""pydantic model FraudDecision
    Attributes:
        ACCEPT(Any): --
        REVIEW(Any): --
        REJECT(Any): --

    """
    ACCEPT: Any = 'ACCEPT'
    REVIEW: Any = 'REVIEW'
    REJECT: Any = 'REJECT'


class ErrorDetail(BaseModel):
    r"""pydantic model ErrorDetail: Error details in case of any errors.
    Attributes:
        code(Optional[int], optional): --
        message(Optional[constr(max_length=200)], optional): Description of the error. Clients may choose to use the description field to display to end clients.
        detailed_message(Optional[constr(max_length=500)], optional): Detailed description of the error.

    """
    code: Optional[int] = None
    message: Optional[constr(max_length=200)] = None
    """
    Description of the error. Clients may choose to use the description field to display to end clients.
    """
    detailed_message: Optional[constr(max_length=500)] = None
    """
    Detailed description of the error.
    """


class Error(BaseModel):
    r"""pydantic model Error: The object used the describe an error, containing both human-readable and in a machine-readable information.
    Attributes:
        type(AnyUrl): A URI reference, compliant with the standard EG error type format, which identifies the error type. It provides a machine-readable identifier for the error type. The error type will be aligned with the HTTP status code of the response. The URI can either be absolute or relative to the API's base URI. When dereferenced, it can also provide human-readable documentation for the error type.
        detail(str): A human-readable explanation of the error, specific to this error occurrence.

    """
    type: AnyUrl = Field(..., example='https://apis.expediagroup.com/errors/common/invalid-argument')
    """
    A URI reference, compliant with the standard EG error type format, which identifies the error type. It provides a machine-readable identifier for the error type. The error type will be aligned with the HTTP status code of the response. The URI can either be absolute or relative to the API's base URI. When dereferenced, it can also provide human-readable documentation for the error type.

    """
    detail: str = Field(..., example='The request failed because one or many input values are invalid. Please see the causes for more details.')
    """
    A human-readable explanation of the error, specific to this error occurrence.
    """


class Location(Enum):
    r"""pydantic model Location: The location of the element in the request that identifies this specific cause. When specified, the `name` will be specified and when applicable, the `value` as well. Can be one of:
    * `HEADER` - When an error has been identified in one of the request headers.
    * `PATH` - When an error has been identified in one of the path parameters.
    * `QUERY` - When an error has been identified in one of the query parameters.
    * `BODY` - When an error has been identified in the request body.

    Attributes:
        HEADER(Any): --
        PATH(Any): --
        QUERY(Any): --
        BODY(Any): --

    """
    HEADER: Any = 'HEADER'
    PATH: Any = 'PATH'
    QUERY: Any = 'QUERY'
    BODY: Any = 'BODY'


class ErrorCause(BaseModel):
    r"""pydantic model ErrorCause: The object used to describe a cause for an error, containing both human-readable and in a machine-readable information.
    Attributes:
        type(AnyUrl): A URI reference, compliant with the standard EG error type format, which identifies the cause type. It provides a machine-readable identifier for the cause type. The cause type will be aligned with the error type. The URI can either be absolute or relative to the API's base URI. When dereferenced, it provides human-readable documentation for the cause type.
        detail(str): A human-readable explanation of the cause, specific to this cause occurrence.
        location(Optional[Location], optional): The location of the element in the request that identifies this specific cause. When specified, the `name` will be specified and when applicable, the `value` as well. Can be one of: * `HEADER` - When an error has been identified in one of the request headers. * `PATH` - When an error has been identified in one of the path parameters. * `QUERY` - When an error has been identified in one of the query parameters. * `BODY` - When an error has been identified in the request body.
        name(Optional[str], optional): The name of the element for this cause. When specified, the `location` will be specified and when applicable, the `value` as well. This name is a function of the value of the `location` property:   * When the `location` is set to `HEADER`, this will be the name of the request header (e.g. `Content-Type`).   * When the `location` is set to `PATH`, this will be the name of the path parameter (e.g. in a path defined as `/users/{user_id}`, the value would be `user_id`).   * When the `location` is set to `QUERY`, this will be the name of the query string parameter (e.g. `offset`).   * When the `location` is set to `BODY`, this will one of the field names specified in the body of the request.     * For a top level field, it should only be set to the field name (e.g. `firstName`).     * For a field in a nested object, it may contain the path to reach the field (e.g. `address.city`).     * For a field in an object part of collection, it may contain the index in the collection (e.g. `permissions[0].name`).
        value(Optional[str], optional): A string representation of the erroneous value of the element identified in `name`, perceived to be the cause of the error. When specified, the `location` and `name` should be specified as well. This value may be omitted in cases where it cannot be provided (e.g. missing require field), or the erroneous value cannot be represented as a string.

    """
    type: AnyUrl = Field(..., example='https://apis.expediagroup.com/errors/common/invalid-number')
    """
    A URI reference, compliant with the standard EG error type format, which identifies the cause type. It provides a machine-readable identifier for the cause type. The cause type will be aligned with the error type. The URI can either be absolute or relative to the API's base URI. When dereferenced, it provides human-readable documentation for the cause type.

    """
    detail: str = Field(
        ..., example="The number of results per page you provided ('NotANumber') is invalid. Please provide a valid integer value between 1 and 100."
    )
    """
    A human-readable explanation of the cause, specific to this cause occurrence.
    """
    location: Optional[Location] = Field(None, example='QUERY')
    """
    The location of the element in the request that identifies this specific cause. When specified, the `name` will be specified and when applicable, the `value` as well. Can be one of:
    * `HEADER` - When an error has been identified in one of the request headers.
    * `PATH` - When an error has been identified in one of the path parameters.
    * `QUERY` - When an error has been identified in one of the query parameters.
    * `BODY` - When an error has been identified in the request body.

    """
    name: Optional[str] = Field(None, example='results_per_page')
    """
    The name of the element for this cause. When specified, the `location` will be specified and when applicable, the `value` as well. This name is a function of the value of the `location` property:
      * When the `location` is set to `HEADER`, this will be the name of the request header (e.g. `Content-Type`).
      * When the `location` is set to `PATH`, this will be the name of the path parameter (e.g. in a path defined as `/users/{user_id}`, the value would be `user_id`).
      * When the `location` is set to `QUERY`, this will be the name of the query string parameter (e.g. `offset`).
      * When the `location` is set to `BODY`, this will one of the field names specified in the body of the request.
        * For a top level field, it should only be set to the field name (e.g. `firstName`).
        * For a field in a nested object, it may contain the path to reach the field (e.g. `address.city`).
        * For a field in an object part of collection, it may contain the index in the collection (e.g. `permissions[0].name`).

    """
    value: Optional[str] = Field(None, example='NotANumber')
    """
    A string representation of the erroneous value of the element identified in `name`, perceived to be the cause of the error. When specified, the `location` and `name` should be specified as well. This value may be omitted in cases where it cannot be provided (e.g. missing require field), or the erroneous value cannot be represented as a string.

    """


class SiteInfo(BaseModel):
    r"""pydantic model SiteInfo
    Attributes:
        country_code(constr(regex=r'^[A-Z]{3}$')): The alpha-3 ISO code that represents a country name.
        agent_assisted(bool): Identifies if an agent assisted in booking travel for the customer. `False` if the order was directly booked by customer.

    """
    country_code: constr(regex=r'^[A-Z]{3}$') = Field(..., example='USA')
    """
    The alpha-3 ISO code that represents a country name.
    """
    agent_assisted: bool
    """
    Identifies if an agent assisted in booking travel for the customer. `False` if the order was directly booked by customer.
    """


class DeviceDetails(BaseModel):
    r"""pydantic model DeviceDetails
    Attributes:
        source(Optional[constr(max_length=50)], optional): Source of the device_box. Default value is `TrustWidget`.
        device_box(constr(max_length=16000)): Device related information retrieved from TrustWidget.
        ip_address(constr(regex=r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$')): IP address of the device used for booking.

    """
    source: Optional[constr(max_length=50)] = None
    """
    Source of the device_box. Default value is `TrustWidget`.
    """
    device_box: constr(max_length=16000)
    """
    Device related information retrieved from TrustWidget.
    """
    ip_address: constr(
        regex=r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$'
    ) = Field(..., example='192.168.32.48')
    """
    IP address of the device used for booking.
    """


class CurrentOrderStatus(Enum):
    r"""pydantic model CurrentOrderStatus: Status of the order.
    Attributes:
        IN_PROGRESS(Any): --
        COMPLETED(Any): --

    """
    IN_PROGRESS: Any = 'IN_PROGRESS'
    COMPLETED: Any = 'COMPLETED'


class OrderType(Enum):
    r"""pydantic model OrderType: Type of order. Possible `order_types`.

    `CREATE` - Initial type of a brand new order.

    `CHANGE` - If a `OrderPurchaseScreenRequest` has already been submitted for the initial booking with `order_type = CREATE`, but has now been modified and partner wishes to resubmit for Fraud screening then the `order_type = CHANGE`. Examples of changes that are supported are changes made to `check-in/checkout dates` or `price of a TravelProduct`.

    Attributes:
        CREATE(Any): --
        CHANGE(Any): --

    """
    CREATE: Any = 'CREATE'
    CHANGE: Any = 'CHANGE'


class AccountType(Enum):
    r"""pydantic model AccountType: Identifies if the customer account is known to the client. Possible values are:

    -`GUEST` - Applicable if the partner maintains record to distinguish whether the transaction was booked via a guest account.

    -`STANDARD` - Default account type.

    Attributes:
        GUEST(Any): --
        STANDARD(Any): --

    """
    GUEST: Any = 'GUEST'
    STANDARD: Any = 'STANDARD'


class AddressType(Enum):
    r"""pydantic model AddressType
    Attributes:
        HOME(Any): --
        WORK(Any): --

    """
    HOME: Any = 'HOME'
    WORK: Any = 'WORK'


class Address(BaseModel):
    r"""pydantic model Address
    Attributes:
        address_type(Optional[AddressType], optional): --
        address_line1(Optional[constr(max_length=200)], optional): Address line 1 of the address provided.
        address_line2(Optional[constr(max_length=200)], optional): Address line 2 of the address provided.
        city(Optional[constr(max_length=200)], optional): City of the address provided.
        state(Optional[constr(regex=r'^[A-Z]{2}$')], optional): The two-characters ISO code for the state or province of the address.
        zip_code(Optional[constr(max_length=20)], optional): Zip code of the address provided.
        country_code(Optional[constr(regex=r'^[A-Z]{3}$')], optional): ISO alpha-3 country code of the address provided.

    """
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
    state: Optional[constr(regex=r'^[A-Z]{2}$')] = None
    """
    The two-characters ISO code for the state or province of the address.
    """
    zip_code: Optional[constr(max_length=20)] = None
    """
    Zip code of the address provided.
    """
    country_code: Optional[constr(regex=r'^[A-Z]{3}$')] = None
    """
    ISO alpha-3 country code of the address provided.
    """


class InventorySource(Enum):
    r"""pydantic model InventorySource: Identifies the business model through which the supply is being sold. Merchant/Agency.
    Attributes:
        MERCHANT(Any): --
        AGENCY(Any): --

    """
    MERCHANT: Any = 'MERCHANT'
    AGENCY: Any = 'AGENCY'


class TravelersReference(BaseModel):
    r"""pydantic model TravelersReference
    Attributes:
        __root__(constr(max_length=50)): --

    """
    __root__: constr(max_length=50)


class FlightType(Enum):
    r"""pydantic model FlightType: Identifies the type of air trip based on the air destinations.
    Attributes:
        ROUNDTRIP(Any): --
        ONEWAY(Any): --
        MULTIPLE_DESTINATION(Any): --

    """
    ROUNDTRIP: Any = 'ROUNDTRIP'
    ONEWAY: Any = 'ONEWAY'
    MULTIPLE_DESTINATION: Any = 'MULTIPLE_DESTINATION'


class AirSegment(BaseModel):
    r"""pydantic model AirSegment
    Attributes:
        airline_code(constr(max_length=10)): Airline code of the trip segment
        departure_airport_code(constr(max_length=10)): Departure airport of the trip segment
        arrival_airport_code(constr(max_length=10)): Arrival airport of the trip segment
        departure_time(Optional[datetime], optional): Local date and time of departure from departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        arrival_time(Optional[datetime], optional): Local date and time of arrival to destination location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

    """
    airline_code: constr(max_length=10)
    """
    Airline code of the trip segment
    """
    departure_airport_code: constr(max_length=10)
    """
    Departure airport of the trip segment
    """
    arrival_airport_code: constr(max_length=10)
    """
    Arrival airport of the trip segment
    """
    departure_time: Optional[datetime] = None
    """
    Local date and time of departure from departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    arrival_time: Optional[datetime] = None
    """
    Local date and time of arrival to destination location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """


class Brand(Enum):
    r"""pydantic model Brand: Payment brand used for payment on this transaction.
    Attributes:
        AMERICAN_EXPRESS(Any): --
        CARTE_BLANCHE(Any): --
        CARTE_BLEUE(Any): --
        DINERS_CLUB_INTERNATIONAL(Any): --
        BC_CARD(Any): --
        DISCOVER(Any): --
        CHINA_UNION_PAY(Any): --
        JCB(Any): --
        ELV(Any): --
        MASTER_CARD(Any): --
        MAESTRO(Any): --
        POSTEPAY_MASTERCARD(Any): --
        SOLO(Any): --
        SWITCH(Any): --
        VISA(Any): --
        VISA_DELTA(Any): --
        VISA_ELECTRON(Any): --
        CARTE_SI(Any): --
        CARTA_SI(Any): --
        VISA_DANKORT(Any): --
        POSTEPAY_VISA_ELECTRON(Any): --
        IBP(Any): --
        CASH_CARD(Any): --
        LOCAL_DEBIT_CARD(Any): --
        INTER_COMPANY(Any): --
        GIRO_PAY(Any): --
        SOFORT(Any): --
        PAY_PAL(Any): --
        GIFT_CARD(Any): --

    """
    AMERICAN_EXPRESS: Any = 'AMERICAN_EXPRESS'
    CARTE_BLANCHE: Any = 'CARTE_BLANCHE'
    CARTE_BLEUE: Any = 'CARTE_BLEUE'
    DINERS_CLUB_INTERNATIONAL: Any = 'DINERS_CLUB_INTERNATIONAL'
    BC_CARD: Any = 'BC_CARD'
    DISCOVER: Any = 'DISCOVER'
    CHINA_UNION_PAY: Any = 'CHINA_UNION_PAY'
    JCB: Any = 'JCB'
    ELV: Any = 'ELV'
    MASTER_CARD: Any = 'MASTER_CARD'
    MAESTRO: Any = 'MAESTRO'
    POSTEPAY_MASTERCARD: Any = 'POSTEPAY_MASTERCARD'
    SOLO: Any = 'SOLO'
    SWITCH: Any = 'SWITCH'
    VISA: Any = 'VISA'
    VISA_DELTA: Any = 'VISA_DELTA'
    VISA_ELECTRON: Any = 'VISA_ELECTRON'
    CARTE_SI: Any = 'CARTE_SI'
    CARTA_SI: Any = 'CARTA_SI'
    VISA_DANKORT: Any = 'VISA_DANKORT'
    POSTEPAY_VISA_ELECTRON: Any = 'POSTEPAY_VISA_ELECTRON'
    IBP: Any = 'IBP'
    CASH_CARD: Any = 'CASH_CARD'
    LOCAL_DEBIT_CARD: Any = 'LOCAL_DEBIT_CARD'
    INTER_COMPANY: Any = 'INTER_COMPANY'
    GIRO_PAY: Any = 'GIRO_PAY'
    SOFORT: Any = 'SOFORT'
    PAY_PAL: Any = 'PAY_PAL'
    GIFT_CARD: Any = 'GIFT_CARD'


class PaymentThreeDSCriteria(BaseModel):
    r"""pydantic model PaymentThreeDSCriteria: Payment ThreeDS criteria attributes.
    Attributes:
        probable_flag(Optional[bool], optional): This is a flag passed that indicates that this transaction could potentially go through 3DS.
        transaction_model(Optional[constr(max_length=200)], optional): Model used to process payment transaction.

    """
    probable_flag: Optional[bool] = None
    """
    This is a flag passed that indicates that this transaction could potentially go through 3DS.
    """
    transaction_model: Optional[constr(max_length=200)] = None
    """
    Model used to process payment transaction.
    """


class PaymentReason(Enum):
    r"""pydantic model PaymentReason: The reason of payment. Possible values:
    - `FULL` - If the amount is paid i full for the order
    - `DEPOSIT` - The initial payment. Amount to be paid up front.
    - `SCHEDULED` - The amount to be payment based on a schedule for the remaining portion of the booking amount.
    - `SUBSEQUENT` - An additional amount paid that was not originally scheduled.
    - `DEFERRED`

    Attributes:
        FULL(Any): --
        DEPOSIT(Any): --
        SCHEDULED(Any): --
        SUBSEQUENT(Any): --
        DEFERRED(Any): --

    """
    FULL: Any = 'FULL'
    DEPOSIT: Any = 'DEPOSIT'
    SCHEDULED: Any = 'SCHEDULED'
    SUBSEQUENT: Any = 'SUBSEQUENT'
    DEFERRED: Any = 'DEFERRED'


class VerificationType(Enum):
    r"""pydantic model VerificationType: The type of the verification used to verify the instrument. If the Card Verfication Value was provided to verify the credit card used for the transaction, `type = CVV`.
    Attributes:
        CVV(Any): --
        field_3DS(Any): --

    """
    CVV: Any = 'CVV'
    field_3DS: Any = '3DS'


class PaymentStatus(Enum):
    r"""pydantic model PaymentStatus: The status of the payment operation.
    Attributes:
        COMPLETED(Any): --
        FAILED(Any): --

    """
    COMPLETED: Any = 'COMPLETED'
    FAILED: Any = 'FAILED'


class PaymentMethod(Enum):
    r"""pydantic model PaymentMethod: The payment method used at the time of purchase for the transaction. Supported `method`'s are: `CREDIT_CARD`, `PAYPAL`, `POINTS`.
    Attributes:
        CREDIT_CARD(Any): --
        PAYPAL(Any): --
        POINTS(Any): --

    """
    CREDIT_CARD: Any = 'CREDIT_CARD'
    PAYPAL: Any = 'PAYPAL'
    POINTS: Any = 'POINTS'


class TravelProductType(Enum):
    r"""pydantic model TravelProductType: Type of product.
    Attributes:
        CRUISE(Any): --
        AIR(Any): --
        CAR(Any): --
        INSURANCE(Any): --
        HOTEL(Any): --

    """
    CRUISE: Any = 'CRUISE'
    AIR: Any = 'AIR'
    CAR: Any = 'CAR'
    INSURANCE: Any = 'INSURANCE'
    HOTEL: Any = 'HOTEL'


class CardType(Enum):
    r"""pydantic model CardType: card_type is an enum value which associated with the payment method of the specific payment instrument.
    Attributes:
        AMERICAN_EXPRESS(Any): --
        CARTE_BLANCHE(Any): --
        CARTE_BLEUE(Any): --
        DINERS_CLUB(Any): --
        DISCOVER(Any): --
        ELV(Any): --
        JCB(Any): --
        MASTER_CARD(Any): --
        SOLO(Any): --
        SWITCH(Any): --
        VISA(Any): --
        IBP(Any): --
        CASH_CARD(Any): --
        LOCAL_DEBIT_CARD(Any): --
        INTER_COMPANY(Any): --
        GIRO_PAY(Any): --
        SOFORT(Any): --
        PAY_PAL(Any): --
        MAESTRO(Any): --
        YANDEX(Any): --
        WEB_MONEY(Any): --
        QIWI(Any): --
        GIFT_CARD(Any): --
        BITCOIN(Any): --
        ELV_IBAN(Any): --
        CHINA_UNION_PAY(Any): --

    """
    AMERICAN_EXPRESS: Any = 'AMERICAN_EXPRESS'
    CARTE_BLANCHE: Any = 'CARTE_BLANCHE'
    CARTE_BLEUE: Any = 'CARTE_BLEUE'
    DINERS_CLUB: Any = 'DINERS_CLUB'
    DISCOVER: Any = 'DISCOVER'
    ELV: Any = 'ELV'
    JCB: Any = 'JCB'
    MASTER_CARD: Any = 'MASTER_CARD'
    SOLO: Any = 'SOLO'
    SWITCH: Any = 'SWITCH'
    VISA: Any = 'VISA'
    IBP: Any = 'IBP'
    CASH_CARD: Any = 'CASH_CARD'
    LOCAL_DEBIT_CARD: Any = 'LOCAL_DEBIT_CARD'
    INTER_COMPANY: Any = 'INTER_COMPANY'
    GIRO_PAY: Any = 'GIRO_PAY'
    SOFORT: Any = 'SOFORT'
    PAY_PAL: Any = 'PAY_PAL'
    MAESTRO: Any = 'MAESTRO'
    YANDEX: Any = 'YANDEX'
    WEB_MONEY: Any = 'WEB_MONEY'
    QIWI: Any = 'QIWI'
    GIFT_CARD: Any = 'GIFT_CARD'
    BITCOIN: Any = 'BITCOIN'
    ELV_IBAN: Any = 'ELV_IBAN'
    CHINA_UNION_PAY: Any = 'CHINA_UNION_PAY'


class Name(BaseModel):
    r"""pydantic model Name: Group of attributes intended to hold information about a customer or traveler's name for the order.
    Attributes:
        last_name(constr(max_length=200)): Surname, or last name, of the person.
        first_name(constr(max_length=200)): Given, or first name, of the person.
        middle_name(Optional[constr(max_length=200)], optional): Middle name of the person.
        title(Optional[constr(max_length=200)], optional): Title of the person for name (e.g. Mr., Ms. etc).
        suffix(Optional[constr(max_length=50)], optional): Generational designations (e.g. Sr, Jr, III) or values that indicate the individual holds a position, educational degree, accreditation, office, or honor (e.g. PhD, CCNA, OBE).

    """
    last_name: constr(max_length=200)
    """
    Surname, or last name, of the person.
    """
    first_name: constr(max_length=200)
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


class TelephoneType(Enum):
    r"""pydantic model TelephoneType: Classification of the phone (e.g. `Home`, `Mobile`).
    Attributes:
        HOME(Any): --
        MOBILE(Any): --
        BUSINESS(Any): --
        FAX(Any): --
        OTHER(Any): --

    """
    HOME: Any = 'HOME'
    MOBILE: Any = 'MOBILE'
    BUSINESS: Any = 'BUSINESS'
    FAX: Any = 'FAX'
    OTHER: Any = 'OTHER'


class TelephonePlatformType(Enum):
    r"""pydantic model TelephonePlatformType: Classification of the phone platform.
    Attributes:
        MOBILE(Any): --
        LANDLINE(Any): --
        VOIP(Any): --

    """
    MOBILE: Any = 'MOBILE'
    LANDLINE: Any = 'LANDLINE'
    VOIP: Any = 'VOIP'


class Email(BaseModel):
    r"""pydantic model Email: Group of attributes intended to hold information about email address associated with the transaction.
    Attributes:
        email_address(Optional[EmailStr], optional): Full email address including the alias, @ symbol, domain, and root domain.

    """
    email_address: Optional[EmailStr] = None
    """
    Full email address including the alias, @ symbol, domain, and root domain.
    """


class Amount(BaseModel):
    r"""pydantic model Amount
    Attributes:
        value(float): The amount required in payment for the product/order in local currency.
        currency_code(constr(regex=r'^[A-Z]{3}$', max_length=3)): The ISO  alpha-3 country code for the amount currency.

    """
    value: float
    """
    The amount required in payment for the product/order in local currency.
    """
    currency_code: constr(regex=r'^[A-Z]{3}$', max_length=3)
    """
    The ISO  alpha-3 country code for the amount currency.
    """


class ContentType(Enum):
    r"""pydantic model ContentType
    Attributes:
        application_json(Any): --

    """
    application_json: Any = 'application/json'


class IssuedRefundUpdateDetails(BaseModel):
    r"""pydantic model IssuedRefundUpdateDetails: Data that describes issued refund that should be updated.
    Attributes:
        refund_issued_date_time(datetime): Date and time when the 3rd party payment processor confirmed that a previously submitted payment refund has issued at the participating financial institutions.
        refund_issued_amount(Amount): --

    """
    refund_issued_date_time: datetime
    """
    Date and time when the 3rd party payment processor confirmed that a previously submitted payment refund has issued at the participating financial institutions.
    """
    refund_issued_amount: Amount


class SettledRefundUpdateDetails(BaseModel):
    r"""pydantic model SettledRefundUpdateDetails: Data that describes settled refund that should be updated.
    Attributes:
        refund_settlement_date_time(datetime): Date and time when the 3rd party payment processor confirmed that a previously submitted payment refund has settled at the participating financial institutions.
        refund_deposit_date_time(datetime): Date and time when the refund was deposited to the original form of payment.
        acquirer_reference_number(constr(max_length=200)): A unique number that tags a credit or debit card transaction when it goes from the merchant's bank through to the cardholder's bank.
        settlement_id(constr(max_length=200)): Unique settlement identifier generated for a previously submitted payment refund.
        refund_settled_amount(Amount): --

    """
    refund_settlement_date_time: datetime
    """
    Date and time when the 3rd party payment processor confirmed that a previously submitted payment refund has settled at the participating financial institutions.
    """
    refund_deposit_date_time: datetime
    """
    Date and time when the refund was deposited to the original form of payment.
    """
    acquirer_reference_number: constr(max_length=200)
    """
    A unique number that tags a credit or debit card transaction when it goes from the merchant's bank through to the cardholder's bank.
    """
    settlement_id: constr(max_length=200)
    """
    Unique settlement identifier generated for a previously submitted payment refund.
    """
    refund_settled_amount: Amount


class ChargebackDetail(BaseModel):
    r"""pydantic model ChargebackDetail: Details related to the chargeback.
    Attributes:
        chargeback_status(ChargebackStatus): Identifies the chargeback status. Possible values are:  -`RECEIVED` - The chargeback was received.  -`REVERSAL` - The chargeback reversal was received.
        chargeback_reason(ChargebackReason): Reason for chargeback which can be `Fraud` or `Non Fraud`.
        chargeback_amount(Amount): --
        currency_code(constr(regex=r'^[A-Z]{3}$', max_length=200)): The 3-letter currency code defined in ISO 4217. https://www.currency-iso.org/dam/downloads/lists/list_one.xml.
        bank_reason_code(Optional[constr(max_length=200)], optional): Unique code provided by the acquiring bank for the category of fraud.
        chargeback_reported_date_time(Optional[datetime], optional): Date and time when the chargeback was reported to the partner, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

    """
    chargeback_status: ChargebackStatus
    """
    Identifies the chargeback status. Possible values are:

    -`RECEIVED` - The chargeback was received.

    -`REVERSAL` - The chargeback reversal was received.

    """
    chargeback_reason: ChargebackReason
    """
    Reason for chargeback which can be `Fraud` or `Non Fraud`.
    """
    chargeback_amount: Amount
    currency_code: constr(regex=r'^[A-Z]{3}$', max_length=200)
    """
    The 3-letter currency code defined in ISO 4217. https://www.currency-iso.org/dam/downloads/lists/list_one.xml.
    """
    bank_reason_code: Optional[constr(max_length=200)] = None
    """
    Unique code provided by the acquiring bank for the category of fraud.
    """
    chargeback_reported_date_time: Optional[datetime] = None
    """
    Date and time when the chargeback was reported to the partner, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """


class OrderPurchaseScreenResponse(BaseModel):
    r"""pydantic model OrderPurchaseScreenResponse
    Attributes:
        risk_id(Optional[constr(max_length=200)], optional): Unique identifier assigned to the transaction by Expedia's Fraud Prevention Service.
        decision(Optional[FraudDecision], optional): --
        error_detail(Optional[ErrorDetail], optional): --

    """
    risk_id: Optional[constr(max_length=200)] = Field(None, example='1234567')
    """
    Unique identifier assigned to the transaction by Expedia's Fraud Prevention Service.
    """
    decision: Optional[FraudDecision] = None
    error_detail: Optional[ErrorDetail] = None


class ExtendedError(BaseModel):
    r"""pydantic model ExtendedError: The object used the describe an error, containing both human-readable and in a machine-readable information.
    Attributes:
        type(AnyUrl): A URI reference, compliant with the standard EG error type format, which identifies the error type. It provides a machine-readable identifier for the error type. The error type will be aligned with the HTTP status code of the response. The URI can either be absolute or relative to the API's base URI. When dereferenced, it can also provide human-readable documentation for the error type.
        detail(str): A human-readable explanation of the error, specific to this error occurrence.
        causes(Optional[List[ErrorCause]], optional): An array of cause objects, that identify the specific causes of the error.

    """
    type: AnyUrl = Field(..., example='https://apis.expediagroup.com/errors/common/invalid-argument')
    """
    A URI reference, compliant with the standard EG error type format, which identifies the error type. It provides a machine-readable identifier for the error type. The error type will be aligned with the HTTP status code of the response. The URI can either be absolute or relative to the API's base URI. When dereferenced, it can also provide human-readable documentation for the error type.

    """
    detail: str = Field(..., example='The request failed because one or many input values are invalid. Please see the causes for more details.')
    """
    A human-readable explanation of the error, specific to this error occurrence.
    """
    causes: Optional[List[ErrorCause]] = None
    """
    An array of cause objects, that identify the specific causes of the error.
    """


class PaymentOutcome(BaseModel):
    r"""pydantic model PaymentOutcome
    Attributes:
        status(Optional[PaymentStatus], optional): --
        code(Optional[constr(max_length=200)], optional): A mnemonic code for the payment processing.
        description(Optional[constr(max_length=200)], optional): A short description providing additional explanation regarding the mnemonic code.

    """
    status: Optional[PaymentStatus] = None
    code: Optional[constr(max_length=200)] = None
    """
    A mnemonic code for the payment processing.
    """
    description: Optional[constr(max_length=200)] = None
    """
    A short description providing additional explanation regarding the mnemonic code.
    """


class Telephone(BaseModel):
    r"""pydantic model Telephone: Group of attributes intended to hold information about phone number associated with the transaction.  A user can have one to many phone numbers (home, work, mobile, etc.).
    Attributes:
        type(Optional[TelephoneType], optional): --
        platform_type(Optional[TelephonePlatformType], optional): --
        country_access_code(constr(regex=r'^[0-9]{1,3}$', max_length=3)): Numeric digit between 1 to 3 characters used to represent the country code for international dialing.  Does not include symbols, spaces, or leading zeros.
        area_code(constr(regex=r'^[0-9]{1,20}$', max_length=20)): A number prefixed to an individual telephone number: used in making long-distance calls.  Does not include symbols, spaces, or leading zeros.
        phone_number(constr(regex=r'^[0-9]{1,50}$', max_length=50)): A number that is dialed on a telephone, without the country or area codes, to reach a particular person, business, etc.  Does not include symbols, spaces, or leading zeros.
        extension_number(Optional[constr(regex=r'^[0-9]{1,20}$', max_length=20)], optional): The number used to reach an individual once a phone connection is established.  Does not include symbols, spaces, or leading zeros.
        preference_rank(Optional[float], optional): Ranking of order of user preference for contact via text (if type is Mobile) or voice.  `0` means no preference.  `1` is the primary phone, `2` is the secondary phone, etc.
        last_verified_date_time(Optional[datetime], optional): Local date and time user validated possession of their phone number via a text or voice multi factor authentication challenge, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        verified_flag(Optional[bool], optional): Flag indicating whether user passed validation of possession of their phone number via a text or voice multi factor authentication challenge.

    """
    type: Optional[TelephoneType] = None
    platform_type: Optional[TelephonePlatformType] = None
    country_access_code: constr(regex=r'^[0-9]{1,3}$', max_length=3) = Field(..., example='1')
    """
    Numeric digit between 1 to 3 characters used to represent the country code for international dialing.  Does not include symbols, spaces, or leading zeros.
    """
    area_code: constr(regex=r'^[0-9]{1,20}$', max_length=20) = Field(..., example='1')
    """
    A number prefixed to an individual telephone number: used in making long-distance calls.  Does not include symbols, spaces, or leading zeros.
    """
    phone_number: constr(regex=r'^[0-9]{1,50}$', max_length=50) = Field(..., example='1234567')
    """
    A number that is dialed on a telephone, without the country or area codes, to reach a particular person, business, etc.  Does not include symbols, spaces, or leading zeros.
    """
    extension_number: Optional[constr(regex=r'^[0-9]{1,20}$', max_length=20)] = Field(None, example='89')
    """
    The number used to reach an individual once a phone connection is established.  Does not include symbols, spaces, or leading zeros.
    """
    preference_rank: Optional[float] = None
    """
    Ranking of order of user preference for contact via text (if type is Mobile) or voice.  `0` means no preference.  `1` is the primary phone, `2` is the secondary phone, etc.
    """
    last_verified_date_time: Optional[datetime] = None
    """
    Local date and time user validated possession of their phone number via a text or voice multi factor authentication challenge, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    verified_flag: Optional[bool] = None
    """
    Flag indicating whether user passed validation of possession of their phone number via a text or voice multi factor authentication challenge.
    """


class CustomerAccount(BaseModel):
    r"""pydantic model CustomerAccount
    Attributes:
        user_id(Optional[str], optional): Unique identifier assigned to the account owner by the partner. `user_id` is specific to the partner namespace
        account_type(AccountType): Identifies if the customer account is known to the client. Possible values are:  -`GUEST` - Applicable if the partner maintains record to distinguish whether the transaction was booked via a guest account.  -`STANDARD` - Default account type.
        name(Name): --
        email_address(EmailStr): Email address for the account owner.
        telephones(Optional[List[Telephone]], optional): --
        address(Optional[Address], optional): --
        registered_time(Optional[datetime], optional): The local date and time that the customer first registered on the client site, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

    """
    user_id: Optional[str] = None
    """
    Unique identifier assigned to the account owner by the partner. `user_id` is specific to the partner namespace
    """
    account_type: AccountType = Field(..., example='STANDARD')
    """
    Identifies if the customer account is known to the client. Possible values are:

    -`GUEST` - Applicable if the partner maintains record to distinguish whether the transaction was booked via a guest account.

    -`STANDARD` - Default account type.

    """
    name: Name
    email_address: EmailStr
    """
    Email address for the account owner.
    """
    telephones: Optional[List[Telephone]] = None
    address: Optional[Address] = None
    registered_time: Optional[datetime] = None
    """
    The local date and time that the customer first registered on the client site, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """


class Traveler(BaseModel):
    r"""pydantic model Traveler
    Attributes:
        traveler_name(Name): --
        email_address(Optional[EmailStr], optional): Email address associated with the traveler as supplied by the partner system.
        telephones(Optional[List[Telephone]], optional): --
        primary(bool): Indicator for one of the travelers who is the primary traveler. One traveler in each itinerary item must be listed as primary. By default, for a single traveler this should be set to `true`.
        age(Optional[float], optional): Age of the traveler.
        birth_date(Optional[datetime], optional): Date of birth for traveler, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        citizenship_country_code(Optional[constr(regex=r'^[A-Z]{3}$', min_length=3, max_length=3)], optional): The alpha-3 ISO country code of the traveler's nationality.
        traveler_id(Optional[constr(max_length=100)], optional): A unique identifier for travelers in the transaction.

    """
    traveler_name: Name
    email_address: Optional[EmailStr] = None
    """
    Email address associated with the traveler as supplied by the partner system.
    """
    telephones: Optional[List[Telephone]] = Field(None, maxItems=250, minItems=1)
    primary: bool
    """
    Indicator for one of the travelers who is the primary traveler. One traveler in each itinerary item must be listed as primary. By default, for a single traveler this should be set to `true`.
    """
    age: Optional[float] = None
    """
    Age of the traveler.
    """
    birth_date: Optional[datetime] = None
    """
    Date of birth for traveler, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    citizenship_country_code: Optional[constr(regex=r'^[A-Z]{3}$', min_length=3, max_length=3)] = None
    """
    The alpha-3 ISO country code of the traveler's nationality.
    """
    traveler_id: Optional[constr(max_length=100)] = None
    """
    A unique identifier for travelers in the transaction.
    """


class PaymentOperation(BaseModel):
    r"""pydantic model PaymentOperation
    Attributes:
        id(Optional[constr(max_length=200)], optional): --
        amount(Optional[Amount], optional): --
        outcome(Optional[PaymentOutcome], optional): --

    """
    id: Optional[constr(max_length=200)] = None
    amount: Optional[Amount] = None
    outcome: Optional[PaymentOutcome] = None


class Verify(PaymentOperation):
    r"""pydantic model Verify: A verify operation represents the intent to verify the payment associated with this transaction.
    Attributes:
        type(Optional[VerificationType], optional): --

    """
    type: Optional[VerificationType] = None


class Authorize(PaymentOperation):
    r"""pydantic model Authorize: Authorize operation on the payment. An authorize operation represents placing the funds on hold with the specified form of payment."""
    pass


class AuthorizeReversal(PaymentOperation):
    r"""pydantic model AuthorizeReversal: Authorize Reversal operation on the payment. An authorize reversal operation represents a notification received usually from a 3rd party payment processor to indicate that an authorization hold should be released as a result of a sale being partially or completely cancelled."""
    pass


class Capture(PaymentOperation):
    r"""pydantic model Capture: Capture operation on the payment. A capture operation represents a notification received usually from a 3rd party payment processor to indicate that the funds placed on hold will be captured and the funds transfer process will occur from the customer's funds to the merchant's funds."""
    pass


class Refund(PaymentOperation):
    r"""pydantic model Refund: Refund operation on the payment. A refund operation represents the intent to refund a previous charge."""
    pass


class Operations(BaseModel):
    r"""pydantic model Operations: All operations related to a payment throughout its lifespan. An operation represents an event external to Fraud Prevention Service that specifies to perform a payment operation. Possible operation types include:

    - `Verify`

    - `Authorize`

    - `AuthorizeReversal`

    - `Capture`

    - `Refund`

    Attributes:
        verify(Optional[Verify], optional): --
        authorize(Optional[Authorize], optional): --
        authorize_reversal(Optional[AuthorizeReversal], optional): --
        capture(Optional[Capture], optional): --
        refunds(Optional[List[Refund]], optional): --

    """
    verify: Optional[Verify] = None
    authorize: Optional[Authorize] = None
    authorize_reversal: Optional[AuthorizeReversal] = None
    capture: Optional[Capture] = None
    refunds: Optional[List[Refund]] = Field(None, maxItems=20)


class Payment(BaseModel):
    r"""pydantic model Payment: The `method` field value is used as a discriminator, with the following mapping:
    * `CREDIT_CARD`: `CreditCard`
    * `PAYPAL`: `PayPal`
    * `POINTS`: `Points`

    Attributes:
        brand(Brand): Payment brand used for payment on this transaction.
        method(PaymentMethod): --
        reason(Optional[PaymentReason], optional): --
        billing_name(Name): --
        billing_address(Address): --
        billing_email_address(EmailStr): Email address associated with the payment.
        authorized_amount(Optional[Amount], optional): --
        verified_amount(Optional[Amount], optional): --
        three_digits_secure_criteria(Optional[PaymentThreeDSCriteria], optional): --
        operations(Optional[Operations], optional): --

    """
    brand: Brand
    """
    Payment brand used for payment on this transaction.
    """
    method: PaymentMethod
    reason: Optional[PaymentReason] = None
    billing_name: Name
    billing_address: Address
    billing_email_address: EmailStr
    """
    Email address associated with the payment.
    """
    authorized_amount: Optional[Amount] = None
    verified_amount: Optional[Amount] = None
    three_digits_secure_criteria: Optional[PaymentThreeDSCriteria] = None
    operations: Optional[Operations] = None


class CreditCard(Payment):
    r"""pydantic model CreditCard
    Attributes:
        card_type(CardType): card_type is an enum value which associated with the payment method of the specific payment instrument.
        card_number(constr(max_length=200)): All the digits (unencrypted) of the credit card number associated with the payment.
        expiry_date(Optional[datetime], optional): Expiration date of the credit card used for payment.
        electronic_commerce_indicator(Optional[constr(max_length=200)], optional): Electronic Commerce Indicator, a two or three digit number usually returned by a 3rd party payment processor in regards to the authentication used when gathering the cardholder's payment credentials.
        virtual_credit_card_flag(Optional[bool], optional): A flag to indicate that the bank card being used for the charge is a virtual credit card.
        wallet_type(Optional[constr(max_length=200)], optional): If a virtual/digital form of payment was used, the type of digital wallet should be specified here. Possible `wallet_type`'s include: `Google` or `ApplePay`.
        card_avs_response(constr(max_length=50)): A field used to confirm if the address provided at the time of purchase matches what the bank has on file for the Credit Card.
        card_cvv_response(constr(max_length=20)): A field used to confirm the Card Verification Value on the Credit Card matches the Credit Card used at the time of purchase.
        telephones(List[Telephone]): Telephone(s) associated with card holder and credit card.
        merchant_order_code(Optional[constr(max_length=200)], optional): Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.
        card_authentication_failure_count(Optional[int], optional): Total authentication failure count for given card

    """
    card_type: CardType
    """
    card_type is an enum value which associated with the payment method of the specific payment instrument.
    """
    card_number: constr(max_length=200)
    """
    All the digits (unencrypted) of the credit card number associated with the payment.
    """
    expiry_date: Optional[datetime] = None
    """
    Expiration date of the credit card used for payment.
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
    card_avs_response: constr(max_length=50)
    """
    A field used to confirm if the address provided at the time of purchase matches what the bank has on file for the Credit Card.
    """
    card_cvv_response: constr(max_length=20)
    """
    A field used to confirm the Card Verification Value on the Credit Card matches the Credit Card used at the time of purchase.
    """
    telephones: List[Telephone] = Field(..., maxItems=20, minItems=1)
    """
    Telephone(s) associated with card holder and credit card.
    """
    merchant_order_code: Optional[constr(max_length=200)] = None
    """
    Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.
    """
    card_authentication_failure_count: Optional[int] = None
    """
    Total authentication failure count for given card
    """


class PayPal(Payment):
    r"""pydantic model PayPal
    Attributes:
        payer_id(constr(max_length=200)): Unique PayPal Customer Account identification number.
        transaction_id(constr(max_length=200)): Unique transaction number to identify Auth calls at PayPal.
        merchant_order_code(Optional[constr(max_length=200)], optional): Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.

    """
    payer_id: constr(max_length=200)
    """
    Unique PayPal Customer Account identification number.
    """
    transaction_id: constr(max_length=200)
    """
    Unique transaction number to identify Auth calls at PayPal.
    """
    merchant_order_code: Optional[constr(max_length=200)] = None
    """
    Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.
    """


class Points(Payment):
    r"""pydantic model Points"""
    pass


class OrderPurchaseScreenRequest(BaseModel):
    r"""pydantic model OrderPurchaseScreenRequest
    Attributes:
        transaction(Optional[OrderPurchaseTransaction], optional): --

    """
    transaction: Optional[OrderPurchaseTransaction] = None


class OrderPurchaseTransaction(BaseModel):
    r"""pydantic model OrderPurchaseTransaction
    Attributes:
        site_info(SiteInfo): --
        device_details(DeviceDetails): --
        customer_account(CustomerAccount): --
        transaction_details(TransactionDetails): --

    """
    site_info: SiteInfo
    device_details: DeviceDetails
    customer_account: CustomerAccount
    transaction_details: TransactionDetails


class TransactionDetails(BaseModel):
    r"""pydantic model TransactionDetails
    Attributes:
        order_id(constr(max_length=50)): Unique identifier assigned to the order by the partner. `order_id` is specific to the partner namespace.
        current_order_status(CurrentOrderStatus): Status of the order.
        order_type(OrderType): Type of order. Possible `order_types`.  `CREATE` - Initial type of a brand new order.  `CHANGE` - If a `OrderPurchaseScreenRequest` has already been submitted for the initial booking with `order_type = CREATE`, but has now been modified and partner wishes to resubmit for Fraud screening then the `order_type = CHANGE`. Examples of changes that are supported are changes made to `check-in/checkout dates` or `price of a TravelProduct`.
        travel_products(List[TravelProduct]): --
        travelers(List[Traveler]): Individuals who are part of the travel party for the order. At minimum there must be at least `1` traveler.
        payments(List[Payment]): List of the form(s) of payment being used to purchase the order.  One or more forms of payment can be used within an order. Information gathered will be specific to the form of payment.

    """
    order_id: constr(max_length=50) = Field(..., example='1000000234')
    """
    Unique identifier assigned to the order by the partner. `order_id` is specific to the partner namespace.
    """
    current_order_status: CurrentOrderStatus
    """
    Status of the order.
    """
    order_type: OrderType = Field(..., example='CREATE')
    """
    Type of order. Possible `order_types`.

    `CREATE` - Initial type of a brand new order.

    `CHANGE` - If a `OrderPurchaseScreenRequest` has already been submitted for the initial booking with `order_type = CREATE`, but has now been modified and partner wishes to resubmit for Fraud screening then the `order_type = CHANGE`. Examples of changes that are supported are changes made to `check-in/checkout dates` or `price of a TravelProduct`.

    """
    travel_products: List[TravelProduct] = Field(..., maxItems=20, minItems=1)
    travelers: List[Traveler] = Field(..., maxItems=30, minItems=1)
    """
    Individuals who are part of the travel party for the order. At minimum there must be at least `1` traveler.
    """
    payments: List[Payment] = Field(..., maxItems=30, minItems=1)
    """
    List of the form(s) of payment being used to purchase the order.  One or more forms of payment can be used within an order. Information gathered will be specific to the form of payment.
    """


class OrderUpdate(BaseModel):
    r"""pydantic model OrderUpdate: Order related data that should be updated.
    Attributes:
        risk_id(constr(max_length=200)): The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
        order_status(Status): --
        cancellation_reason(Optional[CancellationReason], optional): --
        type(Literal["OrderUpdate"]): --

    """
    risk_id: constr(max_length=200) = Field(..., example='123456789')
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """
    order_status: Status
    cancellation_reason: Optional[CancellationReason] = None
    type: Literal["OrderUpdate"]


class ChargebackFeedback(BaseModel):
    r"""pydantic model ChargebackFeedback: Feedback from EG external partners if they receive a chargeback for a false negative recommendation from Fraud Prevention system.
    Attributes:
        risk_id(constr(max_length=200)): The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
        chargeback_detail(Optional[ChargebackDetail], optional): --
        type(Literal["ChargebackFeedback"]): --

    """
    risk_id: constr(max_length=200) = Field(..., example='123456789')
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """
    chargeback_detail: Optional[ChargebackDetail] = None
    type: Literal["ChargebackFeedback"]


class InsultFeedback(BaseModel):
    r"""pydantic model InsultFeedback: Feedback from EG external partners regarding a false positive recommendation that from Fraud Prevention system gave for their customer.
    Attributes:
        risk_id(constr(max_length=200)): The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
        insult_detail(Optional[InsultDetail], optional): --
        type(Literal["InsultFeedback"]): --

    """
    risk_id: constr(max_length=200) = Field(..., example='123456789')
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """
    insult_detail: Optional[InsultDetail] = None
    type: Literal["InsultFeedback"]


class RefundUpdate(BaseModel):
    r"""pydantic model RefundUpdate: Refund related data. Update should be sent when refund is issued or settled. Amounts should include all fees and taxes.
    Attributes:
        risk_id(constr(max_length=200)): The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
        refund_status(RefundStatus): Identifies the refund status. Possible values are: -`ISSUED` - The refund was issued. -`SETTLED` - The refund was settled.
        type(Literal["RefundUpdate"]): --

    """
    risk_id: constr(max_length=200) = Field(..., example='123456789')
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """
    refund_status: RefundStatus
    """
    Identifies the refund status. Possible values are:
    -`ISSUED` - The refund was issued.
    -`SETTLED` - The refund was settled.

    """
    type: Literal["RefundUpdate"]


class IssuedRefundUpdate(BaseModel):
    r"""pydantic model IssuedRefundUpdate: Data related to the issued refund that should be updated.
    Attributes:
        risk_id(constr(max_length=200)): The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
        refund_details(Optional[IssuedRefundUpdateDetails], optional): --
        type(Literal["IssuedRefundUpdate"]): --

    """
    risk_id: constr(max_length=200) = Field(..., example='123456789')
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """
    refund_details: Optional[IssuedRefundUpdateDetails] = None
    type: Literal["IssuedRefundUpdate"]


class SettledRefundUpdate(BaseModel):
    r"""pydantic model SettledRefundUpdate: Data related to the settled refund that should be updated.
    Attributes:
        risk_id(constr(max_length=200)): The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
        refund_details(Optional[SettledRefundUpdateDetails], optional): --
        type(Literal["SettledRefundUpdate"]): --

    """
    risk_id: constr(max_length=200) = Field(..., example='123456789')
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """
    refund_details: Optional[SettledRefundUpdateDetails] = None
    type: Literal["SettledRefundUpdate"]


class PaymentUpdate(BaseModel):
    r"""pydantic model PaymentUpdate: Payment related data that should be updated.
    Attributes:
        risk_id(constr(max_length=200)): The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
        merchant_order_code(constr(max_length=200)): Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.
        type(Literal["PaymentUpdate"]): --

    """
    risk_id: constr(max_length=200) = Field(..., example='123456789')
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """
    merchant_order_code: constr(max_length=200)
    """
    Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.
    """
    type: Literal["PaymentUpdate"]


class Air(BaseModel):
    r"""pydantic model Air
    Attributes:
        price(Amount): --
        inventory_type(constr(max_length=30)): Type of inventory.
        inventory_source(InventorySource): Identifies the business model through which the supply is being sold. Merchant/Agency.
        travelers_references(List[constr(max_length=50)]): List of travelerGuids who are part of the traveling party on the order for the product.
        departure_time(datetime): Local date and time of departure from original departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        arrival_time(datetime): Local date and time of arrival to final destination location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        air_segments(List[AirSegment]): Additional airline and flight details for each of the trip segments.
        flight_type(Optional[FlightType], optional): Identifies the type of air trip based on the air destinations.
        passenger_name_record(Optional[constr(max_length=100)], optional): Airline booking confirmation code for the trip.
        global_distribution_system_type(Optional[constr(max_length=100)], optional): Associated with Passenger Name Record (PNR).
        type(Literal["Air"]): --

    """
    price: Amount
    inventory_type: constr(max_length=30)
    """
    Type of inventory.
    """
    inventory_source: InventorySource
    """
    Identifies the business model through which the supply is being sold. Merchant/Agency.
    """
    travelers_references: List[constr(max_length=50)] = Field(..., maxItems=40, minItems=1)
    """
    List of travelerGuids who are part of the traveling party on the order for the product.
    """
    departure_time: datetime
    """
    Local date and time of departure from original departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    arrival_time: datetime
    """
    Local date and time of arrival to final destination location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    air_segments: List[AirSegment] = Field(..., maxItems=30, minItems=1)
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
    type: Literal["Air"]


class Cruise(BaseModel):
    r"""pydantic model Cruise
    Attributes:
        price(Amount): --
        inventory_type(constr(max_length=30)): Type of inventory.
        inventory_source(InventorySource): Identifies the business model through which the supply is being sold. Merchant/Agency.
        travelers_references(List[constr(max_length=50)]): List of travelerGuids who are part of the traveling party on the order for the product.
        departure_time(datetime): Local date and time of departure from original departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        arrival_time(datetime): Local date and time of arrival from original arrival location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        embarkation_port(constr(max_length=200)): Location from where cruise will depart.
        disembarkation_port(constr(max_length=200)): The cruise's final destination.
        ship_name(constr(max_length=200)): Name of the cruise ship.
        type(Literal["Cruise"]): --

    """
    price: Amount
    inventory_type: constr(max_length=30)
    """
    Type of inventory.
    """
    inventory_source: InventorySource
    """
    Identifies the business model through which the supply is being sold. Merchant/Agency.
    """
    travelers_references: List[constr(max_length=50)] = Field(..., maxItems=40, minItems=1)
    """
    List of travelerGuids who are part of the traveling party on the order for the product.
    """
    departure_time: datetime
    """
    Local date and time of departure from original departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    arrival_time: datetime
    """
    Local date and time of arrival from original arrival location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    embarkation_port: constr(max_length=200)
    """
    Location from where cruise will depart.
    """
    disembarkation_port: constr(max_length=200)
    """
    The cruise's final destination.
    """
    ship_name: constr(max_length=200)
    """
    Name of the cruise ship.
    """
    type: Literal["Cruise"]


class Car(BaseModel):
    r"""pydantic model Car
    Attributes:
        price(Amount): --
        inventory_type(constr(max_length=30)): Type of inventory.
        inventory_source(InventorySource): Identifies the business model through which the supply is being sold. Merchant/Agency.
        travelers_references(List[constr(max_length=50)]): List of travelerGuids who are part of the traveling party on the order for the product.
        pick_up_location(constr(max_length=200)): Location where the automobile will be picked up.
        drop_off_location(constr(max_length=200)): Location at which the automobile will be returned.
        pickup_time(datetime): Local date and time the automobile will be picked-up, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        return_time(datetime): Local date and time the automobile will be returned, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        type(Literal["Car"]): --

    """
    price: Amount
    inventory_type: constr(max_length=30)
    """
    Type of inventory.
    """
    inventory_source: InventorySource
    """
    Identifies the business model through which the supply is being sold. Merchant/Agency.
    """
    travelers_references: List[constr(max_length=50)] = Field(..., maxItems=40, minItems=1)
    """
    List of travelerGuids who are part of the traveling party on the order for the product.
    """
    pick_up_location: constr(max_length=200)
    """
    Location where the automobile will be picked up.
    """
    drop_off_location: constr(max_length=200)
    """
    Location at which the automobile will be returned.
    """
    pickup_time: datetime
    """
    Local date and time the automobile will be picked-up, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    return_time: datetime
    """
    Local date and time the automobile will be returned, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    type: Literal["Car"]


class Hotel(BaseModel):
    r"""pydantic model Hotel
    Attributes:
        price(Amount): --
        inventory_type(constr(max_length=30)): Type of inventory.
        inventory_source(InventorySource): Identifies the business model through which the supply is being sold. Merchant/Agency.
        travelers_references(List[constr(max_length=50)]): List of travelerGuids who are part of the traveling party on the order for the product.
        hotel_id(constr(max_length=200)): Unique hotel identifier assigned by the partner.
        price_withheld(Optional[bool], optional): Identifies if the product price was withheld from the customer during the booking process.
        hotel_name(constr(max_length=200)): Name of the hotel.
        room_count(Optional[int], optional): Total number of rooms booked within the hotel product collection.
        address(Address): --
        checkin_time(datetime): Local date and time of the hotel check-in, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        checkout_time(datetime): Local date and time of the hotel check-out, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        type(Literal["Hotel"]): --

    """
    price: Amount
    inventory_type: constr(max_length=30)
    """
    Type of inventory.
    """
    inventory_source: InventorySource
    """
    Identifies the business model through which the supply is being sold. Merchant/Agency.
    """
    travelers_references: List[constr(max_length=50)] = Field(..., maxItems=40, minItems=1)
    """
    List of travelerGuids who are part of the traveling party on the order for the product.
    """
    hotel_id: constr(max_length=200) = Field(..., example='8883333999221')
    """
    Unique hotel identifier assigned by the partner.
    """
    price_withheld: Optional[bool] = None
    """
    Identifies if the product price was withheld from the customer during the booking process.
    """
    hotel_name: constr(max_length=200) = Field(..., example='Hotel Expedia')
    """
    Name of the hotel.
    """
    room_count: Optional[int] = None
    """
    Total number of rooms booked within the hotel product collection.
    """
    address: Address
    checkin_time: datetime
    """
    Local date and time of the hotel check-in, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    checkout_time: datetime
    """
    Local date and time of the hotel check-out, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    type: Literal["Hotel"]


class Insurance(BaseModel):
    r"""pydantic model Insurance
    Attributes:
        price(Amount): --
        inventory_type(constr(max_length=30)): Type of inventory.
        inventory_source(InventorySource): Identifies the business model through which the supply is being sold. Merchant/Agency.
        travelers_references(List[constr(max_length=50)]): List of travelerGuids who are part of the traveling party on the order for the product.
        type(Literal["Insurance"]): --

    """
    price: Amount
    inventory_type: constr(max_length=30)
    """
    Type of inventory.
    """
    inventory_source: InventorySource
    """
    Identifies the business model through which the supply is being sold. Merchant/Agency.
    """
    travelers_references: List[constr(max_length=50)] = Field(..., maxItems=40, minItems=1)
    """
    List of travelerGuids who are part of the traveling party on the order for the product.
    """
    type: Literal["Insurance"]


OrderPurchaseUpdateRequest = Union[OrderUpdate, ChargebackFeedback, InsultFeedback, RefundUpdate, IssuedRefundUpdate, SettledRefundUpdate, PaymentUpdate]

TravelProduct = Union[Air, Cruise, Car, Hotel, Insurance]


CancellationReason.update_forward_refs()


InsultDetail.update_forward_refs()


OrderPurchaseUpdateResponse.update_forward_refs()


ErrorDetail.update_forward_refs()


Error.update_forward_refs()


ErrorCause.update_forward_refs()


SiteInfo.update_forward_refs()


DeviceDetails.update_forward_refs()


Address.update_forward_refs()


TravelersReference.update_forward_refs()


AirSegment.update_forward_refs()


PaymentThreeDSCriteria.update_forward_refs()


Name.update_forward_refs()


Email.update_forward_refs()


Amount.update_forward_refs()


IssuedRefundUpdateDetails.update_forward_refs()


SettledRefundUpdateDetails.update_forward_refs()


ChargebackDetail.update_forward_refs()


OrderPurchaseScreenResponse.update_forward_refs()


ExtendedError.update_forward_refs()


PaymentOutcome.update_forward_refs()


Telephone.update_forward_refs()


CustomerAccount.update_forward_refs()


Traveler.update_forward_refs()


PaymentOperation.update_forward_refs()


Verify.update_forward_refs()


Authorize.update_forward_refs()


AuthorizeReversal.update_forward_refs()


Capture.update_forward_refs()


Refund.update_forward_refs()


Operations.update_forward_refs()


Payment.update_forward_refs()


CreditCard.update_forward_refs()


PayPal.update_forward_refs()


Points.update_forward_refs()


OrderPurchaseScreenRequest.update_forward_refs()


OrderPurchaseTransaction.update_forward_refs()


TransactionDetails.update_forward_refs()


OrderUpdate.update_forward_refs()


ChargebackFeedback.update_forward_refs()


InsultFeedback.update_forward_refs()


RefundUpdate.update_forward_refs()


IssuedRefundUpdate.update_forward_refs()


SettledRefundUpdate.update_forward_refs()


PaymentUpdate.update_forward_refs()


Air.update_forward_refs()


Cruise.update_forward_refs()


Car.update_forward_refs()


Hotel.update_forward_refs()


Insurance.update_forward_refs()
