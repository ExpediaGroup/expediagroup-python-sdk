[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Type6](Type6.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Type6`

```python
Type6()
```

pydantic model Type6: The kind of challenge served by the Partner’‘s
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

object > Enum > Type6
