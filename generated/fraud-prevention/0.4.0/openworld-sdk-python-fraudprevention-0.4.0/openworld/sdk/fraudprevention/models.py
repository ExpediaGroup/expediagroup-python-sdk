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
from typing import List, Optional

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr


class UpdateType(Enum):
    ORDER_UPDATE = 'ORDER_UPDATE'
    CHARGEBACK_FEEDBACK = 'CHARGEBACK_FEEDBACK'
    INSULT_FEEDBACK = 'INSULT_FEEDBACK'
    REFUND_UPDATE = 'REFUND_UPDATE'
    PAYMENT_UPDATE = 'PAYMENT_UPDATE'


class CancellationReason(BaseModel):
    primary_reason_code: Optional[constr(max_length=200)] = Field(None, description='Primary cancellation reason code.')
    sub_reason_code: Optional[constr(max_length=200)] = Field(None, description='Substitute cancellation reason code.')
    primary_reason_description: constr(max_length=200) = Field(..., description='Primary cancellation reason code. Required if `order_status = CANCELLED`.')
    sub_reason_description: Optional[constr(max_length=200)] = Field(None, description='Substitute cancellation reason description.')


class ChargebackReason(Enum):
    FRAUD = 'FRAUD'
    NON_FRAUD = 'NON_FRAUD'


class ChargebackDetail(BaseModel):
    chargeback_reason: ChargebackReason = Field(..., description='Reason for chargeback which can be `Fraud` or `Non Fraud`.')
    chargeback_amount: float = Field(..., description='Chargeback amount received by the partner.')
    currency_code: constr(regex=r'^[A-Z]{3}$', max_length=200) = Field(
        ..., description='The 3-letter currency code defined in ISO 4217. https://www.currency-iso.org/dam/downloads/lists/list_one.xml.'
    )
    bank_reason_code: Optional[constr(max_length=200)] = Field(None, description='Unique code provided by the acquiring bank for the category of fraud.')
    chargeback_reported_timestamp: Optional[datetime] = Field(
        None, description='Date and time when the chargeback was reported to the partner, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.'
    )


class InsultDetail(BaseModel):
    insult_reported_timestamp: Optional[datetime] = Field(
        None, description='Date and time when the insult was reported to the partner, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.'
    )


class Status(Enum):
    COMPLETED = 'COMPLETED'
    CHANGE_COMPLETED = 'CHANGE_COMPLETED'
    CANCELLED = 'CANCELLED'
    FAILED = 'FAILED'
    CHANGE_FAILED = 'CHANGE_FAILED'


class FraudDecision(Enum):
    ACCEPT = 'ACCEPT'
    REVIEW = 'REVIEW'
    REJECT = 'REJECT'


class ErrorDetail(BaseModel):
    code: Optional[int] = None
    message: Optional[constr(max_length=200)] = Field(
        None, description='Description of the error. Clients may choose to use the description field to display to end clients.'
    )
    detailed_message: Optional[constr(max_length=500)] = Field(None, description='Detailed description of the error.')


class Error(BaseModel):
    type: AnyUrl = Field(
        ...,
        description="A URI reference, compliant with the standard EG error type format, which identifies the error type. It provides a machine-readable identifier for the error type. The error type will be aligned with the HTTP status code of the response. The URI can either be absolute or relative to the API's base URI. When dereferenced, it can also provide human-readable documentation for the error type.\n",
        example='https://apis.expediagroup.com/errors/common/invalid-argument',
    )
    detail: str = Field(
        ...,
        description='A human-readable explanation of the error, specific to this error occurrence.',
        example='The request failed because one or many input values are invalid. Please see the causes for more details.',
    )


class Location(Enum):
    HEADER = 'HEADER'
    PATH = 'PATH'
    QUERY = 'QUERY'
    BODY = 'BODY'


class ErrorCause(BaseModel):
    type: AnyUrl = Field(
        ...,
        description="A URI reference, compliant with the standard EG error type format, which identifies the cause type. It provides a machine-readable identifier for the cause type. The cause type will be aligned with the error type. The URI can either be absolute or relative to the API's base URI. When dereferenced, it provides human-readable documentation for the cause type.\n",
        example='https://apis.expediagroup.com/errors/common/invalid-number',
    )
    detail: str = Field(
        ...,
        description='A human-readable explanation of the cause, specific to this cause occurrence.',
        example="The number of results per page you provided ('NotANumber') is invalid. Please provide a valid integer value between 1 and 100.",
    )
    location: Optional[Location] = Field(
        None,
        description='The location of the element in the request that identifies this specific cause. When specified, the `name` will be specified and when applicable, the `value` as well. Can be one of:\n* `HEADER` - When an error has been identified in one of the request headers.\n* `PATH` - When an error has been identified in one of the path parameters.\n* `QUERY` - When an error has been identified in one of the query parameters.\n* `BODY` - When an error has been identified in the request body.\n',
        example='QUERY',
    )
    name: Optional[str] = Field(
        None,
        description='The name of the element for this cause. When specified, the `location` will be specified and when applicable, the `value` as well. This name is a function of the value of the `location` property:\n  * When the `location` is set to `HEADER`, this will be the name of the request header (e.g. `Content-Type`).\n  * When the `location` is set to `PATH`, this will be the name of the path parameter (e.g. in a path defined as `/users/{user_id}`, the value would be `user_id`).\n  * When the `location` is set to `QUERY`, this will be the name of the query string parameter (e.g. `offset`).\n  * When the `location` is set to `BODY`, this will one of the field names specified in the body of the request.\n    * For a top level field, it should only be set to the field name (e.g. `firstName`).\n    * For a field in a nested object, it may contain the path to reach the field (e.g. `address.city`).\n    * For a field in an object part of collection, it may contain the index in the collection (e.g. `permissions[0].name`).\n',
        example='results_per_page',
    )
    value: Optional[str] = Field(
        None,
        description='A string representation of the erroneous value of the element identified in `name`, perceived to be the cause of the error. When specified, the `location` and `name` should be specified as well. This value may be omitted in cases where it cannot be provided (e.g. missing require field), or the erroneous value cannot be represented as a string.\n',
        example='NotANumber',
    )


class SiteInfo(BaseModel):
    country_code: constr(regex=r'^[A-Z]{3}$') = Field(..., description='The alpha-3 ISO code that represents a country name.', example='USA')
    agent_assisted: bool = Field(
        ..., description='Identifies if an agent assisted in booking travel for the customer. `False` if the order was directly booked by customer.'
    )


class DeviceDetails(BaseModel):
    source: Optional[constr(max_length=50)] = Field(None, description='Source of the device_box. Default value is `TrustWidget`.')
    device_box: constr(max_length=16000) = Field(..., description='Device related information retrieved from TrustWidget.')
    ip_address: Optional[
        constr(regex=r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$')
    ] = Field(None, description='IP address of the device used for booking.', example='192.168.32.48')


class CurrentOrderStatus(Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'


class OrderType(Enum):
    CREATE = 'CREATE'
    CHANGE = 'CHANGE'


class AccountType(Enum):
    GUEST = 'GUEST'
    STANDARD = 'STANDARD'


class AddressType(Enum):
    HOME = 'HOME'
    WORK = 'WORK'


class Address(BaseModel):
    address_type: Optional[AddressType] = None
    address_line1: constr(max_length=200) = Field(..., description='Address line 1 of the address provided.')
    address_line2: Optional[constr(max_length=200)] = Field(None, description='Address line 2 of the address provided.')
    city: constr(max_length=200) = Field(..., description='City of the address provided.')
    state: constr(regex=r'^[A-Z]{2}$') = Field(..., description='The two-characters ISO code for the state or province of the address.')
    zip_code: constr(max_length=20) = Field(..., description='Zip code of the address provided.')
    country_code: constr(regex=r'^[A-Z]{3}$') = Field(..., description='ISO alpha-3 country code of the address provided.')


class InventorySource(Enum):
    MERCHANT = 'MERCHANT'
    AGENCY = 'AGENCY'


class TravelersReference(BaseModel):
    __root__: constr(max_length=50)


class FlightType(Enum):
    ROUNDTRIP = 'ROUNDTRIP'
    ONEWAY = 'ONEWAY'
    MULTIPLE_DESTINATION = 'MULTIPLE_DESTINATION'


class AirSegment(BaseModel):
    airline_code: constr(max_length=10) = Field(..., description='Airline code of the trip segment')
    departure_airport_code: constr(max_length=10) = Field(..., description='Departure airport of the trip segment')
    arrival_airport_code: constr(max_length=10) = Field(..., description='Arrival airport of the trip segment')
    departure_time: Optional[datetime] = Field(
        None, description='Local date and time of departure from departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.'
    )
    arrival_time: Optional[datetime] = Field(
        None, description='Local date and time of arrival to destination location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.'
    )


class PaymentThreeDSCriteria(BaseModel):
    probable_flag: Optional[bool] = Field(None, description='This is a flag passed that indicates that this transaction could potentially go through 3DS.')
    transaction_model: Optional[constr(max_length=200)] = Field(None, description='Model used to process payment transaction.')


class PaymentReason(Enum):
    FULL = 'FULL'
    DEPOSIT = 'DEPOSIT'
    SCHEDULED = 'SCHEDULED'
    SUBSEQUENT = 'SUBSEQUENT'
    DEFERRED = 'DEFERRED'


class VerificationType(Enum):
    CVV = 'CVV'
    field_3DS = '3DS'


class PaymentStatus(Enum):
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'


class PaymentMethod(Enum):
    CREDIT_CARD = 'CREDIT_CARD'
    PAYPAL = 'PAYPAL'
    POINTS = 'POINTS'


class Name(BaseModel):
    last_name: constr(max_length=200) = Field(..., description='Surname, or last name, of the person.')
    first_name: constr(max_length=200) = Field(..., description='Given, or first name, of the person.')
    middle_name: Optional[constr(max_length=200)] = Field(None, description='Middle name of the person.')
    title: Optional[constr(max_length=200)] = Field(None, description='Title of the person for name (e.g. Mr., Ms. etc).')
    suffix: Optional[constr(max_length=50)] = Field(
        None,
        description='Generational designations (e.g. Sr, Jr, III) or values that indicate the individual holds a position, educational degree, accreditation, office, or honor (e.g. PhD, CCNA, OBE).',
    )
    full_name: Optional[constr(max_length=500)] = Field(
        None, description='Full name of the person that includes title, first_name, middle_name, last_name, suffix.', example='Sally Expedia'
    )


class TelephoneType(Enum):
    HOME = 'HOME'
    MOBILE = 'MOBILE'
    BUSINESS = 'BUSINESS'
    FAX = 'FAX'
    OTHER = 'OTHER'


class TelephonePlatformType(Enum):
    MOBILE = 'MOBILE'
    LANDLINE = 'LANDLINE'
    VOIP = 'VOIP'


class Email(BaseModel):
    email_address: Optional[EmailStr] = Field(None, description='Full email address including the alias, @ symbol, domain, and root domain.')


class Amount(BaseModel):
    value: float = Field(..., description='The amount required in payment for the product/order in local currency.')
    currency_code: constr(regex=r'^[A-Z]{3}$', max_length=3) = Field(..., description='The ISO  alpha-3 country code for the amount currency.')


class ContentType(Enum):
    application_json = 'application/json'


class ContentType1(Enum):
    application_json = 'application/json'


class ContentType2(Enum):
    application_json = 'application/json'


class ContentType3(Enum):
    application_json = 'application/json'


class ContentType4(Enum):
    application_json = 'application/json'


class ContentType5(Enum):
    application_json = 'application/json'


class OrderPurchaseUpdateRequest(BaseModel):
    type: UpdateType
    risk_id: constr(max_length=200) = Field(
        ..., description="The `risk_id` provided by Expedia's Fraud Prevention Service in the `OrderPurchaseScreenResponse`.", example='123456789'
    )


class OrderUpdate(OrderPurchaseUpdateRequest):
    order_status: Status
    cancellation_reason: Optional[CancellationReason] = None


class ChargebackFeedback(OrderPurchaseUpdateRequest):
    chargeback_detail: Optional[ChargebackDetail] = None


class InsultFeedback(OrderPurchaseUpdateRequest):
    insult_detail: Optional[InsultDetail] = None


class RefundUpdate(OrderPurchaseUpdateRequest):
    acquirer_reference_number: constr(max_length=200) = Field(
        ..., description="A unique number that tags a credit or debit card transaction when it goes from the merchant's bank through to the cardholder's bank."
    )
    refund_deposit_timestamp: datetime = Field(..., description='Date and time when the refund was deposited to the original form of payment.')
    refund_settlement_timestamp: datetime = Field(
        ...,
        description='Date and time when the 3rd party payment processor confirmed that a previously submitted payment refund has settled at the participating financial institutions.',
    )
    settlement_id: constr(max_length=200) = Field(..., description='Unique settlement identifier generated for a previously submitted payment refund.')
    refund_amount: Amount


class PaymentUpdate(OrderPurchaseUpdateRequest):
    merchant_order_code: constr(max_length=200) = Field(
        ...,
        description='Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.',
    )


class OrderPurchaseScreenResponse(BaseModel):
    risk_id: Optional[constr(max_length=200)] = Field(None, example='1234567')
    decision: Optional[FraudDecision] = None
    error_detail: Optional[ErrorDetail] = None


class ExtendedError(BaseModel):
    type: AnyUrl = Field(
        ...,
        description="A URI reference, compliant with the standard EG error type format, which identifies the error type. It provides a machine-readable identifier for the error type. The error type will be aligned with the HTTP status code of the response. The URI can either be absolute or relative to the API's base URI. When dereferenced, it can also provide human-readable documentation for the error type.\n",
        example='https://apis.expediagroup.com/errors/common/invalid-argument',
    )
    detail: str = Field(
        ...,
        description='A human-readable explanation of the error, specific to this error occurrence.',
        example='The request failed because one or many input values are invalid. Please see the causes for more details.',
    )
    causes: Optional[List[ErrorCause]] = Field(None, description='An array of cause objects, that identify the specific causes of the error.')


class TravelProduct(BaseModel):
    price: Amount
    type: constr(max_length=40) = Field(..., description='Type of product advertised on the website.')
    inventory_type: constr(max_length=30) = Field(..., description='Type of inventory.')
    inventory_source: InventorySource = Field(..., description='Identifies the business model through which the supply is being sold. Merchant/Agency.')
    travelers_references: List[TravelersReference] = Field(
        ..., description='List of travelerGuids who are part of the traveling party on the order for the product.', max_items=40, min_items=1
    )


class Air(TravelProduct):
    departure_time: datetime = Field(
        ..., description='Local date and time of departure from original departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.'
    )
    arrival_time: datetime = Field(
        ..., description='Local date and time of arrival to final destination location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.'
    )
    air_segments: List[AirSegment] = Field(..., description='Additional airline and flight details for each of the trip segments.', max_items=30, min_items=1)
    flight_type: Optional[FlightType] = Field(None, description='Identifies the type of air trip based on the air destinations.')
    passenger_name_record: Optional[constr(max_length=100)] = Field(None, description='Airline booking confirmation code for the trip.')
    global_distribution_system_type: Optional[constr(max_length=100)] = Field(None, description='Associated with Passenger Name Record (PNR).')


class Cruise(TravelProduct):
    departure_time: datetime = Field(
        ..., description='Local date and time of departure from original departure location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.'
    )
    arrival_time: datetime = Field(
        ..., description='Local date and time of arrival from original arrival location, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.'
    )
    embarkation_port: constr(max_length=200) = Field(..., description='Location from where cruise will depart.')
    disembarkation_port: constr(max_length=200) = Field(..., description="The cruise's final destination.")
    ship_name: constr(max_length=200) = Field(..., description='Name of the cruise ship.')


class Car(TravelProduct):
    pick_up_location: constr(max_length=200) = Field(..., description='Location where the automobile will be picked up.')
    drop_off_location: constr(max_length=200) = Field(..., description='Location at which the automobile will be returned.')
    pickup_time: datetime = Field(
        ..., description='Local date and time the automobile will be picked-up, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.'
    )
    return_time: datetime = Field(
        ..., description='Local date and time the automobile will be returned, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.'
    )


class Hotel(TravelProduct):
    hotel_id: constr(max_length=200) = Field(..., description='Unique hotel identifier assigned by the partner.', example='8883333999221')
    price_withheld: Optional[bool] = Field(None, description='Identifies if the product price was withheld from the customer during the booking process.')
    hotel_name: constr(max_length=200) = Field(..., description='Name of the hotel.', example='Hotel Expedia')
    room_count: Optional[int] = Field(None, description='Total number of rooms booked within the hotel product collection.')
    address: Address
    checkin_time: datetime = Field(..., description='Local date and time of the hotel check-in, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.')
    checkout_time: datetime = Field(..., description='Local date and time of the hotel check-out, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.')


class PaymentOutcome(BaseModel):
    status: Optional[PaymentStatus] = None
    code: Optional[constr(max_length=200)] = Field(None, description='A mnemonic code for the payment processing.')
    description: Optional[constr(max_length=200)] = Field(None, description='A short description providing additional explanation regarding the mnemonic code.')


class Insurance(TravelProduct):
    pass


class Telephone(BaseModel):
    type: Optional[TelephoneType] = None
    platform_type: Optional[TelephonePlatformType] = None
    country_access_code: constr(regex=r'^[0-9]{1,3}$', max_length=3) = Field(
        ...,
        description='Numeric digit between 1 to 3 characters used to represent the country code for international dialing.  Does not include symbols, spaces, or leading zeros.',
        example='1',
    )
    area_code: constr(regex=r'^[0-9]{1,20}$', max_length=20) = Field(
        ...,
        description='A number prefixed to an individual telephone number: used in making long-distance calls.  Does not include symbols, spaces, or leading zeros.',
        example='1',
    )
    phone_number: constr(regex=r'^[0-9]{1,50}$', max_length=50) = Field(
        ...,
        description='A number that is dialed on a telephone, without the country or area codes, to reach a particular person, business, etc.  Does not include symbols, spaces, or leading zeros.',
        example='1234567',
    )
    full_phone_number: Optional[constr(regex=r'^[0-9]{1,100}$', max_length=100)] = Field(
        None,
        description='The concatenated countryAccessCode, areaCode, and phoneNumber with leading zeros from the original fields and symbols  (-,.+) removed.  It does not include a phone extension.',
        example='12345689',
    )
    extension_number: Optional[constr(regex=r'^[0-9]{1,20}$', max_length=20)] = Field(
        None,
        description='The number used to reach an individual once a phone connection is established.  Does not include symbols, spaces, or leading zeros.',
        example='89',
    )
    preference_rank: Optional[float] = Field(
        None,
        description='Ranking of order of user preference for contact via text (if type is Mobile) or voice.  `0` means no preference.  `1` is the primary phone, `2` is the secondary phone, etc.',
    )
    last_verified_timestamp: Optional[datetime] = Field(
        None,
        description='Local date and time user validated possession of their phone number via a text or voice multi factor authentication challenge, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.',
    )
    verified_flag: Optional[bool] = Field(
        None,
        description='Flag indicating whether user passed validation of possession of their phone number via a text or voice multi factor authentication challenge.',
    )


class CustomerAccount(BaseModel):
    user_id: Optional[str] = Field(
        None, description='Unique identifier assigned to the account owner by the partner. `user_id` is specific to the partner namespace'
    )
    account_type: AccountType = Field(
        ...,
        description='Identifies if the customer account is known to the client. Possible values are:\n\n-`GUEST` - Applicable if the partner maintains record to distinguish whether the transaction was booked via a guest account.\n\n-`STANDARD` - Default account type.\n',
        example='STANDARD',
    )
    name: Name
    email_address: EmailStr = Field(..., description='Email address for the account owner.')
    telephones: Optional[List[Telephone]] = None
    address: Optional[Address] = None
    registered_time: Optional[datetime] = Field(
        None,
        description='The local date and time that the customer first registered on the client site, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.',
    )


class Traveler(BaseModel):
    traveler_name: Name
    email_address: Optional[EmailStr] = Field(None, description='Email address associated with the traveler as supplied by the partner system.')
    telephones: Optional[List[Telephone]] = Field(None, max_items=250, min_items=1)
    primary: bool = Field(
        ...,
        description='Indicator for one of the travelers who is the primary traveler. One traveler in each itinerary item must be listed as primary. By default, for a single traveler this should be set to `true`.',
    )
    age: Optional[float] = Field(None, description='Age of the traveler.')
    birth_date: Optional[datetime] = Field(None, description='Date of birth for traveler, in ISO-8061 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.')
    citizenship_country_code: Optional[constr(regex=r'^[A-Z]{3}$', min_length=3, max_length=3)] = Field(
        None, description="The alpha-3 ISO country code of the traveler's nationality."
    )
    traveler_id: Optional[constr(max_length=100)] = Field(None, description='A unique identifier for travelers in the transaction.')


class PaymentOperation(BaseModel):
    id: Optional[constr(max_length=200)] = None
    amount: Optional[Amount] = None
    outcome: Optional[PaymentOutcome] = None


class Verify(PaymentOperation):
    type: Optional[VerificationType] = None


class Authorize(PaymentOperation):
    pass


class AuthorizeReversal(PaymentOperation):
    pass


class Capture(PaymentOperation):
    pass


class Refund(PaymentOperation):
    pass


class Operations(BaseModel):
    verify: Optional[Verify] = None
    authorize: Optional[Authorize] = None
    authorize_reversal: Optional[AuthorizeReversal] = None
    capture: Optional[Capture] = None
    refunds: Optional[List[Refund]] = Field(None, max_items=20)


class Payment(BaseModel):
    brand: constr(max_length=200) = Field(..., description='Payment brand used for payment on this transaction.')
    method: PaymentMethod
    reason: Optional[PaymentReason] = None
    billing_name: Name
    billing_address: Optional[Address] = None
    billing_email_address: Optional[EmailStr] = Field(None, description='Email address associated with the payment.')
    authorized_amount: Optional[Amount] = None
    verified_amount: Optional[Amount] = None
    three_digits_secure_criteria: Optional[PaymentThreeDSCriteria] = None
    operations: Optional[Operations] = None
    total_refund_amount: Optional[float] = Field(None, description='Total amount refunded towards the transaction.')


class CreditCard(Payment):
    card_type: constr(max_length=200) = Field(..., description='Type of card used for payment, (eg. `CREDIT`, `DEBIT`).')
    card_number: constr(max_length=200) = Field(..., description='All the digits (unencrypted) of the credit card number associated with the payment.')
    expiry_date: Optional[datetime] = Field(None, description='Expiration date of the credit card used for payment.')
    electronic_commerce_indicator: Optional[constr(max_length=200)] = Field(
        None,
        description="Electronic Commerce Indicator, a two or three digit number usually returned by a 3rd party payment processor in regards to the authentication used when gathering the cardholder's payment credentials.",
    )
    virtual_credit_card_flag: Optional[bool] = Field(
        None, description='A flag to indicate that the bank card being used for the charge is a virtual credit card.'
    )
    wallet_type: Optional[constr(max_length=200)] = Field(
        None,
        description="If a virtual/digital form of payment was used, the type of digital wallet should be specified here. Possible `wallet_type`'s include: `Google` or `ApplePay`.",
    )
    card_avs_response: constr(max_length=50) = Field(
        ..., description='A field used to confirm if the address provided at the time of purchase matches what the bank has on file for the Credit Card.'
    )
    card_cvv_response: constr(max_length=20) = Field(
        ..., description='A field used to confirm the Card Verification Value on the Credit Card matches the Credit Card used at the time of purchase.'
    )
    telephones: List[Telephone] = Field(..., description='Telephone(s) associated with card holder and credit card.', max_items=20, min_items=1)
    merchant_order_code: Optional[constr(max_length=200)] = Field(
        None,
        description='Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.',
    )


class PayPal(Payment):
    payer_id: constr(max_length=200) = Field(..., description='Unique PayPal Customer Account identification number.')
    transaction_id: constr(max_length=200) = Field(..., description='Unique transaction number to identify Auth calls at PayPal.')
    merchant_order_code: Optional[constr(max_length=200)] = Field(
        None,
        description='Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level.',
    )


class Points(Payment):
    pass


class TransactionDetails(BaseModel):
    order_id: constr(max_length=50) = Field(
        ..., description='Unique identifier assigned to the order by the partner. `order_id` is specific to the partner namespace.', example='1000000234'
    )
    current_order_status: CurrentOrderStatus = Field(..., description='Status of the order.')
    order_type: OrderType = Field(
        ...,
        description='Type of order. Possible `order_types`.\n\n`CREATE` - Initial type of a brand new order.\n\n`CHANGE` - If a `OrderPurchaseScreenRequest` has already been submitted for the initial booking with `order_type = CREATE`, but has now been modified and partner wishes to resubmit for Fraud screening then the `order_type = CHANGE`. Examples of changes that are supported are changes made to `check-in/checkout dates` or `price of a TravelProduct`.\n',
        example='CREATE',
    )
    travel_products: List[TravelProduct] = Field(..., max_items=20, min_items=1)
    travelers: List[Traveler] = Field(
        ...,
        description='Individuals who are part of the travel party for the order. At minimum there must be at least `1` traveler.',
        max_items=30,
        min_items=1,
    )
    payments: List[Payment] = Field(
        ...,
        description='List of the form(s) of payment being used to purchase the order.  One or more forms of payment can be used within an order. Information gathered will be specific to the form of payment.',
        max_items=30,
        min_items=1,
    )
    credit_card_authentication_failure_count: Optional[int] = Field(
        None,
        description='Total authentication failure count for given credit card. Authentication failures happen when a cardholder enters their card information incorrectly.',
    )


class OrderPurchaseTransaction(BaseModel):
    site_info: SiteInfo
    device_details: DeviceDetails
    customer_account: CustomerAccount
    transaction_details: TransactionDetails
    bypass_risk_flag: Optional[bool] = Field(
        None,
        description='A flag to indicate whether the client is ignoring the decision by Trust validation and proceeds to process the even in-case the outcome is ‘Reject’ or ‘Review’.',
    )


class OrderPurchaseScreenRequest(BaseModel):
    transaction: Optional[OrderPurchaseTransaction] = None
