[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [MandateType](MandateType.md)

# class `expediagroup.sdk.fraudpreventionv2.model.MandateType`

```python
MandateType()
```

pydantic model MandateType: The `mandate_type` is required if given
`brand` as `SEPA_ELV` under `DirectDebit`. It is used for the wire
transfer or direct debit transaction whose `routing_number` could not be
provided or not supported. Allows values:

- `ONE_OFF`
- `RECURRING`

## Attributes

| Name      | Type | Required | Description |
| --------- | ---- | -------- | ----------- |
| ONE_OFF   | Any  | True     | …           |
| RECURRING | Any  | True     | …           |

# Inheritance

object > Enum > MandateType
