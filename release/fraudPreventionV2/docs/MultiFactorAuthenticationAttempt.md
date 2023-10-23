[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/
[MultiFactorAuthenticationAttempt](MultiFactorAuthenticationAttempt.md)

# class `expediagroup.sdk.fraudpreventionv2.model.MultiFactorAuthenticationAttempt`

```
MultiFactorAuthenticationAttempt(
    delivery_method: DeliveryMethod,
    status: Status1,
    reference_id: constr(max_length=200),
    provider_name: constr(max_length=200),
    attempt_count: float,
    update_start_date_time: Optional[datetime],
    update_end_date_time: Optional[datetime],
    telephone: Optional[Telephone],
    email_address: Optional[EmailStr],
)
```

pydantic model MultiFactorAuthenticationAttempt: Information specific to
the update event by a user.

## Attributes

| Name                   | Type                                  | Required | Description                                                                                                                                                                                                                                                                                                                             |
| ---------------------- | ------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| attempt_count          | float                                 | True     | The number of attempts a user tried for this Multi-Factor Authentication.                                                                                                                                                                                                                                                               |
| delivery_method        | [DeliveryMethod](DeliveryMethod.md)   | True     | The delivery method of the Multi-Factor Authentication to a user.                                                                                                                                                                                                                                                                       |
| email_address          | Optional\[EmailStr\]                  | False    | Email address used for the Multi-Factor Authentication by a user.                                                                                                                                                                                                                                                                       |
| provider_name          | constr(max_length=200)                | True     | The vendor providing the Multi-Factor Authentication verification.                                                                                                                                                                                                                                                                      |
| reference_id           | constr(max_length=200)                | True     | The identifier related to a Multi-Factor Authentication attempt by the Partner’s system to the Multi-Factor Authentication provider.                                                                                                                                                                                                    |
| status                 | [Status1](Status1.md)                 | True     | The status of a user’‘s response to the Multi-Factor Authentication initiated by the Partner’‘s system to the user.’<br/>- `SUCCESS` - Applicable if the user successfully passed the challenge.<br/>- `ABANDON` - Applicable if the user did not complete the challenge.<br/>- `FAILED` - Applicable if the user failed the challenge. |
| telephone              | Optional\[[Telephone](Telephone.md)\] | False    | …                                                                                                                                                                                                                                                                                                                                       |
| update_end_date_time   | Optional\[datetime\]                  | False    | The local date and time the Multi-Factor Authentication to a user ended in the Partner’s system, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.                                                                                                                                                                           |
| update_start_date_time | Optional\[datetime\]                  | False    | The local date and time the Multi-Factor Authentication was initiated to a user from the Partner’s system, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.                                                                                                                                                                 |

# Inheritance

object > BaseModel > MultiFactorAuthenticationAttempt
