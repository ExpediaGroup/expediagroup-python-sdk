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
    """pydantic model UpdateType: Transaction type associated with the update event.
    Attributes:
        ORDER_UPDATE(Any, True): --
        CHARGEBACK_FEEDBACK(Any, True): --
        INSULT_FEEDBACK(Any, True): --
        REFUND_UPDATE(Any, True): --
        PAYMENT_UPDATE(Any, True): --

    """

    ORDER_UPDATE: Any = 'ORDER_UPDATE'
    CHARGEBACK_FEEDBACK: Any = 'CHARGEBACK_FEEDBACK'
    INSULT_FEEDBACK: Any = 'INSULT_FEEDBACK'
    REFUND_UPDATE: Any = 'REFUND_UPDATE'
    PAYMENT_UPDATE: Any = 'PAYMENT_UPDATE'


class CancellationReason(BaseModel):
    """pydantic model CancellationReason: Reason of order update cancellation.
    Attributes:
        primary_reason_code(Optional[constr(max_length=200)], False): Primary cancellation reason code.
        sub_reason_code(Optional[constr(max_length=200)], False): Substitute cancellation reason code.
        primary_reason_description(constr(max_length=200), True): Primary cancellation reason code. Required if `order_status = CANCELLED`.
        sub_reason_description(Optional[constr(max_length=200)], False): Substitute cancellation reason description.

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


class ChargebackReason(Enum):
    """pydantic model ChargebackReason: Reason for chargeback which can be `Fraud` or `Non Fraud`.
    Attributes:
        FRAUD(Any, True): --
        NON_FRAUD(Any, True): --

    """

    FRAUD: Any = 'FRAUD'
    NON_FRAUD: Any = 'NON_FRAUD'


class ChargebackDetail(BaseModel):
    """pydantic model ChargebackDetail: Details related to the chargeback.
    Attributes:
        chargeback_reason(ChargebackReason, True): Reason for chargeback which can be `Fraud` or `Non Fraud`.
        chargeback_amount(float, True): Chargeback amount received by the partner.
        currency_code(constr(regex=r'^[A-Z]{3}$', max_length=200), True): The 3-letter currency code defined in ISO 4217. https://www.currency-iso.org/dam/downloads/lists/list_one.xml.
        bank_reason_code(Optional[constr(max_length=200)], False): Unique code provided by the acquiring bank for the category of fraud.
        chargeback_reported_timestamp(Optional[datetime], False): Date and time when the chargeback was reported to the partner, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

    """

    chargeback_reason: ChargebackReason
    """
    Reason for chargeback which can be `Fraud` or `Non Fraud`.
    """
    chargeback_amount: float
    """
    Chargeback amount received by the partner.
    """
    currency_code: constr(regex=r'^[A-Z]{3}$', max_length=200)
    """
    The 3-letter currency code defined in ISO 4217. https://www.currency-iso.org/dam/downloads/lists/list_one.xml.
    """
    bank_reason_code: Optional[constr(max_length=200)] = None
    """
    Unique code provided by the acquiring bank for the category of fraud.
    """
    chargeback_reported_timestamp: Optional[datetime] = None
    """
    Date and time when the chargeback was reported to the partner, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """


class InsultDetail(BaseModel):
    """pydantic model InsultDetail: Details related to the insult.
    Attributes:
        insult_reported_timestamp(Optional[datetime], False): Date and time when the insult was reported to the partner, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

    """

    insult_reported_timestamp: Optional[datetime] = None
    """
    Date and time when the insult was reported to the partner, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """


class Status(Enum):
    """pydantic model Status: Defines the current state of the Order.
    Attributes:
        COMPLETED(Any, True): --
        CHANGE_COMPLETED(Any, True): --
        CANCELLED(Any, True): --
        FAILED(Any, True): --
        CHANGE_FAILED(Any, True): --

    """

    COMPLETED: Any = 'COMPLETED'
    CHANGE_COMPLETED: Any = 'CHANGE_COMPLETED'
    CANCELLED: Any = 'CANCELLED'
    FAILED: Any = 'FAILED'
    CHANGE_FAILED: Any = 'CHANGE_FAILED'


class FraudDecision(Enum):
    """pydantic model FraudDecision
    Attributes:
        ACCEPT(Any, True): --
        REVIEW(Any, True): --
        REJECT(Any, True): --

    """

    ACCEPT: Any = 'ACCEPT'
    REVIEW: Any = 'REVIEW'
    REJECT: Any = 'REJECT'


class ErrorDetail(BaseModel):
    """pydantic model ErrorDetail: Error details in case of any errors.
    Attributes:
        code(Optional[int], False): --
        message(Optional[constr(max_length=200)], False): Description of the error. Clients may choose to use the description field to display to end clients.
        detailed_message(Optional[constr(max_length=500)], False): Detailed description of the error.

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
    """pydantic model Error: The object used the describe an error, containing both human-readable and in a machine-readable information.
    Attributes:
        type(AnyUrl, True): A URI reference, compliant with the standard EG error type format, which identifies the error type. It provides a machine-readable identifier for the error type. The error type will be aligned with the HTTP status code of the response. The URI can either be absolute or relative to the API's base URI. When dereferenced, it can also provide human-readable documentation for the error type.

        detail(str, True): A human-readable explanation of the error, specific to this error occurrence.

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
    """pydantic model Location: The location of the element in the request that identifies this specific cause. When specified, the `name` will be specified and when applicable, the `value` as well. Can be one of:
    * `HEADER` - When an error has been identified in one of the request headers.
    * `PATH` - When an error has been identified in one of the path parameters.
    * `QUERY` - When an error has been identified in one of the query parameters.
    * `BODY` - When an error has been identified in the request body.

        Attributes:
            HEADER(Any, True): --
            PATH(Any, True): --
            QUERY(Any, True): --
            BODY(Any, True): --

    """

    HEADER: Any = 'HEADER'
    PATH: Any = 'PATH'
    QUERY: Any = 'QUERY'
    BODY: Any = 'BODY'


class ErrorCause(BaseModel):
    """pydantic model ErrorCause: The object used to describe a cause for an error, containing both human-readable and in a machine-readable information.
        Attributes:
            type(AnyUrl, True): A URI reference, compliant with the standard EG error type format, which identifies the cause type. It provides a machine-readable identifier for the cause type. The cause type will be aligned with the error type. The URI can either be absolute or relative to the API's base URI. When dereferenced, it provides human-readable documentation for the cause type.

            detail(str, True): A human-readable explanation of the cause, specific to this cause occurrence.
            location(Optional[Location], False): The location of the element in the request that identifies this specific cause. When specified, the `name` will be specified and when applicable, the `value` as well. Can be one of:
    * `HEADER` - When an error has been identified in one of the request headers.
    * `PATH` - When an error has been identified in one of the path parameters.
    * `QUERY` - When an error has been identified in one of the query parameters.
    * `BODY` - When an error has been identified in the request body.

            name(Optional[str], False): The name of the element for this cause. When specified, the `location` will be specified and when applicable, the `value` as well. This name is a function of the value of the `location` property:
      * When the `location` is set to `HEADER`, this will be the name of the request header (e.g. `Content-Type`).
      * When the `location` is set to `PATH`, this will be the name of the path parameter (e.g. in a path defined as `/users/{user_id}`, the value would be `user_id`).
      * When the `location` is set to `QUERY`, this will be the name of the query string parameter (e.g. `offset`).
      * When the `location` is set to `BODY`, this will one of the field names specified in the body of the request.
        * For a top level field, it should only be set to the field name (e.g. `firstName`).
        * For a field in a nested object, it may contain the path to reach the field (e.g. `address.city`).
        * For a field in an object part of collection, it may contain the index in the collection (e.g. `permissions[0].name`).

            value(Optional[str], False): A string representation of the erroneous value of the element identified in `name`, perceived to be the cause of the error. When specified, the `location` and `name` should be specified as well. This value may be omitted in cases where it cannot be provided (e.g. missing require field), or the erroneous value cannot be represented as a string.


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
    """pydantic model SiteInfo
    Attributes:
        country_code(constr(regex=r'^[A-Z]{3}$'), True): The alpha-3 ISO code that represents a country name.
        agent_assisted(bool, True): Identifies if an agent assisted in booking travel for the customer. `False` if the order was directly booked by customer.

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
    """pydantic model DeviceDetails
    Attributes:
        source(Optional[constr(max_length=50)], False): Source of the device_box. Default value is `TrustWidget`.
        device_box(constr(max_length=16000), True): Device related information retrieved from TrustWidget.
        ip_address(Optional[constr(regex=r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$')], False): IP address of the device used for booking.

    """

    source: Optional[constr(max_length=50)] = None
    """
    Source of the device_box. Default value is `TrustWidget`.
    """
    device_box: constr(max_length=16000)
    """
    Device related information retrieved from TrustWidget.
    """
    ip_address: Optional[
        constr(regex=r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$')
    ] = Field(None, example='192.168.32.48')
    """
    IP address of the device used for booking.
    """


class CurrentOrderStatus(Enum):
    """pydantic model CurrentOrderStatus: Status of the order.
    Attributes:
        IN_PROGRESS(Any, True): --
        COMPLETED(Any, True): --

    """

    IN_PROGRESS: Any = 'IN_PROGRESS'
    COMPLETED: Any = 'COMPLETED'


class OrderType(Enum):
    """pydantic model OrderType: Type of order. Possible `order_types`.

    `CREATE` - Initial type of a brand new order.

    `CHANGE` - If a `OrderPurchaseScreenRequest` has already been submitted for the initial booking with `order_type = CREATE`, but has now been modified and partner wishes to resubmit for Fraud screening then the `order_type = CHANGE`. Examples of changes that are supported are changes made to `check-in/checkout dates` or `price of a TravelProduct`.

        Attributes:
            CREATE(Any, True): --
            CHANGE(Any, True): --

    """

    CREATE: Any = 'CREATE'
    CHANGE: Any = 'CHANGE'


class AccountType(Enum):
    """pydantic model AccountType: Identifies if the customer account is known to the client. Possible values are:

    -`GUEST` - Applicable if the partner maintains record to distinguish whether the transaction was booked via a guest account.

    -`STANDARD` - Default account type.

        Attributes:
            GUEST(Any, True): --
            STANDARD(Any, True): --

    """

    GUEST: Any = 'GUEST'
    STANDARD: Any = 'STANDARD'


class AddressType(Enum):
    """pydantic model AddressType
    Attributes:
        HOME(Any, True): --
        WORK(Any, True): --

    """

    HOME: Any = 'HOME'
    WORK: Any = 'WORK'


class Address(BaseModel):
    """pydantic model Address
    Attributes:
        address_type(Optional[AddressType], False): --
        address_line1(constr(max_length=200), True): Address line 1 of the address provided.
        address_line2(Optional[constr(max_length=200)], False): Address line 2 of the address provided.
        city(constr(max_length=200), True): City of the address provided.
        state(constr(regex=r'^[A-Z]{2}$'), True): The two-characters ISO code for the state or province of the address.
        zip_code(constr(max_length=20), True): Zip code of the address provided.
        country_code(constr(regex=r'^[A-Z]{3}$'), True): ISO alpha-3 country code of the address provided.

    """

    address_type: Optional[AddressType] = None
    address_line1: constr(max_length=200)
    """
    Address line 1 of the address provided.
    """
    address_line2: Optional[constr(max_length=200)] = None
    """
    Address line 2 of the address provided.
    """
    city: constr(max_length=200)
    """
    City of the address provided.
    """
    state: constr(regex=r'^[A-Z]{2}$')
    """
    The two-characters ISO code for the state or province of the address.
    """
    zip_code: constr(max_length=20)
    """
    Zip code of the address provided.
    """
    country_code: constr(regex=r'^[A-Z]{3}$')
    """
    ISO alpha-3 country code of the address provided.
    """


class InventorySource(Enum):
    """pydantic model InventorySource: Identifies the business model through which the supply is being sold. Merchant/Agency.
    Attributes:
        MERCHANT(Any, True): --
        AGENCY(Any, True): --

    """

    MERCHANT: Any = 'MERCHANT'
    AGENCY: Any = 'AGENCY'


class TravelersReference(BaseModel):
    """pydantic model TravelersReference
    Attributes:
        __root__(constr(max_length=50), True): --

    """

    __root__: constr(max_length=50)


class FlightType(Enum):
    """pydantic model FlightType: Identifies the type of air trip based on the air destinations.
    Attributes:
        ROUNDTRIP(Any, True): --
        ONEWAY(Any, True): --
        MULTIPLE_DESTINATION(Any, True): --

    """

    ROUNDTRIP: Any = 'ROUNDTRIP'
    ONEWAY: Any = 'ONEWAY'
    MULTIPLE_DESTINATION: Any = 'MULTIPLE_DESTINATION'


class AirSegment(BaseModel):
    """pydantic model AirSegment
    Attributes:
        airline_code(constr(max_length=10), True): Airline code of the trip segment
        departure_airport_code(constr(max_length=10), True): Departure airport of the trip segment
        arrival_airport_code(constr(max_length=10), True): Arrival airport of the trip segment
        departure_time(Optional[datetime], False): Local date and time of departure from departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        arrival_time(Optional[datetime], False): Local date and time of arrival to destination location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

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


class PaymentThreeDSCriteria(BaseModel):
    """pydantic model PaymentThreeDSCriteria: Payment 3DS criteria attributes.
    Attributes:
        probable_flag(Optional[bool], False): This is a flag passed that indicates that this transaction could potentially go through 3DS.
        transaction_model(Optional[constr(max_length=200)], False): Model used to process payment transaction.

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
    """pydantic model PaymentReason: The reason of payment. Possible values:
    - `FULL` - If the amount is paid i full for the order
    - `DEPOSIT` - The initial payment. Amount to be paid up front.
    - `SCHEDULED` - The amount to be payment based on a schedule for the remaining portion of the booking amount.
    - `SUBSEQUENT` - An additional amount paid that was not originally scheduled.
    - `DEFERRED`

        Attributes:
            FULL(Any, True): --
            DEPOSIT(Any, True): --
            SCHEDULED(Any, True): --
            SUBSEQUENT(Any, True): --
            DEFERRED(Any, True): --

    """

    FULL: Any = 'FULL'
    DEPOSIT: Any = 'DEPOSIT'
    SCHEDULED: Any = 'SCHEDULED'
    SUBSEQUENT: Any = 'SUBSEQUENT'
    DEFERRED: Any = 'DEFERRED'


class VerificationType(Enum):
    """pydantic model VerificationType: The type of the verification used to verify the instrument. If the Card Verfication Value was provided to verify the credit card used for the transaction, `type = CVV`.
    Attributes:
        CVV(Any, True): --
        field_3DS(Any, True): --

    """

    CVV: Any = 'CVV'
    field_3DS: Any = '3DS'


class PaymentStatus(Enum):
    """pydantic model PaymentStatus: The status of the payment operation.
    Attributes:
        COMPLETED(Any, True): --
        FAILED(Any, True): --

    """

    COMPLETED: Any = 'COMPLETED'
    FAILED: Any = 'FAILED'


class PaymentMethod(Enum):
    """pydantic model PaymentMethod: The payment method used at the time of purchase for the transaction. Supported `method`'s are: `CREDIT_CARD`, `PAYPAL`, `POINTS`.
    Attributes:
        CREDIT_CARD(Any, True): --
        PAYPAL(Any, True): --
        POINTS(Any, True): --

    """

    CREDIT_CARD: Any = 'CREDIT_CARD'
    PAYPAL: Any = 'PAYPAL'
    POINTS: Any = 'POINTS'


class Name(BaseModel):
    """pydantic model Name: Group of attributes intended to hold information about a customer or traveler's name for the order.
    Attributes:
        last_name(constr(max_length=200), True): Surname, or last name, of the person.
        first_name(constr(max_length=200), True): Given, or first name, of the person.
        middle_name(Optional[constr(max_length=200)], False): Middle name of the person.
        title(Optional[constr(max_length=200)], False): Title of the person for name (e.g. Mr., Ms. etc).
        suffix(Optional[constr(max_length=50)], False): Generational designations (e.g. Sr, Jr, III) or values that indicate the individual holds a position, educational degree, accreditation, office, or honor (e.g. PhD, CCNA, OBE).
        full_name(Optional[constr(max_length=500)], False): Full name of the person that includes title, first_name, middle_name, last_name, suffix.

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
    full_name: Optional[constr(max_length=500)] = Field(None, example='Sally Expedia')
    """
    Full name of the person that includes title, first_name, middle_name, last_name, suffix.
    """


class TelephoneType(Enum):
    """pydantic model TelephoneType: Classification of the phone (e.g. `Home`, `Mobile`).
    Attributes:
        HOME(Any, True): --
        MOBILE(Any, True): --
        BUSINESS(Any, True): --
        FAX(Any, True): --
        OTHER(Any, True): --

    """

    HOME: Any = 'HOME'
    MOBILE: Any = 'MOBILE'
    BUSINESS: Any = 'BUSINESS'
    FAX: Any = 'FAX'
    OTHER: Any = 'OTHER'


class TelephonePlatformType(Enum):
    """pydantic model TelephonePlatformType: Classification of the phone platform.
    Attributes:
        MOBILE(Any, True): --
        LANDLINE(Any, True): --
        VOIP(Any, True): --

    """

    MOBILE: Any = 'MOBILE'
    LANDLINE: Any = 'LANDLINE'
    VOIP: Any = 'VOIP'


class Email(BaseModel):
    """pydantic model Email: Group of attributes intended to hold information about email address associated with the transaction.
    Attributes:
        email_address(Optional[EmailStr], False): Full email address including the alias, @ symbol, domain, and root domain.

    """

    email_address: Optional[EmailStr] = None
    """
    Full email address including the alias, @ symbol, domain, and root domain.
    """


class Amount(BaseModel):
    """pydantic model Amount
    Attributes:
        value(float, True): The amount required in payment for the product/order in local currency.
        currency_code(constr(regex=r'^[A-Z]{3}$', max_length=3), True): The ISO  alpha-3 country code for the amount currency.

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
    """pydantic model ContentType
    Attributes:
        application_json(Any, True): --

    """

    application_json: Any = 'application/json'


class ContentType1(Enum):
    """pydantic model ContentType1
    Attributes:
        application_json(Any, True): --

    """

    application_json: Any = 'application/json'


class ContentType2(Enum):
    """pydantic model ContentType2
    Attributes:
        application_json(Any, True): --

    """

    application_json: Any = 'application/json'


class ContentType3(Enum):
    """pydantic model ContentType3
    Attributes:
        application_json(Any, True): --

    """

    application_json: Any = 'application/json'


class ContentType4(Enum):
    """pydantic model ContentType4
    Attributes:
        application_json(Any, True): --

    """

    application_json: Any = 'application/json'


class ContentType5(Enum):
    """pydantic model ContentType5
    Attributes:
        application_json(Any, True): --

    """

    application_json: Any = 'application/json'


class OrderPurchaseScreenResponse(BaseModel):
    """pydantic model OrderPurchaseScreenResponse
    Attributes:
        risk_id(Optional[constr(max_length=200)], False): --
        decision(Optional[FraudDecision], False): --
        error_detail(Optional[ErrorDetail], False): --

    """

    risk_id: Optional[constr(max_length=200)] = Field(None, example='1234567')
    decision: Optional[FraudDecision] = None
    error_detail: Optional[ErrorDetail] = None


class ExtendedError(BaseModel):
    """pydantic model ExtendedError: The object used the describe an error, containing both human-readable and in a machine-readable information.
    Attributes:
        type(AnyUrl, True): A URI reference, compliant with the standard EG error type format, which identifies the error type. It provides a machine-readable identifier for the error type. The error type will be aligned with the HTTP status code of the response. The URI can either be absolute or relative to the API's base URI. When dereferenced, it can also provide human-readable documentation for the error type.

        detail(str, True): A human-readable explanation of the error, specific to this error occurrence.
        causes(Optional[List[ErrorCause]], False): An array of cause objects, that identify the specific causes of the error.

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
    """pydantic model PaymentOutcome
    Attributes:
        status(Optional[PaymentStatus], False): --
        code(Optional[constr(max_length=200)], False): A mnemonic code for the payment processing.
        description(Optional[constr(max_length=200)], False): A short description providing additional explanation regarding the mnemonic code.

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
    """pydantic model Telephone: Group of attributes intended to hold information about phone number associated with the transaction.  A user can have one to many phone numbers (home, work, mobile, etc.).
    Attributes:
        type(Optional[TelephoneType], False): --
        platform_type(Optional[TelephonePlatformType], False): --
        country_access_code(constr(regex=r'^[0-9]{1,3}$', max_length=3), True): Numeric digit between 1 to 3 characters used to represent the country code for international dialing.  Does not include symbols, spaces, or leading zeros.
        area_code(constr(regex=r'^[0-9]{1,20}$', max_length=20), True): A number prefixed to an individual telephone number: used in making long-distance calls.  Does not include symbols, spaces, or leading zeros.
        phone_number(constr(regex=r'^[0-9]{1,50}$', max_length=50), True): A number that is dialed on a telephone, without the country or area codes, to reach a particular person, business, etc.  Does not include symbols, spaces, or leading zeros.
        full_phone_number(Optional[constr(regex=r'^[0-9]{1,100}$', max_length=100)], False): The concatenated countryAccessCode, areaCode, and phoneNumber with leading zeros from the original fields and symbols  (-,.+) removed.  It does not include a phone extension.
        extension_number(Optional[constr(regex=r'^[0-9]{1,20}$', max_length=20)], False): The number used to reach an individual once a phone connection is established.  Does not include symbols, spaces, or leading zeros.
        preference_rank(Optional[float], False): Ranking of order of user preference for contact via text (if type is Mobile) or voice.  `0` means no preference.  `1` is the primary phone, `2` is the secondary phone, etc.
        last_verified_timestamp(Optional[datetime], False): Local date and time user validated possession of their phone number via a text or voice multi factor authentication challenge, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        verified_flag(Optional[bool], False): Flag indicating whether user passed validation of possession of their phone number via a text or voice multi factor authentication challenge.

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
    full_phone_number: Optional[constr(regex=r'^[0-9]{1,100}$', max_length=100)] = Field(None, example='12345689')
    """
    The concatenated countryAccessCode, areaCode, and phoneNumber with leading zeros from the original fields and symbols  (-,.+) removed.  It does not include a phone extension.
    """
    extension_number: Optional[constr(regex=r'^[0-9]{1,20}$', max_length=20)] = Field(None, example='89')
    """
    The number used to reach an individual once a phone connection is established.  Does not include symbols, spaces, or leading zeros.
    """
    preference_rank: Optional[float] = None
    """
    Ranking of order of user preference for contact via text (if type is Mobile) or voice.  `0` means no preference.  `1` is the primary phone, `2` is the secondary phone, etc.
    """
    last_verified_timestamp: Optional[datetime] = None
    """
    Local date and time user validated possession of their phone number via a text or voice multi factor authentication challenge, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
    """
    verified_flag: Optional[bool] = None
    """
    Flag indicating whether user passed validation of possession of their phone number via a text or voice multi factor authentication challenge.
    """


class CustomerAccount(BaseModel):
    """pydantic model CustomerAccount
        Attributes:
            user_id(Optional[str], False): Unique identifier assigned to the account owner by the partner. `user_id` is specific to the partner namespace
            account_type(AccountType, True): Identifies if the customer account is known to the client. Possible values are:

    -`GUEST` - Applicable if the partner maintains record to distinguish whether the transaction was booked via a guest account.

    -`STANDARD` - Default account type.

            name(Name, True): --
            email_address(EmailStr, True): Email address for the account owner.
            telephones(Optional[List[Telephone]], False): --
            address(Optional[Address], False): --
            registered_time(Optional[datetime], False): The local date and time that the customer first registered on the client site, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.

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
    """pydantic model Traveler
    Attributes:
        traveler_name(Name, True): --
        email_address(Optional[EmailStr], False): Email address associated with the traveler as supplied by the partner system.
        telephones(Optional[List[Telephone]], False): --
        primary(bool, True): Indicator for one of the travelers who is the primary traveler. One traveler in each itinerary item must be listed as primary. By default, for a single traveler this should be set to `true`.
        age(Optional[float], False): Age of the traveler.
        birth_date(Optional[datetime], False): Date of birth for traveler, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        citizenship_country_code(Optional[constr(regex=r'^[A-Z]{3}$', min_length=3, max_length=3)], False): The alpha-3 ISO country code of the traveler's nationality.
        traveler_id(Optional[constr(max_length=100)], False): A unique identifier for travelers in the transaction.

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
    """pydantic model PaymentOperation
    Attributes:
        id(Optional[constr(max_length=200)], False): --
        amount(Optional[Amount], False): --
        outcome(Optional[PaymentOutcome], False): --

    """

    id: Optional[constr(max_length=200)] = None
    amount: Optional[Amount] = None
    outcome: Optional[PaymentOutcome] = None


class Verify(PaymentOperation):
    """pydantic model Verify: A verify operation represents the intent to verify the payment associated with this transaction.
    Attributes:
        type(Optional[VerificationType], False): --

    """

    type: Optional[VerificationType] = None


class Authorize(PaymentOperation):
    """pydantic model Authorize: Authorize operation on the payment. An authorize operation represents placing the funds on hold with the specified form of payment."""

    pass


class AuthorizeReversal(PaymentOperation):
    """pydantic model AuthorizeReversal: Authorize Reversal operation on the payment. An authorize reversal operation represents a notification received usually from a 3rd party payment processor to indicate that an authorization hold should be released as a result of a sale being partially or completely cancelled."""

    pass


class Capture(PaymentOperation):
    """pydantic model Capture: Capture operation on the payment. A capture operation represents a notification received usually from a 3rd party payment processor to indicate that the funds placed on hold will be captured and the funds transfer process will occur from the customer's funds to the merchant's funds."""

    pass


class Refund(PaymentOperation):
    """pydantic model Refund: Refund operation on the payment. A refund operation represents the intent to refund a previous charge."""

    pass


class Operations(BaseModel):
    """pydantic model Operations: All operations related to a payment throughout its lifespan. An operation represents an event external to Fraud Prevention Service that specifies to perform a payment operation. Possible operation types include:

    - `Verify`

    - `Authorize`

    - `AuthorizeReversal`

    - `Capture`

    - `Refund`

        Attributes:
            verify(Optional[Verify], False): --
            authorize(Optional[Authorize], False): --
            authorize_reversal(Optional[AuthorizeReversal], False): --
            capture(Optional[Capture], False): --
            refunds(Optional[List[Refund]], False): --

    """

    verify: Optional[Verify] = None
    authorize: Optional[Authorize] = None
    authorize_reversal: Optional[AuthorizeReversal] = None
    capture: Optional[Capture] = None
    refunds: Optional[List[Refund]] = Field(None, maxItems=20)


class Payment(BaseModel):
    """pydantic model Payment
    Attributes:
        brand(constr(max_length=200), True): Payment brand used for payment on this transaction.
        method(PaymentMethod, True): --
        reason(Optional[PaymentReason], False): --
        billing_name(Name, True): --
        billing_address(Optional[Address], False): --
        billing_email_address(Optional[EmailStr], False): Email address associated with the payment.
        authorized_amount(Optional[Amount], False): --
        verified_amount(Optional[Amount], False): --
        three_digits_secure_criteria(Optional[PaymentThreeDSCriteria], False): --
        operations(Optional[Operations], False): --
        total_refund_amount(Optional[float], False): Total amount refunded towards the transaction.

    """

    brand: constr(max_length=200)
    """
    Payment brand used for payment on this transaction.
    """
    method: PaymentMethod
    reason: Optional[PaymentReason] = None
    billing_name: Name
    billing_address: Optional[Address] = None
    billing_email_address: Optional[EmailStr] = None
    """
    Email address associated with the payment.
    """
    authorized_amount: Optional[Amount] = None
    verified_amount: Optional[Amount] = None
    three_digits_secure_criteria: Optional[PaymentThreeDSCriteria] = None
    operations: Optional[Operations] = None
    total_refund_amount: Optional[float] = None
    """
    Total amount refunded towards the transaction.
    """


class CreditCard(Payment):
    """pydantic model CreditCard
    Attributes:
        card_type(constr(max_length=200), True): Type of card used for payment, (eg. `CREDIT`, `DEBIT`).
        card_number(constr(max_length=200), True): All the digits (unencrypted) of the credit card number associated with the payment.
        expiry_date(Optional[datetime], False): Expiration date of the credit card used for payment.
        electronic_commerce_indicator(Optional[constr(max_length=200)], False): Electronic Commerce Indicator, a two or three digit number usually returned by a 3rd party payment processor in regards to the authentication used when gathering the cardholder's payment credentials.
        virtual_credit_card_flag(Optional[bool], False): A flag to indicate that the bank card being used for the charge is a virtual credit card.
        wallet_type(Optional[constr(max_length=200)], False): If a virtual/digital form of payment was used, the type of digital wallet should be specified here. Possible `wallet_type`'s include: `Google` or `ApplePay`.
        card_avs_response(constr(max_length=50), True): A field used to confirm if the address provided at the time of purchase matches what the bank has on file for the Credit Card.
        card_cvv_response(constr(max_length=20), True): A field used to confirm the Card Verification Value on the Credit Card matches the Credit Card used at the time of purchase.
        telephones(List[Telephone], True): Telephone(s) associated with card holder and credit card.
        merchant_order_code(Optional[constr(max_length=200)], False): Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.

    """

    card_type: constr(max_length=200)
    """
    Type of card used for payment, (eg. `CREDIT`, `DEBIT`).
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


class PayPal(Payment):
    """pydantic model PayPal
    Attributes:
        payer_id(constr(max_length=200), True): Unique PayPal Customer Account identification number.
        transaction_id(constr(max_length=200), True): Unique transaction number to identify Auth calls at PayPal.
        merchant_order_code(Optional[constr(max_length=200)], False): Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.

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
    """pydantic model Points"""

    pass


class OrderPurchaseScreenRequest(BaseModel):
    """pydantic model OrderPurchaseScreenRequest
    Attributes:
        transaction(Optional[OrderPurchaseTransaction], False): --

    """

    transaction: Optional[OrderPurchaseTransaction] = None


class OrderPurchaseTransaction(BaseModel):
    """pydantic model OrderPurchaseTransaction
    Attributes:
        site_info(SiteInfo, True): --
        device_details(DeviceDetails, True): --
        customer_account(CustomerAccount, True): --
        transaction_details(TransactionDetails, True): --
        bypass_risk_flag(Optional[bool], False): A flag to indicate whether the client is ignoring the decision by Trust validation and proceeds to process the even in-case the outcome is ‘Reject’ or ‘Review’.

    """

    site_info: SiteInfo
    device_details: DeviceDetails
    customer_account: CustomerAccount
    transaction_details: TransactionDetails
    bypass_risk_flag: Optional[bool] = None
    """
    A flag to indicate whether the client is ignoring the decision by Trust validation and proceeds to process the even in-case the outcome is ‘Reject’ or ‘Review’.
    """


class TransactionDetails(BaseModel):
    """pydantic model TransactionDetails
        Attributes:
            order_id(constr(max_length=50), True): Unique identifier assigned to the order by the partner. `order_id` is specific to the partner namespace.
            current_order_status(CurrentOrderStatus, True): Status of the order.
            order_type(OrderType, True): Type of order. Possible `order_types`.

    `CREATE` - Initial type of a brand new order.

    `CHANGE` - If a `OrderPurchaseScreenRequest` has already been submitted for the initial booking with `order_type = CREATE`, but has now been modified and partner wishes to resubmit for Fraud screening then the `order_type = CHANGE`. Examples of changes that are supported are changes made to `check-in/checkout dates` or `price of a TravelProduct`.

            travel_products(List[TravelProduct], True): --
            travelers(List[Traveler], True): Individuals who are part of the travel party for the order. At minimum there must be at least `1` traveler.
            payments(List[Payment], True): List of the form(s) of payment being used to purchase the order.  One or more forms of payment can be used within an order. Information gathered will be specific to the form of payment.
            credit_card_authentication_failure_count(Optional[int], False): Total authentication failure count for given credit card. Authentication failures happen when a cardholder enters their card information incorrectly.

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
    credit_card_authentication_failure_count: Optional[int] = None
    """
    Total authentication failure count for given credit card. Authentication failures happen when a cardholder enters their card information incorrectly.
    """


class OrderUpdate(BaseModel):
    """pydantic model OrderUpdate
    Attributes:
        risk_id(constr(max_length=200), True): The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
        order_status(Status, True): --
        cancellation_reason(Optional[CancellationReason], False): --
        type(Literal["OrderUpdate"], True): --

    """

    risk_id: constr(max_length=200) = Field(..., example='123456789')
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """
    order_status: Status
    cancellation_reason: Optional[CancellationReason] = None
    type: Literal["OrderUpdate"]


class ChargebackFeedback(BaseModel):
    """pydantic model ChargebackFeedback
    Attributes:
        risk_id(constr(max_length=200), True): The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
        chargeback_detail(Optional[ChargebackDetail], False): --
        type(Literal["ChargebackFeedback"], True): --

    """

    risk_id: constr(max_length=200) = Field(..., example='123456789')
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """
    chargeback_detail: Optional[ChargebackDetail] = None
    type: Literal["ChargebackFeedback"]


class InsultFeedback(BaseModel):
    """pydantic model InsultFeedback
    Attributes:
        risk_id(constr(max_length=200), True): The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
        insult_detail(Optional[InsultDetail], False): --
        type(Literal["InsultFeedback"], True): --

    """

    risk_id: constr(max_length=200) = Field(..., example='123456789')
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """
    insult_detail: Optional[InsultDetail] = None
    type: Literal["InsultFeedback"]


class RefundUpdate(BaseModel):
    """pydantic model RefundUpdate
    Attributes:
        risk_id(constr(max_length=200), True): The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
        acquirer_reference_number(constr(max_length=200), True): A unique number that tags a credit or debit card transaction when it goes from the merchant's bank through to the cardholder's bank.
        refund_deposit_timestamp(datetime, True): Date and time when the refund was deposited to the original form of payment.
        refund_settlement_timestamp(datetime, True): Date and time when the 3rd party payment processor confirmed that a previously submitted payment refund has settled at the participating financial institutions.
        settlement_id(constr(max_length=200), True): Unique settlement identifier generated for a previously submitted payment refund.
        refund_amount(Amount, True): --
        type(Literal["RefundUpdate"], True): --

    """

    risk_id: constr(max_length=200) = Field(..., example='123456789')
    """
    The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
    """
    acquirer_reference_number: constr(max_length=200)
    """
    A unique number that tags a credit or debit card transaction when it goes from the merchant's bank through to the cardholder's bank.
    """
    refund_deposit_timestamp: datetime
    """
    Date and time when the refund was deposited to the original form of payment.
    """
    refund_settlement_timestamp: datetime
    """
    Date and time when the 3rd party payment processor confirmed that a previously submitted payment refund has settled at the participating financial institutions.
    """
    settlement_id: constr(max_length=200)
    """
    Unique settlement identifier generated for a previously submitted payment refund.
    """
    refund_amount: Amount
    type: Literal["RefundUpdate"]


class PaymentUpdate(BaseModel):
    """pydantic model PaymentUpdate
    Attributes:
        risk_id(constr(max_length=200), True): The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.
        merchant_order_code(constr(max_length=200), True): Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.
        type(Literal["PaymentUpdate"], True): --

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


OrderPurchaseUpdateRequest = Union[
    OrderUpdate,
    ChargebackFeedback,
    InsultFeedback,
    RefundUpdate,
    PaymentUpdate,
]


class Air(BaseModel):
    """pydantic model Air
    Attributes:
        price(Amount, True): --
        inventory_type(constr(max_length=30), True): Type of inventory.
        inventory_source(InventorySource, True): Identifies the business model through which the supply is being sold. Merchant/Agency.
        travelers_references(List[constr(max_length=50)], True): List of travelerGuids who are part of the traveling party on the order for the product.
        departure_time(datetime, True): Local date and time of departure from original departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        arrival_time(datetime, True): Local date and time of arrival to final destination location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        air_segments(List[AirSegment], True): Additional airline and flight details for each of the trip segments.
        flight_type(Optional[FlightType], False): Identifies the type of air trip based on the air destinations.
        passenger_name_record(Optional[constr(max_length=100)], False): Airline booking confirmation code for the trip.
        global_distribution_system_type(Optional[constr(max_length=100)], False): Associated with Passenger Name Record (PNR).
        type(Literal["Air"], True): Type of product advertised on the website.

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
    """
    Type of product advertised on the website.
    """


class Cruise(BaseModel):
    """pydantic model Cruise
    Attributes:
        price(Amount, True): --
        inventory_type(constr(max_length=30), True): Type of inventory.
        inventory_source(InventorySource, True): Identifies the business model through which the supply is being sold. Merchant/Agency.
        travelers_references(List[constr(max_length=50)], True): List of travelerGuids who are part of the traveling party on the order for the product.
        departure_time(datetime, True): Local date and time of departure from original departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        arrival_time(datetime, True): Local date and time of arrival from original arrival location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        embarkation_port(constr(max_length=200), True): Location from where cruise will depart.
        disembarkation_port(constr(max_length=200), True): The cruise's final destination.
        ship_name(constr(max_length=200), True): Name of the cruise ship.
        type(Literal["Cruise"], True): Type of product advertised on the website.

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
    """
    Type of product advertised on the website.
    """


class Car(BaseModel):
    """pydantic model Car
    Attributes:
        price(Amount, True): --
        inventory_type(constr(max_length=30), True): Type of inventory.
        inventory_source(InventorySource, True): Identifies the business model through which the supply is being sold. Merchant/Agency.
        travelers_references(List[constr(max_length=50)], True): List of travelerGuids who are part of the traveling party on the order for the product.
        pick_up_location(constr(max_length=200), True): Location where the automobile will be picked up.
        drop_off_location(constr(max_length=200), True): Location at which the automobile will be returned.
        pickup_time(datetime, True): Local date and time the automobile will be picked-up, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        return_time(datetime, True): Local date and time the automobile will be returned, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        type(Literal["Car"], True): Type of product advertised on the website.

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
    """
    Type of product advertised on the website.
    """


class Hotel(BaseModel):
    """pydantic model Hotel
    Attributes:
        price(Amount, True): --
        inventory_type(constr(max_length=30), True): Type of inventory.
        inventory_source(InventorySource, True): Identifies the business model through which the supply is being sold. Merchant/Agency.
        travelers_references(List[constr(max_length=50)], True): List of travelerGuids who are part of the traveling party on the order for the product.
        hotel_id(constr(max_length=200), True): Unique hotel identifier assigned by the partner.
        price_withheld(Optional[bool], False): Identifies if the product price was withheld from the customer during the booking process.
        hotel_name(constr(max_length=200), True): Name of the hotel.
        room_count(Optional[int], False): Total number of rooms booked within the hotel product collection.
        address(Address, True): --
        checkin_time(datetime, True): Local date and time of the hotel check-in, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        checkout_time(datetime, True): Local date and time of the hotel check-out, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.
        type(Literal["Hotel"], True): Type of product advertised on the website.

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
    """
    Type of product advertised on the website.
    """


class Insurance(BaseModel):
    """pydantic model Insurance
    Attributes:
        price(Amount, True): --
        inventory_type(constr(max_length=30), True): Type of inventory.
        inventory_source(InventorySource, True): Identifies the business model through which the supply is being sold. Merchant/Agency.
        travelers_references(List[constr(max_length=50)], True): List of travelerGuids who are part of the traveling party on the order for the product.
        type(Literal["Insurance"], True): Type of product advertised on the website.

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
    """
    Type of product advertised on the website.
    """


TravelProduct = Union[
    Air,
    Cruise,
    Car,
    Hotel,
    Insurance,
]


CancellationReason.update_forward_refs()


ChargebackDetail.update_forward_refs()


InsultDetail.update_forward_refs()


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


PaymentUpdate.update_forward_refs()


Air.update_forward_refs()


Cruise.update_forward_refs()


Car.update_forward_refs()


Hotel.update_forward_refs()


Insurance.update_forward_refs()
