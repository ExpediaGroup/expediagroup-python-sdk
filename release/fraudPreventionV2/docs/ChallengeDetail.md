[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [ChallengeDetail](ChallengeDetail.md)

# class `expediagroup.sdk.fraudpreventionv2.model.ChallengeDetail`

```
ChallengeDetail(
    displayed_flag: bool,
    type: Type4,
    status: Status3,
)
```

pydantic model ChallengeDetail: Information related to challenges
initiated by the Partner’s system to a user before calling Expedia’s
Fraud Prevention Service.

## Attributes

| Name           | Type                  | Required | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------- | --------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| displayed_flag | bool                  | True     | Indicates that there was a challenge initiated by the Partner’s system to a user before calling Expedia’s Fraud Prevention Service.                                                                                                                                                                                                                                                                    |
| status         | [Status3](Status3.md) | True     | The status of the challenge served by the Partner’‘s system to a user before calling Expedia’’s Fraud Prevention Service.<br/>- `SUCCESS` - Applicable if the user successfully passed the challenge.<br/>- `FAILED` - Applicable if the user failed the challenge.                                                                                                                                    |
| type           | [Type4](Type4.md)     | True     | The kind of challenge served by the Partner’‘s system to a user prior to calling Expedia’‘s Fraud Prevention Service.<br/>- `CAPTCHA` - Applicable if the challenge served by the Partner’‘s system was a Captcha challenge.<br/>- `TWO_FACTOR` - Applicable if the challenge served by the Partner’’s system was a two-factor challenge including (Email verification, One Time Password, Okta, etc). |

# Inheritance

object > BaseModel > ChallengeDetail
