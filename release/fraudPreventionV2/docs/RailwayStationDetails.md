[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [RailwayStationDetails](RailwayStationDetails.md)

# class `expediagroup.sdk.fraudpreventionv2.model.RailwayStationDetails`

```
RailwayStationDetails(
    name: constr(max_length=200),
    type: Optional[Type],
    station_code: constr(max_length=200),
    address: Address,
    timezone: Optional[constr(max_length=200)],
)
```

pydantic model RailwayStationDetails

## Attributes

| Name         | Type                               | Required | Description                                                                                                                                                                                                                                |
| ------------ | ---------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| address      | [Address](Address.md)              | True     | …                                                                                                                                                                                                                                          |
| name         | constr(max_length=200)             | True     | The popularly known name or title by which the railway station is identified.                                                                                                                                                              |
| station_code | constr(max_length=200)             | True     | The unique identifier or code assigned to an individual rail station or a pseudo-station representing all the stations within a specific city, from which rail travel originates.                                                          |
| timezone     | Optional\[constr(max_length=200)\] | False    | The timezone associated with the location of the station, specifying the local time offset from Coordinated Universal Time (UTC).                                                                                                          |
| type         | Optional\[[Type](Type.md)\]        | False    | This attribute provides information about the specific classification assigned to the rail station. It helps differentiate between different types of stations, such as major stations (STATION) or stations located within a city (city). |

# Inheritance

object > BaseModel > RailwayStationDetails
