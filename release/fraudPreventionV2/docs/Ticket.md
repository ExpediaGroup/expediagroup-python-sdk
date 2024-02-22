[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Ticket](Ticket.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Ticket`

```python
Ticket(
    type: Type2,
    quantity: conint(ge=1, le=30),
)
```

pydantic model Ticket

## Attributes

| Name     | Type                | Required | Description                                                                        |
| -------- | ------------------- | -------- | ---------------------------------------------------------------------------------- |
| quantity | conint(ge=1, le=30) | True     | This field represents the count or number of tickets associated with the type.     |
| type     | [Type2](Type2.md)   | True     | Specifies the type of the ticket, such as ADULT, CHILD, SENIOR, STUDENT, or OTHER. |

# Inheritance

object > [PydanticModel](PydanticModel.md) > Ticket
