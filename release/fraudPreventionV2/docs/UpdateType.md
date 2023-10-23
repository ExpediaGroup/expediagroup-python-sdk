[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [UpdateType](UpdateType.md)

# class `expediagroup.sdk.fraudpreventionv2.model.UpdateType`

```
UpdateType(
)
```

pydantic model UpdateType: Transaction type associated with the update
event.

## Attributes

| Name                | Type | Required | Description |
| ------------------- | ---- | -------- | ----------- |
| CHARGEBACK_FEEDBACK | Any  | True     | …           |
| INSULT_FEEDBACK     | Any  | True     | …           |
| ORDER_UPDATE        | Any  | True     | …           |
| PAYMENT_UPDATE      | Any  | True     | …           |
| REFUND_UPDATE       | Any  | True     | …           |

# Inheritance

object > Enum > UpdateType
