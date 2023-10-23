[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Air](Air.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Air`

```python
Air(
    departure_time: datetime,
    arrival_time: datetime,
    air_segments: list[AirSegment],
    flight_type: Optional[FlightType],
    passenger_name_record: Optional[constr(max_length=100)],
    global_distribution_system_type: Optional[constr(max_length=100)],
    type: Literal["AIR"],
)
```

pydantic model Air

## Attributes

| Name                            | Type                                    | Required | Description                                                                                                                     |
| ------------------------------- | --------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------- |
| air_segments                    | list\[[AirSegment](AirSegment.md)\]     | True     | Additional airline and flight details for each of the trip segments.                                                            |
| arrival_time                    | datetime                                | True     | Local date and time of arrival to final destination location, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.      |
| departure_time                  | datetime                                | True     | Local date and time of departure from original departure location, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`. |
| flight_type                     | Optional\[[FlightType](FlightType.md)\] | False    | Identifies the type of air trip based on the air destinations.                                                                  |
| global_distribution_system_type | Optional\[constr(max_length=100)\]      | False    | Associated with Passenger Name Record (PNR).                                                                                    |
| passenger_name_record           | Optional\[constr(max_length=100)\]      | False    | Airline booking confirmation code for the trip.                                                                                 |
| type                            | Literal\[“AIR”\]                        | True     | …                                                                                                                               |

# Inheritance

object > [TravelProductGeneric](TravelProductGeneric.md) > Air
