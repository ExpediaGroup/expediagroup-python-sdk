[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Status1](Status1.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Status1`

```
Status1(
)
```

pydantic model Status1: The status of a user’‘s response to the
Multi-Factor Authentication initiated by the Partner’‘s system to the
user.’

- `SUCCESS` - Applicable if the user successfully passed the
  challenge.
- `ABANDON` - Applicable if the user did not complete the challenge.
- `FAILED` - Applicable if the user failed the challenge.

## Attributes

| Name    | Type | Required | Description |
| ------- | ---- | -------- | ----------- |
| ABANDON | Any  | True     | …           |
| FAILED  | Any  | True     | …           |
| SUCCESS | Any  | True     | …           |

# Inheritance

object > Enum > Status1
