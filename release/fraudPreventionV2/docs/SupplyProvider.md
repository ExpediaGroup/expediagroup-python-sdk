[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [SupplyProvider](SupplyProvider.md)

# class `expediagroup.sdk.fraudpreventionv2.model.SupplyProvider`

```python
SupplyProvider(
    name: constr(max_length=200),
    type: Type1,
    vendor_name: Optional[constr(max_length=200)],
)
```

pydantic model SupplyProvider

## Attributes

| Name        | Type                               | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------- | ---------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| name        | constr(max_length=200)             | True     | This field provides name of the partner involved in offering the activity.                                                                                                                                                                                                                                                                                                                                   |
| type        | [Type1](Type1.md)                  | True     | This field indicates the nature or relationship of the vendor associated with a particular activity.<br/>\_ `THIRD_PARTY`: This value indicates that the partner integrates with a third-party platform via APIs and ingests activities from them.<br/>\_ `DIRECT`: This value signifies that the partner is a direct entity or provider associated with the organization or platform offering the activity. |
| vendor_name | Optional\[constr(max_length=200)\] | False    | This field describes the name of the third-party vendor who provided the supply provider or the operating company with the activity.                                                                                                                                                                                                                                                                         |

# Inheritance

object > [PydanticModel](PydanticModel.md) > SupplyProvider
