[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/
[OrderPurchaseUpdateRequestGeneric](OrderPurchaseUpdateRequestGeneric.md)

# class `expediagroup.sdk.fraudpreventionv2.model.OrderPurchaseUpdateRequestGeneric`

```python
OrderPurchaseUpdateRequestGeneric(
    type: UpdateType,
    risk_id: constr(max_length=200),
)
```

pydantic model OrderPurchaseUpdateRequest: The `type` field value is
used as a discriminator, with the following mapping:

- `ORDER_UPDATE`: `OrderUpdate`
- `CHARGEBACK_FEEDBACK`: `ChargebackFeedback`
- `INSULT_FEEDBACK`: `InsultFeedback`
- `REFUND_UPDATE`: `RefundUpdate`
- `PAYMENT_UPDATE`: `PaymentUpdate`

## Attributes

| Name    | Type                        | Required | Description                                                                                        |
| ------- | --------------------------- | -------- | -------------------------------------------------------------------------------------------------- |
| risk_id | constr(max_length=200)      | True     | The `risk_id` provided by Expedia’s Fraud Prevention Service in the `OrderPurchaseScreenResponse`. |
| type    | [UpdateType](UpdateType.md) | True     | …                                                                                                  |

# Inheritance

object > [PydanticModel](PydanticModel.md) >
OrderPurchaseUpdateRequestGeneric
