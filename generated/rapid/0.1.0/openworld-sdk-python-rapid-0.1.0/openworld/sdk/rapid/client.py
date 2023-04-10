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

import json
import platform
from typing import *
from uuid import UUID, uuid4

import pydantic.schema
from furl import furl

from openworld.sdk.core.client.api import ApiClient
from openworld.sdk.core.client.rapid_auth_client import _RapidAuthClient
from openworld.sdk.core.configuration.client_config import ClientConfig
from openworld.sdk.core.constant import header

from .model import *


class RapidClient:
    def __init__(self, client_config: ClientConfig):
        """Rapid Client.

        :param client_config: Client configuration holder.
        """
        python_version = platform.python_version()
        os_name, os_version, *_ = platform.platform().split('-')
        sdk_metadata = f'open-world-sdk-python-rapid/0.1.0'

        self.__api_client = ApiClient(client_config, _RapidAuthClient)

        self.__user_agent = f'{sdk_metadata} (Python {python_version}; {os_name} {os_version})'

    def get_calendar_availability(
        self, transaction_id: UUID = uuid4(), test: Optional[str] = None, property_id: List[str] = None, start_date: date = None, end_date: date = None
    ) -> Union[List[PropertyCalendarAvailability], Error]:
        """Returns availability information for the specified properties (maximum of 25 properties per request).
         The response includes per day information about the property's availability, information about if check-in or check-out is available for the day,
          and information regarding the stay constraints.

        Args:
           test(Optional[str], optional): Shop calls have a test header that can be used to return set responses with the following keywords:<br>* `standard`* `service_unavailable`* `unknown_internal_error`
           property_id(List[str]): The ID of the property you want to search for. You can provide 1 to 250 property_id parameters.
           start_date(date): The first day of availability information to be returned, in ISO 8601 format (YYYY-MM-DD), up to 500 days in the future from the current date.
           end_date(date): The last day of availability information to be returned, in ISO 8601 format (YYYY-MM-DD). This must be 365 days or less from the start_date.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'property_id': json.loads(json.dumps(property_id, default=pydantic.schema.pydantic_encoder)),
                'start_date': json.loads(json.dumps(start_date, default=pydantic.schema.pydantic_encoder)),
                'end_date': json.loads(json.dumps(end_date, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/calendars/availability'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[List[PropertyCalendarAvailability], Error], url=request_url)

    def get_chain_reference(
        self,
        transaction_id: UUID = uuid4(),
        customer_session_id: Optional[str] = None,
        billing_terms: Optional[str] = None,
        partner_point_of_sale: Optional[str] = None,
        payment_terms: Optional[str] = None,
        platform_name: Optional[str] = None,
    ) -> Union[Optional[Dict[str, Chain]], Error]:
        """Returns a complete collection of chains recognized by the Rapid API.

        <br>Chains represent a parent company which can have multiple brands associated with it. A brand can only be associated with one chain. For example, Hilton Worldwide is a chain that has multiple associated brands including Doubletree, Hampton Inn and Embassy Suites.

        <br>The response is a JSON map where the key is the chain ID and the value is a chain object. Each chain object also contains a map of its related brands.

        <br>Note that the set of chain IDs and brand IDs are totally independent of one another. It is possible for a chain and a brand to both use the same number as their ID, but this is just a coincidence that holds no meaning.

        <br>Chain and brand names are provided in English only.

        Args:
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           billing_terms(Optional[str], optional): This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.
           partner_point_of_sale(Optional[str], optional): This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           payment_terms(Optional[str], optional): This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.
           platform_name(Optional[str], optional): This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Session-Id': customer_session_id,
        }

        query = {
            key: value
            for key, value in {
                'billing_terms': json.loads(json.dumps(billing_terms, default=pydantic.schema.pydantic_encoder)),
                'partner_point_of_sale': json.loads(json.dumps(partner_point_of_sale, default=pydantic.schema.pydantic_encoder)),
                'payment_terms': json.loads(json.dumps(payment_terms, default=pydantic.schema.pydantic_encoder)),
                'platform_name': json.loads(json.dumps(platform_name, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/chains'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[Optional[Dict[str, Chain]], Error], url=request_url)

    def get_property_catalog_file(
        self,
        transaction_id: UUID = uuid4(),
        customer_session_id: Optional[str] = None,
        language: str = None,
        supply_source: str = None,
        billing_terms: Optional[str] = None,
        payment_terms: Optional[str] = None,
        partner_point_of_sale: Optional[str] = None,
        platform_name: Optional[str] = None,
    ) -> Union[Link, Error]:
        """Returns a link to download the master list of EPS's active properties in the requested language. The response includes high-level details about each property.

        <br>This file is in JSONL format and is gzipped. The schema of each JSON object in the JSONL file is a subset of the schema of each JSON object from the Property Content call. The subset of fields included are:

          * property_id
          * name
          * address
          * ratings
          * location
          * phone
          * fax
          * category
          * rank
          * business_model
          * dates
          * statistics
          * chain
          * brand
          * supply_source

        <br>Example of a JSONL file with 2 properties:
        ```
        {"property_id":"12345","name":"Test Property Name","address":{"line_1":"123 Main St","line_2":"Apt A","city":"Springfield","state_province_code":"MO","state_province_name":"Missouri","postal_code":"65804","country_code":"US","obfuscation_required":false,"localized":{"links":{"es-ES":{"method":"GET","href":"https://api.ean.com/v3/properties/content?language=es-ES&include=address&property_id=12345"},"fr-FR":{"method":"GET","href":"https://api.ean.com/v3/properties/content?language=fr-FR&include=address&property_id=12345"}}}},"ratings":{"property":{"rating":"3.5","type":"Star"},"guest":{"count":48382,"overall":"3.1","cleanliness":"4.2","service":"1.1","comfort":"4.3","condition":"1.6","location":"4.0","neighborhood":"3.4","quality":"3.4","value":"2.2","amenities":"1.4","recommendation_percent":"73%"}},"location":{"coordinates":{"latitude":37.15845,"longitude":-93.26838}},"phone":"1-417-862-0153","fax":"1-417-863-7249","category":{"id":"1","name":"Hotel"},"rank":42,"business_model":{"expedia_collect":true,"property_collect":false},"dates":{"added":"1998-07-19T05:00:00.000Z","updated":"2018-03-22T07:23:14.000Z"},"statistics":{"52":{"id":"52","name":"Total number of rooms - 820","value":"820"},"54":{"id":"54","name":"Number of floors - 38","value":"38"}},"chain":{"id":"-6","name":"Hyatt Hotels"},"brand":{"id":"2209","name":"Hyatt Place"},"supply_source":"expedia"}
        {"property_id":"67890","name":"Test Property Name 2","address":{"line_1":"123 Main St","line_2":"Apt A","city":"Springfield","state_province_code":"MO","state_province_name":"Missouri","postal_code":"65804","country_code":"US","obfuscation_required":true,"localized":{"links":{"es-ES":{"method":"GET","href":"https://api.ean.com/v3/properties/content?language=es-ES&include=address&property_id=67890"},"de-DE":{"method":"GET","href":"https://api.ean.com/v3/properties/content?language=de-DE&include=address&property_id=67890"}}}},"ratings":{"property":{"rating":"3.5","type":"Star"},"guest":{"count":7651,"overall":"4.3","cleanliness":"4.2","service":"1.1","comfort":"4.3","condition":"1.6","location":"4.0","neighborhood":"3.4","quality":"3.4","value":"2.2","amenities":"1.4","recommendation_percent":"80%"}},"location":{"coordinates":{"latitude":37.15845,"longitude":-93.26838}},"phone":"1-417-862-0153","fax":"1-417-863-7249","category":{"id":"1","name":"Hotel"},"rank":42,"business_model":{"expedia_collect":true,"property_collect":true},"dates":{"added":"1998-07-20T05:00:00.000Z","updated":"2018-03-22T13:'33':17.000Z"},"statistics":{"52":{"id":"52","name":"Total number of rooms - 820","value":"820"},"54":{"id":"54","name":"Number of floors - 38","value":"38"}},"chain":{"id":"-5","name":"Hilton Worldwide"},"brand":{"id":"358","name":"Hampton Inn"},"supply_source":"expedia"}
        ```

        Args:
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           language(str): Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)Language Options: [https://developers.expediagroup.com/docs/rapid/resources/reference/language-options](https://developers.expediagroup.com/docs/rapid/resources/reference/language-options)
           supply_source(str): Options for which supply source you would like returned in the content response. This parameter may only be supplied once and will return all properties that match the requested supply source. An error is thrown if the parameter is provided multiple times.  * expedia - Standard Expedia supply.  * vrbo - VRBO supply.
           billing_terms(Optional[str], optional): This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.
           payment_terms(Optional[str], optional): This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.
           partner_point_of_sale(Optional[str], optional): This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           platform_name(Optional[str], optional): This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Session-Id': customer_session_id,
        }

        query = {
            key: value
            for key, value in {
                'language': json.loads(json.dumps(language, default=pydantic.schema.pydantic_encoder)),
                'supply_source': json.loads(json.dumps(supply_source, default=pydantic.schema.pydantic_encoder)),
                'billing_terms': json.loads(json.dumps(billing_terms, default=pydantic.schema.pydantic_encoder)),
                'payment_terms': json.loads(json.dumps(payment_terms, default=pydantic.schema.pydantic_encoder)),
                'partner_point_of_sale': json.loads(json.dumps(partner_point_of_sale, default=pydantic.schema.pydantic_encoder)),
                'platform_name': json.loads(json.dumps(platform_name, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/files/properties/catalog'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[Link, Error], url=request_url)

    def get_property_content_file(
        self,
        transaction_id: UUID = uuid4(),
        customer_session_id: Optional[str] = None,
        language: str = None,
        supply_source: str = None,
        billing_terms: Optional[str] = None,
        payment_terms: Optional[str] = None,
        partner_point_of_sale: Optional[str] = None,
        platform_name: Optional[str] = None,
    ) -> Union[Link, Error]:
        """Returns a link to download all content for all of EPS’s active properties in the requested language. The response includes property-level, room-level and rate-level information.

        <br>This file is in JSONL format and is gzipped. The schema of each JSON object in the JSONL file is the same as the schema of each JSON object from the Property Content call.

        <br>Example of a JSONL file with 2 properties:
          ```
          {"property_id":"12345","name":"Test Property Name","address":{"line_1":"123 Main St","line_2":"Apt A","city":"Springfield","state_province_code":"MO","state_province_name":"Missouri","postal_code":"65804","country_code":"US","obfuscation_required":false,"localized":{"links":{"es-ES":{"method":"GET","href":"https://api.ean.com/v3/properties/content?language=es-ES&include=address&property_id=12345"},"fr-FR":{"method":"GET","href":"https://api.ean.com/v3/properties/content?language=fr-FR&include=address&property_id=12345"}}}},"ratings":{"property":{"rating":"3.5","type":"Star"},"guest":{"count":48382,"overall":"3.1","cleanliness":"4.2","service":"1.1","comfort":"4.3","condition":"1.6","location":"4.0","neighborhood":"3.4","quality":"3.4","value":"2.2","amenities":"1.4","recommendation_percent":"73%"}},"location":{"coordinates":{"latitude":37.15845,"longitude":-93.26838}},"phone":"1-417-862-0153","fax":"1-417-863-7249","category":{"id":"1","name":"Hotel"},"rank":42,"business_model":{"expedia_collect":true,"property_collect":false},"checkin":{"24_hour":"24-hour check-in","begin_time":"3:00 PM","end_time":"11:00 PM","instructions":"Extra-person charges may apply and vary depending on hotel policy. &lt;br />Government-issued photo identification and a credit card or cash deposit are required at check-in for incidental charges. &lt;br />Special requests are subject to availability upon check-in and may incur additional charges. Special requests cannot be guaranteed. &lt;br />","special_instructions":"There is no front desk at this property. To make arrangements for check-in please contact the property ahead of time using the information on the booking confirmation.","min_age":18},"checkout":{"time":"11:00 AM"},"fees":{"mandatory":"<p>You'll be asked to pay the following charges at the hotel:</p> <ul><li>Deposit: USD 50 per day</li><li>Resort fee: USD 29.12 per accommodation, per night</li></ul> The hotel resort fee includes:<ul><li>Fitness center access</li><li>Internet access</li><li>Phone calls</li><li>Additional inclusions</li></ul> <p>We have included all charges provided to us by the property. However, charges can vary, for example, based on length of stay or the room you book. </p>","optional":"Fee for in-room wireless Internet: USD 15 per hour (rates may vary)</li> <li>Airport shuttle fee: USD 350 per vehicle (one way)</li>           <li>Rollaway bed fee: USD 175 per night</li>"},"policies":{"know_before_you_go":"Reservations are required for massage services and spa treatments. Reservations can be made by contacting the hotel prior to arrival, using the contact information on the booking confirmation. </li><li>Children 11 years old and younger stay free when occupying the parent or guardian's room, using existing bedding. </li><li>Only registered guests are allowed in the guestrooms. </li> <li>Some facilities may have restricted access. Guests can contact the property for details using the contact information on the booking confirmation. </li> </ul>"},"attributes":{"general":{"2549":{"id":"2549","name":"No elevators"},"3357":{"id":"3357","name":"Caters to adults only"}},"pets":{"51":{"id":"51","name":"Pets allowed"},"2809":{"id":"2809","name":"Dogs only"},"3321":{"id":"3321","name":"Pet maximum weight in kg is - 24","value":24}}},"amenities":{"9":{"id":"9","name":"Fitness facilities"},"2820":{"id":"2820","name":"Number of indoor pools - 10","value":10}},"images":[{"caption":"Featured Image","hero_image":true,"category":3,"links":{"70px":{"method":"GET","href":"https://i.travelapi.com/hotels/1000000/20000/15300/15237/bef1b976_t.jpg"}}}],"onsite_payments":{"currency":"USD","types":{"171":{"id":"171","name":"American Express"}}},"rooms":{"224829":{"id":"224829","name":"Single Room","descriptions":{"overview":"<strong>2 Twin Beds</strong><br />269-sq-foot (25-sq-meter) room with mountain views<br /><br /><b>Internet</b> - Free WiFi <br /> <b>Entertainment</b> - Flat-screen TV with cable channels<br /><b>Food & Drink</b> - Refrigerator, coffee/tea maker,  room service, and free bottled water<br /><b>Sleep</b> - Premium bedding <br /><b>Bathroom</b> - Private bathroom, shower, bathrobes, and free toiletries<br /><b>Practical</b> - Safe and desk; cribs/infant beds available on request<br /><b>Comfort</b> - Climate-controlled air conditioning and daily housekeeping<br />Non-Smoking<br />"},"amenities":{"130":{"id":"130","name":"Refrigerator"},"1234":{"id":"1234","name":"Test Amenity - 200","value":"200"}},"images":[{"hero_image":true,"category":21001,"links":{"70px":{"method":"GET","href":"https://i.travelapi.com/hotels/1000000/20000/15300/15237/bef1b976_t.jpg"}},"caption":"Guestroom"}],"bed_groups":{"37321":{"id":"37321","description":"1 King Bed","configuration":[{"type":"KingBed","size":"King","quantity":1}]}},"area":{"square_meters":20,"square_feet":215},"views":{"4146":{"id":"4146","name":"Courtyard view"}},"occupancy":{"max_allowed":{"total":5,"children":2,"adults":4},"age_categories":{"Adult":{"name":"Adult","minimum_age":9}}}}},"rates":{"333abc":{"id":"333abc","amenities":{"1234":{"id":"1234","name":"Test Amenity - 200","value":"200"},"2104":{"id":"2104","name":"Full Breakfast"}},"special_offer_description":"<strong>Breakfast for 2</strong> - Rate includes the following:\r\n<ul><li>Accommodations as selected</li>\r\n<li>Breakfast in hotel restaurant for up to 2 adults and children 12 years old and under registered in the same room</li>\r\n</ul><em>Must book this rate plan to receive benefits. Details provided at check-in. Taxes and gratuity may not be included. No refunds for any unused portion of offer. Offer subject to availability. Offer is not valid with groups/conventions and may not be combined with other promotional offers. Other restrictions and blackout dates may apply.</em>\r\n"}},"dates":{"added":"1998-07-19T05:00:00.000Z","updated":"2018-03-22T07:23:14.000Z"},"descriptions":{"amenities":"Don't miss out on the many recreational opportunities, including an outdoor pool, a sauna, and a fitness center. Additional features at this hotel include complimentary wireless Internet access, concierge services, and an arcade/game room.","dining":"Grab a bite at one of the hotel's 3 restaurants, or stay in and take advantage of 24-hour room service. Quench your thirst with your favorite drink at a bar/lounge. Buffet breakfasts are available daily for a fee.","renovations":"During renovations, the hotel will make every effort to minimize noise and disturbance.  The property will be renovating from 08 May 2017 to 18 May 2017 (completion date subject to change). The following areas are affected:  <ul><li>Fitness facilities</li></ul>","national_ratings":"For the benefit of our customers, we have provided a rating based on our rating system.","business_amenities":"Featured amenities include complimentary wired Internet access, a 24-hour business center, and limo/town car service. Event facilities at this hotel consist of a conference center and meeting rooms. Free self parking is available onsite.","rooms":"Make yourself at home in one of the 334 air-conditioned rooms featuring LCD televisions. Complimentary wired and wireless Internet access keeps you connected, and satellite programming provides entertainment. Private bathrooms with separate bathtubs and showers feature deep soaking bathtubs and complimentary toiletries. Conveniences include phones, as well as safes and desks.","attractions":"Distances are calculated in a straight line from the property's location to the point of interest or attraction, and may not reflect actual travel distance. <br /><br /> Distances are displayed to the nearest 0.1 mile and kilometer. <p>Sogo Department Store - 0.7 km / 0.4 mi <br />National Museum of Natural Science - 1.1 km / 0.7 mi <br />Shr-Hwa International Tower - 1.4 km / 0.8 mi <br />Shinkong Mitsukoshi Department Store - 1.5 km / 0.9 mi <br />Taichung Metropolitan Opera House - 1.7 km / 1 mi <br />Tiger City Mall - 1.8 km / 1.1 mi <br />Maple Garden Park - 1.9 km / 1.2 mi <br />National Museum of Fine Arts - 2.1 km / 1.3 mi <br />Feng Chia University - 2.4 km / 1.5 mi <br />Bao An Temple - 2.5 km / 1.6 mi <br />Fengjia Night Market - 2.5 km / 1.6 mi <br />Zhonghua Night Market - 2.7 km / 1.7 mi <br />Chonglun Park - 2.9 km / 1.8 mi <br />Wan He Temple - 2.9 km / 1.8 mi <br />Chungyo Department Store - 3.1 km / 1.9 mi <br /></p><p>The nearest airports are:<br />Taichung (RMQ) - 12 km / 7.5 mi<br />Taipei (TPE-Taoyuan Intl.) - 118.3 km / 73.5 mi<br />Taipei (TSA-Songshan) - 135.5 km / 84.2 mi<br /></p><p></p>","location":"This 4-star hotel is within close proximity of Shr-Hwa International Tower and Shinkong Mitsukoshi Department Store.  A stay at Tempus Hotel Taichung places you in the heart of Taichung, convenient to Sogo Department Store and National Museum of Natural Science.","headline":"Near National Museum of Natural Science","general":"General description"},"statistics":{"52":{"id":"52","name":"Total number of rooms - 820","value":"820"},"54":{"id":"54","name":"Number of floors - 38","value":"38"}},"airports":{"preferred":{"iata_airport_code":"SGF"}},"themes":{"2337":{"id":"2337","name":"Luxury Hotel"},"2341":{"id":"2341","name":"Spa Hotel"}},"all_inclusive":{"all_rate_plans":true,"some_rate_plans":false,"details":"<p>This resort is all-inclusive. Onsite food and beverages are included in the room price (some restrictions may apply). </p><p><strong>Activities and facilities/equipment</strong><br />Land activities<ul><li>Fitness facilities</li></ul><br />Lessons/classes/games <ul><li>Pilates</li><li>Yoga</li></ul></p><p><strong>Entertainment</strong><ul><li>Onsite entertainment and activities</li><li>Onsite live performances</li></ul></p>"},"tax_id":"AB-012-987-1234-01","chain":{"id":"-6","name":"Hyatt Hotels"},"brand":{"id":"2209","name":"Hyatt Place"},"spoken_languages":{"vi":{"id":"vi","name":"Vietnamese"}},"multi_unit":true,"payment_registration_recommended":false,"vacation_rental_details": {"registry_number": "Property Registration Number 123456","private_host": "true","property_manager": {"name": "Victor","links": {"image": {"method": "GET","href": "https://test-image/test/test/836f1097-fbcf-43b5-bc02-c8ff6658cb90.c1.jpg"}}},"rental_agreement": {"links": {"rental_agreement": {"method": "GET","href": "https://test-link.test.amazonaws.com/rentalconditions_property_d65e7eb5-4a7c-4a80-a8a3-171999f9f444.pdf"}}},"house_rules": ["Children welcome","No pets","No smoking","No parties or events"],"amenities": {"4296": {"id": "4296","name": "Furnished balcony or patio"},"2859": {"id": "2859","name": "Private pool"}},"vrbo_srp_id": "123.1234567.5678910","listing_id": "1234567","listing_number": "5678910","listing_source": "HOMEAWAY_US","listing_unit": "/units/0000/32d82dfa-1a48-45d6-9132-49fdbf1bfc60"},"supply_source":"vrbo"}
          {"property_id":"67890","name":"Test Property Name 2","address":{"line_1":"123 Main St","line_2":"Apt A","city":"Springfield","state_province_code":"MO","state_province_name":"Missouri","postal_code":"65804","country_code":"US","obfuscation_required":true,"localized":{"links":{"es-ES":{"method":"GET","href":"https://api.ean.com/v3/properties/content?language=es-ES&include=address&property_id=67890"},"de-DE":{"method":"GET","href":"https://api.ean.com/v3/properties/content?language=de-DE&include=address&property_id=67890"}}}},"ratings":{"property":{"rating":"3.5","type":"Star"},"guest":{"count":7651,"overall":"4.3","cleanliness":"4.2","service":"1.1","comfort":"4.3","condition":"1.6","location":"4.0","neighborhood":"3.4","quality":"3.4","value":"2.2","amenities":"1.4","recommendation_percent":"80%"}},"location":{"coordinates":{"latitude":37.15845,"longitude":-93.26838},"obfuscated_coordinates":{"latitude":28.339303,"longitude":-81.47791},"obfuscation_required":true},"phone":"1-417-862-0153","fax":"1-417-863-7249","category":{"id":"1","name":"Hotel"},"rank":42,"business_model":{"expedia_collect":true,"property_collect":true},"checkin":{"24_hour":"24-hour check-in","begin_time":"3:00 PM","end_time":"11:00 PM","instructions":"Extra-person charges may apply and vary depending on hotel policy. &lt;br />Government-issued photo identification and a credit card or cash deposit are required at check-in for incidental charges. &lt;br />Special requests are subject to availability upon check-in and may incur additional charges. Special requests cannot be guaranteed. &lt;br />","special_instructions":"There is no front desk at this property. To make arrangements for check-in please contact the property ahead of time using the information on the booking confirmation.","min_age":18},"checkout":{"time":"11:00 AM"},"fees":{"mandatory":"<p>You'll be asked to pay the following charges at the hotel:</p> <ul><li>Deposit: USD 50 per day</li><li>Resort fee: USD 29.12 per accommodation, per night</li></ul> The hotel resort fee includes:<ul><li>Fitness center access</li><li>Internet access</li><li>Phone calls</li><li>Additional inclusions</li></ul> <p>We have included all charges provided to us by the property. However, charges can vary, for example, based on length of stay or the room you book. </p>","optional":"Fee for in-room wireless Internet: USD 15 per hour (rates may vary)</li> <li>Airport shuttle fee: USD 350 per vehicle (one way)</li>           <li>Rollaway bed fee: USD 175 per night</li>"},"policies":{"know_before_you_go":"Reservations are required for massage services and spa treatments. Reservations can be made by contacting the hotel prior to arrival, using the contact information on the booking confirmation. </li><li>Children 11 years old and younger stay free when occupying the parent or guardian's room, using existing bedding. </li><li>Only registered guests are allowed in the guestrooms. </li> <li>Some facilities may have restricted access. Guests can contact the property for details using the contact information on the booking confirmation. </li> </ul>"},"attributes":{"general":{"2549":{"id":"2549","name":"No elevators"},"3357":{"id":"3357","name":"Caters to adults only"}},"pets":{"51":{"id":"51","name":"Pets allowed"},"2809":{"id":"2809","name":"Dogs only"},"3321":{"id":"3321","name":"Pet maximum weight in kg is - 24","value":24}}},"amenities":{"9":{"id":"9","name":"Fitness facilities"},"2820":{"id":"2820","name":"Number of indoor pools - 10","value":10}},"images":[{"caption":"Featured Image","hero_image":true,"category":3,"links":{"70px":{"method":"GET","href":"https://i.travelapi.com/hotels/1000000/20000/15300/15237/bef1b976_t.jpg"}}}],"onsite_payments":{"currency":"USD","types":{"171":{"id":"171","name":"American Express"}}},"rooms":{"224829":{"id":"224829","name":"Single Room","descriptions":{"overview":"<strong>2 Twin Beds</strong><br />269-sq-foot (25-sq-meter) room with mountain views<br /><br /><b>Internet</b> - Free WiFi <br /> <b>Entertainment</b> - Flat-screen TV with cable channels<br /><b>Food & Drink</b> - Refrigerator, coffee/tea maker,  room service, and free bottled water<br /><b>Sleep</b> - Premium bedding <br /><b>Bathroom</b> - Private bathroom, shower, bathrobes, and free toiletries<br /><b>Practical</b> - Safe and desk; cribs/infant beds available on request<br /><b>Comfort</b> - Climate-controlled air conditioning and daily housekeeping<br />Non-Smoking<br />"},"amenities":{"130":{"id":"130","name":"Refrigerator"},"1234":{"id":"1234","name":"Test Amenity - 200","value":"200"}},"images":[{"hero_image":true,"category":21001,"links":{"70px":{"method":"GET","href":"https://i.travelapi.com/hotels/1000000/20000/15300/15237/bef1b976_t.jpg"}},"caption":"Guestroom"}],"bed_groups":{"37321":{"id":"37321","description":"1 King Bed","configuration":[{"type":"KingBed","size":"King","quantity":1}]}},"area":{"square_meters":17},"views":{"4134":{"id":"4134","name":"City view"}},"occupancy":{"max_allowed":{"total":3,"children":2,"adults":3},"age_categories":{"ChildAgeA":{"name":"ChildAgeA","minimum_age":3}}}}},"rates":{"333abc":{"id":"333abc","amenities":{"1234":{"id":"1234","name":"Test Amenity - 200","value":"200"},"2104":{"id":"2104","name":"Full Breakfast"}},"special_offer_description":"<strong>Breakfast for 2</strong> - Rate includes the following:\r\n<ul><li>Accommodations as selected</li>\r\n<li>Breakfast in hotel restaurant for up to 2 adults and children 12 years old and under registered in the same room</li>\r\n</ul><em>Must book this rate plan to receive benefits. Details provided at check-in. Taxes and gratuity may not be included. No refunds for any unused portion of offer. Offer subject to availability. Offer is not valid with groups/conventions and may not be combined with other promotional offers. Other restrictions and blackout dates may apply.</em>\r\n"}},"dates":{"added":"1998-07-20T05:00:00.000Z","updated":"2018-03-22T13:'33':17.000Z"},"descriptions":{"amenities":"Don't miss out on the many recreational opportunities, including an outdoor pool, a sauna, and a fitness center. Additional features at this hotel include complimentary wireless Internet access, concierge services, and an arcade/game room.","dining":"Grab a bite at one of the hotel's 3 restaurants, or stay in and take advantage of 24-hour room service. Quench your thirst with your favorite drink at a bar/lounge. Buffet breakfasts are available daily for a fee.","renovations":"During renovations, the hotel will make every effort to minimize noise and disturbance.  The property will be renovating from 08 May 2017 to 18 May 2017 (completion date subject to change). The following areas are affected:  <ul><li>Fitness facilities</li></ul>","national_ratings":"For the benefit of our customers, we have provided a rating based on our rating system.","business_amenities":"Featured amenities include complimentary wired Internet access, a 24-hour business center, and limo/town car service. Event facilities at this hotel consist of a conference center and meeting rooms. Free self parking is available onsite.","rooms":"Make yourself at home in one of the 334 air-conditioned rooms featuring LCD televisions. Complimentary wired and wireless Internet access keeps you connected, and satellite programming provides entertainment. Private bathrooms with separate bathtubs and showers feature deep soaking bathtubs and complimentary toiletries. Conveniences include phones, as well as safes and desks.","attractions":"Distances are calculated in a straight line from the property's location to the point of interest or attraction, and may not reflect actual travel distance. <br /><br /> Distances are displayed to the nearest 0.1 mile and kilometer. <p>Sogo Department Store - 0.7 km / 0.4 mi <br />National Museum of Natural Science - 1.1 km / 0.7 mi <br />Shr-Hwa International Tower - 1.4 km / 0.8 mi <br />Shinkong Mitsukoshi Department Store - 1.5 km / 0.9 mi <br />Taichung Metropolitan Opera House - 1.7 km / 1 mi <br />Tiger City Mall - 1.8 km / 1.1 mi <br />Maple Garden Park - 1.9 km / 1.2 mi <br />National Museum of Fine Arts - 2.1 km / 1.3 mi <br />Feng Chia University - 2.4 km / 1.5 mi <br />Bao An Temple - 2.5 km / 1.6 mi <br />Fengjia Night Market - 2.5 km / 1.6 mi <br />Zhonghua Night Market - 2.7 km / 1.7 mi <br />Chonglun Park - 2.9 km / 1.8 mi <br />Wan He Temple - 2.9 km / 1.8 mi <br />Chungyo Department Store - 3.1 km / 1.9 mi <br /></p><p>The nearest airports are:<br />Taichung (RMQ) - 12 km / 7.5 mi<br />Taipei (TPE-Taoyuan Intl.) - 118.3 km / 73.5 mi<br />Taipei (TSA-Songshan) - 135.5 km / 84.2 mi<br /></p><p></p>","location":"This 4-star hotel is within close proximity of Shr-Hwa International Tower and Shinkong Mitsukoshi Department Store.  A stay at Tempus Hotel Taichung places you in the heart of Taichung, convenient to Sogo Department Store and National Museum of Natural Science.","headline":"Near National Museum of Natural Science","general":"General description"},"statistics":{"52":{"id":"52","name":"Total number of rooms - 820","value":"820"},"54":{"id":"54","name":"Number of floors - 38","value":"38"}},"airports":{"preferred":{"iata_airport_code":"SGF"}},"themes":{"2337":{"id":"2337","name":"Luxury Hotel"},"2341":{"id":"2341","name":"Spa Hotel"}},"all_inclusive":{"all_rate_plans":true,"some_rate_plans":false,"details":"<p>This resort is all-inclusive. Onsite food and beverages are included in the room price (some restrictions may apply). </p><p><strong>Activities and facilities/equipment</strong><br />Land activities<ul><li>Fitness facilities</li></ul><br />Lessons/classes/games <ul><li>Pilates</li><li>Yoga</li></ul></p><p><strong>Entertainment</strong><ul><li>Onsite entertainment and activities</li><li>Onsite live performances</li></ul></p>"},"tax_id":"CD-012-987-1234-02","chain":{"id":"-5","name":"Hilton Worldwide"},"brand":{"id":"358","name":"Hampton Inn"},"spoken_languages":{"en":{"id":"en","name":"English"}},"multi_unit":true,"payment_registration_recommended":true,"vacation_rental_details":{"registry_number":"Property Registration Number 123456","private_host":"true","property_manager":{"name":"John Smith","links":{"image":{"method":"GET","href":"https://example.com/profile.jpg"}}},"rental_agreement":{"links":{"rental_agreement":{"method":"GET","href":"https:/example.com/rentalconditions.pdf"}}},"house_rules":["Children welcome","No pets","No smoking","No parties or events"],"amenities":{"2859":{"id":"2859","name":"Private pool"},"4296":{"id":"4296","name":"Furnished balcony or patio"}},"vrbo_srp_id":"123.1234567.5678910","listing_id":"1234567","listing_number":"5678910","listing_source":"HOMEAWAY_US","listing_unit":"/units/0000/32d82dfa-1a48-45d6-9132-49fdbf1bfc60"},"supply_source":"vrbo"}
          ```

        Args:
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           language(str): Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)Language Options: [https://developers.expediagroup.com/docs/rapid/resources/reference/language-options](https://developers.expediagroup.com/docs/rapid/resources/reference/language-options)
           supply_source(str): Options for which supply source you would like returned in the content response. This parameter may only be supplied once and will return all properties that match the requested supply source. An error is thrown if the parameter is provided multiple times.  * expedia - Standard Expedia supply.  * vrbo - VRBO supply.
           billing_terms(Optional[str], optional): This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.
           payment_terms(Optional[str], optional): This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.
           partner_point_of_sale(Optional[str], optional): This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           platform_name(Optional[str], optional): This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Session-Id': customer_session_id,
        }

        query = {
            key: value
            for key, value in {
                'language': json.loads(json.dumps(language, default=pydantic.schema.pydantic_encoder)),
                'supply_source': json.loads(json.dumps(supply_source, default=pydantic.schema.pydantic_encoder)),
                'billing_terms': json.loads(json.dumps(billing_terms, default=pydantic.schema.pydantic_encoder)),
                'payment_terms': json.loads(json.dumps(payment_terms, default=pydantic.schema.pydantic_encoder)),
                'partner_point_of_sale': json.loads(json.dumps(partner_point_of_sale, default=pydantic.schema.pydantic_encoder)),
                'platform_name': json.loads(json.dumps(platform_name, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/files/properties/content'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[Link, Error], url=request_url)

    def get_reservation(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: str = None,
        customer_session_id: Optional[str] = None,
        test: Optional[str] = None,
        affiliate_reference_id: str = None,
        email: str = None,
    ) -> Union[List[Itinerary], Error]:
        """This can be called directly without a token when an affiliate reference id is provided. It returns details about bookings associated with an affiliate reference id, along with cancel links to cancel the bookings.

        <i>Note: Newly created itineraries may sometimes have a small delay between the time of creation and the time that the itinerary can be retrieved. If you receive no results while trying to find an itinerary that was successfully created, please wait a few minutes before trying to search for the itinerary again.</i>

        Args:
           customer_ip(str): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           test(Optional[str], optional): The retrieve call has a test header that can be used to return set responses with the following keywords:<br>* `standard` - Requires valid test booking.* `service_unavailable`* `internal_server_error`
           affiliate_reference_id(str): The affilliate reference id value. This field supports a maximum of 28 characters.
           email(str): Email associated with the booking. Special characters in the local part or domain should be encoded.<br>"""
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'affiliate_reference_id': json.loads(json.dumps(affiliate_reference_id, default=pydantic.schema.pydantic_encoder)),
                'email': json.loads(json.dumps(email, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/itineraries'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[List[Itinerary], Error], url=request_url)

    def post_itinerary(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: str = None,
        customer_session_id: Optional[str] = None,
        test: Optional[str] = None,
        token: str = None,
        body: CreateItineraryRequest = None,
    ) -> Union[None, ItineraryCreation, Error]:
        """This link will be available in the Price Check response or in the register payments response when Two-Factor Authentication is used. It returns an itinerary id and links to retrieve reservation details, cancel a held booking, resume a held booking or complete payment session. Please note that depending on the state of the booking, the response will contain only the applicable link(s).

        Args:
           customer_ip(str): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           test(Optional[str], optional): The book call has a test header that can be used to return set responses with the following keywords:<br>* `standard`* `complete_payment_session`* `service_unavailable`* `internal_server_error`* `price_mismatch`* `cc_declined`* `rooms_unavailable`
           token(str): Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed.
           body(CreateItineraryRequest): ..."""
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'token': json.loads(json.dumps(token, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/itineraries'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='post', body=body, response_models=[None, ItineraryCreation, Error], url=request_url)

    def get_reservation_by_itinerary_id(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: str = None,
        customer_session_id: Optional[str] = None,
        test: Optional[str] = None,
        itinerary_id: str = None,
        token: Optional[str] = None,
        email: Optional[str] = None,
    ) -> Union[Itinerary, Error]:
        """This API call returns itinerary details and links to resume or cancel the booking. There are two methods to retrieve a booking:
        * Using the link included in the original Book response, example: https://api.ean.com/v3/itineraries/8955599932111?token=QldfCGlcUA4GXVlSAQ4W
        * Using the email of the booking. If the email contains special characters, they must be encoded to successfully retrieve the booking. Example: https://api.ean.com/v3/itineraries/8955599932111?email=customer@email.com

        <i>Note: Newly created itineraries may sometimes have a small delay between the time of creation and the time that the itinerary can be retrieved. If you receive an error when trying to retrieve an itinerary that was successfully created, please wait a few minutes before trying to retrieve the itinerary again.</i>

        Args:
           customer_ip(str): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           test(Optional[str], optional): The retrieve call has a test header that can be used to return set responses. Passing standard in the Test header will retrieve a test booking, and passing any of the errors listed below will return a stubbed error response that you can use to test your error handling code. Additionally, refer to the Test Request documentation for more details on how these header values are used.* `standard` - Requires valid test booking.* `service_unavailable`* `internal_server_error`
           itinerary_id(str): This parameter is used only to prefix the token value - no ID value is used.<br>
           token(Optional[str], optional): Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed.
           email(Optional[str], optional): Email associated with the booking. Special characters in the local part or domain should be encoded. (Email is required if the token is not provided the request) <br>
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'token': json.loads(json.dumps(token, default=pydantic.schema.pydantic_encoder)),
                'email': json.loads(json.dumps(email, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/itineraries/{itinerary_id}'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[Itinerary, Error], url=request_url)

    def put_resume_booking(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: str = None,
        customer_session_id: Optional[str] = None,
        test: Optional[str] = None,
        itinerary_id: str = None,
        token: str = None,
    ) -> Union[None, Error]:
        """This link will be available in the booking response after creating a held booking.

        Args:
           customer_ip(str): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           test(Optional[str], optional): The resume call has a test header that can be used to return set responses with the following keywords:<br>* `standard` - Requires valid test held booking.* `service_unavailable` - Returns the HTTP 202 response caused by partial service unavailablity.* `internal_server_error`
           itinerary_id(str): This parameter is used only to prefix the token value - no ID value is used.<br>
           token(str): Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'token': json.loads(json.dumps(token, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/itineraries/{itinerary_id}'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='put', body=None, response_models=[None, Error], url=request_url)

    def delete_held_booking(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: str = None,
        customer_session_id: Optional[str] = None,
        test: Optional[str] = None,
        itinerary_id: str = None,
        token: str = None,
    ) -> Union[None, Error]:
        """This link will be available in a held booking response.

        Args:
           customer_ip(str): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           test(Optional[str], optional): The cancel call has a test header that can be used to return set responses with the following keywords:<br>* `standard` - Requires valid test held booking.* `service_unavailable`* `internal_server_error`* `post_stay_cancel`
           itinerary_id(str): This parameter is used only to prefix the token value - no ID value is used.<br>
           token(str): Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'token': json.loads(json.dumps(token, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/itineraries/{itinerary_id}'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='delete', body=None, response_models=[None, Error], url=request_url)

    def put_complete_payment_session(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: str = None,
        customer_session_id: Optional[str] = None,
        test: Optional[str] = None,
        itinerary_id: str = None,
        token: str = None,
    ) -> Union[CompletePaymentSession, Error]:
        """<b>This link only applies to transactions where EPS takes the customer's payment information. This includes both Expedia Collect and Property Collect transactions.</b><br>
        This link will be available in the booking response only if you've opted into Two-Factor Authentication to comply with the September 2019 EU Regulations for PSD2. It should be called after Two-Factor Authentication has been completed by the customer in order to finalize the payment and complete the booking or hold attempt. Learn more with our [PSD2 Overview](https://developers.expediagroup.com/docs/rapid/lodging/booking/psd2-regulation)

        Args:
           customer_ip(str): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           test(Optional[str], optional): The payment-sessions call has a test header that can be used to return set responses with the following keywords:<br>* `standard`* `service_unavailable`* `internal_server_error`
           itinerary_id(str): This parameter is used only to prefix the token value - no ID value is used.<br>
           token(str): Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'token': json.loads(json.dumps(token, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/itineraries/{itinerary_id}/payment-sessions'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='put', body=None, response_models=[CompletePaymentSession, Error], url=request_url)

    def change_room_details(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: str = None,
        customer_session_id: Optional[str] = None,
        test: Optional[str] = None,
        itinerary_id: str = None,
        room_id: str = None,
        token: str = None,
        body: ChangeRoomDetailsRequest = None,
    ) -> Union[None, Error]:
        """This link will be available in the retrieve response. Changes in smoking preference and special request will be passed along to the property and are not guaranteed.

        Args:
           customer_ip(str): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           test(Optional[str], optional): The change call has a test header that can be used to return set responses with the following keywords:<br>* `standard` - Requires valid test booking.* `service_unavailable`* `unknown_internal_error`
           itinerary_id(str): This parameter is used only to prefix the token value - no ID value is used.<br>
           room_id(str): Room ID of a property.<br>
           token(str): Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed.
           body(ChangeRoomDetailsRequest): The request body is required, but only the fields that are being changed need to be passed in. Fields that are not being changed should not be included in the request body.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'token': json.loads(json.dumps(token, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/itineraries/{itinerary_id}/rooms/{room_id}'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='put', body=body, response_models=[None, Error], url=request_url)

    def delete_room(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: str = None,
        customer_session_id: Optional[str] = None,
        test: Optional[str] = None,
        itinerary_id: str = None,
        room_id: str = None,
        token: str = None,
    ) -> Union[None, Error]:
        """This link will be available in the retrieve response.

        Args:
           customer_ip(str): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           test(Optional[str], optional): The cancel call has a test header that can be used to return set responses with the following keywords:<br>* `standard` - Requires valid test booking.* `service_unavailable`* `unknown_internal_error`* `post_stay_cancel`
           itinerary_id(str): This parameter is used only to prefix the token value - no ID value is used.<br>
           room_id(str): Room ID of a property.<br>
           token(str): Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'token': json.loads(json.dumps(token, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/itineraries/{itinerary_id}/rooms/{room_id}'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='delete', body=None, response_models=[None, Error], url=request_url)

    def request_undelivered_notifications(
        self,
        transaction_id: UUID = uuid4(),
        undeliverable: bool = None,
        billing_terms: Optional[str] = None,
        partner_point_of_sale: Optional[str] = None,
        payment_terms: Optional[str] = None,
        platform_name: Optional[str] = None,
    ) -> List[Notification]:
        """Use this API to fetch undelivered notifications. Up to 25 notifications are returned with each call.
        Each undelivered notification will be returned only once.

        Args:
           undeliverable(bool): Undeliverable notifications are returned when this parameter is set to `true`.
           billing_terms(Optional[str], optional): This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.
           partner_point_of_sale(Optional[str], optional): This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           payment_terms(Optional[str], optional): This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.
           platform_name(Optional[str], optional): This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
        }

        query = {
            key: value
            for key, value in {
                'undeliverable': json.loads(json.dumps(undeliverable, default=pydantic.schema.pydantic_encoder)),
                'billing_terms': json.loads(json.dumps(billing_terms, default=pydantic.schema.pydantic_encoder)),
                'partner_point_of_sale': json.loads(json.dumps(partner_point_of_sale, default=pydantic.schema.pydantic_encoder)),
                'payment_terms': json.loads(json.dumps(payment_terms, default=pydantic.schema.pydantic_encoder)),
                'platform_name': json.loads(json.dumps(platform_name, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/notifications'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=List[Notification], url=request_url)

    def request_test_notification(
        self,
        transaction_id: UUID = uuid4(),
        billing_terms: Optional[str] = None,
        partner_point_of_sale: Optional[str] = None,
        payment_terms: Optional[str] = None,
        platform_name: Optional[str] = None,
        body: TestNotificationRequest = None,
    ) -> Union[None, Error]:
        """This request triggers a test notification according to the specified event_type.
        All event types supported by the Notifications API are available to test.

        Args:
           billing_terms(Optional[str], optional): This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.
           partner_point_of_sale(Optional[str], optional): This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           payment_terms(Optional[str], optional): This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.
           platform_name(Optional[str], optional): This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           body(TestNotificationRequest): ..."""
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
        }

        query = {
            key: value
            for key, value in {
                'billing_terms': json.loads(json.dumps(billing_terms, default=pydantic.schema.pydantic_encoder)),
                'partner_point_of_sale': json.loads(json.dumps(partner_point_of_sale, default=pydantic.schema.pydantic_encoder)),
                'payment_terms': json.loads(json.dumps(payment_terms, default=pydantic.schema.pydantic_encoder)),
                'platform_name': json.loads(json.dumps(platform_name, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/notifications'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='post', body=body, response_models=[None, Error], url=request_url)

    def post_payment_sessions(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: str = None,
        customer_session_id: Optional[str] = None,
        test: Optional[str] = None,
        token: str = None,
        body: PaymentSessionsRequest = None,
    ) -> Union[None, PaymentSessions, Error]:
        """<b>This link only applies to transactions where EPS takes the customer's payment information. This includes both Expedia Collect and Property Collect transactions.</b><br>
        This link will be available in the Price Check response if payment registration is required. It returns a payment session ID and a link to create a booking. This will be the first step in the booking flow only if you've opted into Two-Factor Authentication to comply with the September 2019 EU Regulations for PSD2. Learn more with our [PSD2 Overview](https://developers.expediagroup.com/docs/rapid/lodging/booking/psd2-regulation)

        Args:
           customer_ip(str): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           test(Optional[str], optional): The book call has a test header that can be used to return set responses with the following keywords:<br>* `standard`* `service_unavailable`* `internal_server_error`
           token(str): Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed.
           body(PaymentSessionsRequest): ..."""
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'token': json.loads(json.dumps(token, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/payment-sessions'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='post', body=body, response_models=[None, PaymentSessions, Error], url=request_url)

    def get_availability(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: Optional[str] = None,
        customer_session_id: Optional[str] = None,
        test: Optional[str] = None,
        checkin: str = None,
        checkout: str = None,
        currency: str = None,
        language: str = None,
        country_code: str = None,
        occupancy: List[str] = None,
        property_id: List[str] = None,
        sales_channel: str = None,
        sales_environment: str = None,
        filter: Optional[List[Filter]] = None,
        rate_plan_count: float = None,
        rate_option: Optional[List[RateOption]] = None,
        billing_terms: Optional[str] = None,
        payment_terms: Optional[str] = None,
        partner_point_of_sale: Optional[str] = None,
        platform_name: Optional[str] = None,
        exclusion: Optional[List[Exclusion]] = None,
    ) -> Union[List[PropertyAvailability], Error]:
        """Returns rates on available room types for specified properties (maximum of 250 properties per request).  The response includes rate details such as promos, whether the rate is refundable, cancellation penalties and a full price breakdown to meet the price display requirements for your market.
        _Note_: If there are no available rooms, the response will be an empty array.
        * Multiple rooms of the same type may be requested by including multiple instances of the `occupancy` parameter.
        * The `nightly` array includes each individual night's charges. When the total price includes fees, charges, or adjustments that are not divided by night, these amounts will be included in the `stay` rate array, which details charges applied to the entire stay (each check-in).

        Args:
           customer_ip(Optional[str], optional): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           test(Optional[str], optional): Shop calls have a test header that can be used to return set responses with the following keywords:<br>* `standard`* `service_unavailable`* `unknown_internal_error`
           checkin(str): Check-in date, in ISO 8601 format (YYYY-MM-DD)
           checkout(str): Check-out date, in ISO 8601 format (YYYY-MM-DD). Availability can be searched up to 500 days in advance of this date. Total length of stay cannot exceed 28 nights.
           currency(str): Requested currency for the rates, in ISO 4217 format<br><br>Currency Options: [https://developers.expediagroup.com/docs/rapid/resources/reference/currency-options](https://developers.expediagroup.com/docs/rapid/resources/reference/currency-options)
           language(str): Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)Language Options: [https://developers.expediagroup.com/docs/rapid/resources/reference/language-options](https://developers.expediagroup.com/docs/rapid/resources/reference/language-options)
           country_code(str): The country code of the traveler's point of sale, in ISO 3166-1 alpha-2 format. This should represent the country where the shopping transaction is taking place.For more information see: [https://www.iso.org/obp/ui/#search/code/](https://www.iso.org/obp/ui/#search/code/)
           occupancy(List[str]): Defines the requested occupancy for a single room. Each room must have at least 1 adult occupant.<br>Format: `numberOfAdults[-firstChildAge[,nextChildAge]]`<br>To request multiple rooms (of the same type), include one instance of occupancy for each room requested. Up to 8 rooms may be requested or booked at once.<br>Examples:* 2 adults, one 9-year-old and one 4-year-old would be represented by `occupancy=2-9,4`.<br>* A multi-room request to lodge an additional 2 adults would be represented by `occupancy=2-9,4&occupancy=2`
           property_id(List[str]): The ID of the property you want to search for. You can provide 1 to 250 property_id parameters.
           sales_channel(str): You must provide the sales channel for the display of rates. EPS dynamically provides the best content for optimal conversion on each sales channel. If you have a sales channel that is not currently supported in this list, please contact our support team.<br>* `website` - Standard website accessed from the customer's computer* `agent_tool` - Your own agent tool used by your call center or retail store agent* `mobile_app` - An application installed on a phone or tablet device* `mobile_web` - A web browser application on a phone or tablet device* `meta` - Rates will be passed to and displayed on a 3rd party comparison website* `cache` - Rates will be used to populate a local cache
           sales_environment(str): You must provide the sales environment in which rates will be sold. EPS dynamically provides the best content for optimal conversion. If you have a sales environment that is not currently supported in this list, please contact our support team.<br>* `hotel_package` - Use when selling the hotel with a transport product, e.g. flight & hotel.* `hotel_only` - Use when selling the hotel as an individual product.* `loyalty` - Use when you are selling the hotel as part of a loyalty program and the price is converted to points.
           filter(Optional[List[Filter]], optional): Single filter type. Send multiple instances of this parameter to request multiple filters.<br>* `refundable` - Filters results to only show fully refundable rates.* `expedia_collect` - Filters results to only show rates where payment is collected by Expedia at the time of booking. These properties can be eligible for payments via Expedia Affiliate Collect(EAC).* `property_collect` - Filters results to only show rates where payment is collected by the property after booking. This can include rates that require a deposit by the property, dependent upon the deposit policies.
           rate_plan_count(float): The number of rates to return per property. The rates with the best value will be returned, e.g. a rate_plan_count=4 will return the best 4 rates, but the rates are not ordered from lowest to highest or vice versa in the response. Generally lowest rates will be prioritized.The value must be between 1 and 250.
           rate_option(Optional[List[RateOption]], optional): Request specific rate options for each property. Send multiple instances of this parameter to request multiple rate options.Accepted values:<br>* `member` - Return member rates for each property. This feature must be enabled and requires a user to be logged in to request these rates.* `net_rates` - Return net rates for each property. This feature must be enabled to request these rates.* `cross_sell` - Identify if the traffic is coming from a cross sell booking. Where the traveler has booked another service (flight, car, activities...) before hotel.
           billing_terms(Optional[str], optional): This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.
           payment_terms(Optional[str], optional): This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.
           partner_point_of_sale(Optional[str], optional): This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           platform_name(Optional[str], optional): This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           exclusion(Optional[List[Exclusion]], optional): Single exclusion type. Send multiple instances of this parameter to request multiple exclusions.<br>* `refundable_damage_deposit` - Excludes rates with refundable damage deposits from the response.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'checkin': json.loads(json.dumps(checkin, default=pydantic.schema.pydantic_encoder)),
                'checkout': json.loads(json.dumps(checkout, default=pydantic.schema.pydantic_encoder)),
                'currency': json.loads(json.dumps(currency, default=pydantic.schema.pydantic_encoder)),
                'language': json.loads(json.dumps(language, default=pydantic.schema.pydantic_encoder)),
                'country_code': json.loads(json.dumps(country_code, default=pydantic.schema.pydantic_encoder)),
                'occupancy': json.loads(json.dumps(occupancy, default=pydantic.schema.pydantic_encoder)),
                'property_id': json.loads(json.dumps(property_id, default=pydantic.schema.pydantic_encoder)),
                'sales_channel': json.loads(json.dumps(sales_channel, default=pydantic.schema.pydantic_encoder)),
                'sales_environment': json.loads(json.dumps(sales_environment, default=pydantic.schema.pydantic_encoder)),
                'filter': json.loads(json.dumps(filter, default=pydantic.schema.pydantic_encoder)),
                'rate_plan_count': json.loads(json.dumps(rate_plan_count, default=pydantic.schema.pydantic_encoder)),
                'rate_option': json.loads(json.dumps(rate_option, default=pydantic.schema.pydantic_encoder)),
                'billing_terms': json.loads(json.dumps(billing_terms, default=pydantic.schema.pydantic_encoder)),
                'payment_terms': json.loads(json.dumps(payment_terms, default=pydantic.schema.pydantic_encoder)),
                'partner_point_of_sale': json.loads(json.dumps(partner_point_of_sale, default=pydantic.schema.pydantic_encoder)),
                'platform_name': json.loads(json.dumps(platform_name, default=pydantic.schema.pydantic_encoder)),
                'exclusion': json.loads(json.dumps(exclusion, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/properties/availability'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[List[PropertyAvailability], Error], url=request_url)

    def get_property_content(
        self,
        transaction_id: UUID = uuid4(),
        customer_session_id: Optional[str] = None,
        language: str = None,
        brand_id: Optional[List[str]] = None,
        business_model: Optional[List[GetPropertyContentBusinessModel]] = None,
        category_id_exclude: Optional[List[str]] = None,
        chain_id: Optional[List[str]] = None,
        country_code: Optional[List[str]] = None,
        date_added_end: Optional[str] = None,
        date_added_start: Optional[str] = None,
        date_updated_end: Optional[str] = None,
        date_updated_start: Optional[str] = None,
        include: Optional[List[GetPropertyContentInclude]] = None,
        multi_unit: Optional[bool] = None,
        property_id: Optional[List[str]] = None,
        property_rating_max: Optional[str] = None,
        property_rating_min: Optional[str] = None,
        supply_source: str = None,
        billing_terms: Optional[str] = None,
        partner_point_of_sale: Optional[str] = None,
        payment_terms: Optional[str] = None,
        platform_name: Optional[str] = None,
    ) -> Union[Optional[Dict[str, PropertyContent]], Error]:
        """Search property content for active properties in the requested language.<br><br>

        When searching with query parameter, `property_id`, you may request 1 to 250 properties at a time.<br><br>

        When searching with query parameters other than `property_id`, the response will be paginated. The response will contain a header, `Link`. The `Link` header contains a single URL to get the immediate next page of results, and follows the [IETF standard](https://tools.ietf.org/html/rfc5988). To get the next page of results, simply follow the `next` URL in the `Link` header without modifying it. When no `Link` header is returned with an empty body and a 200 response code, the pagination has completed. If the link expires, there will be an `expires` link-extension that is the UTC date the link will expire, in ISO 8601 format.<br>

          * Example: `<https://api.ean.com/v3/properties/content?token=MY5S3j36cOcLfLBZjPYQ1abhfc8CqmjmFVzkk7euvWaunE57LLeDgaxm516m>; rel="next"; expires="2019-03-05T07:23:14.000Z"`<br><br>

        The response is a JSON map where the key is the property ID and the value is the property object itself, which can include property-level, room-level and rate-level information.

        Args:
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           language(str): Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)Language Options: [https://developers.expediagroup.com/docs/rapid/resources/reference/language-options](https://developers.expediagroup.com/docs/rapid/resources/reference/language-options)
           brand_id(Optional[List[str]], optional): The ID of the brand you want to search for. This parameter can be supplied multiple times with different values, which will include properties that match any of the requested brand IDs.
           business_model(Optional[List[GetPropertyContentBusinessModel]], optional): Search for properties with the requested business model enabled. This parameter can be supplied multiple times with different values, which will return all properties that match any of the requested business models. The value must be lower case.Possible values:  * expedia_collect - Return only properties where the payment is collected by Expedia.  * property_collect - Return only properties where the payment is collected at the property.
           category_id_exclude(Optional[List[str]], optional): Search to exclude properties that do not have the requested [category ID](https://developers.expediagroup.com/docs/rapid/lodging/content/content-reference-lists). If this parameter is not supplied, all category IDs are included. This parameter can be supplied multiple times with different values, which will exclude properties that match any of the requested category IDs.
           chain_id(Optional[List[str]], optional): The ID of the chain you want to search for. These chain IDs can be positive and negative numbers. This parameter can be supplied multiple times with different values, which will include properties that match any of the requested chain IDs.
           country_code(Optional[List[str]], optional): Search for properties with the requested country code, in ISO 3166-1 alpha-2 format. This parameter can be supplied multiple times with different values, which will include properties that match any of the requested country codes.
           date_added_end(Optional[str], optional): Search for properties added on or before the requested UTC date, in ISO 8601 format (YYYY-MM-DD)
           date_added_start(Optional[str], optional): Search for properties added on or after the requested UTC date, in ISO 8601 format (YYYY-MM-DD)
           date_updated_end(Optional[str], optional): Search for properties updated on or before the requested UTC date, in ISO 8601 format (YYYY-MM-DD)
           date_updated_start(Optional[str], optional): Search for properties updated on or after the requested UTC date, in ISO 8601 format (YYYY-MM-DD)
           include(Optional[List[GetPropertyContentInclude]], optional): Option for limiting what fields to return in the response. The value must be lower case. This parameter can be supplied multiple times with different values, which will return a combination of all fields asked for.Possible values: * property_ids - Return only the property id of the property object. * catalog - Return only the property catalog property-level fields. * address - Returns only the address fields.
           multi_unit(Optional[bool], optional): Search for multi-unit properties. If this parameter is not supplied, both single-unit and multi-unit properties will be included.Possible values:  * true - Include only properties that are multi-unit.  * false - Do not include properties that are multi-unit.
           property_id(Optional[List[str]], optional): The ID of the property you want to search for. You can provide 1 to 250 property_id parameters.
           property_rating_max(Optional[str], optional): Search for properties with a property rating less than or equal to the requested rating. The highest property rating value is 5.0.
           property_rating_min(Optional[str], optional): Search for properties with a property rating greater than or equal to the requested rating. The lowest property rating value is 0.0.
           supply_source(str): Options for which supply source you would like returned in the content response. This parameter may only be supplied once and will return all properties that match the requested supply source. An error is thrown if the parameter is provided multiple times.  * expedia - Standard Expedia supply.  * vrbo - VRBO supply.
           billing_terms(Optional[str], optional): This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.
           partner_point_of_sale(Optional[str], optional): This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           payment_terms(Optional[str], optional): This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.
           platform_name(Optional[str], optional): This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Session-Id': customer_session_id,
        }

        query = {
            key: value
            for key, value in {
                'language': json.loads(json.dumps(language, default=pydantic.schema.pydantic_encoder)),
                'brand_id': json.loads(json.dumps(brand_id, default=pydantic.schema.pydantic_encoder)),
                'business_model': json.loads(json.dumps(business_model, default=pydantic.schema.pydantic_encoder)),
                'category_id_exclude': json.loads(json.dumps(category_id_exclude, default=pydantic.schema.pydantic_encoder)),
                'chain_id': json.loads(json.dumps(chain_id, default=pydantic.schema.pydantic_encoder)),
                'country_code': json.loads(json.dumps(country_code, default=pydantic.schema.pydantic_encoder)),
                'date_added_end': json.loads(json.dumps(date_added_end, default=pydantic.schema.pydantic_encoder)),
                'date_added_start': json.loads(json.dumps(date_added_start, default=pydantic.schema.pydantic_encoder)),
                'date_updated_end': json.loads(json.dumps(date_updated_end, default=pydantic.schema.pydantic_encoder)),
                'date_updated_start': json.loads(json.dumps(date_updated_start, default=pydantic.schema.pydantic_encoder)),
                'include': json.loads(json.dumps(include, default=pydantic.schema.pydantic_encoder)),
                'multi_unit': json.loads(json.dumps(multi_unit, default=pydantic.schema.pydantic_encoder)),
                'property_id': json.loads(json.dumps(property_id, default=pydantic.schema.pydantic_encoder)),
                'property_rating_max': json.loads(json.dumps(property_rating_max, default=pydantic.schema.pydantic_encoder)),
                'property_rating_min': json.loads(json.dumps(property_rating_min, default=pydantic.schema.pydantic_encoder)),
                'supply_source': json.loads(json.dumps(supply_source, default=pydantic.schema.pydantic_encoder)),
                'billing_terms': json.loads(json.dumps(billing_terms, default=pydantic.schema.pydantic_encoder)),
                'partner_point_of_sale': json.loads(json.dumps(partner_point_of_sale, default=pydantic.schema.pydantic_encoder)),
                'payment_terms': json.loads(json.dumps(payment_terms, default=pydantic.schema.pydantic_encoder)),
                'platform_name': json.loads(json.dumps(platform_name, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/properties/content'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[Optional[Dict[str, PropertyContent]], Error], url=request_url)

    def post_geography(
        self,
        transaction_id: UUID = uuid4(),
        customer_session_id: Optional[str] = None,
        include: str = None,
        billing_terms: Optional[str] = None,
        partner_point_of_sale: Optional[str] = None,
        payment_terms: Optional[str] = None,
        platform_name: Optional[str] = None,
        supply_source: Optional[str] = None,
        body: PropertiesGeoJsonRequest = None,
    ) -> Union[Optional[Dict[str, PropertyGeography]], Error]:
        """Returns the properties within an custom polygon that represents a multi-city area or smaller.
        The coordinates of the polygon should be in [GeoJSON format](https://tools.ietf.org/html/rfc7946) and the polygon must conform to the following restrictions:
          * Polygon size - diagonal distance of the polygon must be less than 500km
          * Polygon type - only single polygons are supported
          * Number of coordinates - must be <= 2000

        Args:
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           include(str): Options for which content to return in the response. The value must be lower case.  * property_ids - Include the property IDs.
           billing_terms(Optional[str], optional): This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.
           partner_point_of_sale(Optional[str], optional): This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           payment_terms(Optional[str], optional): This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.
           platform_name(Optional[str], optional): This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           supply_source(Optional[str], optional): Filter the results to a specified supply source.
           body(PropertiesGeoJsonRequest): ..."""
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Session-Id': customer_session_id,
        }

        query = {
            key: value
            for key, value in {
                'include': json.loads(json.dumps(include, default=pydantic.schema.pydantic_encoder)),
                'billing_terms': json.loads(json.dumps(billing_terms, default=pydantic.schema.pydantic_encoder)),
                'partner_point_of_sale': json.loads(json.dumps(partner_point_of_sale, default=pydantic.schema.pydantic_encoder)),
                'payment_terms': json.loads(json.dumps(payment_terms, default=pydantic.schema.pydantic_encoder)),
                'platform_name': json.loads(json.dumps(platform_name, default=pydantic.schema.pydantic_encoder)),
                'supply_source': json.loads(json.dumps(supply_source, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/properties/geography'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(
            headers=headers, method='post', body=body, response_models=[Optional[Dict[str, PropertyGeography]], Error], url=request_url
        )

    def get_additional_availability(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: Optional[str] = None,
        customer_session_id: Optional[str] = None,
        test: Optional[str] = None,
        property_id: str = None,
        sales_channel: Optional[str] = None,
        token: str = None,
    ) -> Union[List[PropertyAvailability], Error]:
        """Returns additional rates on available room types, using the parameters of the previous call.  The response includes rate details such as promos, whether the rate is refundable, cancellation penalties and a full price breakdown to meet the price display requirements for your market.
        _Note_: If there are no available rooms, the response will be an empty array.
        * The `nightly` array includes each individual night's charges. When the total price includes fees, charges, or adjustments that are not divided by night, these amounts will be included in the `stay` rate array, which details charges applied to the entire stay (each check-in).

        Args:
           customer_ip(Optional[str], optional): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           test(Optional[str], optional): Shop calls have a test header that can be used to return set responses with the following keywords:<br>* `standard`* `service_unavailable`* `unknown_internal_error`* `no_availability`* `forbidden`
           property_id(str): Expedia Property ID.<br>
           sales_channel(Optional[str], optional): Provide the sales channel if you wish to override the sales_channel provided in the previous call. EPS dynamically provides the best content for optimal conversion on each sales channel.<br>* `website` - Standard website accessed from the customer's computer* `agent_tool` - Your own agent tool used by your call center or retail store agent* `mobile_app` - An application installed on a phone or tablet device* `mobile_web` - A web browser application on a phone or tablet device* `meta` - Rates will be passed to and displayed on a 3rd party comparison website* `cache` - Rates will be used to populate a local cache
           token(str): A hashed collection of query parameters. Used to maintain state across calls. This token is provided as part of the additional rates link from the shop or price check responses.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'sales_channel': json.loads(json.dumps(sales_channel, default=pydantic.schema.pydantic_encoder)),
                'token': json.loads(json.dumps(token, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/properties/{property_id}/availability'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[List[PropertyAvailability], Error], url=request_url)

    def get_property_guest_reviews(
        self,
        transaction_id: UUID = uuid4(),
        customer_session_id: Optional[str] = None,
        property_id: str = None,
        language: str = None,
        billing_terms: Optional[str] = None,
        payment_terms: Optional[str] = None,
        partner_point_of_sale: Optional[str] = None,
        platform_name: Optional[str] = None,
    ) -> Union[GuestReviews, Error]:
        """<i>Note: Property Guest Reviews are only available if your account is configured for access and all launch requirements have been followed. Please find the launch requirements here [https://support.expediapartnersolutions.com/hc/en-us/articles/360008646799](https://support.expediapartnersolutions.com/hc/en-us/articles/360008646799) and contact your Account Manager for more details.</i>

        The response is an individual Guest Reviews object containing multiple guest reviews for the requested active property.

        To ensure you always show the latest guest reviews, this call should be made whenever a customer looks at the details for a specific property.

        Args:
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           property_id(str): Expedia Property ID.<br>
           language(str): Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)Language Options: [https://developers.expediagroup.com/docs/rapid/resources/reference/language-options](https://developers.expediagroup.com/docs/rapid/resources/reference/language-options)
           billing_terms(Optional[str], optional): This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.
           payment_terms(Optional[str], optional): This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.
           partner_point_of_sale(Optional[str], optional): This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           platform_name(Optional[str], optional): This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Session-Id': customer_session_id,
        }

        query = {
            key: value
            for key, value in {
                'language': json.loads(json.dumps(language, default=pydantic.schema.pydantic_encoder)),
                'billing_terms': json.loads(json.dumps(billing_terms, default=pydantic.schema.pydantic_encoder)),
                'payment_terms': json.loads(json.dumps(payment_terms, default=pydantic.schema.pydantic_encoder)),
                'partner_point_of_sale': json.loads(json.dumps(partner_point_of_sale, default=pydantic.schema.pydantic_encoder)),
                'platform_name': json.loads(json.dumps(platform_name, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/properties/{property_id}/guest-reviews'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[GuestReviews, Error], url=request_url)

    def get_payment_options(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: Optional[str] = None,
        customer_session_id: Optional[str] = None,
        property_id: str = None,
        token: str = None,
    ) -> Union[PaymentOption, Error]:
        """Returns the accepted payment options.  Use this API to power your checkout page and display valid forms of payment, ensuring a smooth booking.

        Args:
           customer_ip(Optional[str], optional): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           property_id(str): Expedia Property ID.<br>
           token(str): Provided as part of the link object and used to maintain state across calls. This simplifies each subsequent call by limiting the amount of information required at each step and reduces the potential for errors. Token values cannot be viewed or changed.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
        }

        query = {
            key: value
            for key, value in {
                'token': json.loads(json.dumps(token, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/properties/{property_id}/payment-options'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[PaymentOption, Error], url=request_url)

    def price_check(
        self,
        transaction_id: UUID = uuid4(),
        customer_ip: Optional[str] = None,
        customer_session_id: Optional[str] = None,
        test: Optional[str] = None,
        property_id: str = None,
        room_id: str = None,
        rate_id: str = None,
        token: str = None,
    ) -> Union[RoomPriceCheck, Error]:
        """Confirms the price returned by the Property Availability response. Use this API to verify a previously-selected rate is still valid before booking. If the price is matched, the response returns a link to request a booking. If the price has changed, the response returns new price details and a booking link for the new price. If the rate is no longer available, the response will return a new Property Availability request link to search again for different rates. In the event of a price change, go back to Property Availability and book the property at the new price or return to additional rates for the property.

        Args:
           customer_ip(Optional[str], optional): IP address of the customer, as captured by your integration.<br>Ensure your integration passes the customer's IP, not your own. This value helps determine their location and assign the correct payment gateway.<br>Also used for fraud recovery and other important analytics.
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           test(Optional[str], optional): Price check calls have a test header that can be used to return set responses with the following keywords:  * `available`  * `price_changed`  * `sold_out`  * `service_unavailable`  * `unknown_internal_error`
           property_id(str): Expedia Property ID.<br>
           room_id(str): Room ID of a property.<br>
           rate_id(str): Rate ID of a room.<br>
           token(str): A hashed collection of query parameters. Used to maintain state across calls. This token is provided as part of the price check link from the shop response.
        """
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Ip': customer_ip,
            'Customer-Session-Id': customer_session_id,
            'Test': test,
        }

        query = {
            key: value
            for key, value in {
                'token': json.loads(json.dumps(token, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/properties/{property_id}/rooms/{room_id}/rates/{rate_id}'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[RoomPriceCheck, Error], url=request_url)

    def get_regions(
        self,
        transaction_id: UUID = uuid4(),
        customer_session_id: Optional[str] = None,
        language: str = None,
        ancestor_id: Optional[str] = None,
        iata_location_code: Optional[str] = None,
        include: List[GetRegionsInclude] = None,
        billing_terms: Optional[str] = None,
        partner_point_of_sale: Optional[str] = None,
        payment_terms: Optional[str] = None,
        platform_name: Optional[str] = None,
        country_code: Optional[List[str]] = None,
        type: Optional[List[str]] = None,
        supply_source: Optional[str] = None,
    ) -> Union[List[Region], Error]:
        """Returns the geographic definition and property mappings of regions matching the specified parameters.<br><br>

        To request all regions in the world, omit the `ancestor` query parameter. To request all regions in a specific continent, country or other level, specify the ID of that region as the `ancestor`. Refer to the list of [top level regions](https://developers.expediagroup.com/docs/rapid/lodging/geography/geography-reference-lists).<br><br>

        The response is a paginated list of regions. The response will contain a header, `Link`. The `Link` header contains a single URL to get the immediate next page of results, and follows the [IETF standard](https://tools.ietf.org/html/rfc5988). To get the next page of results, simply follow the `next` URL in the `Link` header without modifying it. When no `Link` header is returned with an empty body and a 200 response code, the pagination has completed. If the link expires, there will be an `expires` link-extension that is the UTC date the link will expire, in ISO 8601 format.<br>

        * Example: `<https://api.ean.com/v3/regions?token=DXF1ZXJ5QW5kRmV0Y2gBAAAAAAdcoBgWbUpHYTdsdFVRc2U4c0xfLUhGMzM1QQ>; rel="next"; expires="2019-03-05T07:23:14.000Z"`

        Args:
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           language(str): Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)Language Options: [https://developers.expediagroup.com/docs/rapid/resources/reference/language-options](https://developers.expediagroup.com/docs/rapid/resources/reference/language-options)
           ancestor_id(Optional[str], optional): Search for regions whose ancestors include the requested ancestor region ID. Refer to the list of [top level regions](https://developers.expediagroup.com/docs/rapid/lodging/geography/geography-reference-lists).
           iata_location_code(Optional[str], optional): Search for regions by the requested 3-character IATA location code, which will apply to both iata_airport_code and iata_airport_metro_code. The code must be upper case.
           include(List[GetRegionsInclude]): Options for which content to return in the response. This parameter can be supplied multiple times with different values. The standard and details options cannot be requested together. The value must be lower case.  * standard - Include the metadata and basic hierarchy of each region.  * details - Include the metadata, coordinates and full hierarchy of each region.  * property_ids - Include the list of property IDs within the bounding polygon of each region.  * property_ids_expanded - Include the list of property IDs within the bounding polygon of each region and property IDs from the surrounding area if minimal properties are within the region.
           billing_terms(Optional[str], optional): This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.
           partner_point_of_sale(Optional[str], optional): This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           payment_terms(Optional[str], optional): This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.
           platform_name(Optional[str], optional): This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           country_code(Optional[List[str]], optional): Filter the results to a specified country code.For more information see: [https://www.iso.org/obp/ui/#search/code/](https://www.iso.org/obp/ui/#search/code/)
           type(Optional[List[str]], optional): Filter the results to a specified region type.
           supply_source(Optional[str], optional): Filter the results to a specified supply source."""
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Session-Id': customer_session_id,
        }

        query = {
            key: value
            for key, value in {
                'language': json.loads(json.dumps(language, default=pydantic.schema.pydantic_encoder)),
                'ancestor_id': json.loads(json.dumps(ancestor_id, default=pydantic.schema.pydantic_encoder)),
                'iata_location_code': json.loads(json.dumps(iata_location_code, default=pydantic.schema.pydantic_encoder)),
                'include': json.loads(json.dumps(include, default=pydantic.schema.pydantic_encoder)),
                'billing_terms': json.loads(json.dumps(billing_terms, default=pydantic.schema.pydantic_encoder)),
                'partner_point_of_sale': json.loads(json.dumps(partner_point_of_sale, default=pydantic.schema.pydantic_encoder)),
                'payment_terms': json.loads(json.dumps(payment_terms, default=pydantic.schema.pydantic_encoder)),
                'platform_name': json.loads(json.dumps(platform_name, default=pydantic.schema.pydantic_encoder)),
                'country_code': json.loads(json.dumps(country_code, default=pydantic.schema.pydantic_encoder)),
                'type': json.loads(json.dumps(type, default=pydantic.schema.pydantic_encoder)),
                'supply_source': json.loads(json.dumps(supply_source, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/regions'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[List[Region], Error], url=request_url)

    def get_region(
        self,
        transaction_id: UUID = uuid4(),
        customer_session_id: Optional[str] = None,
        region_id: str = None,
        language: str = None,
        include: List[GetRegionInclude] = None,
        billing_terms: Optional[str] = None,
        partner_point_of_sale: Optional[str] = None,
        payment_terms: Optional[str] = None,
        platform_name: Optional[str] = None,
        supply_source: Optional[str] = None,
    ) -> Union[Region, Error]:
        """Returns the geographic definition and property mappings for the requested Region ID. The response is a single JSON formatted region object.

        Args:
           customer_session_id(Optional[str], optional): Insert your own unique value for each user session, beginning with the first API call.Continue to pass the same value for each subsequent API call during the user's session, using a new value for every new customer session.<br>Including this value greatly eases EPS's internal debugging process for issues with partner requests, as it explicitly links together request paths for individual user's session.
           region_id(str): ID of the region to retrieve.
           language(str): Desired language for the response as a subset of BCP47 format that only uses hyphenated pairs of two-digit language and country codes. Use only ISO639-1 alpha 2 language codes and ISO3166-1 alpha 2 country codes. See [https://www.w3.org/International/articles/language-tags/](https://www.w3.org/International/articles/language-tags/)Language Options: [https://developers.expediagroup.com/docs/rapid/resources/reference/language-options](https://developers.expediagroup.com/docs/rapid/resources/reference/language-options)
           include(List[GetRegionInclude]): Options for which content to return in the response. This parameter can be supplied multiple times with different values. The value must be lower case.  * details - Include the metadata, coordinates and full hierarchy of the region.  * property_ids - Include the list of property IDs within the bounding polygon of the region.  * property_ids_expanded - Include the list of property IDs within the bounding polygon of the region and property IDs from the surrounding area if minimal properties are within the region.
           billing_terms(Optional[str], optional): This parameter is to specify the terms of how a resulting booking should be billed. If this field is needed, the value for this will be provided to you separately.
           partner_point_of_sale(Optional[str], optional): This parameter is to specify what point of sale is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           payment_terms(Optional[str], optional): This parameter is to specify what terms should be used when being paid for a resulting booking. If this field is needed, the value for this will be provided to you separately.
           platform_name(Optional[str], optional): This parameter is to specify what platform is being used to shop and book. If this field is needed, the value for this will be provided to you separately.
           supply_source(Optional[str], optional): Filter the results to a specified supply source."""
        headers = {
            header.TRANSACTION_ID: transaction_id,
            header.USER_AGENT: self.__user_agent,
            'Customer-Session-Id': customer_session_id,
        }

        query = {
            key: value
            for key, value in {
                'language': json.loads(json.dumps(language, default=pydantic.schema.pydantic_encoder)),
                'include': json.loads(json.dumps(include, default=pydantic.schema.pydantic_encoder)),
                'billing_terms': json.loads(json.dumps(billing_terms, default=pydantic.schema.pydantic_encoder)),
                'partner_point_of_sale': json.loads(json.dumps(partner_point_of_sale, default=pydantic.schema.pydantic_encoder)),
                'payment_terms': json.loads(json.dumps(payment_terms, default=pydantic.schema.pydantic_encoder)),
                'platform_name': json.loads(json.dumps(platform_name, default=pydantic.schema.pydantic_encoder)),
                'supply_source': json.loads(json.dumps(supply_source, default=pydantic.schema.pydantic_encoder)),
            }.items()
            if value
        }

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/regions/{region_id}'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='get', body=None, response_models=[Region, Error], url=request_url)
