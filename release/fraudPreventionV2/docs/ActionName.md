[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [ActionName](ActionName.md)

# class `expediagroup.sdk.fraudpreventionv2.model.ActionName`

```python
ActionName()
```

pydantic model ActionName: The categorized remediation action initiated
by the Partner’’s system to a user. Possible values are:

- `PASSWORD_RESET` - Applicable if this event is the result of a
  password reset by the Partner’’s system.
- `DISABLE_ACCOUNT` - Applicable if this event is the result of
  disabling an account by the Partner’’s system.
- `TERMINATE_ALL_SESSIONS` - Applicable if this event is the result of
  terminating all active user sessions of an account by the Partner’’s
  system.

## Attributes

| Name                   | Type | Required | Description |
| ---------------------- | ---- | -------- | ----------- |
| DISABLE_ACCOUNT        | Any  | True     | …           |
| PASSWORD_RESET         | Any  | True     | …           |
| TERMINATE_ALL_SESSIONS | Any  | True     | …           |

# Inheritance

object > Enum > ActionName
