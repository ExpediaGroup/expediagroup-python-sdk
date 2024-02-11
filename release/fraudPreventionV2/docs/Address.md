[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Address](Address.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Address`

```python
Address(
    address_type: Optional[AddressType],
    address_line1: Optional[constr(max_length=200)],
    address_line2: Optional[constr(max_length=200)],
    city: Optional[constr(max_length=200)],
    state: Optional[constr(pattern=r"^[A-Z]{2}$")],
    zip_code: Optional[constr(max_length=20)],
    country_code: Optional[constr(pattern=r"^[A-Z]{3}$")],
)
```

pydantic model Address

## Attributes

| Name          | Type                                      | Required | Description                                       |
| ------------- | ----------------------------------------- | -------- | ------------------------------------------------- |
| address_line1 | Optional\[constr(max_length=200)\]        | False    | Address line 1 of the address provided.           |
| address_line2 | Optional\[constr(max_length=200)\]        | False    | Address line 2 of the address provided.           |
| address_type  | Optional\[[AddressType](AddressType.md)\] | False    | …                                                 |
| city          | Optional\[constr(max_length=200)\]        | False    | City of the address provided.                     |
| country_code  | Optional\[constr(pattern=r”[^1]{3}$")\]   | False    | ISO alpha-3 country code of the address provided. |

```
             | state         | Optional[constr(pattern=r"^[A-Z]{2}$“)\]                                                                   | False    | The two-characters ISO code for the state or province of the address. |
```

| zip_code      | Optional\[constr(max_length=20)\]                                                                                           | False    | Zip code of the address provided.                                     |

# Inheritance

object > [PydanticModel](PydanticModel.md) > Address

[^1]: A-Z
