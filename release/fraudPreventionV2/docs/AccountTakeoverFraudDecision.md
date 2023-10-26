[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [AccountTakeoverFraudDecision](AccountTakeoverFraudDecision.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AccountTakeoverFraudDecision`

```python
AccountTakeoverFraudDecision()
```

pydantic model AccountTakeoverFraudDecision: Fraud recommendation for an
account transaction. A recommendation can be ACCEPT, CHALLENGE, or
REJECT.

- `ACCEPT` - Represents an account transaction where the user’’s account
  activity is accepted.
- `CHALLENGE` - Represents an account transaction that requires
  additional verification or challenges the user’’s identity (example:
  CAPTCHA, MULTI_FACTOR_AUTHENTICATION, etc).
- `REJECT` - Represents a suspicious account transaction where the
  user’’s credentials or their behavior requires us to block the account
  activity.

## Attributes

| Name      | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| ACCEPT    | Any  | True     | …           |
| CHALLENGE | Any  | True     | …           |
| REJECT    | Any  | True     | …           |

# Inheritance

object > Enum > AccountTakeoverFraudDecision
