[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [IssuedRefundUpdateDetails](IssuedRefundUpdateDetails.md)

# class `expediagroup.sdk.fraudpreventionv2.model.IssuedRefundUpdateDetails`

```
IssuedRefundUpdateDetails(
    refund_issued_date_time: datetime,
    refund_issued_amount: Amount,
)
```

pydantic model IssuedRefundUpdateDetails: Data that describes issued
refund that should be updated.

## Attributes

| Name                    | Type                | Required | Description                                                                                                                                                     |
| ----------------------- | ------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| refund_issued_amount    | [Amount](Amount.md) | True     | …                                                                                                                                                               |
| refund_issued_date_time | datetime            | True     | Date and time when the 3rd party payment processor confirmed that a previously submitted payment refund has issued at the participating financial institutions. |

# Inheritance

object > BaseModel > IssuedRefundUpdateDetails
