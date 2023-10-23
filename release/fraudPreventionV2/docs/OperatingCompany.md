[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [OperatingCompany](OperatingCompany.md)

# class `expediagroup.sdk.fraudpreventionv2.model.OperatingCompany`

```
OperatingCompany(
    marketing_name: Optional[constr(max_length=200)],
)
```

pydantic model OperatingCompany: This attribute captures the name or
identifier of the company responsible for operating the Rail product. It
represents the specific operating entity, such as Amtrak, British
Railways, or a bus company.

## Attributes

| Name           | Type                               | Required | Description                                                                                                            |
| -------------- | ---------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------- |
| marketing_name | Optional\[constr(max_length=200)\] | False    | The name used by the transportation carrier for marketing purposes in the travel segment. Example: ARX, AMTRAC, ARRIVA |

# Inheritance

object > BaseModel > OperatingCompany
