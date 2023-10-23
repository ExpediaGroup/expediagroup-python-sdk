[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Type4](Type4.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Type4`

```python
Type4()
```

pydantic model Type4: The kind of challenge served by the Partner’‘s
system to a user prior to calling Expedia’’s Fraud Prevention Service.

- `CAPTCHA` - Applicable if the challenge served by the Partner’’s
  system was a Captcha challenge.
- `TWO_FACTOR` - Applicable if the challenge served by the Partner’’s
  system was a two-factor challenge including (Email verification, One
  Time Password, Okta, etc).

## Attributes

| Name       | Type | Required | Description |
| ---------- | ---- | -------- | ----------- |
| CAPTCHA    | Any  | True     | …           |
| TWO_FACTOR | Any  | True     | …           |

# Inheritance

object > Enum > Type4
