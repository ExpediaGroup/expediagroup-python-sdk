[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Hotel](Hotel.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Hotel`

```python
Hotel(
    hotel_id: constr(max_length=200),
    price_withheld: Optional[bool],
    hotel_name: constr(max_length=200),
    room_count: Optional[int],
    address: HotelAddress,
    checkin_time: datetime,
    checkout_time: datetime,
    type: Literal["HOTEL"],
)
```

pydantic model Hotel

## Attributes

| Name           | Type                            | Required | Description                                                                                              |
| -------------- | ------------------------------- | -------- | -------------------------------------------------------------------------------------------------------- |
| address        | [HotelAddress](HotelAddress.md) | True     | …                                                                                                        |
| checkin_time   | datetime                        | True     | Local date and time of the hotel check-in, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.  |
| checkout_time  | datetime                        | True     | Local date and time of the hotel check-out, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`. |
| hotel_id       | constr(max_length=200)          | True     | Unique hotel identifier assigned by the partner.                                                         |
| hotel_name     | constr(max_length=200)          | True     | Name of the hotel.                                                                                       |
| price_withheld | Optional\[bool\]                | False    | Identifies if the product price was withheld from the customer during the booking process.               |
| room_count     | Optional\[int\]                 | False    | Total number of rooms booked within the hotel product collection.                                        |
| type           | Literal\[“HOTEL”\]              | True     | …                                                                                                        |

# Inheritance

object > [TravelProductGeneric](TravelProductGeneric.md) > Hotel
