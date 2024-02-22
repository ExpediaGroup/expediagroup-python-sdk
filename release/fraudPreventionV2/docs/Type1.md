[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Type1](Type1.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Type1`

```python
Type1()
```

pydantic model Type1: This field indicates the nature or relationship of
the vendor associated with a particular activity.

- `THIRD_PARTY`: This value indicates that the partner integrates with a
  third-party platform via APIs and ingests activities from them.
- `DIRECT`: This value signifies that the partner is a direct entity or
  provider associated with the organization or platform offering the
  activity.

## Attributes

| Name        | Type | Required | Description |
| ----------- | ---- | -------- | ----------- |
| DIRECT      | Any  | True     | …           |
| THIRD_PARTY | Any  | True     | …           |

# Inheritance

object > Enum > Type1
