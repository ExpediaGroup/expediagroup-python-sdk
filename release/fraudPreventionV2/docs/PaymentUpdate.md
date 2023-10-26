[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [PaymentUpdate](PaymentUpdate.md)

# class `expediagroup.sdk.fraudpreventionv2.model.PaymentUpdate`

```python
PaymentUpdate(
    merchant_order_code: constr(max_length=200),
    type: Literal["PAYMENT_UPDATE"],
)
```

pydantic model PaymentUpdate: Payment related data that should be
updated.

## Attributes

| Name                | Type                        | Required | Description                                                                                                                                   |
| ------------------- | --------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| merchant_order_code | constr(max_length=200)      | True     | Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level. |
| type                | Literal\[“PAYMENT_UPDATE”\] | True     | …                                                                                                                                             |

# Inheritance

object >
[OrderPurchaseUpdateRequestGeneric](OrderPurchaseUpdateRequestGeneric.md)
\> PaymentUpdate
