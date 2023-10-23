[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [CurrentOrderStatus](CurrentOrderStatus.md)

# class `expediagroup.sdk.fraudpreventionv2.model.CurrentOrderStatus`

```
CurrentOrderStatus(
)
```

pydantic model CurrentOrderStatus: Status of the order:

- `IN_PROGRESS` is used when order has not processed fully. For
  example, inventory has not yet been reserved, or payment has not yet
  been settled.
- `COMPLETED` is used when an order has been processed fully. For
  example, inventory has been reserved, and the payment has been
  settled.

## Attributes

| Name        | Type | Required | Description |
| ----------- | ---- | -------- | ----------- |
| COMPLETED   | Any  | True     | …           |
| IN_PROGRESS | Any  | True     | …           |

# Inheritance

object > Enum > CurrentOrderStatus
