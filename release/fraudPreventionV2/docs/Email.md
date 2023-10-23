[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Email](Email.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Email`

```
Email(
    email_address: Optional[EmailStr],
)
```

pydantic model Email: Group of attributes intended to hold information
about email address associated with the transaction.

## Attributes

| Name          | Type                 | Required | Description                                                                |
| ------------- | -------------------- | -------- | -------------------------------------------------------------------------- |
| email_address | Optional\[EmailStr\] | False    | Full email address including the alias, @ symbol, domain, and root domain. |

# Inheritance

object > BaseModel > Email
