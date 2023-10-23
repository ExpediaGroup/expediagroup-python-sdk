[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [PaymentOperation](PaymentOperation.md)

# class `expediagroup.sdk.fraudpreventionv2.model.PaymentOperation`

```
PaymentOperation(
    id: Optional[constr(max_length=200)],
    amount: Optional[Amount],
    outcome: Optional[PaymentOutcome],
)
```

pydantic model PaymentOperation

## Attributes

| Name    | Type                                            | Required | Description |
| ------- | ----------------------------------------------- | -------- | ----------- |
| amount  | Optional\[[Amount](Amount.md)\]                 | False    | …           |
| id      | Optional\[constr(max_length=200)\]              | False    | …           |
| outcome | Optional\[[PaymentOutcome](PaymentOutcome.md)\] | False    | …           |

# Inheritance

object > BaseModel > PaymentOperation
