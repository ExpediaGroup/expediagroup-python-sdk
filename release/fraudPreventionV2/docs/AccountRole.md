[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [AccountRole](AccountRole.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AccountRole`

```
AccountRole(
)
```

pydantic model AccountRole: Identifies the account role and associated
permissions of a user’’s account. Possible values are:

- `USER`: Basic account with no special privileges.
- `MANAGER`: Account with additional privileges, such as the ability
  to make bookings for others.
- `ADMIN`: Account with higher privileges than a manager, including
  the ability to grant manager access to other users.

## Attributes

| Name    | Type | Required | Description |
| ------- | ---- | -------- | ----------- |
| ADMIN   | Any  | True     | …           |
| MANAGER | Any  | True     | …           |
| USER    | Any  | True     | …           |

# Inheritance

object > Enum > AccountRole
