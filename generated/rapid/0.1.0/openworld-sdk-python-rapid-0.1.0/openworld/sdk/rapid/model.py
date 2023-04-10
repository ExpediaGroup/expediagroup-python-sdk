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

from datetime import date
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field


class PropertyRating(BaseModel):
    """pydantic model PropertyRating: Information about the property's rating.
    Attributes:
        rating(Optional[str], False): The rating assigned to this property. Returns a value between 0.0 and 5.0. A value of 0.0 or a blank value indicates no rating is available.
        type(Optional[str], False): Returns a value of either "Star" or "Alternate". Star indicates the rating is provided by the property’s local star rating authority. Alternate indicates that the rating is an Expedia-assigned value; an official rating was not available.

    """

    rating: Optional[str] = None
    """
    The rating assigned to this property. Returns a value between 0.0 and 5.0. A value of 0.0 or a blank value indicates no rating is available.
    """
    type: Optional[str] = None
    """
    Returns a value of either "Star" or "Alternate". Star indicates the rating is provided by the property’s local star rating authority. Alternate indicates that the rating is an Expedia-assigned value; an official rating was not available.
    """


class GuestRating(BaseModel):
    """pydantic model GuestRating: Rating information provided by guests who stayed at this property.
    Attributes:
        count(Optional[float], False): A count of all of the guest review ratings which currently exist for this property.
        overall(Optional[str], False): The overall rating for the property, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
        cleanliness(Optional[str], False): The cleanliness rating for the property, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
        service(Optional[str], False): The rating of the staff's service for the property, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
        comfort(Optional[str], False): The comfort rating of the rooms, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
        condition(Optional[str], False): The rating for the property's condition, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
        location(Optional[str], False): The rating for how convinent the location of the property is, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
        neighborhood(Optional[str], False): The rating for how satisfying the neighborhood of the property is, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
        quality(Optional[str], False): The quality rating of the rooms, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
        value(Optional[str], False): The rating for how much value the property provided for the cost of the stay, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
        amenities(Optional[str], False): The rating for the amenities provided by the property, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
        recommendation_percent(Optional[str], False): The percent of guests who recommend staying at this property.

    """

    count: Optional[float] = None
    """
    A count of all of the guest review ratings which currently exist for this property.
    """
    overall: Optional[str] = None
    """
    The overall rating for the property, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
    """
    cleanliness: Optional[str] = None
    """
    The cleanliness rating for the property, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
    """
    service: Optional[str] = None
    """
    The rating of the staff's service for the property, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
    """
    comfort: Optional[str] = None
    """
    The comfort rating of the rooms, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
    """
    condition: Optional[str] = None
    """
    The rating for the property's condition, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
    """
    location: Optional[str] = None
    """
    The rating for how convinent the location of the property is, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
    """
    neighborhood: Optional[str] = None
    """
    The rating for how satisfying the neighborhood of the property is, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
    """
    quality: Optional[str] = None
    """
    The quality rating of the rooms, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
    """
    value: Optional[str] = None
    """
    The rating for how much value the property provided for the cost of the stay, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
    """
    amenities: Optional[str] = None
    """
    The rating for the amenities provided by the property, averaged from all guest reviews. Returns a value between 1.0 and 5.0.
    """
    recommendation_percent: Optional[str] = None
    """
    The percent of guests who recommend staying at this property.
    """


class Coordinates(BaseModel):
    """pydantic model Coordinates: The coordinates of the property.
    Attributes:
        latitude(Optional[float], False): The latitude of the property.
        longitude(Optional[float], False): The longitude of the property.

    """

    latitude: Optional[float] = None
    """
    The latitude of the property.
    """
    longitude: Optional[float] = None
    """
    The longitude of the property.
    """


class CategoryProperty(BaseModel):
    """pydantic model CategoryProperty: The property's category. See our [property categories reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known category ID and name values.
    Attributes:
        id(Optional[str], False): The ID of the property's category.
        name(Optional[str], False): The property's category.

    """

    id: Optional[str] = None
    """
    The ID of the property's category.
    """
    name: Optional[str] = None
    """
    The property's category.
    """


class BusinessModel(BaseModel):
    """pydantic model BusinessModel: How and when the payment can be taken.
    Attributes:
        expedia_collect(Optional[bool], False): Whether or not a payment for this property can be taken by Expedia at the time of booking.
        property_collect(Optional[bool], False): Whether or not a payment for this property can be taken by the property upon arrival.

    """

    expedia_collect: Optional[bool] = None
    """
    Whether or not a payment for this property can be taken by Expedia at the time of booking.
    """
    property_collect: Optional[bool] = None
    """
    Whether or not a payment for this property can be taken by the property upon arrival.
    """


class Checkin(BaseModel):
    """pydantic model Checkin: The property's check-in information.
    Attributes:
        field_24_hour(Optional[str], False): Present if the property has 24-hour check-in.
        begin_time(Optional[str], False): The time at which a property begins to allow check-ins.
        end_time(Optional[str], False): The time at which a property stops allowing check-ins.
        instructions(Optional[str], False): The property's check-in policy.
        special_instructions(Optional[str], False): Any special instructions for checking into this property that may be specific to this property.
        min_age(Optional[float], False): The minimum age for a customer to be able to check-in at a property.

    """

    field_24_hour: Optional[str] = Field(None, alias='24_hour')
    """
    Present if the property has 24-hour check-in.
    """
    begin_time: Optional[str] = None
    """
    The time at which a property begins to allow check-ins.
    """
    end_time: Optional[str] = None
    """
    The time at which a property stops allowing check-ins.
    """
    instructions: Optional[str] = None
    """
    The property's check-in policy.
    """
    special_instructions: Optional[str] = None
    """
    Any special instructions for checking into this property that may be specific to this property.
    """
    min_age: Optional[float] = None
    """
    The minimum age for a customer to be able to check-in at a property.
    """


class Checkout(BaseModel):
    """pydantic model Checkout: The property's check-out information.
    Attributes:
        time(Optional[str], False): The time by which a guest must check out.

    """

    time: Optional[str] = None
    """
    The time by which a guest must check out.
    """


class Fees(BaseModel):
    """pydantic model Fees: Information related to a property's fees.
    Attributes:
        mandatory(Optional[str], False): Describes resort fees and other mandatory taxes or charges. May describe which services are covered by any fees, such as fitness centers or internet access.
        optional(Optional[str], False): Describes additional optional fees for items such as breakfast, wifi, parking, pets etc.

    """

    mandatory: Optional[str] = None
    """
    Describes resort fees and other mandatory taxes or charges. May describe which services are covered by any fees, such as fitness centers or internet access.
    """
    optional: Optional[str] = None
    """
    Describes additional optional fees for items such as breakfast, wifi, parking, pets etc.
    """


class Policies(BaseModel):
    """pydantic model Policies: Information about property policies that guests need to be aware of.
    Attributes:
        know_before_you_go(Optional[str], False): Description of information that may be helpful when planning a trip to this property.

    """

    know_before_you_go: Optional[str] = None
    """
    Description of information that may be helpful when planning a trip to this property.
    """


class Attribute(BaseModel):
    """pydantic model Attribute: An individual attribute.
    Attributes:
        id(Optional[str], False): The attribute definition ID for this attribute.
        name(Optional[str], False): Attribute name.
        value(Optional[str], False): Attribute value.

    """

    id: Optional[str] = None
    """
    The attribute definition ID for this attribute.
    """
    name: Optional[str] = None
    """
    Attribute name.
    """
    value: Optional[str] = None
    """
    Attribute value.
    """


class PaymentType(BaseModel):
    """pydantic model PaymentType: An individual payment type.
    Attributes:
        id(Optional[str], False): The identifier of the payment type.
        name(Optional[str], False): The name of the payment type.

    """

    id: Optional[str] = None
    """
    The identifier of the payment type.
    """
    name: Optional[str] = None
    """
    The name of the payment type.
    """


class DescriptionsRoom(BaseModel):
    """pydantic model DescriptionsRoom: Descriptions of a room.
    Attributes:
        overview(Optional[str], False): Provides an overview of a room.

    """

    overview: Optional[str] = None
    """
    Provides an overview of a room.
    """


class Area(BaseModel):
    """pydantic model Area: Information about the area of the room.
    Attributes:
        square_meters(Optional[float], False): The room's area, measured in square meters.
        square_feet(Optional[float], False): The room's area, measured in square feet.

    """

    square_meters: Optional[float] = None
    """
    The room's area, measured in square meters.
    """
    square_feet: Optional[float] = None
    """
    The room's area, measured in square feet.
    """


class View(BaseModel):
    """pydantic model View: An individual view.
    Attributes:
        id(Optional[str], False): Identifier for the view.
        name(Optional[str], False): View name.

    """

    id: Optional[str] = None
    """
    Identifier for the view.
    """
    name: Optional[str] = None
    """
    View name.
    """


class MaxAllowed(BaseModel):
    """pydantic model MaxAllowed: Maximum occupancy counts.
    Attributes:
        total(Optional[float], False): Total maximum occupancy allowed.
        children(Optional[float], False): Maximum number of children allowed.
        adults(Optional[float], False): Maximum number of adults allowed.

    """

    total: Optional[float] = None
    """
    Total maximum occupancy allowed.
    """
    children: Optional[float] = None
    """
    Maximum number of children allowed.
    """
    adults: Optional[float] = None
    """
    Maximum number of adults allowed.
    """


class CategoryAge(BaseModel):
    """pydantic model CategoryAge: An age category.
    Attributes:
        name(Optional[str], False): Age category name.
        minimum_age(Optional[float], False): Age category minimum age.

    """

    name: Optional[str] = None
    """
    Age category name.
    """
    minimum_age: Optional[float] = None
    """
    Age category minimum age.
    """


class Dates(BaseModel):
    """pydantic model Dates: Dates about the property.
    Attributes:
        added(Optional[str], False): The UTC date the property’s content was added to EPS, in ISO 8601 format
        updated(Optional[str], False): The UTC date the property’s content was updated by EPS, in ISO 8601 format.

    """

    added: Optional[str] = None
    """
    The UTC date the property’s content was added to EPS, in ISO 8601 format
    """
    updated: Optional[str] = None
    """
    The UTC date the property’s content was updated by EPS, in ISO 8601 format.
    """


class Descriptions(BaseModel):
    """pydantic model Descriptions: Descriptions of a property.
    Attributes:
        amenities(Optional[str], False): Describes general building amenities at the property.
        dining(Optional[str], False): Describes dining accommodations at the property.
        renovations(Optional[str], False): Describes any recent room or property renovations.
        national_ratings(Optional[str], False): States the source of the property's star rating (such as a regional or national tourism agency) and any other ratings claimed.
        business_amenities(Optional[str], False): Describes any business-specific amenities at the property, e.g. conference rooms.
        rooms(Optional[str], False): Describes typical room amenities.
        attractions(Optional[str], False): Nearby attractions/areas, often including distances from the property.
        location(Optional[str], False): General location as entered by the property.
        headline(Optional[str], False): A headline description for the property.
        general(Optional[str], False): A general description of a vacation rental property.

    """

    amenities: Optional[str] = None
    """
    Describes general building amenities at the property.
    """
    dining: Optional[str] = None
    """
    Describes dining accommodations at the property.
    """
    renovations: Optional[str] = None
    """
    Describes any recent room or property renovations.
    """
    national_ratings: Optional[str] = None
    """
    States the source of the property's star rating (such as a regional or national tourism agency) and any other ratings claimed.
    """
    business_amenities: Optional[str] = None
    """
    Describes any business-specific amenities at the property, e.g. conference rooms.
    """
    rooms: Optional[str] = None
    """
    Describes typical room amenities.
    """
    attractions: Optional[str] = None
    """
    Nearby attractions/areas, often including distances from the property.
    """
    location: Optional[str] = None
    """
    General location as entered by the property.
    """
    headline: Optional[str] = None
    """
    A headline description for the property.
    """
    general: Optional[str] = None
    """
    A general description of a vacation rental property.
    """


class Statistic(BaseModel):
    """pydantic model Statistic: An individual statistic.
    Attributes:
        id(Optional[str], False): The statistic definition ID for this statistic.
        name(Optional[str], False): Statistic name.
        value(Optional[str], False): Statistic value.

    """

    id: Optional[str] = None
    """
    The statistic definition ID for this statistic.
    """
    name: Optional[str] = None
    """
    Statistic name.
    """
    value: Optional[str] = None
    """
    Statistic value.
    """


class Preferred(BaseModel):
    """pydantic model Preferred: The preferred airport of the property.
    Attributes:
        iata_airport_code(Optional[str], False): The airport's IATA code.

    """

    iata_airport_code: Optional[str] = None
    """
    The airport's IATA code.
    """


class Theme(BaseModel):
    """pydantic model Theme: An individual theme.
    Attributes:
        id(Optional[str], False): Identifier for the theme.
        name(Optional[str], False): Theme name.

    """

    id: Optional[str] = None
    """
    Identifier for the theme.
    """
    name: Optional[str] = None
    """
    Theme name.
    """


class AllInclusive(BaseModel):
    """pydantic model AllInclusive: Information about the all-inclusive rate plans available at the property.
    Attributes:
        all_rate_plans(Optional[bool], False): Indicates if all rate plans at the property provide all-inclusive amenities.
        some_rate_plans(Optional[bool], False): Indicates if some, but not all, rate plans at the property provide all-inclusive amenities.
        details(Optional[str], False): Details about amenities and services included in the all-inclusive rates.

    """

    all_rate_plans: Optional[bool] = None
    """
    Indicates if all rate plans at the property provide all-inclusive amenities.
    """
    some_rate_plans: Optional[bool] = None
    """
    Indicates if some, but not all, rate plans at the property provide all-inclusive amenities.
    """
    details: Optional[str] = None
    """
    Details about amenities and services included in the all-inclusive rates.
    """


class Brand(BaseModel):
    """pydantic model Brand: An individual brand.
    Attributes:
        id(Optional[str], False): Brand id.
        name(Optional[str], False): Brand name.

    """

    id: Optional[str] = None
    """
    Brand id.
    """
    name: Optional[str] = None
    """
    Brand name.
    """


class SpokenLanguage(BaseModel):
    """pydantic model SpokenLanguage: An individual spoken language.
    Attributes:
        id(Optional[str], False): The language code as a subset of BCP47 format, using the shortest ISO639 alpha language code and, optionally, ISO3166-1 alpha 2 country code.
        name(Optional[str], False): Spoken language name.

    """

    id: Optional[str] = None
    """
    The language code as a subset of BCP47 format, using the shortest ISO639 alpha language code and, optionally, ISO3166-1 alpha 2 country code.
    """
    name: Optional[str] = None
    """
    Spoken language name.
    """


class EnhancedHouseRules(BaseModel):
    """pydantic model EnhancedHouseRules
    Attributes:
        rule(Optional[str], False): Describes the house rule.
        additional_information(Optional[List[str]], False): List of strings detailing further information about the rule.

    """

    rule: Optional[str] = Field(None, example='Children allowed.')
    """
    Describes the house rule.
    """
    additional_information: Optional[List[str]] = Field(None, example=['Children allowed ages 13-17', 'Three children are possible if one is in a cot'])
    """
    List of strings detailing further information about the rule.
    """


class UnitConfiguration(BaseModel):
    """pydantic model UnitConfiguration: A room configuration.
    Attributes:
        type(Optional[str], False): Bed type.
        description(Optional[str], False): A description of the bed(s) in requested language.
        quantity(Optional[int], False): The number of beds of this size.

    """

    type: Optional[str] = None
    """
    Bed type.
    """
    description: Optional[str] = None
    """
    A description of the bed(s) in requested language.
    """
    quantity: Optional[int] = None
    """
    The number of beds of this size.
    """


class FieldModel(BaseModel):
    """pydantic model FieldModel: An individual field that had an error.
    Attributes:
        name(Optional[str], False): The field that had an error.
        type(Optional[str], False): The type of the field that had an error.
        value(Optional[str], False): The value of the field that had an error.

    """

    name: Optional[str] = None
    """
    The field that had an error.
    """
    type: Optional[str] = None
    """
    The type of the field that had an error.
    """
    value: Optional[str] = None
    """
    The value of the field that had an error.
    """


class ErrorIndividual(BaseModel):
    """pydantic model ErrorIndividual: An individual error.
    Attributes:
        type(Optional[str], False): The error type.
        message(Optional[str], False): A human readable message giving details about this error.
        fields(Optional[List[FieldModel]], False): Details about the specific fields that had an error.

    """

    type: Optional[str] = None
    """
    The error type.
    """
    message: Optional[str] = None
    """
    A human readable message giving details about this error.
    """
    fields: Optional[List[FieldModel]] = None
    """
    Details about the specific fields that had an error.
    """


class TripReason(Enum):
    """pydantic model TripReason: The reason category for this reviewer's trip.
    Attributes:
        business(Any, True): --
        leisure(Any, True): --
        friends_and_family(Any, True): --
        business_and_leisure(Any, True): --

    """

    business: Any = 'business'
    leisure: Any = 'leisure'
    friends_and_family: Any = 'friends_and_family'
    business_and_leisure: Any = 'business_and_leisure'


class TravelCompanion(Enum):
    """pydantic model TravelCompanion: The companion category for any travelers that accompanied this reviewer.
    Attributes:
        family(Any, True): --
        family_with_children(Any, True): --
        partner(Any, True): --
        self(Any, True): --
        friends(Any, True): --
        pet(Any, True): --

    """

    family: Any = 'family'
    family_with_children: Any = 'family_with_children'
    partner: Any = 'partner'
    self: Any = 'self'
    friends: Any = 'friends'
    pet: Any = 'pet'


class Link(BaseModel):
    """pydantic model Link: An individual link.
    Attributes:
        method(Optional[str], False): The request method used to access the link.
        href(Optional[str], False): The URL for the link. This can be absolute or relative.
        expires(Optional[str], False): If the link expires, this will be the UTC date the link will expire, in ISO 8601 format.

    """

    method: Optional[str] = None
    """
    The request method used to access the link.
    """
    href: Optional[str] = None
    """
    The URL for the link. This can be absolute or relative.
    """
    expires: Optional[str] = None
    """
    If the link expires, this will be the UTC date the link will expire, in ISO 8601 format.
    """


class PolygonCoordinate(BaseModel):
    """pydantic model PolygonCoordinate
    Attributes:
        __root__(List[Any], True): Individual coordinates as a geojson Point, in longitude, latitude order (x,y).

    """

    __root__: List[Any]
    """
    Individual coordinates as a geojson Point, in longitude, latitude order (x,y).
    """


class PolygonCoordinates(BaseModel):
    """pydantic model PolygonCoordinates: An array of linear ring coordinate arrays that combine to make up a single [Polygon](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6) in geojson format. If there is more than one linear ring at this level, the first is the outer boundary and the remaining linear rings are interior rings or holes.
    Attributes:
        __root__(List[List[List[Any]]], True): An array of linear ring coordinate arrays that combine to make up a single [Polygon](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6) in geojson format. If there is more than one linear ring at this level, the first is the outer boundary and the remaining linear rings are interior rings or holes.

    """

    __root__: List[List[List[Any]]]
    """
    An array of linear ring coordinate arrays that combine to make up a single [Polygon](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6) in geojson format. If there is more than one linear ring at this level, the first is the outer boundary and the remaining linear rings are interior rings or holes.
    """


class Ancestors(BaseModel):
    """pydantic model Ancestors: A region ancestor.
    Attributes:
        id(Optional[str], False): Id of ancestor region.
        type(Optional[str], False): Region type of ancestor region.

    """

    id: Optional[str] = None
    """
    Id of ancestor region.
    """
    type: Optional[str] = None
    """
    Region type of ancestor region.
    """


class PropertiesGeoJsonRequest(BaseModel):
    """pydantic model PropertiesGeoJsonRequest: GeoJSON geometry
    Attributes:
        type(str, True): The geometry type. The only supported type is `Polygon`
        coordinates(List[List[List[Any]]], True): An array of linear ring coordinate arrays that combine to make up a single [Polygon](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6) in geojson format. If there is more than one linear ring at this level, the first is the outer boundary and the remaining linear rings are interior rings or holes.

    """

    type: str
    """
    The geometry type. The only supported type is `Polygon`
    """
    coordinates: List[List[List[Any]]]
    """
    An array of linear ring coordinate arrays that combine to make up a single [Polygon](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6) in geojson format. If there is more than one linear ring at this level, the first is the outer boundary and the remaining linear rings are interior rings or holes.
    """


class PropertyGeography(BaseModel):
    """pydantic model PropertyGeography: A property object.
    Attributes:
        property_id(Optional[str], False): Unique Expedia property ID.

    """

    property_id: Optional[str] = None
    """
    Unique Expedia property ID.
    """


class Status(Enum):
    """pydantic model Status: Indicates the status of the rate. If the rate is still available then available will be returned. If the rate is no longer available at that price then price_changed will be returned. If the rate is no longer available at all then sold_out will be returned.
    Attributes:
        available(Any, True): --
        price_changed(Any, True): --
        sold_out(Any, True): --

    """

    available: Any = 'available'
    price_changed: Any = 'price_changed'
    sold_out: Any = 'sold_out'


class SaleScenario(BaseModel):
    """pydantic model SaleScenario: Provides the special scenarios that need to be taken into account when using this rate.
        Attributes:
            package(Optional[bool], False): If true, this rate has been provided to be bundled with car, air, etc. and displayed as a total package price.

    If shopping in a cross-sell scenario and using the cross-sell rate option, this indicates that the rate is a package rate available to be sold as an add-on to an existing itinerary.

            member(Optional[bool], False): If true, this rate has a "Member Only Deal" discount applied to the rate.

    Partners must be enabled to receive "Member Only Deals". If interested, partners should speak to their account representatives.

    This parameter can be used to merchandise if a "Member Only Deal" has been applied, which will help drive loyalty. In addition, it can be used by OTA's to create an opaque, but public shopping experience.

    This value will always be false for requests where the sales_environment is equal to "hotel_package".

            corporate(Optional[bool], False): If true, this rate is a corporate negotiated rate.  These rates provide additional value adds (e.g. free breakfast, free wifi, discount) and same-day cancellation.

            distribution(Optional[bool], False): If true, this rate is an EPS Optimized Distribution rate. These rates are procured exclusively for EPS distribution and may contain benefits such as larger marketing fee, less restrictive cancellation policies, additional value adds, or unique availability.


    """

    package: Optional[bool] = None
    """
    If true, this rate has been provided to be bundled with car, air, etc. and displayed as a total package price.

    If shopping in a cross-sell scenario and using the cross-sell rate option, this indicates that the rate is a package rate available to be sold as an add-on to an existing itinerary.

    """
    member: Optional[bool] = None
    """
    If true, this rate has a "Member Only Deal" discount applied to the rate.

    Partners must be enabled to receive "Member Only Deals". If interested, partners should speak to their account representatives.

    This parameter can be used to merchandise if a "Member Only Deal" has been applied, which will help drive loyalty. In addition, it can be used by OTA's to create an opaque, but public shopping experience.

    This value will always be false for requests where the sales_environment is equal to "hotel_package".

    """
    corporate: Optional[bool] = None
    """
    If true, this rate is a corporate negotiated rate.  These rates provide additional value adds (e.g. free breakfast, free wifi, discount) and same-day cancellation.

    """
    distribution: Optional[bool] = None
    """
    If true, this rate is an EPS Optimized Distribution rate. These rates are procured exclusively for EPS distribution and may contain benefits such as larger marketing fee, less restrictive cancellation policies, additional value adds, or unique availability.

    """


class RateLinks(BaseModel):
    """pydantic model RateLinks: A map of links, including a link to request payment options.
    Attributes:
        payment_options(Optional[Link], False): --

    """

    payment_options: Optional[Link] = None


class BedGroupAvailabilityLinks(BaseModel):
    """pydantic model BedGroupAvailabilityLinks: A map of links, including links to confirm pricing and availability for the selected rate.
    Attributes:
        price_check(Optional[Link], False): --

    """

    price_check: Optional[Link] = None


class Deal(BaseModel):
    """pydantic model Deal: The deal that applies to this rate.
    Attributes:
        id(Optional[str], False): Unique identifier for the deal.
        description(Optional[str], False): The description for the deal.

    """

    id: Optional[str] = None
    """
    Unique identifier for the deal.
    """
    description: Optional[str] = None
    """
    The description for the deal.
    """


class Deposit(BaseModel):
    """pydantic model Deposit: A deposit policy associated with the rate.
    Attributes:
        value(Optional[str], False): The amount that must be paid as a deposit.
        due(Optional[str], False): The due date in ISO 8601 format.
        currency(Optional[str], False): The currency for the deposit amount.

    """

    value: Optional[str] = None
    """
    The amount that must be paid as a deposit.
    """
    due: Optional[str] = None
    """
    The due date in ISO 8601 format.
    """
    currency: Optional[str] = None
    """
    The currency for the deposit amount.
    """


class PropertyAvailabilityLinks(BaseModel):
    """pydantic model PropertyAvailabilityLinks: A map of links, including links to request additional rates. Note that the recommendations feature has been retired and will return an error if the link is followed.
    Attributes:
        additional_rates(Optional[Link], False): --
        recommendations(Optional[Link], False): --

    """

    additional_rates: Optional[Link] = None
    recommendations: Optional[Link] = None


class StatusPriceCheck(Enum):
    """pydantic model StatusPriceCheck: Indicates the status of the rate. If the rate is still available then available will be returned. If the rate is no longer available at that price then price_changed will be returned. If the rate is no longer available at all then sold_out will be returned.
    Attributes:
        available(Any, True): --
        price_changed(Any, True): --
        sold_out(Any, True): --

    """

    available: Any = 'available'
    price_changed: Any = 'price_changed'
    sold_out: Any = 'sold_out'


class RoomPriceCheckLinks(BaseModel):
    """pydantic model RoomPriceCheckLinks: A map of links, including links to continue booking this rate or to shop for additional rates.

    If this rate is still available for booking then a book link will be present if PSD2 is not a requirement for you or a payment_session link will be present if PSD2 is a requirement for you.

        Attributes:
            book(Optional[Link], False): --
            payment_session(Optional[Link], False): --
            additional_rates(Optional[Link], False): --

    """

    book: Optional[Link] = None
    payment_session: Optional[Link] = None
    additional_rates: Optional[Link] = None


class AffiliateCollect(BaseModel):
    """pydantic model AffiliateCollect: This option will be returned if a booking can be made using Expedia Affiliate Collect.
    Attributes:
        name(Optional[str], False): Display name of payment option.

    """

    name: Optional[str] = None
    """
    Display name of payment option.
    """


class CardOption(BaseModel):
    """pydantic model CardOption
    Attributes:
        name(Optional[str], False): Brand name for the accepted credit or debit card. Use this value to determine which cards to display on your checkout page.
        processing_country(Optional[str], False): The country in which the payment will be processed.

    """

    name: Optional[str] = None
    """
    Brand name for the accepted credit or debit card. Use this value to determine which cards to display on your checkout page.
    """
    processing_country: Optional[str] = None
    """
    The country in which the payment will be processed.
    """


class CreditCardMerchant(BaseModel):
    """pydantic model CreditCardMerchant
    Attributes:
        name(Optional[str], False): Name of the merchant to use during 3rd party authorization for PSD2.

    """

    name: Optional[str] = None
    """
    Name of the merchant to use during 3rd party authorization for PSD2.
    """


class CheckInValidity(BaseModel):
    """pydantic model CheckInValidity
        Attributes:
            __root__(str, True): Enumeration indicating the capability of check-in on the date.

    `CHECKIN_VALID`: The associated date is valid for check in.

    `CHECKIN_INVALID`: Generic or Unknown reason for being not being a valid day for check in.

    `CHECKIN_INVALID_DUE_TO_BEING_IN_PAST`: The associated date is not valid for check in due to being in the past.

    `CHECKIN_INVALID_DUE_TO_MIN_PRIOR_NOTIFICATION`:  The associated date is not valid for check in because checking in on this date would not meet the owner's minimum prior notification requirements.

    `CHECKIN_INVALID_DUE_TO_MAX_FUTURE_BOOKING`: The associated date is not valid for check in because it is too far in the future.

    `CHECKIN_INVALID_DUE_TO_NOT_AVAILABLE`: The associated date is not valid for check in because it is not available (ie. the date is already reserved).

    `CHECKIN_INVALID_DUE_TO_NON_CHANGEOVER_DAY_OF_WEEK`: The associated date is not valid for check in because it falls on a day of the week that check in is prohibited.

    `CHECKIN_INVALID_DUE_TO_CHANGEOVER_EXCLUSION`: The associated date is not valid for check in because check in was prohibited on that specific date.

    `CHECKIN_INVALID_DUE_TO_MIN_STAY_NOT_ACHIEVABLE`: The associated date is not valid for check in because checking in on this date does not satisfy the minimum stay duration.

    `CHECKIN_INVALID_DUE_TO_NO_VALID_CHECKOUT_WITHIN_CONSTRAINTS`: The associated date is not valid for check in because there is not an associated check out date that would allow the stay to satisfy stay constraints.


    """

    __root__: str = Field(..., example='CHECKIN_VALID')
    """
    Enumeration indicating the capability of check-in on the date.

    `CHECKIN_VALID`: The associated date is valid for check in.

    `CHECKIN_INVALID`: Generic or Unknown reason for being not being a valid day for check in.

    `CHECKIN_INVALID_DUE_TO_BEING_IN_PAST`: The associated date is not valid for check in due to being in the past.

    `CHECKIN_INVALID_DUE_TO_MIN_PRIOR_NOTIFICATION`:  The associated date is not valid for check in because checking in on this date would not meet the owner's minimum prior notification requirements.

    `CHECKIN_INVALID_DUE_TO_MAX_FUTURE_BOOKING`: The associated date is not valid for check in because it is too far in the future.

    `CHECKIN_INVALID_DUE_TO_NOT_AVAILABLE`: The associated date is not valid for check in because it is not available (ie. the date is already reserved).

    `CHECKIN_INVALID_DUE_TO_NON_CHANGEOVER_DAY_OF_WEEK`: The associated date is not valid for check in because it falls on a day of the week that check in is prohibited.

    `CHECKIN_INVALID_DUE_TO_CHANGEOVER_EXCLUSION`: The associated date is not valid for check in because check in was prohibited on that specific date.

    `CHECKIN_INVALID_DUE_TO_MIN_STAY_NOT_ACHIEVABLE`: The associated date is not valid for check in because checking in on this date does not satisfy the minimum stay duration.

    `CHECKIN_INVALID_DUE_TO_NO_VALID_CHECKOUT_WITHIN_CONSTRAINTS`: The associated date is not valid for check in because there is not an associated check out date that would allow the stay to satisfy stay constraints.

    """


class CheckOutValidity(BaseModel):
    """pydantic model CheckOutValidity
        Attributes:
            __root__(str, True): Enumeration indicating the capability of check-out on the date.

    `CHECKOUT_VALID`: The associated date is valid for check out.

    `CHECKOUT_INVALID`: The checkout validity value is invalid or unknown.

    `CHECKOUT_INVALID_DUE_TO_NON_CHANGEOVER_DAY_OF_WEEK`: The associated date is not valid for check out because it falls on a day of the week that check out is prohibited.

    `CHECKOUT_INVALID_DUE_TO_CHANGEOVER_EXCLUSION`: The associated date is not valid for check out because check out was prohibited on that specific date.


    """

    __root__: str = Field(..., example='CHECKOUT_VALID')
    """
    Enumeration indicating the capability of check-out on the date.

    `CHECKOUT_VALID`: The associated date is valid for check out.

    `CHECKOUT_INVALID`: The checkout validity value is invalid or unknown.

    `CHECKOUT_INVALID_DUE_TO_NON_CHANGEOVER_DAY_OF_WEEK`: The associated date is not valid for check out because it falls on a day of the week that check out is prohibited.

    `CHECKOUT_INVALID_DUE_TO_CHANGEOVER_EXCLUSION`: The associated date is not valid for check out because check out was prohibited on that specific date.

    """


class StayConstraints(BaseModel):
    """pydantic model StayConstraints
    Attributes:
        min_stay(Optional[int], False): The minimum number of days for a stay.
        max_stay(Optional[int], False): The maximum number of days for a stay.

    """

    min_stay: Optional[int] = Field(None, example=1)
    """
    The minimum number of days for a stay.
    """
    max_stay: Optional[int] = Field(None, example=14)
    """
    The maximum number of days for a stay.
    """


class PreferredChallengeWindowSize(Enum):
    """pydantic model PreferredChallengeWindowSize: The preferred window size that needs to be displayed to the customer. Following are the possible values of this field:
    * `extra_small`: 250 x 400
    * `small`: 390 x 400
    * `medium`: 600 x 400
    * `large`: 500 x 600
    * `full_screen`: Full screen

      Attributes:
          extra_small(Any, True): --
          small(Any, True): --
          medium(Any, True): --
          large(Any, True): --
          full_screen(Any, True): --

    """

    extra_small: Any = 'extra_small'
    small: Any = 'small'
    medium: Any = 'medium'
    large: Any = 'large'
    full_screen: Any = 'full_screen'


class AuthenticationMethod(Enum):
    """pydantic model AuthenticationMethod: Mechanism used by the cardholder to authenticate to the merchant.
    Attributes:
        guest(Any, True): --
        own_credentials(Any, True): --
        federated_id(Any, True): --
        issuer_credentials(Any, True): --
        third_party_authentication(Any, True): --
        fido_authentication(Any, True): --

    """

    guest: Any = 'guest'
    own_credentials: Any = 'own_credentials'
    federated_id: Any = 'federated_id'
    issuer_credentials: Any = 'issuer_credentials'
    third_party_authentication: Any = 'third_party_authentication'
    fido_authentication: Any = 'fido_authentication'


class PaymentSessionsRequestCustomerAccountDetails(BaseModel):
    """pydantic model PaymentSessionsRequestCustomerAccountDetails
    Attributes:
        authentication_method(Optional[AuthenticationMethod], False): Mechanism used by the cardholder to authenticate to the merchant.
        authentication_timestamp(Optional[str], False): Date and time in UTC of the cardholder authentication, in extended ISO 8601 format.
        create_date(Optional[str], False): Date the cardholder opened the account with the merchant, in ISO 8601 format (YYYY-MM-DD).
        change_date(Optional[str], False): Date the cardholder’s account with the merchant was last changed, including Billing or Shipping address, new payment account, or new user(s) added, in ISO 8601 format (YYYY-MM-DD).
        password_change_date(Optional[str], False): Date the cardholder’s account with the merchant had a password change or account reset, in ISO 8601 format (YYYY-MM-DD).
        add_card_attempts(Optional[float], False): Number of add card attempts in the last 24 hours.
        account_purchases(Optional[float], False): Number of purchases with this cardholder's account during the previous six months.

    """

    authentication_method: Optional[AuthenticationMethod] = None
    """
    Mechanism used by the cardholder to authenticate to the merchant.
    """
    authentication_timestamp: Optional[str] = None
    """
    Date and time in UTC of the cardholder authentication, in extended ISO 8601 format.
    """
    create_date: Optional[str] = None
    """
    Date the cardholder opened the account with the merchant, in ISO 8601 format (YYYY-MM-DD).
    """
    change_date: Optional[str] = None
    """
    Date the cardholder’s account with the merchant was last changed, including Billing or Shipping address, new payment account, or new user(s) added, in ISO 8601 format (YYYY-MM-DD).
    """
    password_change_date: Optional[str] = None
    """
    Date the cardholder’s account with the merchant had a password change or account reset, in ISO 8601 format (YYYY-MM-DD).
    """
    add_card_attempts: Optional[float] = None
    """
    Number of add card attempts in the last 24 hours.
    """
    account_purchases: Optional[float] = None
    """
    Number of purchases with this cardholder's account during the previous six months.
    """


class Type(Enum):
    """pydantic model Type: Identifier for the type of payment. If affiliate_collect, card information is not required as EPS will not be processing the payment. However, billing contact information is still required.
    Attributes:
        corporate_card(Any, True): --
        customer_card(Any, True): --
        virtual_card(Any, True): --
        affiliate_collect(Any, True): --

    """

    corporate_card: Any = 'corporate_card'
    customer_card: Any = 'customer_card'
    virtual_card: Any = 'virtual_card'
    affiliate_collect: Any = 'affiliate_collect'


class BillingContactRequestAddress(BaseModel):
    """pydantic model BillingContactRequestAddress
    Attributes:
        line_1(Optional[str], False): First line of customer's street address. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
        line_2(Optional[str], False): Second line of customer's street address. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
        line_3(Optional[str], False): Third line of customer's street address. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
        city(Optional[str], False): Customer's city. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
        state_province_code(Optional[str], False): Customer's state or province code. Mandatory for AU, CA and US. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
        postal_code(Optional[str], False): Customer's postal code. Mandatory for CA, GB, and US. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
        country_code(str, True): Customer's country code, in two-letter ISO 3166-1 alpha-2 format. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.

    """

    line_1: Optional[str] = None
    """
    First line of customer's street address. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
    """
    line_2: Optional[str] = None
    """
    Second line of customer's street address. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
    """
    line_3: Optional[str] = None
    """
    Third line of customer's street address. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
    """
    city: Optional[str] = None
    """
    Customer's city. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
    """
    state_province_code: Optional[str] = None
    """
    Customer's state or province code. Mandatory for AU, CA and US. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
    """
    postal_code: Optional[str] = None
    """
    Customer's postal code. Mandatory for CA, GB, and US. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
    """
    country_code: str
    """
    Customer's country code, in two-letter ISO 3166-1 alpha-2 format. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded. Only ISO-8859-1 compliant characters are allowed.
    """


class ThirdPartyAuthRequest(BaseModel):
    """pydantic model ThirdPartyAuthRequest
        Attributes:
            cavv(str, True): Cryptographic element used to indicate Authentication was successfully performed

            eci(str, True): Electronic Commerce Indicator. The ECI is used in payer authentication to indicate the level of security used when the cardholder provided payment information to the merchant. Its value corresponds to the authentication result and the characteristics of the merchant checkout process. Each card network, e.g., Visa, MasterCard, JCB, has specific rules around the appropriate values and use of the ECI.

            three_ds_version(str, True): Indicates what version of 3DS was used to authenticate the user.

            ds_transaction_id(str, True): Directory Server Transaction Id. Returned during authentication and is used as an additional parameter to validate that transaction was authenticated.

            pa_res_status(Optional[str], False): set only if PAResStatus value is received in the authentication response

            ve_res_status(Optional[str], False): set this only if PAResStatus value is received in the authentication response
    if Authentication was Frictionless → AuthenticationResponse.PAResStatus,
    if Authentication was a successful challenge → "C" (This is the directory response for challenge)

            xid(Optional[str], False): String used by both Visa and MasterCard which identifies a specific transaction on the Directory
    This string value should remain consistent throughout a transaction's history.

            cavv_algorithm(Optional[str], False): Used in some scenarios for 3DS 1.0.

            ucaf_indicator(Optional[str], False): Only received for Mastercard transactions, else can be null.
    0 - Non-SecureCode transaction, bypassed by the Merchant
    1 - Merchant-Only SecureCode transaction
    2 - Fully authenticated SecureCode transaction


    """

    cavv: str
    """
    Cryptographic element used to indicate Authentication was successfully performed

    """
    eci: str
    """
    Electronic Commerce Indicator. The ECI is used in payer authentication to indicate the level of security used when the cardholder provided payment information to the merchant. Its value corresponds to the authentication result and the characteristics of the merchant checkout process. Each card network, e.g., Visa, MasterCard, JCB, has specific rules around the appropriate values and use of the ECI.

    """
    three_ds_version: str = Field(..., example='xxx')
    """
    Indicates what version of 3DS was used to authenticate the user.

    """
    ds_transaction_id: str
    """
    Directory Server Transaction Id. Returned during authentication and is used as an additional parameter to validate that transaction was authenticated.

    """
    pa_res_status: Optional[str] = None
    """
    set only if PAResStatus value is received in the authentication response

    """
    ve_res_status: Optional[str] = Field(None, example='C')
    """
    set this only if PAResStatus value is received in the authentication response
    if Authentication was Frictionless → AuthenticationResponse.PAResStatus,
    if Authentication was a successful challenge → "C" (This is the directory response for challenge)

    """
    xid: Optional[str] = None
    """
    String used by both Visa and MasterCard which identifies a specific transaction on the Directory
    This string value should remain consistent throughout a transaction's history.

    """
    cavv_algorithm: Optional[str] = None
    """
    Used in some scenarios for 3DS 1.0.

    """
    ucaf_indicator: Optional[str] = None
    """
    Only received for Mastercard transactions, else can be null.
    0 - Non-SecureCode transaction, bypassed by the Merchant
    1 - Merchant-Only SecureCode transaction
    2 - Fully authenticated SecureCode transaction

    """


class PaymentSessionsLinks(BaseModel):
    """pydantic model PaymentSessionsLinks: A map of links, including links to create a booking.
    Attributes:
        book(Optional[Link], False): --

    """

    book: Optional[Link] = None


class ItineraryLinks(BaseModel):
    """pydantic model ItineraryLinks: A map of links, including links to resume or cancel a held booking. This is only included for held bookings.
    Attributes:
        resume(Optional[Link], False): --
        cancel(Optional[Link], False): --

    """

    resume: Optional[Link] = None
    cancel: Optional[Link] = None


class Phone(BaseModel):
    """pydantic model Phone: The entire phone number must be represented across the three fields in this object.
    Attributes:
        country_code(Optional[str], False): The numerical portion of the country code from the phone number. Do not include the leading '+' character.
        area_code(Optional[str], False): The area code of the phone number.
        number(Optional[str], False): The remaining digits of the phone number.

    """

    country_code: Optional[str] = Field(None, example='1')
    """
    The numerical portion of the country code from the phone number. Do not include the leading '+' character.
    """
    area_code: Optional[str] = Field(None, example='487')
    """
    The area code of the phone number.
    """
    number: Optional[str] = Field(None, example='5550077')
    """
    The remaining digits of the phone number.
    """


class ConfirmationId(BaseModel):
    """pydantic model ConfirmationId: The confirmation ids.
    Attributes:
        expedia(Optional[str], False): The expedia confirmation id.
        property(Optional[str], False): The property confirmation id.

    """

    expedia: Optional[str] = None
    """
    The expedia confirmation id.
    """
    property: Optional[str] = None
    """
    The property confirmation id.
    """


class StatusItinerary(Enum):
    """pydantic model StatusItinerary: The booking status of the room.
    Attributes:
        pending(Any, True): --
        booked(Any, True): --
        canceled(Any, True): --

    """

    pending: Any = 'pending'
    booked: Any = 'booked'
    canceled: Any = 'canceled'


class CancelRefund(BaseModel):
    """pydantic model CancelRefund: The refund information for cancelling the itinerary.
    Attributes:
        amount(Optional[str], False): The amount of the refund on cancelling the itinerary.
        currency(Optional[str], False): The currency of the refund amount.

    """

    amount: Optional[str] = None
    """
    The amount of the refund on cancelling the itinerary.
    """
    currency: Optional[str] = None
    """
    The currency of the refund amount.
    """


class DepositItinerary(BaseModel):
    """pydantic model DepositItinerary: The deposit policy associated with the itinerary.
    Attributes:
        currency(Optional[str], False): The currency of the deposit.
        value(Optional[str], False): The amount required as deposit.
        due(Optional[str], False): The due date/time of the deposit.

    """

    currency: Optional[str] = None
    """
    The currency of the deposit.
    """
    value: Optional[str] = None
    """
    The amount required as deposit.
    """
    due: Optional[str] = None
    """
    The due date/time of the deposit.
    """


class RoomItineraryLinks(BaseModel):
    """pydantic model RoomItineraryLinks: A map of links, including links to cancel a room, or change a room's details.
    Attributes:
        cancel(Optional[Link], False): --
        change(Optional[Link], False): --

    """

    cancel: Optional[Link] = None
    change: Optional[Link] = None


class Address1(BaseModel):
    """pydantic model Address1
    Attributes:
        line_1(Optional[str], False): First line of street address.
        line_2(Optional[str], False): Second line of street address.
        line_3(Optional[str], False): Third line of street address.
        city(Optional[str], False): City where address is located.
        state_province_code(Optional[str], False): State or province code of address, if applicable.
        postal_code(Optional[str], False): Postal code of address, if applicable.
        country_code(Optional[str], False): Country code, in two-letter ISO 3166-1 alpha-2 format.

    """

    line_1: Optional[str] = Field(None, example='555 1st St.')
    """
    First line of street address.
    """
    line_2: Optional[str] = Field(None, example='10th Floor')
    """
    Second line of street address.
    """
    line_3: Optional[str] = Field(None, example='Unit 12')
    """
    Third line of street address.
    """
    city: Optional[str] = Field(None, example='Seattle')
    """
    City where address is located.
    """
    state_province_code: Optional[str] = Field(None, example='WA')
    """
    State or province code of address, if applicable.
    """
    postal_code: Optional[str] = Field(None, example='98121')
    """
    Postal code of address, if applicable.
    """
    country_code: Optional[str] = Field(None, example='US')
    """
    Country code, in two-letter ISO 3166-1 alpha-2 format.
    """


class Adjustment(BaseModel):
    """pydantic model Adjustment: Any price adjustments associated with this itinerary.
    Attributes:
        value(Optional[str], False): The amount of the adjustment.
        type(Optional[str], False): The type of the adjustment.
        currency(Optional[str], False): The currency of the adjustment.

    """

    value: Optional[str] = None
    """
    The amount of the adjustment.
    """
    type: Optional[str] = None
    """
    The type of the adjustment.
    """
    currency: Optional[str] = None
    """
    The currency of the adjustment.
    """


class Conversations(BaseModel):
    """pydantic model Conversations: Details about initiating conversations.
    Attributes:
        links(Optional[Dict[str, Link]], False): Contains urls for links to initiate conversations via EPS.

    """

    links: Optional[Dict[str, Link]] = None
    """
    Contains urls for links to initiate conversations via EPS.
    """


class SupplyContact(BaseModel):
    """pydantic model SupplyContact: The supply contact information. Note that full details may not be displayed until a short time prior to checkin.
    Attributes:
        name(Optional[str], False): The contact name.
        phone(Optional[Phone], False): --
        email(Optional[str], False): Email address for the contact.
        address(Optional[Address1], False): --

    """

    name: Optional[str] = Field(None, example='Pat Host')
    """
    The contact name.
    """
    phone: Optional[Phone] = None
    email: Optional[str] = Field(None, example='pat_host@ilovevrbo.com')
    """
    Email address for the contact.
    """
    address: Optional[Address1] = None


class Image1(BaseModel):
    """pydantic model Image1
    Attributes:
        url(Optional[str], False): The url of the image.
        width(Optional[str], False): The width of the image.
        height(Optional[str], False): The height of the image.

    """

    url: Optional[str] = Field(None, example='https://www.expedia.com/logo.svg')
    """
    The url of the image.
    """
    width: Optional[str] = Field(None, example='144')
    """
    The width of the image.
    """
    height: Optional[str] = Field(None, example='32')
    """
    The height of the image.
    """


class PhoneRequest(BaseModel):
    """pydantic model PhoneRequest: The entire phone number must be represented across the three fields in this object. The entire phone number should not exceed 25 characters.
    Attributes:
        country_code(str, True): The numerical portion of the country code from the phone number. Do not include the leading '+' character. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
        area_code(Optional[str], False): The area code of the phone number. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
        number(str, True): The remaining digits of the phone number. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.

    """

    country_code: str
    """
    The numerical portion of the country code from the phone number. Do not include the leading '+' character. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """
    area_code: Optional[str] = None
    """
    The area code of the phone number. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """
    number: str
    """
    The remaining digits of the phone number. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """


class CreateItineraryRequestRoom(BaseModel):
    """pydantic model CreateItineraryRequestRoom
    Attributes:
        given_name(str, True): First name of room guest. Max 60 characters. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
        family_name(str, True): Last name of room guest. Max 60 characters. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
        smoking(bool, True): Specify if the guest would prefer a smoking room. This field is only a request and the property is not guaranteed to honor it, it will not override any non-smoking policies by the hotel. Defaults to false.
        special_request(Optional[str], False): Special requests to send to hotel (not guaranteed). Do not use this field to communicate B2B customer service requests or pass any sensitive personal or financial information (PII). Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
        loyalty_id(Optional[str], False): A loyalty identifier for a hotel loyalty program associated with this room guest.

    """

    given_name: str
    """
    First name of room guest. Max 60 characters. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """
    family_name: str
    """
    Last name of room guest. Max 60 characters. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """
    smoking: bool
    """
    Specify if the guest would prefer a smoking room. This field is only a request and the property is not guaranteed to honor it, it will not override any non-smoking policies by the hotel. Defaults to false.
    """
    special_request: Optional[str] = None
    """
    Special requests to send to hotel (not guaranteed). Do not use this field to communicate B2B customer service requests or pass any sensitive personal or financial information (PII). Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """
    loyalty_id: Optional[str] = None
    """
    A loyalty identifier for a hotel loyalty program associated with this room guest.
    """


class ItineraryCreationLinks(BaseModel):
    """pydantic model ItineraryCreationLinks: A map of links, including links to retrieve a booking, resume a held booking, cancel a held booking, or complete a payment session if a challenge is used.
    Attributes:
        retrieve(Optional[Link], False): --
        resume(Optional[Link], False): --
        complete_payment_session(Optional[Link], False): --
        cancel(Optional[Link], False): --

    """

    retrieve: Optional[Link] = None
    resume: Optional[Link] = None
    complete_payment_session: Optional[Link] = None
    cancel: Optional[Link] = None


class CompletePaymentSessionLinks(BaseModel):
    """pydantic model CompletePaymentSessionLinks: A map of links, including links to retrieve a booking, resume a held booking, or cancel a held booking.
    Attributes:
        retrieve(Optional[Link], False): --
        resume(Optional[Link], False): --
        cancel(Optional[Link], False): --

    """

    retrieve: Optional[Link] = None
    resume: Optional[Link] = None
    cancel: Optional[Link] = None


class ChangeRoomDetailsRequest(BaseModel):
    """pydantic model ChangeRoomDetailsRequest
    Attributes:
        given_name(Optional[str], False): First name of room guest. Max 60 characters. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
        family_name(Optional[str], False): Last name of room guest. Max 60 characters. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
        smoking(Optional[bool], False): Specify if the guest would prefer a smoking room. This field is only a request and the property is not guaranteed to honor it, it will not override any non-smoking policies by the hotel. Defaults to false.
        special_request(Optional[str], False): Special requests to send to hotel (not guaranteed). Do not use this field to communicate B2B customer service requests or pass any sensitive personal or financial information (PII). Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
        loyalty_id(Optional[str], False): A loyalty identifier for a hotel loyalty program associated with this room guest.

    """

    given_name: Optional[str] = None
    """
    First name of room guest. Max 60 characters. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """
    family_name: Optional[str] = None
    """
    Last name of room guest. Max 60 characters. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """
    smoking: Optional[bool] = None
    """
    Specify if the guest would prefer a smoking room. This field is only a request and the property is not guaranteed to honor it, it will not override any non-smoking policies by the hotel. Defaults to false.
    """
    special_request: Optional[str] = None
    """
    Special requests to send to hotel (not guaranteed). Do not use this field to communicate B2B customer service requests or pass any sensitive personal or financial information (PII). Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """
    loyalty_id: Optional[str] = None
    """
    A loyalty identifier for a hotel loyalty program associated with this room guest.
    """


class Notification(BaseModel):
    """pydantic model Notification: A notification.
    Attributes:
        event_id(Optional[str], False): Unique identifier for each message
        event_type(Optional[str], False): An indication of what event caused the notification. This value can be used for message handling and routing. Refer to the list of event types for more information.
        event_time(Optional[str], False): Timestamp of the event notification, in UTC
        itinerary_id(Optional[str], False): The Itinerary ID of the affected booking
        email(Optional[str], False): The customer e-mail address associated with the affected itinerary
        message(Optional[str], False): Description of event notification
        affiliate_reference_id(Optional[str], False): The Affiliate Reference ID of the affected booking

    """

    event_id: Optional[str] = None
    """
    Unique identifier for each message
    """
    event_type: Optional[str] = None
    """
    An indication of what event caused the notification. This value can be used for message handling and routing. Refer to the list of event types for more information.
    """
    event_time: Optional[str] = None
    """
    Timestamp of the event notification, in UTC
    """
    itinerary_id: Optional[str] = None
    """
    The Itinerary ID of the affected booking
    """
    email: Optional[str] = None
    """
    The customer e-mail address associated with the affected itinerary
    """
    message: Optional[str] = None
    """
    Description of event notification
    """
    affiliate_reference_id: Optional[str] = None
    """
    The Affiliate Reference ID of the affected booking
    """


class TestNotificationRequest(BaseModel):
    """pydantic model TestNotificationRequest
    Attributes:
        event_type(str, True): The event type for which the test notification is requested.

    """

    event_type: str
    """
    The event type for which the test notification is requested.
    """


class CategoryAmenity(Enum):
    """pydantic model CategoryAmenity
    Attributes:
        accessibility(Any, True): --
        accessible_bathroom(Any, True): --
        accessible_parking(Any, True): --
        accessible_wheelchair(Any, True): --
        air_conditioning(Any, True): --
        airport_transfer(Any, True): --
        bar(Any, True): --
        casino(Any, True): --
        crib(Any, True): --
        dry_cleaning_laundry(Any, True): --
        dryer(Any, True): --
        free_airport_transfer(Any, True): --
        free_breakfast(Any, True): --
        free_wifi(Any, True): --
        gym(Any, True): --
        kitchen(Any, True): --
        meeting_facility(Any, True): --
        ocean_view(Any, True): --
        parking(Any, True): --
        pets_allowed(Any, True): --
        restaurant_in_hotel(Any, True): --
        spa_services(Any, True): --
        swimming_pool(Any, True): --
        washer(Any, True): --
        wifi(Any, True): --

    """

    accessibility: Any = 'accessibility'
    accessible_bathroom: Any = 'accessible_bathroom'
    accessible_parking: Any = 'accessible_parking'
    accessible_wheelchair: Any = 'accessible_wheelchair'
    air_conditioning: Any = 'air_conditioning'
    airport_transfer: Any = 'airport_transfer'
    bar: Any = 'bar'
    casino: Any = 'casino'
    crib: Any = 'crib'
    dry_cleaning_laundry: Any = 'dry_cleaning_laundry'
    dryer: Any = 'dryer'
    free_airport_transfer: Any = 'free_airport_transfer'
    free_breakfast: Any = 'free_breakfast'
    free_wifi: Any = 'free_wifi'
    gym: Any = 'gym'
    kitchen: Any = 'kitchen'
    meeting_facility: Any = 'meeting_facility'
    ocean_view: Any = 'ocean_view'
    parking: Any = 'parking'
    pets_allowed: Any = 'pets_allowed'
    restaurant_in_hotel: Any = 'restaurant_in_hotel'
    spa_services: Any = 'spa_services'
    swimming_pool: Any = 'swimming_pool'
    washer: Any = 'washer'
    wifi: Any = 'wifi'


class BedGroupConfiguration(BaseModel):
    """pydantic model BedGroupConfiguration: An individual bed configuration.
    Attributes:
        type(Optional[str], False): The type of this bed configuration in the room.
        size(Optional[str], False): The size of this bed configuration in the room.
        quantity(Optional[float], False): The number of this bed configuration in the room.

    """

    type: Optional[str] = None
    """
    The type of this bed configuration in the room.
    """
    size: Optional[str] = None
    """
    The size of this bed configuration in the room.
    """
    quantity: Optional[float] = None
    """
    The number of this bed configuration in the room.
    """


class MerchantOfRecord(Enum):
    """pydantic model MerchantOfRecord: * `expedia` - Payment is taken by Expedia.
    * `property` - Payment is taken by the property.

        Attributes:
            expedia(Any, True): --
            property(Any, True): --

    """

    expedia: Any = 'expedia'
    property: Any = 'property'


class CancelPenalty(BaseModel):
    """pydantic model CancelPenalty
    Attributes:
        currency(Optional[str], False): Currency of the amount object.
        start(Optional[str], False): Effective date and time of cancellation penalty in extended ISO 8601 format, with ±hh:mm timezone offset
        end(Optional[str], False): End date and time of cancellation penalty in extended ISO 8601 format, with ±hh:mm timezone offset
        amount(Optional[str], False): The monetary amount of the penalty.
        nights(Optional[str], False): Number of nights charged for as penalty.
        percent(Optional[str], False): Percentage of total booking charged for as penalty. A thirty percent penalty would be returned as 30%

    """

    currency: Optional[str] = None
    """
    Currency of the amount object.
    """
    start: Optional[str] = None
    """
    Effective date and time of cancellation penalty in extended ISO 8601 format, with ±hh:mm timezone offset
    """
    end: Optional[str] = None
    """
    End date and time of cancellation penalty in extended ISO 8601 format, with ±hh:mm timezone offset
    """
    amount: Optional[str] = None
    """
    The monetary amount of the penalty.
    """
    nights: Optional[str] = None
    """
    Number of nights charged for as penalty.
    """
    percent: Optional[str] = None
    """
    Percentage of total booking charged for as penalty. A thirty percent penalty would be returned as 30%
    """


class NonrefundableDateRange(BaseModel):
    """pydantic model NonrefundableDateRange
    Attributes:
        start(Optional[str], False): Start date of nonrefundable date range in ISO 8601 format.
        end(Optional[str], False): End date of nonrefundable date range in ISO 8601 format.

    """

    start: Optional[str] = None
    """
    Start date of nonrefundable date range in ISO 8601 format.
    """
    end: Optional[str] = None
    """
    End date of nonrefundable date range in ISO 8601 format.
    """


class NightChargeType(Enum):
    """pydantic model NightChargeType: The price breakout type.
    * `base_rate` - The room rate without any taxes and fees applied.
    * `tax_and_service_fee` - Tax recovery charges, service fees, and taxes. Ensure that you capture these values and display as:
                              "Taxes and Fees"
    * `extra_person_fee` - A per night fee that is charged by a hotel for additional adults over the nightly rate. This fee is included as part of the total.
    * `property_fee` - The property fee surcharge type must be displayed beginning on the initial hotel room selection page, immediately after your hotel search results page. This placement is required by the U.S. Federal Trade Commission (FTC).
                       Display this surcharge as "Property Fee" on your room selection page, as described above, and in all subsequent price breakdowns for the following Points of Sale:
                       * `US`
                       * `Canada`
                       * `Brazil`
                       * `LATAM`
    * `sales_tax` - Taxes that must be displayed by certain jurisdictional laws. Ensure that you capture these values and display as "Taxes".
    * `adjustment` - This is the amount that the individual night have been adjusted/discounted.
    * `recovery_charges_and_fees` - Tax recovery charges, service fees, and taxes. Ensure that you capture these values and display as:
                                    "Taxes and Fees"
    * `traveler_service_fee` - Fee charged by Vrbo to support use of online tools, services and functions on its platform which enable guest self service. May be displayed as 'Traveler Service Fee' or 'Service Fee' any time fees are broken out for display on partner sites.

      Attributes:
          base_rate(Any, True): --
          tax_and_service_fee(Any, True): --
          extra_person_fee(Any, True): --
          property_fee(Any, True): --
          sales_tax(Any, True): --
          adjustment(Any, True): --
          recovery_charges_and_fees(Any, True): --
          traveler_service_fee(Any, True): --

    """

    base_rate: Any = 'base_rate'
    tax_and_service_fee: Any = 'tax_and_service_fee'
    extra_person_fee: Any = 'extra_person_fee'
    property_fee: Any = 'property_fee'
    sales_tax: Any = 'sales_tax'
    adjustment: Any = 'adjustment'
    recovery_charges_and_fees: Any = 'recovery_charges_and_fees'
    traveler_service_fee: Any = 'traveler_service_fee'


class StayType(Enum):
    """pydantic model StayType: The price breakout type.
    Attributes:
        base_rate(Any, True): --
        tax_and_service_fee(Any, True): --
        extra_person_fee(Any, True): --
        property_fee(Any, True): --
        sales_tax(Any, True): --
        adjustment(Any, True): --
        recovery_charges_and_fees(Any, True): --
        traveler_service_fee(Any, True): --

    """

    base_rate: Any = 'base_rate'
    tax_and_service_fee: Any = 'tax_and_service_fee'
    extra_person_fee: Any = 'extra_person_fee'
    property_fee: Any = 'property_fee'
    sales_tax: Any = 'sales_tax'
    adjustment: Any = 'adjustment'
    recovery_charges_and_fees: Any = 'recovery_charges_and_fees'
    traveler_service_fee: Any = 'traveler_service_fee'


class Amount(BaseModel):
    """pydantic model Amount: The monetary amount.
    Attributes:
        value(Optional[str], False): The value of the amount object. Decimal point inline with correct precision.
        currency(Optional[str], False): Currency of the amount object.

    """

    value: Optional[str] = None
    """
    The value of the amount object. Decimal point inline with correct precision.
    """
    currency: Optional[str] = None
    """
    Currency of the amount object.
    """


class ChargeCalculated(BaseModel):
    """pydantic model ChargeCalculated: An object representing a charge. Information about the charge is provided in both the billable currency and the request currency.
    Attributes:
        billable_currency(Optional[Amount], False): --
        request_currency(Optional[Amount], False): --

    """

    billable_currency: Optional[Amount] = None
    request_currency: Optional[Amount] = None


class CategoryValueAdd(Enum):
    """pydantic model CategoryValueAdd: The general category that this value add promotion falls into.
    Attributes:
        food_and_beverage(Any, True): --
        entertainment(Any, True): --
        service(Any, True): --
        activity(Any, True): --
        credit(Any, True): --

    """

    food_and_beverage: Any = 'food_and_beverage'
    entertainment: Any = 'entertainment'
    service: Any = 'service'
    activity: Any = 'activity'
    credit: Any = 'credit'


class OfferType(Enum):
    """pydantic model OfferType: The type of offer this value add promotion is.
    Attributes:
        buy_one_get_one_free(Any, True): --
        credit(Any, True): --
        discount(Any, True): --
        free(Any, True): --
        voucher(Any, True): --

    """

    buy_one_get_one_free: Any = 'buy_one_get_one_free'
    credit: Any = 'credit'
    discount: Any = 'discount'
    free: Any = 'free'
    voucher: Any = 'voucher'


class Frequency(Enum):
    """pydantic model Frequency: The frequency of when this applies.
    Attributes:
        unknown(Any, True): --
        per_night(Any, True): --
        per_day(Any, True): --
        per_stay(Any, True): --
        per_week(Any, True): --
        round_trip(Any, True): --
        one_way(Any, True): --

    """

    unknown: Any = 'unknown'
    per_night: Any = 'per_night'
    per_day: Any = 'per_day'
    per_stay: Any = 'per_stay'
    per_week: Any = 'per_week'
    round_trip: Any = 'round_trip'
    one_way: Any = 'one_way'


class TraderName(BaseModel):
    """pydantic model TraderName
    Attributes:
        __root__(str, True): The trader name.

    """

    __root__: str = Field(..., example='Expedia')
    """
    The trader name.
    """


class TraderAddress(BaseModel):
    """pydantic model TraderAddress: The trader address.
    Attributes:
        line_1(Optional[str], False): First line of customer's street address.
        line_2(Optional[str], False): Second line of customer's street address.
        line_3(Optional[str], False): Third line of customer's street address.
        city(Optional[str], False): Customer's city.
        state_province_code(Optional[str], False): Customer's state or province code.
        postal_code(Optional[str], False): Customer's postal code.
        country_code(Optional[str], False): Customer's country code, in two-letter ISO 3166-1 alpha-2 format.

    """

    line_1: Optional[str] = Field(None, example='555 1st St')
    """
    First line of customer's street address.
    """
    line_2: Optional[str] = Field(None, example='10th Floor')
    """
    Second line of customer's street address.
    """
    line_3: Optional[str] = Field(None, example='Unit 12')
    """
    Third line of customer's street address.
    """
    city: Optional[str] = Field(None, example='Seattle')
    """
    Customer's city.
    """
    state_province_code: Optional[str] = Field(None, example='WA')
    """
    Customer's state or province code.
    """
    postal_code: Optional[str] = Field(None, example='98121')
    """
    Customer's postal code.
    """
    country_code: Optional[str] = Field(None, example='US')
    """
    Customer's country code, in two-letter ISO 3166-1 alpha-2 format.
    """


class TraderContactMessage(BaseModel):
    """pydantic model TraderContactMessage
    Attributes:
        __root__(str, True): The trader contact message.

    """

    __root__: str = Field(
        ..., example='This property is managed by a professional host. The provision of housing is linked to their trade, business or profession.'
    )
    """
    The trader contact message.
    """


class TraderRightToWithdrawMessage(BaseModel):
    """pydantic model TraderRightToWithdrawMessage
    Attributes:
        __root__(str, True): The trader right to withdraw message.

    """

    __root__: str = Field(
        ...,
        example="If you cancel your booking, you'll be subject to the property's cancellation policy. In accordance with EU regulations about consumer rights, property booking services are not subject to the right to withdraw.",
    )
    """
    The trader right to withdraw message.
    """


class TraderTermsAndConditions(BaseModel):
    """pydantic model TraderTermsAndConditions
    Attributes:
        __root__(str, True): The url linking to the full text terms and conditions.

    """

    __root__: str = Field(..., example='https://www.expedia.com/terms_and_conditions')
    """
    The url linking to the full text terms and conditions.
    """


class NightCharge1(BaseModel):
    """pydantic model NightCharge1
    Attributes:
        type(Optional[NightChargeType], False): --
        value(Optional[str], False): The value of the amount object. Decimal point inline with correct precision.
        currency(Optional[str], False): Currency of the amount object.

    """

    type: Optional[NightChargeType] = None
    value: Optional[str] = None
    """
    The value of the amount object. Decimal point inline with correct precision.
    """
    currency: Optional[str] = None
    """
    Currency of the amount object.
    """


class Stay1(BaseModel):
    """pydantic model Stay1
    Attributes:
        type(Optional[StayType], False): --
        value(Optional[str], False): The value of the amount object. Decimal point inline with correct precision.
        currency(Optional[str], False): Currency of the amount object.

    """

    type: Optional[StayType] = None
    value: Optional[str] = None
    """
    The value of the amount object. Decimal point inline with correct precision.
    """
    currency: Optional[str] = None
    """
    Currency of the amount object.
    """


class Charge1(BaseModel):
    """pydantic model Charge1: An object representing a charge. Information about the charge is provided in both the billable currency and the request currency.
    Attributes:
        billable_currency(Optional[Amount], False): --
        request_currency(Optional[Amount], False): --

    """

    billable_currency: Optional[Amount] = None
    request_currency: Optional[Amount] = None


class ChargeCalculated1(BaseModel):
    """pydantic model ChargeCalculated1: An object representing a charge. Information about the charge is provided in both the billable currency and the request currency.
    Attributes:
        billable_currency(Optional[Amount], False): --
        request_currency(Optional[Amount], False): --

    """

    billable_currency: Optional[Amount] = None
    request_currency: Optional[Amount] = None


class ValueAdd1(BaseModel):
    """pydantic model ValueAdd1: An individual value add.
    Attributes:
        id(Optional[str], False): Unique identifier for the value add promotion.
        description(Optional[str], False): A localized description of the value add promotion.
        category(Optional[CategoryValueAdd], False): --
        offer_type(Optional[OfferType], False): --
        frequency(Optional[Frequency], False): --
        person_count(Optional[float], False): Indicates how many guests the value add promotion applies to.

    """

    id: Optional[str] = None
    """
    Unique identifier for the value add promotion.
    """
    description: Optional[str] = None
    """
    A localized description of the value add promotion.
    """
    category: Optional[CategoryValueAdd] = None
    offer_type: Optional[OfferType] = None
    frequency: Optional[Frequency] = None
    person_count: Optional[float] = None
    """
    Indicates how many guests the value add promotion applies to.
    """


class TraderDetailsInner(BaseModel):
    """pydantic model TraderDetailsInner: Information of the professional entity that sells the property inventory or related services.
    Attributes:
        name(Optional[str], False): The trader name.
        address(Optional[TraderAddress], False): --
        contact_message(str, True): The trader contact message.
        right_to_withdraw_message(Optional[str], False): The trader right to withdraw message.
        email(Optional[str], False): The trader email address.
        phone(Optional[str], False): The trader phone number.

    """

    name: Optional[str] = Field(None, example='Expedia')
    """
    The trader name.
    """
    address: Optional[TraderAddress] = None
    contact_message: str = Field(
        ..., example='This property is managed by a professional host. The provision of housing is linked to their trade, business or profession.'
    )
    """
    The trader contact message.
    """
    right_to_withdraw_message: Optional[str] = Field(
        None,
        example="If you cancel your booking, you'll be subject to the property's cancellation policy. In accordance with EU regulations about consumer rights, property booking services are not subject to the right to withdraw.",
    )
    """
    The trader right to withdraw message.
    """
    email: Optional[str] = Field(None, example='travel@support.expedia.com')
    """
    The trader email address.
    """
    phone: Optional[str] = Field(None, example='0330-123-1235')
    """
    The trader phone number.
    """


class IncludeEnum(Enum):
    """pydantic model IncludeEnum
    Attributes:
        property_ids(Any, True): --
        catalog(Any, True): --
        address(Any, True): --

    """

    property_ids: Any = 'property_ids'
    catalog: Any = 'catalog'
    address: Any = 'address'


class GetPropertyContentBusinessModel(Enum):
    """pydantic model GetPropertyContentBusinessModel
    Attributes:
        expedia_collect(Any, True): --
        property_collect(Any, True): --

    """

    expedia_collect: Any = 'expedia_collect'
    property_collect: Any = 'property_collect'


class GetPropertyContentInclude(Enum):
    """pydantic model GetPropertyContentInclude
    Attributes:
        property_ids(Any, True): --
        catalog(Any, True): --
        address(Any, True): --

    """

    property_ids: Any = 'property_ids'
    catalog: Any = 'catalog'
    address: Any = 'address'


class GetRegionsInclude(Enum):
    """pydantic model GetRegionsInclude
    Attributes:
        standard(Any, True): --
        details(Any, True): --
        property_ids(Any, True): --
        property_ids_expanded(Any, True): --

    """

    standard: Any = 'standard'
    details: Any = 'details'
    property_ids: Any = 'property_ids'
    property_ids_expanded: Any = 'property_ids_expanded'


class GetRegionInclude(Enum):
    """pydantic model GetRegionInclude
    Attributes:
        details(Any, True): --
        property_ids(Any, True): --
        property_ids_expanded(Any, True): --

    """

    details: Any = 'details'
    property_ids: Any = 'property_ids'
    property_ids_expanded: Any = 'property_ids_expanded'


class PropertiesGeographyPostResponse(BaseModel):
    """pydantic model PropertiesGeographyPostResponse: A map of property ids to property objects.
    Attributes:
        __root__(Optional[Dict[str, PropertyGeography]], False): --

    """

    __root__: Optional[Dict[str, PropertyGeography]] = None


class Test(Enum):
    """pydantic model Test
    Attributes:
        standard(Any, True): --
        service_unavailable(Any, True): --
        unknown_internal_error(Any, True): --

    """

    standard: Any = 'standard'
    service_unavailable: Any = 'service_unavailable'
    unknown_internal_error: Any = 'unknown_internal_error'


class ExclusionEnum(Enum):
    """pydantic model ExclusionEnum
    Attributes:
        refundable_damage_deposit(Any, True): --

    """

    refundable_damage_deposit: Any = 'refundable_damage_deposit'


class Filter(Enum):
    """pydantic model Filter
    Attributes:
        refundable(Any, True): --
        expedia_collect(Any, True): --
        property_collect(Any, True): --

    """

    refundable: Any = 'refundable'
    expedia_collect: Any = 'expedia_collect'
    property_collect: Any = 'property_collect'


class RateOption(Enum):
    """pydantic model RateOption
    Attributes:
        member(Any, True): --
        net_rates(Any, True): --
        cross_sell(Any, True): --

    """

    member: Any = 'member'
    net_rates: Any = 'net_rates'
    cross_sell: Any = 'cross_sell'


class Exclusion(Enum):
    """pydantic model Exclusion
    Attributes:
        refundable_damage_deposit(Any, True): --

    """

    refundable_damage_deposit: Any = 'refundable_damage_deposit'


class Localized(BaseModel):
    """pydantic model Localized: Container for localized address information.
    Attributes:
        links(Optional[Dict[str, Link]], False): Keyed by the language, a map of links to the property’s localized address(es) based on the primary language(s) spoken in the property’s country. Only languages supported by the Rapid API are provided.

    """

    links: Optional[Dict[str, Link]] = None
    """
    Keyed by the language, a map of links to the property’s localized address(es) based on the primary language(s) spoken in the property’s country. Only languages supported by the Rapid API are provided.
    """


class Ratings(BaseModel):
    """pydantic model Ratings: Various types of ratings for this property.
    Attributes:
        property(Optional[PropertyRating], False): --
        guest(Optional[GuestRating], False): --

    """

    property: Optional[PropertyRating] = None
    guest: Optional[GuestRating] = None


class Location(BaseModel):
    """pydantic model Location: The property's location information.
    Attributes:
        coordinates(Optional[Coordinates], False): --

    """

    coordinates: Optional[Coordinates] = None


class Attributes(BaseModel):
    """pydantic model Attributes: Attributes about the property. See our [attributes reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known attribute ID and name values.
    Attributes:
        general(Optional[Dict[str, Attribute]], False): Lists all of the general attributes about the property.
        pets(Optional[Dict[str, Attribute]], False): Lists all of the pet attributes about the property.

    """

    general: Optional[Dict[str, Attribute]] = None
    """
    Lists all of the general attributes about the property.
    """
    pets: Optional[Dict[str, Attribute]] = None
    """
    Lists all of the pet attributes about the property.
    """


class Image(BaseModel):
    """pydantic model Image: An individual image. See our [image categories reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known caption and category values.
    Attributes:
        hero_image(Optional[bool], False): Whether this image is a hero image or not.
        category(Optional[float], False): The category of the image.
        caption(Optional[str], False): The image caption.
        links(Optional[Dict[str, Link]], False): Contains urls for all of the image sizes available. Sizes may include: 70 px, 200px, 350 px, and 1,000 px

    """

    hero_image: Optional[bool] = None
    """
    Whether this image is a hero image or not.
    """
    category: Optional[float] = None
    """
    The category of the image.
    """
    caption: Optional[str] = None
    """
    The image caption.
    """
    links: Optional[Dict[str, Link]] = None
    """
    Contains urls for all of the image sizes available. Sizes may include: 70 px, 200px, 350 px, and 1,000 px
    """


class OnsitePayments(BaseModel):
    """pydantic model OnsitePayments: The property’s accepted forms of payments when onsite. See our [onsite payment types reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known payment type ID and name values.
    Attributes:
        currency(Optional[str], False): The currency accepted at the property.
        types(Optional[Dict[str, PaymentType]], False): The types of payments accepted at the property.

    """

    currency: Optional[str] = None
    """
    The currency accepted at the property.
    """
    types: Optional[Dict[str, PaymentType]] = None
    """
    The types of payments accepted at the property.
    """


class BedGroup(BaseModel):
    """pydantic model BedGroup: An individual bed group.
    Attributes:
        id(Optional[str], False): Unique identifier for a bed group.
        description(Optional[str], False): This is a display ready description of a bed configuration for this room.
        configuration(Optional[List[BedGroupConfiguration]], False): An array of bed configurations for this room.

    """

    id: Optional[str] = None
    """
    Unique identifier for a bed group.
    """
    description: Optional[str] = None
    """
    This is a display ready description of a bed configuration for this room.
    """
    configuration: Optional[List[BedGroupConfiguration]] = None
    """
    An array of bed configurations for this room.
    """


class Occupancy(BaseModel):
    """pydantic model Occupancy: Occupancy information.
    Attributes:
        max_allowed(Optional[MaxAllowed], False): --
        age_categories(Optional[Dict[str, CategoryAge]], False): Map of the age categories used to determine the maximum children and adult occupancy.

    """

    max_allowed: Optional[MaxAllowed] = None
    age_categories: Optional[Dict[str, CategoryAge]] = None
    """
    Map of the age categories used to determine the maximum children and adult occupancy.
    """


class AssociatedAirports(BaseModel):
    """pydantic model AssociatedAirports: Airports related to the property.
    Attributes:
        preferred(Optional[Preferred], False): --

    """

    preferred: Optional[Preferred] = None


class Chain(BaseModel):
    """pydantic model Chain: An individual chain.
    Attributes:
        id(Optional[str], False): Chain id.
        name(Optional[str], False): Chain name.
        brands(Optional[Dict[str, Brand]], False): Map of the chain's brands.

    """

    id: Optional[str] = None
    """
    Chain id.
    """
    name: Optional[str] = None
    """
    Chain name.
    """
    brands: Optional[Dict[str, Brand]] = None
    """
    Map of the chain's brands.
    """


class PropertyManagerLinks(BaseModel):
    """pydantic model PropertyManagerLinks: A map of links, including link to get image of the property manager.
    Attributes:
        image(Optional[Link], False): --

    """

    image: Optional[Link] = None


class RentalAgreementLinks(BaseModel):
    """pydantic model RentalAgreementLinks: A map of links, including link to get the rental agreement.
    Attributes:
        rental_agreement(Optional[Link], False): --

    """

    rental_agreement: Optional[Link] = None


class Error(BaseModel):
    """pydantic model Error: The overall class of error that occured.
    Attributes:
        type(Optional[str], False): The error type.
        message(Optional[str], False): A human readable message giving details about this error.
        fields(Optional[List[FieldModel]], False): Details about the specific fields that had an error.
        errors(Optional[List[ErrorIndividual]], False): An array of all the actual errors that occured.

    """

    type: Optional[str] = None
    """
    The error type.
    """
    message: Optional[str] = None
    """
    A human readable message giving details about this error.
    """
    fields: Optional[List[FieldModel]] = None
    """
    Details about the specific fields that had an error.
    """
    errors: Optional[List[ErrorIndividual]] = None
    """
    An array of all the actual errors that occured.
    """


class Review(BaseModel):
    """pydantic model Review: A review object for a property.
    Attributes:
        verification_source(Optional[str], False): Where this review has been verified from.
        title(Optional[str], False): Title of this review.
        date_submitted(Optional[str], False): When this review was made, in ISO 8601 format.
        rating(Optional[str], False): The rating for this property given by the reviewer. Returns a value between 1.0 and 5.0.
        reviewer_name(Optional[str], False): The name of the person who wrote this review.
        trip_reason(Optional[TripReason], False): --
        travel_companion(Optional[TravelCompanion], False): --
        text(Optional[str], False): The text of the review itself.

    """

    verification_source: Optional[str] = None
    """
    Where this review has been verified from.
    """
    title: Optional[str] = None
    """
    Title of this review.
    """
    date_submitted: Optional[str] = None
    """
    When this review was made, in ISO 8601 format.
    """
    rating: Optional[str] = None
    """
    The rating for this property given by the reviewer. Returns a value between 1.0 and 5.0.
    """
    reviewer_name: Optional[str] = None
    """
    The name of the person who wrote this review.
    """
    trip_reason: Optional[TripReason] = None
    travel_companion: Optional[TravelCompanion] = None
    text: Optional[str] = None
    """
    The text of the review itself.
    """


class BedGroupAvailability(BaseModel):
    """pydantic model BedGroupAvailability
    Attributes:
        links(Optional[BedGroupAvailabilityLinks], False): --
        id(Optional[str], False): Unique identifier for a bed group.
        description(Optional[str], False): This is a display ready description of a bed configuration for this room.
        configuration(Optional[List[BedGroupConfiguration]], False): The bed configuration for a given room. This array can be empty for the related bed group.

    """

    links: Optional[BedGroupAvailabilityLinks] = None
    id: Optional[str] = None
    """
    Unique identifier for a bed group.
    """
    description: Optional[str] = None
    """
    This is a display ready description of a bed configuration for this room.
    """
    configuration: Optional[List[BedGroupConfiguration]] = None
    """
    The bed configuration for a given room. This array can be empty for the related bed group.
    """


class CreditCard(BaseModel):
    """pydantic model CreditCard
    Attributes:
        card_options(Optional[List[CardOption]], False): --
        merchant(Optional[CreditCardMerchant], False): --
        name(Optional[str], False): Display name of payment option.

    """

    card_options: Optional[List[CardOption]] = None
    merchant: Optional[CreditCardMerchant] = None
    name: Optional[str] = None
    """
    Display name of payment option.
    """


class Day(BaseModel):
    """pydantic model Day
        Attributes:
            date(Optional[date], False): Date associated to the provided information.
            available(Optional[bool], False): True if the property is available on the date.
            checkin(Optional[str], False): Enumeration indicating the capability of check-in on the date.

    `CHECKIN_VALID`: The associated date is valid for check in.

    `CHECKIN_INVALID`: Generic or Unknown reason for being not being a valid day for check in.

    `CHECKIN_INVALID_DUE_TO_BEING_IN_PAST`: The associated date is not valid for check in due to being in the past.

    `CHECKIN_INVALID_DUE_TO_MIN_PRIOR_NOTIFICATION`:  The associated date is not valid for check in because checking in on this date would not meet the owner's minimum prior notification requirements.

    `CHECKIN_INVALID_DUE_TO_MAX_FUTURE_BOOKING`: The associated date is not valid for check in because it is too far in the future.

    `CHECKIN_INVALID_DUE_TO_NOT_AVAILABLE`: The associated date is not valid for check in because it is not available (ie. the date is already reserved).

    `CHECKIN_INVALID_DUE_TO_NON_CHANGEOVER_DAY_OF_WEEK`: The associated date is not valid for check in because it falls on a day of the week that check in is prohibited.

    `CHECKIN_INVALID_DUE_TO_CHANGEOVER_EXCLUSION`: The associated date is not valid for check in because check in was prohibited on that specific date.

    `CHECKIN_INVALID_DUE_TO_MIN_STAY_NOT_ACHIEVABLE`: The associated date is not valid for check in because checking in on this date does not satisfy the minimum stay duration.

    `CHECKIN_INVALID_DUE_TO_NO_VALID_CHECKOUT_WITHIN_CONSTRAINTS`: The associated date is not valid for check in because there is not an associated check out date that would allow the stay to satisfy stay constraints.

            checkout(Optional[str], False): Enumeration indicating the capability of check-out on the date.

    `CHECKOUT_VALID`: The associated date is valid for check out.

    `CHECKOUT_INVALID`: The checkout validity value is invalid or unknown.

    `CHECKOUT_INVALID_DUE_TO_NON_CHANGEOVER_DAY_OF_WEEK`: The associated date is not valid for check out because it falls on a day of the week that check out is prohibited.

    `CHECKOUT_INVALID_DUE_TO_CHANGEOVER_EXCLUSION`: The associated date is not valid for check out because check out was prohibited on that specific date.

            stay_constraints(Optional[StayConstraints], False): --

    """

    date: Optional[date] = None
    """
    Date associated to the provided information.
    """
    available: Optional[bool] = None
    """
    True if the property is available on the date.
    """
    checkin: Optional[str] = Field(None, example='CHECKIN_VALID')
    """
    Enumeration indicating the capability of check-in on the date.

    `CHECKIN_VALID`: The associated date is valid for check in.

    `CHECKIN_INVALID`: Generic or Unknown reason for being not being a valid day for check in.

    `CHECKIN_INVALID_DUE_TO_BEING_IN_PAST`: The associated date is not valid for check in due to being in the past.

    `CHECKIN_INVALID_DUE_TO_MIN_PRIOR_NOTIFICATION`:  The associated date is not valid for check in because checking in on this date would not meet the owner's minimum prior notification requirements.

    `CHECKIN_INVALID_DUE_TO_MAX_FUTURE_BOOKING`: The associated date is not valid for check in because it is too far in the future.

    `CHECKIN_INVALID_DUE_TO_NOT_AVAILABLE`: The associated date is not valid for check in because it is not available (ie. the date is already reserved).

    `CHECKIN_INVALID_DUE_TO_NON_CHANGEOVER_DAY_OF_WEEK`: The associated date is not valid for check in because it falls on a day of the week that check in is prohibited.

    `CHECKIN_INVALID_DUE_TO_CHANGEOVER_EXCLUSION`: The associated date is not valid for check in because check in was prohibited on that specific date.

    `CHECKIN_INVALID_DUE_TO_MIN_STAY_NOT_ACHIEVABLE`: The associated date is not valid for check in because checking in on this date does not satisfy the minimum stay duration.

    `CHECKIN_INVALID_DUE_TO_NO_VALID_CHECKOUT_WITHIN_CONSTRAINTS`: The associated date is not valid for check in because there is not an associated check out date that would allow the stay to satisfy stay constraints.

    """
    checkout: Optional[str] = Field(None, example='CHECKOUT_VALID')
    """
    Enumeration indicating the capability of check-out on the date.

    `CHECKOUT_VALID`: The associated date is valid for check out.

    `CHECKOUT_INVALID`: The checkout validity value is invalid or unknown.

    `CHECKOUT_INVALID_DUE_TO_NON_CHANGEOVER_DAY_OF_WEEK`: The associated date is not valid for check out because it falls on a day of the week that check out is prohibited.

    `CHECKOUT_INVALID_DUE_TO_CHANGEOVER_EXCLUSION`: The associated date is not valid for check out because check out was prohibited on that specific date.

    """
    stay_constraints: Optional[StayConstraints] = None


class BillingContactRequest(BaseModel):
    """pydantic model BillingContactRequest
    Attributes:
        given_name(str, True): First/given name of the payment type account holder. Max 60 characters. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
        family_name(str, True): Last/family name of the payment type account holder. Max 60 characters. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
        address(BillingContactRequestAddress, True): --

    """

    given_name: str
    """
    First/given name of the payment type account holder. Max 60 characters. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """
    family_name: str
    """
    Last/family name of the payment type account holder. Max 60 characters. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """
    address: BillingContactRequestAddress


class PaymentSessions(BaseModel):
    """pydantic model PaymentSessions: The payment registration response.
    Attributes:
        payment_session_id(Optional[str], False): The registered payment session ID.
        encoded_init_config(Optional[str], False): A base64 encoded object which contains configuration needed to perform device fingerprinting. It is used in conjunction with the provided Javascript library for PSD2.
        links(Optional[PaymentSessionsLinks], False): --

    """

    payment_session_id: Optional[str] = None
    """
    The registered payment session ID.
    """
    encoded_init_config: Optional[str] = None
    """
    A base64 encoded object which contains configuration needed to perform device fingerprinting. It is used in conjunction with the provided Javascript library for PSD2.
    """
    links: Optional[PaymentSessionsLinks] = None


class PromotionsItinerary(BaseModel):
    """pydantic model PromotionsItinerary: Promotions that apply to the booked room.
    Attributes:
        value_adds(Optional[Dict[str, ValueAdd1]], False): Promotions provided by the property that add value to the stay, but don’t affect the booking price (i.e., ski lift tickets or premium wifi).

    """

    value_adds: Optional[Dict[str, ValueAdd1]] = None
    """
    Promotions provided by the property that add value to the stay, but don’t affect the booking price (i.e., ski lift tickets or premium wifi).
    """


class BillingContact(BaseModel):
    """pydantic model BillingContact
    Attributes:
        given_name(Optional[str], False): First/given name of the payment type account holder.
        family_name(Optional[str], False): Last/family name of the payment type account holder.
        address(Optional[Address1], False): --

    """

    given_name: Optional[str] = None
    """
    First/given name of the payment type account holder.
    """
    family_name: Optional[str] = None
    """
    Last/family name of the payment type account holder.
    """
    address: Optional[Address1] = None


class Essential(BaseModel):
    """pydantic model Essential
    Attributes:
        name(Optional[str], False): The name of the essential item.
        instructions(Optional[str], False): The instructions for use of the essential item.
        additional_info(Optional[Dict[str, str]], False): A map of additional information that needs to be conveyed to customer.
        images(Optional[List[Image1]], False): An array of images needed for the essential item.

    """

    name: Optional[str] = Field(None, example='access')
    """
    The name of the essential item.
    """
    instructions: Optional[str] = Field(None, example='Use the smart lock located at the side door for access.')
    """
    The instructions for use of the essential item.
    """
    additional_info: Optional[Dict[str, str]] = Field(None, example={'access_type': 'Smart lock', 'access_code': '12345'})
    """
    A map of additional information that needs to be conveyed to customer.
    """
    images: Optional[List[Image1]] = None
    """
    An array of images needed for the essential item.
    """


class Amenity(BaseModel):
    """pydantic model Amenity: An individual amenity.
    Attributes:
        id(Optional[str], False): The amenity definition ID for this amenity.
        name(Optional[str], False): Amenity name.
        value(Optional[str], False): Amenity value.
        categories(Optional[List[CategoryAmenity]], False): This is an optional field and will be present only if the amenity falls into one or more of these amenity categories.

    """

    id: Optional[str] = None
    """
    The amenity definition ID for this amenity.
    """
    name: Optional[str] = None
    """
    Amenity name.
    """
    value: Optional[str] = None
    """
    Amenity value.
    """
    categories: Optional[List[CategoryAmenity]] = None
    """
    This is an optional field and will be present only if the amenity falls into one or more of these amenity categories.
    """


class NightCharge(BaseModel):
    """pydantic model NightCharge
    Attributes:
        type(Optional[NightChargeType], False): --
        value(Optional[str], False): The value of the amount object. Decimal point inline with correct precision.
        currency(Optional[str], False): Currency of the amount object.

    """

    type: Optional[NightChargeType] = None
    value: Optional[str] = None
    """
    The value of the amount object. Decimal point inline with correct precision.
    """
    currency: Optional[str] = None
    """
    Currency of the amount object.
    """


class Stay(BaseModel):
    """pydantic model Stay
    Attributes:
        type(Optional[StayType], False): --
        value(Optional[str], False): The value of the amount object. Decimal point inline with correct precision.
        currency(Optional[str], False): Currency of the amount object.

    """

    type: Optional[StayType] = None
    value: Optional[str] = None
    """
    The value of the amount object. Decimal point inline with correct precision.
    """
    currency: Optional[str] = None
    """
    Currency of the amount object.
    """


class Charge(BaseModel):
    """pydantic model Charge: An object representing a charge. Information about the charge is provided in both the billable currency and the request currency.
    Attributes:
        billable_currency(Optional[Amount], False): --
        request_currency(Optional[Amount], False): --

    """

    billable_currency: Optional[Amount] = None
    request_currency: Optional[Amount] = None


class FeesPricingInformation(BaseModel):
    """pydantic model FeesPricingInformation: The fees collected by the property. The values for each type of fee are the total for that type.

    Mandatory fees are collected by the property at check-in or check-out.
    Resort fees are charged for amenities and extras and collected by the property at check-in or check-out.
    Mandatory taxes are taxes collected by the property at check-in or check-out.

        Attributes:
            mandatory_fee(Optional[ChargeCalculated], False): --
            resort_fee(Optional[ChargeCalculated], False): --
            mandatory_tax(Optional[ChargeCalculated], False): --

    """

    mandatory_fee: Optional[ChargeCalculated] = None
    resort_fee: Optional[ChargeCalculated] = None
    mandatory_tax: Optional[ChargeCalculated] = None


class ValueAdd(BaseModel):
    """pydantic model ValueAdd: An individual value add.
    Attributes:
        id(Optional[str], False): Unique identifier for the value add promotion.
        description(Optional[str], False): A localized description of the value add promotion.
        category(Optional[CategoryValueAdd], False): --
        offer_type(Optional[OfferType], False): --
        frequency(Optional[Frequency], False): --
        person_count(Optional[float], False): Indicates how many guests the value add promotion applies to.

    """

    id: Optional[str] = None
    """
    Unique identifier for the value add promotion.
    """
    description: Optional[str] = None
    """
    A localized description of the value add promotion.
    """
    category: Optional[CategoryValueAdd] = None
    offer_type: Optional[OfferType] = None
    frequency: Optional[Frequency] = None
    person_count: Optional[float] = None
    """
    Indicates how many guests the value add promotion applies to.
    """


class TraderInformation(BaseModel):
    """pydantic model TraderInformation: The professional entity or entities that sells the property inventory or related services.
    Attributes:
        traders(Optional[List[TraderDetailsInner]], False): An array of traders.
        terms_and_conditions(str, True): The url linking to the full text terms and conditions.

    """

    traders: Optional[List[TraderDetailsInner]] = None
    """
    An array of traders.
    """
    terms_and_conditions: str = Field(..., example='https://www.expedia.com/terms_and_conditions')
    """
    The url linking to the full text terms and conditions.
    """


class TraderDetails(BaseModel):
    """pydantic model TraderDetails: An array of traders.
    Attributes:
        __root__(List[TraderDetailsInner], True): An array of traders.

    """

    __root__: List[TraderDetailsInner]
    """
    An array of traders.
    """


class TraderInformation1(BaseModel):
    """pydantic model TraderInformation1: The professional entity or entities that sells the property inventory or related services.
    Attributes:
        traders(Optional[List[TraderDetailsInner]], False): An array of traders.
        terms_and_conditions(str, True): The url linking to the full text terms and conditions.

    """

    traders: Optional[List[TraderDetailsInner]] = None
    """
    An array of traders.
    """
    terms_and_conditions: str = Field(..., example='https://www.expedia.com/terms_and_conditions')
    """
    The url linking to the full text terms and conditions.
    """


class Totals1(BaseModel):
    """pydantic model Totals1: The total price of charges, given various critera.

    Inclusive provides the total price including taxes and fees.  This does not include hotel collected fees such as resort, mandatory taxes, and mandatory fees.
    Exclusive provides the total price excluding taxes and fees.
    Strikethrough provides the tax exclusive total price with any hotel funded discounts added back. Can be used to merchandise the savings due to a discount.
    Marketing fee provides the potential owed earnings per transaction.
    Gross profit provides the estimated gross profit per transaction.
    Minimum selling price provides the minimum selling price.
    Property fees provides the total of the fees collected by the property.

        Attributes:
            inclusive(Optional[Charge1], False): --
            exclusive(Optional[Charge1], False): --
            strikethrough(Optional[Charge1], False): --
            marketing_fee(Optional[Charge1], False): --
            gross_profit(Optional[Charge1], False): --
            minimum_selling_price(Optional[Charge1], False): --
            property_fees(Optional[Charge1], False): --

    """

    inclusive: Optional[Charge1] = None
    exclusive: Optional[Charge1] = None
    strikethrough: Optional[Charge1] = None
    marketing_fee: Optional[Charge1] = None
    gross_profit: Optional[Charge1] = None
    minimum_selling_price: Optional[Charge1] = None
    property_fees: Optional[Charge1] = None


class FeesPricingInformation1(BaseModel):
    """pydantic model FeesPricingInformation1: The fees collected by the property. The values for each type of fee are the total for that type.

    Mandatory fees are collected by the property at check-in or check-out.
    Resort fees are charged for amenities and extras and collected by the property at check-in or check-out.
    Mandatory taxes are taxes collected by the property at check-in or check-out.

        Attributes:
            mandatory_fee(Optional[ChargeCalculated1], False): --
            resort_fee(Optional[ChargeCalculated1], False): --
            mandatory_tax(Optional[ChargeCalculated1], False): --

    """

    mandatory_fee: Optional[ChargeCalculated1] = None
    resort_fee: Optional[ChargeCalculated1] = None
    mandatory_tax: Optional[ChargeCalculated1] = None


class GuestReviewsVerified(BaseModel):
    """pydantic model GuestReviewsVerified: A property's verified guest reviews.
    Attributes:
        recent(Optional[List[Review]], False): A collection of the guest reviews which have been verified, in order, starting with the newest.

    """

    recent: Optional[List[Review]] = None
    """
    A collection of the guest reviews which have been verified, in order, starting with the newest.
    """


class ChainsGetResponse(BaseModel):
    """pydantic model ChainsGetResponse
    Attributes:
        __root__(Optional[Dict[str, Chain]], False): --

    """

    __root__: Optional[Dict[str, Chain]] = None


class Address(BaseModel):
    """pydantic model Address: Container for the property's address information.
    Attributes:
        line_1(Optional[str], False): Address line 1.
        line_2(Optional[str], False): Address line 2.
        city(Optional[str], False): City.
        state_province_code(Optional[str], False): 2-letter or 3-letter state/province code for Australia, Canada and the USA.
        state_province_name(Optional[str], False): Text name of the State/Province - more common for additional countries.
        postal_code(Optional[str], False): Postal/zip code.
        country_code(Optional[str], False): 2-letter country code, in ISO 3166-1 alpha-2 format.
        obfuscation_required(Optional[bool], False): Flag to indicate whether a property address requires obfuscation before the property has been booked. If true, only the city, province, and country of the address can be shown to the customer.
        localized(Optional[Localized], False): --

    """

    line_1: Optional[str] = Field(None, example='123 Main St')
    """
    Address line 1.
    """
    line_2: Optional[str] = Field(None, example='Apt A')
    """
    Address line 2.
    """
    city: Optional[str] = Field(None, example='Springfield')
    """
    City.
    """
    state_province_code: Optional[str] = Field(None, example='MO')
    """
    2-letter or 3-letter state/province code for Australia, Canada and the USA.
    """
    state_province_name: Optional[str] = Field(None, example='Missouri')
    """
    Text name of the State/Province - more common for additional countries.
    """
    postal_code: Optional[str] = Field(None, example='65804')
    """
    Postal/zip code.
    """
    country_code: Optional[str] = Field(None, example='US')
    """
    2-letter country code, in ISO 3166-1 alpha-2 format.
    """
    obfuscation_required: Optional[bool] = Field(None, example=False)
    """
    Flag to indicate whether a property address requires obfuscation before the property has been booked. If true, only the city, province, and country of the address can be shown to the customer.
    """
    localized: Optional[Localized] = None


class RoomContent(BaseModel):
    """pydantic model RoomContent: An individual room.
    Attributes:
        id(Optional[str], False): Unique identifier for a room type.
        name(Optional[str], False): Room type name.
        descriptions(Optional[DescriptionsRoom], False): --
        amenities(Optional[Dict[str, Amenity]], False): Lists all of the amenities available in the room. See our [amenities reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known amenity ID and name values.
        images(Optional[List[Image]], False): The room's images. Contains all room images available.
        bed_groups(Optional[Dict[str, BedGroup]], False): A map of the room's bed groups.
        area(Optional[Area], False): --
        views(Optional[Dict[str, View]], False): A map of the room views. See our [view reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known room view ID and name values.
        occupancy(Optional[Occupancy], False): --

    """

    id: Optional[str] = None
    """
    Unique identifier for a room type.
    """
    name: Optional[str] = None
    """
    Room type name.
    """
    descriptions: Optional[DescriptionsRoom] = None
    amenities: Optional[Dict[str, Amenity]] = None
    """
    Lists all of the amenities available in the room. See our [amenities reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known amenity ID and name values.
    """
    images: Optional[List[Image]] = None
    """
    The room's images. Contains all room images available.
    """
    bed_groups: Optional[Dict[str, BedGroup]] = None
    """
    A map of the room's bed groups.
    """
    area: Optional[Area] = None
    views: Optional[Dict[str, View]] = None
    """
    A map of the room views. See our [view reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known room view ID and name values.
    """
    occupancy: Optional[Occupancy] = None


class RateContent(BaseModel):
    """pydantic model RateContent: An individual rate.
    Attributes:
        id(Optional[str], False): Unique identifier for a rate.
        amenities(Optional[Dict[str, Amenity]], False): This lists all of the Amenities available with a specific rate, including value adds, such as breakfast. See our [amenities reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known amenity ID and name values.
        special_offer_description(Optional[str], False): A text description of any special offers for this rate.

    """

    id: Optional[str] = None
    """
    Unique identifier for a rate.
    """
    amenities: Optional[Dict[str, Amenity]] = None
    """
    This lists all of the Amenities available with a specific rate, including value adds, such as breakfast. See our [amenities reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known amenity ID and name values.
    """
    special_offer_description: Optional[str] = None
    """
    A text description of any special offers for this rate.
    """


class PropertyManager(BaseModel):
    """pydantic model PropertyManager: Information about the property manager.
    Attributes:
        name(Optional[str], False): The name of the property manager.
        links(Optional[PropertyManagerLinks], False): --

    """

    name: Optional[str] = None
    """
    The name of the property manager.
    """
    links: Optional[PropertyManagerLinks] = None


class RentalAgreement(BaseModel):
    """pydantic model RentalAgreement: Information about a vacation rentals rental agreement.
    Attributes:
        links(Optional[RentalAgreementLinks], False): --

    """

    links: Optional[RentalAgreementLinks] = None


class GuestReviews(BaseModel):
    """pydantic model GuestReviews: A property's guest reviews.
    Attributes:
        verified(Optional[GuestReviewsVerified], False): --

    """

    verified: Optional[GuestReviewsVerified] = None


class Promotions(BaseModel):
    """pydantic model Promotions: Available promotions that apply to this rate.
    Attributes:
        value_adds(Optional[Dict[str, ValueAdd]], False): A collection of value adds that apply to this rate.
        deal(Optional[Deal], False): --

    """

    value_adds: Optional[Dict[str, ValueAdd]] = None
    """
    A collection of value adds that apply to this rate.
    """
    deal: Optional[Deal] = None


class PaymentOption(BaseModel):
    """pydantic model PaymentOption: The payment option response.
    Attributes:
        affiliate_collect(Optional[AffiliateCollect], False): --
        credit_card(Optional[CreditCard], False): --

    """

    affiliate_collect: Optional[AffiliateCollect] = None
    credit_card: Optional[CreditCard] = None


class PropertyCalendarAvailability(BaseModel):
    """pydantic model PropertyCalendarAvailability
    Attributes:
        property_id(Optional[str], False): Expedia property ID.
        days(Optional[List[Day]], False): --

    """

    property_id: Optional[str] = Field(None, example='123456')
    """
    Expedia property ID.
    """
    days: Optional[List[Day]] = None


class PaymentRequest(BaseModel):
    """pydantic model PaymentRequest
    Attributes:
        type(Type, True): Identifier for the type of payment. If affiliate_collect, card information is not required as EPS will not be processing the payment. However, billing contact information is still required.
        number(Optional[str], False): Card number. Required for credit card transactions.
        security_code(Optional[str], False): CVV/CSV code from the back of the customer's card. Required for credit card transactions.
        expiration_month(Optional[str], False): Two-digit month the credit card will expire. Required for credit card transactions.
        expiration_year(Optional[str], False): Year the credit card will expire. Required for credit card transactions.
        billing_contact(BillingContactRequest, True): --
        third_party_authentication(Optional[ThirdPartyAuthRequest], False): --
        enrollment_date(Optional[str], False): Date the payment account was enrolled in the cardholder's account with the merchant, in ISO 8601 format (YYYY-MM-DD).

    """

    type: Type
    """
    Identifier for the type of payment. If affiliate_collect, card information is not required as EPS will not be processing the payment. However, billing contact information is still required.
    """
    number: Optional[str] = None
    """
    Card number. Required for credit card transactions.
    """
    security_code: Optional[str] = None
    """
    CVV/CSV code from the back of the customer's card. Required for credit card transactions.
    """
    expiration_month: Optional[str] = None
    """
    Two-digit month the credit card will expire. Required for credit card transactions.
    """
    expiration_year: Optional[str] = None
    """
    Year the credit card will expire. Required for credit card transactions.
    """
    billing_contact: BillingContactRequest
    third_party_authentication: Optional[ThirdPartyAuthRequest] = None
    enrollment_date: Optional[str] = None
    """
    Date the payment account was enrolled in the cardholder's account with the merchant, in ISO 8601 format (YYYY-MM-DD).
    """


class EssentialInformation(BaseModel):
    """pydantic model EssentialInformation: Essential information, including the supply contact information and any other essential information.
    Attributes:
        contact(Optional[SupplyContact], False): --
        essentials(Optional[List[Essential]], False): --
        update_available_date(Optional[str], False): The date and time when new essential information is available for retrieval, in extended ISO 8601 format, with ±hh:mm timezone offset.

    """

    contact: Optional[SupplyContact] = None
    essentials: Optional[List[Essential]] = None
    update_available_date: Optional[str] = Field(None, example='2022-08-12T11:59:00-08:00')
    """
    The date and time when new essential information is available for retrieval, in extended ISO 8601 format, with ±hh:mm timezone offset.
    """


class CreateItineraryRequest(BaseModel):
    """pydantic model CreateItineraryRequest
    Attributes:
        affiliate_reference_id(Optional[str], False): Your unique reference value. This field supports a maximum of 28 characters and is required to be unique (if provided). Entering special characters ("<", ">", "(", ")", and "&") in this field will result in the request being rejected.
        hold(Optional[bool], False): Flag for placing a booking on hold. The booking will be released if the resume link is not followed within the hold period. Please refer to our Hold and Resume documentation.
        email(str, True): Email address for the customer. Must adhere to standard RFC 822 email format. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
        phone(PhoneRequest, True): --
        rooms(List[CreateItineraryRequestRoom], True): --
        payments(Optional[List[PaymentRequest]], False): Required if payment information prior to booking was not submitted. If register payments was called prior to this call, do not submit payment information again.
        affiliate_metadata(Optional[str], False): Field that stores up to 256 characters of additional metadata with the itinerary. Will be returned on all retrieve responses for this itinerary. The data must be in the format 'key1:value|key2:value|key3:value'. Other Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
        tax_registration_number(Optional[str], False): The customer's taxpayer identification number that is provided by the government to nationals or resident aliens. This number should be collected from individuals that pay taxes or participate in activities that provide revenue for one or more tax types. Note: This value is only needed from Brazilian and Indian customers.
        traveler_handling_instructions(Optional[str], False): Custom traveler handling instructions for the hotel. Do not include PCI sensitive data, such as credit card numbers, in this field.

    """

    affiliate_reference_id: Optional[str] = None
    """
    Your unique reference value. This field supports a maximum of 28 characters and is required to be unique (if provided). Entering special characters ("<", ">", "(", ")", and "&") in this field will result in the request being rejected.
    """
    hold: Optional[bool] = None
    """
    Flag for placing a booking on hold. The booking will be released if the resume link is not followed within the hold period. Please refer to our Hold and Resume documentation.
    """
    email: str
    """
    Email address for the customer. Must adhere to standard RFC 822 email format. Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """
    phone: PhoneRequest
    rooms: List[CreateItineraryRequestRoom]
    payments: Optional[List[PaymentRequest]] = None
    """
    Required if payment information prior to booking was not submitted. If register payments was called prior to this call, do not submit payment information again.
    """
    affiliate_metadata: Optional[str] = None
    """
    Field that stores up to 256 characters of additional metadata with the itinerary. Will be returned on all retrieve responses for this itinerary. The data must be in the format 'key1:value|key2:value|key3:value'. Other Special characters ("<", ">", "(", ")", and "&") entered in this field will be re-encoded.
    """
    tax_registration_number: Optional[str] = None
    """
    The customer's taxpayer identification number that is provided by the government to nationals or resident aliens. This number should be collected from individuals that pay taxes or participate in activities that provide revenue for one or more tax types. Note: This value is only needed from Brazilian and Indian customers.
    """
    traveler_handling_instructions: Optional[str] = None
    """
    Custom traveler handling instructions for the hotel. Do not include PCI sensitive data, such as credit card numbers, in this field.
    """


class ItineraryCreation(BaseModel):
    """pydantic model ItineraryCreation: The book response.
    Attributes:
        itinerary_id(Optional[str], False): The itinerary id.
        links(Optional[ItineraryCreationLinks], False): --
        encoded_challenge_config(Optional[str], False): The challenge config that is required to perform payment challenge. This field will be available when payment challenge is needed.
        trader_information(Optional[TraderInformation1], False): --

    """

    itinerary_id: Optional[str] = None
    """
    The itinerary id.
    """
    links: Optional[ItineraryCreationLinks] = None
    encoded_challenge_config: Optional[str] = None
    """
    The challenge config that is required to perform payment challenge. This field will be available when payment challenge is needed.
    """
    trader_information: Optional[TraderInformation1] = None


class CompletePaymentSession(BaseModel):
    """pydantic model CompletePaymentSession: The payment session response.
    Attributes:
        itinerary_id(Optional[str], False): The itinerary id.
        links(Optional[CompletePaymentSessionLinks], False): --
        trader_information(Optional[TraderInformation1], False): --

    """

    itinerary_id: Optional[str] = None
    """
    The itinerary id.
    """
    links: Optional[CompletePaymentSessionLinks] = None
    trader_information: Optional[TraderInformation1] = None


class Totals(BaseModel):
    """pydantic model Totals: The total price of charges, given various critera.

    Inclusive provides the total price including taxes and fees.  This does not include hotel collected fees such as resort, mandatory taxes, and mandatory fees.
    Exclusive provides the total price excluding taxes and fees.
    Strikethrough provides the tax exclusive total price with any hotel funded discounts added back. Can be used to merchandise the savings due to a discount.
    Marketing fee provides the potential owed earnings per transaction.
    Gross profit provides the estimated gross profit per transaction.
    Minimum selling price provides the minimum selling price.
    Property fees provides the total of the fees collected by the property.

        Attributes:
            inclusive(Optional[Charge], False): --
            exclusive(Optional[Charge], False): --
            strikethrough(Optional[Charge], False): --
            marketing_fee(Optional[Charge], False): --
            gross_profit(Optional[Charge], False): --
            minimum_selling_price(Optional[Charge], False): --
            property_fees(Optional[Charge], False): --

    """

    inclusive: Optional[Charge] = None
    exclusive: Optional[Charge] = None
    strikethrough: Optional[Charge] = None
    marketing_fee: Optional[Charge] = None
    gross_profit: Optional[Charge] = None
    minimum_selling_price: Optional[Charge] = None
    property_fees: Optional[Charge] = None


class PricingInformation1(BaseModel):
    """pydantic model PricingInformation1: The pricing information object.
    Attributes:
        nightly(Optional[List[List[NightCharge1]]], False): Array of arrays of amount objects. Each sub-array of amount objects represents a single night's charges.
        stay(Optional[List[Stay1]], False): Array of amount objects. Details any charges that apply to the entire stay (not divided per-night). Any per-room adjustments are applied to the `base_rate` amount within this object.
        totals(Optional[Totals1], False): --
        fees(Optional[FeesPricingInformation1], False): --

    """

    nightly: Optional[List[List[NightCharge1]]] = None
    """
    Array of arrays of amount objects. Each sub-array of amount objects represents a single night's charges.
    """
    stay: Optional[List[Stay1]] = None
    """
    Array of amount objects. Details any charges that apply to the entire stay (not divided per-night). Any per-room adjustments are applied to the `base_rate` amount within this object.
    """
    totals: Optional[Totals1] = None
    fees: Optional[FeesPricingInformation1] = None


class VacationRentalDetails(BaseModel):
    """pydantic model VacationRentalDetails: Details for vacation rental properties.
    Attributes:
        registry_number(Optional[str], False): The property's registry number required by some jurisdictions.
        private_host(Optional[bool], False): Indicates if a property has a private host.
        property_manager(Optional[PropertyManager], False): --
        rental_agreement(Optional[RentalAgreement], False): --
        house_rules(Optional[List[str]], False): List of strings detailing house rules.
        enhanced_house_rules(Optional[Dict[str, EnhancedHouseRules]], False): Map of enhanced house rules.
        amenities(Optional[Amenity], False): --
        vrbo_srp_id(Optional[str], False): The Vrbo srp needed for link-off.
        listing_id(Optional[str], False): The listing id for a Vrbo property.
        listing_number(Optional[str], False): The listing number for a Vrbo property.
        listing_source(Optional[str], False): The listing source.
        listing_unit(Optional[str], False): The specific unit.
        unit_configurations(Optional[Dict[str, List[UnitConfiguration]]], False): Map of the vacation rental unit configurations. The key value is the unit location.

    """

    registry_number: Optional[str] = None
    """
    The property's registry number required by some jurisdictions.
    """
    private_host: Optional[bool] = None
    """
    Indicates if a property has a private host.
    """
    property_manager: Optional[PropertyManager] = None
    rental_agreement: Optional[RentalAgreement] = None
    house_rules: Optional[List[str]] = None
    """
    List of strings detailing house rules.
    """
    enhanced_house_rules: Optional[Dict[str, EnhancedHouseRules]] = Field(
        None,
        example={
            'Children': {'rule': 'Children allowed', 'additional_information': ['Children allowed under age 13.', 'Multiple children must sleep on cots.']},
            'Pets': {'rule': 'Pets allowed', 'additional_information': ['Pets must be kept on the balcony.']},
        },
    )
    """
    Map of enhanced house rules.
    """
    amenities: Optional[Amenity] = None
    vrbo_srp_id: Optional[str] = None
    """
    The Vrbo srp needed for link-off.
    """
    listing_id: Optional[str] = None
    """
    The listing id for a Vrbo property.
    """
    listing_number: Optional[str] = None
    """
    The listing number for a Vrbo property.
    """
    listing_source: Optional[str] = None
    """
    The listing source.
    """
    listing_unit: Optional[str] = None
    """
    The specific unit.
    """
    unit_configurations: Optional[Dict[str, List[UnitConfiguration]]] = Field(
        None,
        example={
            '1': [
                {'type': 'TWIN_SINGLE_BED', 'description': 'Twin/Single bed(s) -', 'quantity': 1},
                {'type': 'CHILD_BED', 'description': 'Child bed(s) -', 'quantity': 1},
            ],
            '2': [{'type': 'QUEEN_BED', 'description': 'Queen bed(s) -', 'quantity': 1}],
            'Other1': [{'type': 'CHILD_BED', 'description': 'Child bed(s) -', 'quantity': 3}],
        },
    )
    """
    Map of the vacation rental unit configurations. The key value is the unit location.
    """


class PaymentSessionsRequest(BaseModel):
    """pydantic model PaymentSessionsRequest
      Attributes:
          version(str, True): The version of the EgPayments.js library.
          browser_accept_header(str, True): The customer's browser accept header that was used in the booking request.
          encoded_browser_metadata(str, True): Encoded browser metadata, provided by the EgPayments.js library.
          preferred_challenge_window_size(PreferredChallengeWindowSize, True): The preferred window size that needs to be displayed to the customer. Following are the possible values of this field:
    * `extra_small`: 250 x 400
    * `small`: 390 x 400
    * `medium`: 600 x 400
    * `large`: 500 x 600
    * `full_screen`: Full screen

          merchant_url(str, True): Fully qualified URL of merchant website or customer care site.
          customer_account_details(PaymentSessionsRequestCustomerAccountDetails, True): --
          payments(List[PaymentRequest], True): --

    """

    version: str
    """
    The version of the EgPayments.js library.
    """
    browser_accept_header: str
    """
    The customer's browser accept header that was used in the booking request.
    """
    encoded_browser_metadata: str
    """
    Encoded browser metadata, provided by the EgPayments.js library.
    """
    preferred_challenge_window_size: PreferredChallengeWindowSize
    """
    The preferred window size that needs to be displayed to the customer. Following are the possible values of this field:
      * `extra_small`: 250 x 400
      * `small`: 390 x 400
      * `medium`: 600 x 400
      * `large`: 500 x 600
      * `full_screen`: Full screen

    """
    merchant_url: str
    """
    Fully qualified URL of merchant website or customer care site.
    """
    customer_account_details: PaymentSessionsRequestCustomerAccountDetails
    payments: List[PaymentRequest]


class RateItinerary(BaseModel):
    """pydantic model RateItinerary: The rate information associated with the itinerary.
    Attributes:
        id(Optional[str], False): The id of the rate.
        merchant_of_record(Optional[MerchantOfRecord], False): --
        refundable(Optional[bool], False): Indicates whether the itinerary is refundable or not.
        cancel_refund(Optional[CancelRefund], False): --
        amenities(Optional[List[str]], False): --
        promotions(Optional[PromotionsItinerary], False): --
        cancel_penalties(Optional[List[CancelPenalty]], False): The cancel penalties associated with the itinerary.
        nonrefundable_date_ranges(Optional[List[NonrefundableDateRange]], False): A list of date exceptions. Dates within these ranges provide no refund on cancellation, regardless of cancel penalty windows.
        deposits(Optional[List[DepositItinerary]], False): --
        card_on_file_limit(Optional[Amount], False): --
        refundable_damage_deposit(Optional[Amount], False): --
        pricing(Optional[PricingInformation1], False): --

    """

    id: Optional[str] = None
    """
    The id of the rate.
    """
    merchant_of_record: Optional[MerchantOfRecord] = None
    refundable: Optional[bool] = None
    """
    Indicates whether the itinerary is refundable or not.
    """
    cancel_refund: Optional[CancelRefund] = None
    amenities: Optional[List[str]] = None
    promotions: Optional[PromotionsItinerary] = None
    cancel_penalties: Optional[List[CancelPenalty]] = None
    """
    The cancel penalties associated with the itinerary.
    """
    nonrefundable_date_ranges: Optional[List[NonrefundableDateRange]] = None
    """
    A list of date exceptions. Dates within these ranges provide no refund on cancellation, regardless of cancel penalty windows.
    """
    deposits: Optional[List[DepositItinerary]] = None
    card_on_file_limit: Optional[Amount] = None
    refundable_damage_deposit: Optional[Amount] = None
    pricing: Optional[PricingInformation1] = None


class PricingInformation(BaseModel):
    """pydantic model PricingInformation: The pricing information object.
    Attributes:
        nightly(Optional[List[List[NightCharge]]], False): Array of arrays of amount objects. Each sub-array of amount objects represents a single night's charges.
        stay(Optional[List[Stay]], False): Array of amount objects. Details any charges that apply to the entire stay (not divided per-night). Any per-room adjustments are applied to the `base_rate` amount within this object.
        totals(Optional[Totals], False): --
        fees(Optional[FeesPricingInformation], False): --

    """

    nightly: Optional[List[List[NightCharge]]] = None
    """
    Array of arrays of amount objects. Each sub-array of amount objects represents a single night's charges.
    """
    stay: Optional[List[Stay]] = None
    """
    Array of amount objects. Details any charges that apply to the entire stay (not divided per-night). Any per-room adjustments are applied to the `base_rate` amount within this object.
    """
    totals: Optional[Totals] = None
    fees: Optional[FeesPricingInformation] = None


class PropertyContent(BaseModel):
    """pydantic model PropertyContent: An individual property object in the map of property objects.
    Attributes:
        property_id(Optional[str], False): Unique Expedia property ID.
        name(Optional[str], False): Property name.
        address(Optional[Address], False): --
        ratings(Optional[Ratings], False): --
        location(Optional[Location], False): --
        phone(Optional[str], False): The property's phone number.
        fax(Optional[str], False): The property's fax number.
        category(Optional[CategoryProperty], False): --
        business_model(Optional[BusinessModel], False): --
        rank(Optional[float], False): The property’s rank across all properties. This value sorts properties based on EPS transactional data and details about the property, with 1 indicating the best-performing property and others following in ascending numerical order.
        checkin(Optional[Checkin], False): --
        checkout(Optional[Checkout], False): --
        fees(Optional[Fees], False): --
        policies(Optional[Policies], False): --
        attributes(Optional[Attributes], False): --
        amenities(Optional[Dict[str, Amenity]], False): Lists all of the amenities available for all guests at the property. See our [amenities reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known amenity ID and name values.
        images(Optional[List[Image]], False): Contains all property images available.
        onsite_payments(Optional[OnsitePayments], False): --
        rooms(Optional[Dict[str, RoomContent]], False): Information about all of the rooms at the property.
        rates(Optional[Dict[str, RateContent]], False): Additional information about the rates offered by the property. This should be used in conjunction with the pricing and other rate-related information in shopping.
        dates(Optional[Dates], False): --
        descriptions(Optional[Descriptions], False): --
        statistics(Optional[Dict[str, Statistic]], False): Statistics of the property, such as number of floors. See our [statistics reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known statistics ID and name values.
        airports(Optional[AssociatedAirports], False): --
        themes(Optional[Dict[str, Theme]], False): Themes that describe the property. See our [themes reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known theme ID and name values.
        all_inclusive(Optional[AllInclusive], False): --
        tax_id(Optional[str], False): Tax ID.
        chain(Optional[Chain], False): --
        brand(Optional[Brand], False): --
        spoken_languages(Optional[Dict[str, SpokenLanguage]], False): Languages spoken at the property.
        multi_unit(Optional[bool], False): Boolean value indicating if a property is a multi-unit property.
        payment_registration_recommended(Optional[bool], False): Boolean value indicating if a property may require payment registration to process payments, even when using the property_collect Business Model. If true, then a property may not be successfully bookable without registering payments first.
        vacation_rental_details(Optional[VacationRentalDetails], False): --
        supply_source(Optional[str], False): The supply source of the property.

    """

    property_id: Optional[str] = None
    """
    Unique Expedia property ID.
    """
    name: Optional[str] = None
    """
    Property name.
    """
    address: Optional[Address] = None
    ratings: Optional[Ratings] = None
    location: Optional[Location] = None
    phone: Optional[str] = None
    """
    The property's phone number.
    """
    fax: Optional[str] = None
    """
    The property's fax number.
    """
    category: Optional[CategoryProperty] = None
    business_model: Optional[BusinessModel] = None
    rank: Optional[float] = None
    """
    The property’s rank across all properties. This value sorts properties based on EPS transactional data and details about the property, with 1 indicating the best-performing property and others following in ascending numerical order.
    """
    checkin: Optional[Checkin] = None
    checkout: Optional[Checkout] = None
    fees: Optional[Fees] = None
    policies: Optional[Policies] = None
    attributes: Optional[Attributes] = None
    amenities: Optional[Dict[str, Amenity]] = None
    """
    Lists all of the amenities available for all guests at the property. See our [amenities reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known amenity ID and name values.
    """
    images: Optional[List[Image]] = None
    """
    Contains all property images available.
    """
    onsite_payments: Optional[OnsitePayments] = None
    rooms: Optional[Dict[str, RoomContent]] = None
    """
    Information about all of the rooms at the property.
    """
    rates: Optional[Dict[str, RateContent]] = None
    """
    Additional information about the rates offered by the property. This should be used in conjunction with the pricing and other rate-related information in shopping.
    """
    dates: Optional[Dates] = None
    descriptions: Optional[Descriptions] = None
    statistics: Optional[Dict[str, Statistic]] = None
    """
    Statistics of the property, such as number of floors. See our [statistics reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known statistics ID and name values.
    """
    airports: Optional[AssociatedAirports] = None
    themes: Optional[Dict[str, Theme]] = None
    """
    Themes that describe the property. See our [themes reference](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists) for current known theme ID and name values.
    """
    all_inclusive: Optional[AllInclusive] = None
    tax_id: Optional[str] = None
    """
    Tax ID.
    """
    chain: Optional[Chain] = None
    brand: Optional[Brand] = None
    spoken_languages: Optional[Dict[str, SpokenLanguage]] = None
    """
    Languages spoken at the property.
    """
    multi_unit: Optional[bool] = None
    """
    Boolean value indicating if a property is a multi-unit property.
    """
    payment_registration_recommended: Optional[bool] = None
    """
    Boolean value indicating if a property may require payment registration to process payments, even when using the property_collect Business Model. If true, then a property may not be successfully bookable without registering payments first.
    """
    vacation_rental_details: Optional[VacationRentalDetails] = None
    supply_source: Optional[str] = None
    """
    The supply source of the property.
    """


class Rate(BaseModel):
    """pydantic model Rate: A rate.
        Attributes:
            id(Optional[str], False): Unique Identifier for a rate.
            status(Optional[Status], False): --
            available_rooms(Optional[float], False): The number of bookable rooms remaining with this rate in EPS inventory. Use this value to create rules for urgency messaging to alert users to low availability on busy travel dates or at popular properties.
    If the value returns as 2147483647 (max int value), the actual value could not be determined. Ensure your urgency messaging ignores such instances when returned.
            refundable(Optional[bool], False): Indicates if the rate is fully refundable at the time of booking. Cancel penalties may still apply. Please refer to the cancel penalties section for reference.
            member_deal_available(Optional[bool], False): Indicates if a "Member Only Deal" is available for this rate.
            sale_scenario(Optional[SaleScenario], False): --
            merchant_of_record(Optional[MerchantOfRecord], False): --
            amenities(Optional[Dict[str, Amenity]], False): Room amenities.
            links(Optional[RateLinks], False): --
            bed_groups(Optional[Dict[str, BedGroupAvailability]], False): A map of the room's bed groups.
            cancel_penalties(Optional[List[CancelPenalty]], False): Array of `cancel_penalty` objects containing cancel penalty information.
            nonrefundable_date_ranges(Optional[List[NonrefundableDateRange]], False): A list of date exceptions. Dates within these ranges provide no refund on cancellation, regardless of cancel penalty windows.
            occupancy_pricing(Optional[Dict[str, PricingInformation]], False): A map of room information by occupancy.
            promotions(Optional[Promotions], False): --
            card_on_file_limit(Optional[Amount], False): --
            refundable_damage_deposit(Optional[Amount], False): --
            deposits(Optional[List[Deposit]], False): Array of deposits for the rate.

    """

    id: Optional[str] = None
    """
    Unique Identifier for a rate.
    """
    status: Optional[Status] = None
    available_rooms: Optional[float] = None
    """
    The number of bookable rooms remaining with this rate in EPS inventory. Use this value to create rules for urgency messaging to alert users to low availability on busy travel dates or at popular properties.
    If the value returns as 2147483647 (max int value), the actual value could not be determined. Ensure your urgency messaging ignores such instances when returned.
    """
    refundable: Optional[bool] = None
    """
    Indicates if the rate is fully refundable at the time of booking. Cancel penalties may still apply. Please refer to the cancel penalties section for reference.
    """
    member_deal_available: Optional[bool] = None
    """
    Indicates if a "Member Only Deal" is available for this rate.
    """
    sale_scenario: Optional[SaleScenario] = None
    merchant_of_record: Optional[MerchantOfRecord] = None
    amenities: Optional[Dict[str, Amenity]] = None
    """
    Room amenities.
    """
    links: Optional[RateLinks] = None
    bed_groups: Optional[Dict[str, BedGroupAvailability]] = None
    """
    A map of the room's bed groups.
    """
    cancel_penalties: Optional[List[CancelPenalty]] = None
    """
    Array of `cancel_penalty` objects containing cancel penalty information.
    """
    nonrefundable_date_ranges: Optional[List[NonrefundableDateRange]] = None
    """
    A list of date exceptions. Dates within these ranges provide no refund on cancellation, regardless of cancel penalty windows.
    """
    occupancy_pricing: Optional[Dict[str, PricingInformation]] = None
    """
    A map of room information by occupancy.
    """
    promotions: Optional[Promotions] = None
    card_on_file_limit: Optional[Amount] = None
    refundable_damage_deposit: Optional[Amount] = None
    deposits: Optional[List[Deposit]] = None
    """
    Array of deposits for the rate.
    """


class RoomPriceCheck(BaseModel):
    """pydantic model RoomPriceCheck: The price check response.
    Attributes:
        status(Optional[StatusPriceCheck], False): --
        occupancy_pricing(Optional[Dict[str, PricingInformation]], False): A map of room information by occupancy.
        links(Optional[RoomPriceCheckLinks], False): --
        card_on_file_limit(Optional[Amount], False): --
        refundable_damage_deposit(Optional[Amount], False): --
        deposits(Optional[List[Deposit]], False): Array of deposits.
        trader_information(Optional[TraderInformation], False): --

    """

    status: Optional[StatusPriceCheck] = None
    occupancy_pricing: Optional[Dict[str, PricingInformation]] = None
    """
    A map of room information by occupancy.
    """
    links: Optional[RoomPriceCheckLinks] = None
    card_on_file_limit: Optional[Amount] = None
    refundable_damage_deposit: Optional[Amount] = None
    deposits: Optional[List[Deposit]] = None
    """
    Array of deposits.
    """
    trader_information: Optional[TraderInformation] = None


class RoomItinerary(BaseModel):
    """pydantic model RoomItinerary: The room information.
    Attributes:
        id(Optional[str], False): The room id.
        confirmation_id(Optional[ConfirmationId], False): --
        bed_group_id(Optional[str], False): Unique identifier for a bed type.
        checkin(Optional[str], False): The check-in date of the itinerary.
        checkout(Optional[str], False): The check-out date of the itinerary.
        number_of_adults(Optional[float], False): The number of adults staying in the room.
        child_ages(Optional[List[float]], False): The ages of children for the room.
        given_name(Optional[str], False): The first name of the main guest staying in the room.
        family_name(Optional[str], False): The last name of the main guest staying in the room.
        status(Optional[StatusItinerary], False): --
        special_request(Optional[str], False): Any special request info associated with the room.
        smoking(Optional[bool], False): Indicates if the room is smoking or non-smoking.
        loyalty_id(Optional[str], False): A loyalty identifier for a hotel loyalty program associated with this room guest.
        rate(Optional[RateItinerary], False): --
        links(Optional[RoomItineraryLinks], False): --

    """

    id: Optional[str] = None
    """
    The room id.
    """
    confirmation_id: Optional[ConfirmationId] = None
    bed_group_id: Optional[str] = None
    """
    Unique identifier for a bed type.
    """
    checkin: Optional[str] = None
    """
    The check-in date of the itinerary.
    """
    checkout: Optional[str] = None
    """
    The check-out date of the itinerary.
    """
    number_of_adults: Optional[float] = None
    """
    The number of adults staying in the room.
    """
    child_ages: Optional[List[float]] = None
    """
    The ages of children for the room.
    """
    given_name: Optional[str] = None
    """
    The first name of the main guest staying in the room.
    """
    family_name: Optional[str] = None
    """
    The last name of the main guest staying in the room.
    """
    status: Optional[StatusItinerary] = None
    special_request: Optional[str] = None
    """
    Any special request info associated with the room.
    """
    smoking: Optional[bool] = None
    """
    Indicates if the room is smoking or non-smoking.
    """
    loyalty_id: Optional[str] = None
    """
    A loyalty identifier for a hotel loyalty program associated with this room guest.
    """
    rate: Optional[RateItinerary] = None
    links: Optional[RoomItineraryLinks] = None


class PropertiesContentGetResponse(BaseModel):
    """pydantic model PropertiesContentGetResponse
    Attributes:
        __root__(Optional[Dict[str, PropertyContent]], False): --

    """

    __root__: Optional[Dict[str, PropertyContent]] = None


class RoomAvailability(BaseModel):
    """pydantic model RoomAvailability: The room information.
    Attributes:
        id(Optional[str], False): Unique Identifier for a room type.
        room_name(Optional[str], False): Name of the room type.
        rates(Optional[List[Rate]], False): Array of objects containing rate information.

    """

    id: Optional[str] = None
    """
    Unique Identifier for a room type.
    """
    room_name: Optional[str] = None
    """
    Name of the room type.
    """
    rates: Optional[List[Rate]] = None
    """
    Array of objects containing rate information.
    """


class Itinerary(BaseModel):
    """pydantic model Itinerary: The itinerary object.
    Attributes:
        itinerary_id(Optional[str], False): The itinerary id.
        property_id(Optional[str], False): The property id.
        links(Optional[ItineraryLinks], False): --
        email(Optional[str], False): Email address for the customer.
        phone(Optional[Phone], False): --
        rooms(Optional[List[RoomItinerary]], False): --
        billing_contact(Optional[BillingContact], False): --
        adjustment(Optional[Adjustment], False): --
        creation_date_time(Optional[str], False): The creation date/time of the booking.
        affiliate_reference_id(Optional[str], False): Your unique reference value. This field supports a maximum of 28 characters.
        affiliate_metadata(Optional[str], False): Field that stores up to 256 characters of additional metadata with the itinerary, uniqueness is not required.
        conversations(Optional[Conversations], False): --
        trader_information(Optional[TraderInformation1], False): --
        essential_information(Optional[EssentialInformation], False): --

    """

    itinerary_id: Optional[str] = None
    """
    The itinerary id.
    """
    property_id: Optional[str] = None
    """
    The property id.
    """
    links: Optional[ItineraryLinks] = None
    email: Optional[str] = None
    """
    Email address for the customer.
    """
    phone: Optional[Phone] = None
    rooms: Optional[List[RoomItinerary]] = None
    billing_contact: Optional[BillingContact] = None
    adjustment: Optional[Adjustment] = None
    creation_date_time: Optional[str] = None
    """
    The creation date/time of the booking.
    """
    affiliate_reference_id: Optional[str] = None
    """
    Your unique reference value. This field supports a maximum of 28 characters.
    """
    affiliate_metadata: Optional[str] = None
    """
    Field that stores up to 256 characters of additional metadata with the itinerary, uniqueness is not required.
    """
    conversations: Optional[Conversations] = None
    trader_information: Optional[TraderInformation1] = None
    essential_information: Optional[EssentialInformation] = None


class PropertyAvailability(BaseModel):
    """pydantic model PropertyAvailability: The rooms and rates for a property.
    Attributes:
        property_id(Optional[str], False): Expedia property ID.
        rooms(Optional[List[RoomAvailability]], False): Array of objects containing room information.
        score(Optional[float], False): A score to sort properties where the higher the value the better. It can be used to:<br> * Sort the properties on the response<br> * Sort properties across multiple responses in parallel searches for large regions<br>
        links(Optional[PropertyAvailabilityLinks], False): --

    """

    property_id: Optional[str] = None
    """
    Expedia property ID.
    """
    rooms: Optional[List[RoomAvailability]] = None
    """
    Array of objects containing room information.
    """
    score: Optional[float] = None
    """
    A score to sort properties where the higher the value the better. It can be used to:<br> * Sort the properties on the response<br> * Sort properties across multiple responses in parallel searches for large regions<br>
    """
    links: Optional[PropertyAvailabilityLinks] = None


class Region(BaseModel):
    """pydantic model Region
    Attributes:
        id(Optional[str], False): Region Id.
        type(Optional[str], False): Region type.
        name(Optional[str], False): Region name.
        name_full(Optional[str], False): Full region name.
        descriptor(Optional[str], False): Specific information about the region e.g. whether it covers surrounding areas for a city. Only present when relevant for a region. See our [region descriptors reference](https://developers.expediagroup.com/docs/rapid/lodging/geography/geography-reference-lists) for current known descriptor values.
        iata_airport_code(Optional[str], False): 3-character IATA airport code.
        iata_airport_metro_code(Optional[str], False): 3-character IATA airport metropolitan code of the metropolitan airport area.
        country_code(Optional[str], False): Region country code (ISO-3166 ALPHA-2).
        coordinates(Optional[CoordinatesRegion], False): --
        associations(Optional[Dict[str, List[str]]], False): A map of region types to a sorted array of region ids with a touristic association to the region.
        ancestors(Optional[List[Ancestors]], False): An array of the region's ancestors.
        descendants(Optional[Dict[str, List[str]]], False): A map of region types to an array of region ids. The region ids are direct descendants of the region.
        property_ids(Optional[List[str]], False): An array of associated property ids for the region.
        property_ids_expanded(Optional[List[str]], False): An array of associated property ids within an expanded radius for the region.
        categories(Optional[List[str]], False): A list of regional categories.
        tags(Optional[List[str]], False): A list of regional tags.

    """

    id: Optional[str] = None
    """
    Region Id.
    """
    type: Optional[str] = None
    """
    Region type.
    """
    name: Optional[str] = None
    """
    Region name.
    """
    name_full: Optional[str] = None
    """
    Full region name.
    """
    descriptor: Optional[str] = None
    """
    Specific information about the region e.g. whether it covers surrounding areas for a city. Only present when relevant for a region. See our [region descriptors reference](https://developers.expediagroup.com/docs/rapid/lodging/geography/geography-reference-lists) for current known descriptor values.
    """
    iata_airport_code: Optional[str] = None
    """
    3-character IATA airport code.
    """
    iata_airport_metro_code: Optional[str] = None
    """
    3-character IATA airport metropolitan code of the metropolitan airport area.
    """
    country_code: Optional[str] = None
    """
    Region country code (ISO-3166 ALPHA-2).
    """
    coordinates: Optional[CoordinatesRegion] = None
    associations: Optional[Dict[str, List[str]]] = None
    """
    A map of region types to a sorted array of region ids with a touristic association to the region.
    """
    ancestors: Optional[List[Ancestors]] = None
    """
    An array of the region's ancestors.
    """
    descendants: Optional[Dict[str, List[str]]] = None
    """
    A map of region types to an array of region ids. The region ids are direct descendants of the region.
    """
    property_ids: Optional[List[str]] = None
    """
    An array of associated property ids for the region.
    """
    property_ids_expanded: Optional[List[str]] = None
    """
    An array of associated property ids within an expanded radius for the region.
    """
    categories: Optional[List[str]] = None
    """
    A list of regional categories.
    """
    tags: Optional[List[str]] = None
    """
    A list of regional tags.
    """


class CoordinatesRegion(BaseModel):
    """pydantic model CoordinatesRegion
    Attributes:
        center_longitude(Optional[float], False): Center Longitude.
        center_latitude(Optional[float], False): Center Latitude.
        bounding_polygon(Optional[BoundingPolygon], False): --

    """

    center_longitude: Optional[float] = None
    """
    Center Longitude.
    """
    center_latitude: Optional[float] = None
    """
    Center Latitude.
    """
    bounding_polygon: Optional[BoundingPolygon] = None


class Polygon(BaseModel):
    """pydantic model Polygon
    Attributes:
        coordinates(Optional[List[List[List[Any]]]], False): An array of linear ring coordinate arrays that combine to make up a single [Polygon](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6) in geojson format. If there is more than one linear ring at this level, the first is the outer boundary and the remaining linear rings are interior rings or holes.
        type(Optional[Literal["Polygon"]], False): Type of bounding polygon.

    """

    coordinates: Optional[List[List[List[Any]]]] = None
    """
    An array of linear ring coordinate arrays that combine to make up a single [Polygon](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6) in geojson format. If there is more than one linear ring at this level, the first is the outer boundary and the remaining linear rings are interior rings or holes.
    """
    type: Optional[Literal["Polygon"]] = None
    """
    Type of bounding polygon.
    """


class MultiPolygon(BaseModel):
    """pydantic model MultiPolygon
    Attributes:
        coordinates(Optional[List[List[List[List[Any]]]]], False): An array of multiple polygon(s) that combine to make a full [MultiPolygon](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.7) in geojson format.
        type(Optional[Literal["MultiPolygon"]], False): Type of bounding polygon.

    """

    coordinates: Optional[List[List[List[List[Any]]]]] = None
    """
    An array of multiple polygon(s) that combine to make a full [MultiPolygon](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.7) in geojson format.
    """
    type: Optional[Literal["MultiPolygon"]] = None
    """
    Type of bounding polygon.
    """


BoundingPolygon = Union[
    Polygon,
    MultiPolygon,
]


PropertyRating.update_forward_refs()


GuestRating.update_forward_refs()


Coordinates.update_forward_refs()


CategoryProperty.update_forward_refs()


BusinessModel.update_forward_refs()


Checkin.update_forward_refs()


Checkout.update_forward_refs()


Fees.update_forward_refs()


Policies.update_forward_refs()


Attribute.update_forward_refs()


PaymentType.update_forward_refs()


DescriptionsRoom.update_forward_refs()


Area.update_forward_refs()


View.update_forward_refs()


MaxAllowed.update_forward_refs()


CategoryAge.update_forward_refs()


Dates.update_forward_refs()


Descriptions.update_forward_refs()


Statistic.update_forward_refs()


Preferred.update_forward_refs()


Theme.update_forward_refs()


AllInclusive.update_forward_refs()


Brand.update_forward_refs()


SpokenLanguage.update_forward_refs()


EnhancedHouseRules.update_forward_refs()


UnitConfiguration.update_forward_refs()


FieldModel.update_forward_refs()


ErrorIndividual.update_forward_refs()


Link.update_forward_refs()


PolygonCoordinate.update_forward_refs()


PolygonCoordinates.update_forward_refs()


Ancestors.update_forward_refs()


PropertiesGeoJsonRequest.update_forward_refs()


PropertyGeography.update_forward_refs()


SaleScenario.update_forward_refs()


RateLinks.update_forward_refs()


BedGroupAvailabilityLinks.update_forward_refs()


Deal.update_forward_refs()


Deposit.update_forward_refs()


PropertyAvailabilityLinks.update_forward_refs()


RoomPriceCheckLinks.update_forward_refs()


AffiliateCollect.update_forward_refs()


CardOption.update_forward_refs()


CreditCardMerchant.update_forward_refs()


CheckInValidity.update_forward_refs()


CheckOutValidity.update_forward_refs()


StayConstraints.update_forward_refs()


PaymentSessionsRequestCustomerAccountDetails.update_forward_refs()


BillingContactRequestAddress.update_forward_refs()


ThirdPartyAuthRequest.update_forward_refs()


PaymentSessionsLinks.update_forward_refs()


ItineraryLinks.update_forward_refs()


Phone.update_forward_refs()


ConfirmationId.update_forward_refs()


CancelRefund.update_forward_refs()


DepositItinerary.update_forward_refs()


RoomItineraryLinks.update_forward_refs()


Address1.update_forward_refs()


Adjustment.update_forward_refs()


Conversations.update_forward_refs()


SupplyContact.update_forward_refs()


Image1.update_forward_refs()


PhoneRequest.update_forward_refs()


CreateItineraryRequestRoom.update_forward_refs()


ItineraryCreationLinks.update_forward_refs()


CompletePaymentSessionLinks.update_forward_refs()


ChangeRoomDetailsRequest.update_forward_refs()


Notification.update_forward_refs()


TestNotificationRequest.update_forward_refs()


BedGroupConfiguration.update_forward_refs()


CancelPenalty.update_forward_refs()


NonrefundableDateRange.update_forward_refs()


Amount.update_forward_refs()


ChargeCalculated.update_forward_refs()


TraderName.update_forward_refs()


TraderAddress.update_forward_refs()


TraderContactMessage.update_forward_refs()


TraderRightToWithdrawMessage.update_forward_refs()


TraderTermsAndConditions.update_forward_refs()


NightCharge1.update_forward_refs()


Stay1.update_forward_refs()


Charge1.update_forward_refs()


ChargeCalculated1.update_forward_refs()


ValueAdd1.update_forward_refs()


TraderDetailsInner.update_forward_refs()


PropertiesGeographyPostResponse.update_forward_refs()


Localized.update_forward_refs()


Ratings.update_forward_refs()


Location.update_forward_refs()


Attributes.update_forward_refs()


Image.update_forward_refs()


OnsitePayments.update_forward_refs()


BedGroup.update_forward_refs()


Occupancy.update_forward_refs()


AssociatedAirports.update_forward_refs()


Chain.update_forward_refs()


PropertyManagerLinks.update_forward_refs()


RentalAgreementLinks.update_forward_refs()


Error.update_forward_refs()


Review.update_forward_refs()


BedGroupAvailability.update_forward_refs()


CreditCard.update_forward_refs()


Day.update_forward_refs()


BillingContactRequest.update_forward_refs()


PaymentSessions.update_forward_refs()


PromotionsItinerary.update_forward_refs()


BillingContact.update_forward_refs()


Essential.update_forward_refs()


Amenity.update_forward_refs()


NightCharge.update_forward_refs()


Stay.update_forward_refs()


Charge.update_forward_refs()


FeesPricingInformation.update_forward_refs()


ValueAdd.update_forward_refs()


TraderInformation.update_forward_refs()


TraderDetails.update_forward_refs()


TraderInformation1.update_forward_refs()


Totals1.update_forward_refs()


FeesPricingInformation1.update_forward_refs()


GuestReviewsVerified.update_forward_refs()


ChainsGetResponse.update_forward_refs()


Address.update_forward_refs()


RoomContent.update_forward_refs()


RateContent.update_forward_refs()


PropertyManager.update_forward_refs()


RentalAgreement.update_forward_refs()


GuestReviews.update_forward_refs()


Promotions.update_forward_refs()


PaymentOption.update_forward_refs()


PropertyCalendarAvailability.update_forward_refs()


PaymentRequest.update_forward_refs()


EssentialInformation.update_forward_refs()


CreateItineraryRequest.update_forward_refs()


ItineraryCreation.update_forward_refs()


CompletePaymentSession.update_forward_refs()


Totals.update_forward_refs()


PricingInformation1.update_forward_refs()


VacationRentalDetails.update_forward_refs()


PaymentSessionsRequest.update_forward_refs()


RateItinerary.update_forward_refs()


PricingInformation.update_forward_refs()


PropertyContent.update_forward_refs()


Rate.update_forward_refs()


RoomPriceCheck.update_forward_refs()


RoomItinerary.update_forward_refs()


PropertiesContentGetResponse.update_forward_refs()


RoomAvailability.update_forward_refs()


Itinerary.update_forward_refs()


PropertyAvailability.update_forward_refs()


Region.update_forward_refs()


CoordinatesRegion.update_forward_refs()


Polygon.update_forward_refs()


MultiPolygon.update_forward_refs()
