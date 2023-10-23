[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Cruise](Cruise.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Cruise`

```python
Cruise(
    departure_time: datetime,
    arrival_time: datetime,
    embarkation_port: constr(max_length=200),
    disembarkation_port: constr(max_length=200),
    ship_name: constr(max_length=200),
    type: Literal["CRUISE"],
)
```

pydantic model Cruise

## Attributes

| Name                | Type                   | Required | Description                                                                                                                     |
| ------------------- | ---------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------- |
| arrival_time        | datetime               | True     | Local date and time of arrival from original arrival location, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.     |
| departure_time      | datetime               | True     | Local date and time of departure from original departure location, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`. |
| disembarkation_port | constr(max_length=200) | True     | The cruise’s final destination.                                                                                                 |
| embarkation_port    | constr(max_length=200) | True     | Location from where cruise will depart.                                                                                         |
| ship_name           | constr(max_length=200) | True     | Name of the cruise ship.                                                                                                        |
| type                | Literal\[“CRUISE”\]    | True     | …                                                                                                                               |

# Inheritance

object > [TravelProductGeneric](TravelProductGeneric.md) > Cruise
