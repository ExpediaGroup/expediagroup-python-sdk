[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [SettledRefundUpdate](SettledRefundUpdate.md)

# class `expediagroup.sdk.fraudpreventionv2.model.SettledRefundUpdate`

```
SettledRefundUpdate(
    refund_details: Optional[SettledRefundUpdateDetails],
    refund_status: Literal["SETTLED"],
)
```

pydantic model SettledRefundUpdate: Data related to the settled refund
that should be updated.

## Attributes

| Name           | Type                                                                    | Required | Description                                                                                                                        |
| -------------- | ----------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| refund_details | Optional\[[SettledRefundUpdateDetails](SettledRefundUpdateDetails.md)\] | False    | …                                                                                                                                  |
| refund_status  | Literal\[“SETTLED”\]                                                    | True     | Identifies the refund status. Possible values are:<br/>-`ISSUED` - The refund was issued.<br/>-`SETTLED` - The refund was settled. |

# Inheritance

object > [RefundUpdateGeneric](RefundUpdateGeneric.md) >
SettledRefundUpdate
