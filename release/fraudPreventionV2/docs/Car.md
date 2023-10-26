[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Car](Car.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Car`

```python
Car(
    pick_up_location: constr(max_length=200),
    drop_off_location: constr(max_length=200),
    pickup_time: datetime,
    return_time: datetime,
    type: Literal["CAR"],
)
```

pydantic model Car

## Attributes

| Name              | Type                   | Required | Description                                                                                                        |
| ----------------- | ---------------------- | -------- | ------------------------------------------------------------------------------------------------------------------ |
| drop_off_location | constr(max_length=200) | True     | Location at which the automobile will be returned.                                                                 |
| pick_up_location  | constr(max_length=200) | True     | Location where the automobile will be picked up.                                                                   |
| pickup_time       | datetime               | True     | Local date and time the automobile will be picked-up, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`. |
| return_time       | datetime               | True     | Local date and time the automobile will be returned, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.  |
| type              | Literal\[“CAR”\]       | True     | …                                                                                                                  |

# Inheritance

object > [TravelProductGeneric](TravelProductGeneric.md) > Car
