[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [SiteInfo](SiteInfo.md)

# class `expediagroup.sdk.fraudpreventionv2.model.SiteInfo`

```python
SiteInfo(
    country_code: constr(pattern=r"^[A-Z]{3}$"),
    agent_assisted: bool,
)
```

pydantic model SiteInfo

## Attributes

| Name           | Type                        | Required | Description                                                                                                               |
| -------------- | --------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------- |
| agent_assisted | bool                        | True     | Identifies if an agent assisted in booking travel for the customer. `False` if the order was directly booked by customer. |
| country_code   | constr(pattern=r”[^1]{3}$“) | True     | The alpha-3 ISO code that represents a country name.                                                                      |

# Inheritance

object > [PydanticModel](PydanticModel.md) > SiteInfo

[^1]: A-Z
