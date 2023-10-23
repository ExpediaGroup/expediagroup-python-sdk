[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [PaymentMethod](PaymentMethod.md)

# class `expediagroup.sdk.fraudpreventionv2.model.PaymentMethod`

```
PaymentMethod(
)
```

pydantic model PaymentMethod: The payment method used at the time of
purchase for the transaction. Supported `method`’s are: `CREDIT_CARD`,
`PAYPAL`, `POINTS`, `GIFT_CARD`, `INTERNET_BANK_PAYMENT`,
`DIRECT_DEBIT`.

## Attributes

| Name                  | Type | Required | Description |
| --------------------- | ---- | -------- | ----------- |
| CREDIT_CARD           | Any  | True     | …           |
| DIRECT_DEBIT          | Any  | True     | …           |
| GIFT_CARD             | Any  | True     | …           |
| INTERNET_BANK_PAYMENT | Any  | True     | …           |
| PAYPAL                | Any  | True     | …           |
| POINTS                | Any  | True     | …           |

# Inheritance

object > Enum > PaymentMethod
