[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [CurrentUserSession](CurrentUserSession.md)

# class `expediagroup.sdk.fraudpreventionv2.model.CurrentUserSession`

```python
CurrentUserSession(
    session_id: Optional[constr(max_length=200)],
    start_date_time: Optional[datetime],
    challenge_detail: Optional[ChallengeDetail],
)
```

pydantic model CurrentUserSession: The current user session prior to
this transaction, which contains details related to any challenge
initiated by the Partner’‘s system to a user before calling Expedia’‘s
Fraud Prevention Service. An example is if the Partner’‘s system sent a
Captcha challenge to the user before calling Expedia’’s Fraud Prevention
Service.

## Attributes

| Name             | Type                                              | Required | Description                                                                                                    |
| ---------------- | ------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| challenge_detail | Optional\[[ChallengeDetail](ChallengeDetail.md)\] | False    | …                                                                                                              |
| session_id       | Optional\[constr(max_length=200)\]                | False    | Unique identifier for a user’s session on their device                                                         |
| start_date_time  | Optional\[datetime\]                              | False    | The local date and time a user’s session started, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`. |

# Inheritance

object > BaseModel > CurrentUserSession
