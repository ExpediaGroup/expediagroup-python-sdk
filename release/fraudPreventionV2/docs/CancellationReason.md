[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [CancellationReason](CancellationReason.md)

# class `expediagroup.sdk.fraudpreventionv2.model.CancellationReason`

```python
CancellationReason(
    primary_reason_code: Optional[constr(max_length=200)],
    sub_reason_code: Optional[constr(max_length=200)],
    primary_reason_description: Optional[constr(max_length=200)],
    sub_reason_description: Optional[constr(max_length=200)],
)
```

pydantic model CancellationReason: Reason of order update cancellation.

## Attributes

| Name                       | Type                               | Required | Description                                                               |
| -------------------------- | ---------------------------------- | -------- | ------------------------------------------------------------------------- |
| primary_reason_code        | Optional\[constr(max_length=200)\] | False    | Primary cancellation reason code.                                         |
| primary_reason_description | Optional\[constr(max_length=200)\] | False    | Primary cancellation reason code. Required if `order_status = CANCELLED`. |
| sub_reason_code            | Optional\[constr(max_length=200)\] | False    | Substitute cancellation reason code.                                      |
| sub_reason_description     | Optional\[constr(max_length=200)\] | False    | Substitute cancellation reason description.                               |

# Inheritance

object > BaseModel > CancellationReason
