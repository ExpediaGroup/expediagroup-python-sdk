[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [AccountScreenResponse](AccountScreenResponse.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AccountScreenResponse`

```python
AccountScreenResponse(
    risk_id: Optional[constr(max_length=200)],
    decision: Optional[AccountTakeoverFraudDecision],
)
```

pydantic model AccountScreenResponse: Response for an account
transaction provided by Expedia’s Fraud Prevention Service.

## Attributes

| Name     | Type                                                                        | Required | Description                                                                          |
| -------- | --------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------ |
| decision | Optional\[[AccountTakeoverFraudDecision](AccountTakeoverFraudDecision.md)\] | False    | …                                                                                    |
| risk_id  | Optional\[constr(max_length=200)\]                                          | False    | Unique identifier assigned to the transaction by Expedia’s Fraud Prevention Service. |

# Inheritance

object > BaseModel > AccountScreenResponse
