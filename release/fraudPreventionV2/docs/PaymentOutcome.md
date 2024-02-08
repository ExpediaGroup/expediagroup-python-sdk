[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [PaymentOutcome](PaymentOutcome.md)

# class `expediagroup.sdk.fraudpreventionv2.model.PaymentOutcome`

```python
PaymentOutcome(
    status: Optional[PaymentStatus],
    code: Optional[constr(max_length=200)],
    description: Optional[constr(max_length=200)],
)
```

pydantic model PaymentOutcome

## Attributes

| Name        | Type                                          | Required | Description                                                                       |
| ----------- | --------------------------------------------- | -------- | --------------------------------------------------------------------------------- |
| code        | Optional\[constr(max_length=200)\]            | False    | A mnemonic code for the payment processing.                                       |
| description | Optional\[constr(max_length=200)\]            | False    | A short description providing additional explanation regarding the mnemonic code. |
| status      | Optional\[[PaymentStatus](PaymentStatus.md)\] | False    | …                                                                                 |

# Inheritance

object > [PydanticModel](PydanticModel.md) > PaymentOutcome
