[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Rail](Rail.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Rail`

```
Rail(
    route_type: RouteType,
    rail_segments: list[RailSegments],
    type: Literal["RAIL"],
)
```

pydantic model Rail

## Attributes

| Name          | Type                                    | Required | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------- | --------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rail_segments | list\[[RailSegments](RailSegments.md)\] | True     | …                                                                                                                                                                                                                                                                                                                                                                |
| route_type    | [RouteType](RouteType.md)               | True     | The type of route or itinerary for the Rail product, indicating the travel arrangement and pattern. Possible values are:<br/>- `MULTIPLE_DESTINATIONS` - The Rail product includes multiple destinations in its itinerary.<br/>- `ONE_WAY` - The Rail product represents a one-way journey.<br/>- `ROUNDTRIP` - The Rail product represents a roundtrip journey. |
| type          | Literal\[“RAIL”\]                       | True     | …                                                                                                                                                                                                                                                                                                                                                                |

# Inheritance

object > [TravelProductGeneric](TravelProductGeneric.md) > Rail
