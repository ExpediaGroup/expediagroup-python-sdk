[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [InsultDetail](InsultDetail.md)

# class `expediagroup.sdk.fraudpreventionv2.model.InsultDetail`

```
InsultDetail(
    insult_reported_date_time: Optional[datetime],
)
```

pydantic model InsultDetail: Details related to the insult.

## Attributes

| Name                      | Type                 | Required | Description                                                                                                             |
| ------------------------- | -------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------- |
| insult_reported_date_time | Optional\[datetime\] | False    | Date and time when the insult was reported to the partner, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`. |

# Inheritance

object > BaseModel > InsultDetail
