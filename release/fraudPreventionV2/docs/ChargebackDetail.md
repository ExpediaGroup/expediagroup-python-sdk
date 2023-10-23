[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [ChargebackDetail](ChargebackDetail.md)

# class `expediagroup.sdk.fraudpreventionv2.model.ChargebackDetail`

```
ChargebackDetail(
    chargeback_status: ChargebackStatus,
    chargeback_reason: ChargebackReason,
    chargeback_amount: Amount,
    bank_reason_code: Optional[constr(max_length=200)],
    chargeback_reported_date_time: Optional[datetime],
)
```

pydantic model ChargebackDetail: Details related to the chargeback.

## Attributes

| Name                          | Type                                    | Required | Description                                                                                                                                                   |
| ----------------------------- | --------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bank_reason_code              | Optional\[constr(max_length=200)\]      | False    | Unique code provided by the acquiring bank for the category of fraud.                                                                                         |
| chargeback_amount             | [Amount](Amount.md)                     | True     | …                                                                                                                                                             |
| chargeback_reason             | [ChargebackReason](ChargebackReason.md) | True     | Reason for chargeback which can be `Fraud` or `Non Fraud`.                                                                                                    |
| chargeback_reported_date_time | Optional\[datetime\]                    | False    | Date and time when the chargeback was reported to the partner, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.                                   |
| chargeback_status             | [ChargebackStatus](ChargebackStatus.md) | True     | Identifies the chargeback status. Possible values are:<br/>-`RECEIVED` - The chargeback was received.<br/>-`REVERSAL` - The chargeback reversal was received. |

# Inheritance

object > BaseModel > ChargebackDetail
