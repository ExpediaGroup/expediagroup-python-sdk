[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [VerificationType](VerificationType.md)

# class `expediagroup.sdk.fraudpreventionv2.model.VerificationType`

```
VerificationType(
)
```

pydantic model VerificationType: The type of the verification used to
verify the instrument. If the Card Verfication Value was provided to
verify the credit card used for the transaction, `type = CVV`.

## Attributes

| Name      | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| CVV       | Any  | True     | …           |
| field_3DS | Any  | True     | …           |

# Inheritance

object > Enum > VerificationType
