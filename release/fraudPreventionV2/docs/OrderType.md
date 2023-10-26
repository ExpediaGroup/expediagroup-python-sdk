[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [OrderType](OrderType.md)

# class `expediagroup.sdk.fraudpreventionv2.model.OrderType`

```python
OrderType()
```

pydantic model OrderType: Type of order. Possible `order_types`.

`CREATE` - Initial type of a brand new order.

`CHANGE` - If a `OrderPurchaseScreenRequest` has already been submitted
for the initial booking with `order_type = CREATE`, but has now been
modified and partner wishes to resubmit for Fraud screening then the
`order_type = CHANGE`. Examples of changes that are supported are
changes made to `check-in/checkout dates` or `price of a TravelProduct`.

## Attributes

| Name   | Type | Required | Description |
| ------ | ---- | -------- | ----------- |
| CHANGE | Any  | True     | …           |
| CREATE | Any  | True     | …           |

# Inheritance

object > Enum > OrderType
