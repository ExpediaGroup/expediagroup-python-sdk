[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [RouteType](RouteType.md)

# class `expediagroup.sdk.fraudpreventionv2.model.RouteType`

```
RouteType(
)
```

pydantic model RouteType: The type of route or itinerary for the Rail
product, indicating the travel arrangement and pattern. Possible values
are:

- `MULTIPLE_DESTINATIONS` - The Rail product includes multiple
  destinations in its itinerary.
- `ONE_WAY` - The Rail product represents a one-way journey.
- `ROUNDTRIP` - The Rail product represents a roundtrip journey.

## Attributes

| Name                  | Type | Required | Description |
| --------------------- | ---- | -------- | ----------- |
| MULTIPLE_DESTINATIONS | Any  | True     | …           |
| ONE_WAY               | Any  | True     | …           |
| ROUND_TRIP            | Any  | True     | …           |

# Inheritance

object > Enum > RouteType
