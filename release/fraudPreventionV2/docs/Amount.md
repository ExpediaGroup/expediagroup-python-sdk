[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Amount](Amount.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Amount`

```python
Amount(
    value: float,
    currency_code: constr(regex=r"^[A-Z]{3}$", max_length=3),
)
```

pydantic model Amount

## Attributes

| Name          | Type                                    | Required | Description                                                                                            |
| ------------- | --------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| currency_code | constr(regex=r”[^1]{3}$“, max_length=3) | True     | The ISO alpha-3 country code for the amount currency.                                                  |
| value         | float                                   | True     | The amount required in payment for the product/order in local currency (including any taxes and fees). |

# Inheritance

object > BaseModel > Amount

[^1]: A-Z
