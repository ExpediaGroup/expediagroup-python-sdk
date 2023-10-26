[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Status3](Status3.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Status3`

```python
Status3()
```

pydantic model Status3: The status of the challenge served by the
Partner’‘s system to a user before calling Expedia’’s Fraud Prevention
Service.

- `SUCCESS` - Applicable if the user successfully passed the challenge.
- `FAILED` - Applicable if the user failed the challenge.

## Attributes

| Name    | Type | Required | Description |
| ------- | ---- | -------- | ----------- |
| FAILED  | Any  | True     | …           |
| SUCCESS | Any  | True     | …           |

# Inheritance

object > Enum > Status3
