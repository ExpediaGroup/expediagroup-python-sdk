[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [FailedLoginReason](FailedLoginReason.md)

# class `expediagroup.sdk.fraudpreventionv2.model.FailedLoginReason`

```python
FailedLoginReason()
```

pydantic model FailedLoginReason: The reason for the failed login
attempt in the Partner’‘s system, related to user failure or Partner’’s
system failure.

- `INVALID_CREDENTIALS` - Applicable if the user provided invalid login
  credentials for this login attempt.
- `ACCOUNT_NOT_FOUND` - Applicable if the user attempted to login to an
  account that doesn’t exist.
- `VERIFICATION_FAILED` - Applicable if the user failed the verification
  for this login, or any authentication exception occured in the Partner
  system for this login attempt.
- `ACCOUNT_LOCKED` - Applicable if the user attempted to login to an
  account that is locked.

## Attributes

| Name                | Type | Required | Description |
| ------------------- | ---- | -------- | ----------- |
| ACCOUNT_LOCKED      | Any  | True     | …           |
| ACCOUNT_NOT_FOUND   | Any  | True     | …           |
| INVALID_CREDENTIALS | Any  | True     | …           |
| VERIFICATION_FAILED | Any  | True     | …           |

# Inheritance

object > Enum > FailedLoginReason
