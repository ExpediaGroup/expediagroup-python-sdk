[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [ChargebackFeedback](ChargebackFeedback.md)

# class `expediagroup.sdk.fraudpreventionv2.model.ChargebackFeedback`

```
ChargebackFeedback(
    chargeback_detail: Optional[ChargebackDetail],
    type: Literal["CHARGEBACK_FEEDBACK"],
)
```

pydantic model ChargebackFeedback: Feedback from EG external partners if
they receive a chargeback for a false negative recommendation from Fraud
Prevention system.

## Attributes

| Name              | Type                                                | Required | Description |
| ----------------- | --------------------------------------------------- | -------- | ----------- |
| chargeback_detail | Optional\[[ChargebackDetail](ChargebackDetail.md)\] | False    | …           |
| type              | Literal\[“CHARGEBACK_FEEDBACK”\]                    | True     | …           |

# Inheritance

object >
[OrderPurchaseUpdateRequestGeneric](OrderPurchaseUpdateRequestGeneric.md)
\> ChargebackFeedback
