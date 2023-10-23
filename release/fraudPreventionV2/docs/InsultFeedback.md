[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [InsultFeedback](InsultFeedback.md)

# class `expediagroup.sdk.fraudpreventionv2.model.InsultFeedback`

```python
InsultFeedback(
    insult_detail: Optional[InsultDetail],
    type: Literal["INSULT_FEEDBACK"],
)
```

pydantic model InsultFeedback: Feedback from EG external partners
regarding a false positive recommendation that from Fraud Prevention
system gave for their customer.

## Attributes

| Name          | Type                                        | Required | Description |
| ------------- | ------------------------------------------- | -------- | ----------- |
| insult_detail | Optional\[[InsultDetail](InsultDetail.md)\] | False    | …           |
| type          | Literal\[“INSULT_FEEDBACK”\]                | True     | …           |

# Inheritance

object >
[OrderPurchaseUpdateRequestGeneric](OrderPurchaseUpdateRequestGeneric.md)
\> InsultFeedback
