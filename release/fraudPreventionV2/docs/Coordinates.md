[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Coordinates](Coordinates.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Coordinates`

```python
Coordinates(
    latitude: confloat(ge=-90.0, le=90.0),
    longitude: confloat(ge=-180.0, le=180.0),
)
```

pydantic model Coordinates: This field signifies the precise
geographical coordinates denoting the location of the activity.

## Attributes

| Name      | Type                          | Required | Description                                                           |
| --------- | ----------------------------- | -------- | --------------------------------------------------------------------- |
| latitude  | confloat(ge=-90.0, le=90.0)   | True     | The latitude in degrees. It must be in the range \[-90.0, +90.0\].    |
| longitude | confloat(ge=-180.0, le=180.0) | True     | The longitude in degrees. It must be in the range \[-180.0, +180.0\]. |

# Inheritance

object > [PydanticModel](PydanticModel.md) > Coordinates
