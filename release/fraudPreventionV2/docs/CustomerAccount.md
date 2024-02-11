[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [CustomerAccount](CustomerAccount.md)

# class `expediagroup.sdk.fraudpreventionv2.model.CustomerAccount`

```python
CustomerAccount(
    user_id: Optional[str],
    account_type: AccountType,
    name: Name,
    email_address: EmailStr,
    telephones: Optional[list[Telephone]],
    address: Optional[Address],
    registered_time: Optional[datetime],
)
```

pydantic model CustomerAccount

## Attributes

| Name            | Type                                          | Required | Description                                                                                                                                                                                                                                                        |
| --------------- | --------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| account_type    | [AccountType](AccountType.md)                 | True     | Identifies if the customer account is known to the client. Possible values are:<br/><br/>-`GUEST` - Applicable if the partner maintains record to distinguish whether the transaction was booked via a guest account.<br/><br/>-`STANDARD` - Default account type. |
| address         | Optional\[[Address](Address.md)\]             | False    | …                                                                                                                                                                                                                                                                  |
| email_address   | EmailStr                                      | True     | Email address for the account owner.                                                                                                                                                                                                                               |
| name            | [Name](Name.md)                               | True     | …                                                                                                                                                                                                                                                                  |
| registered_time | Optional\[datetime\]                          | False    | The local date and time that the customer first registered on the client site, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.                                                                                                                        |
| telephones      | Optional\[list\[[Telephone](Telephone.md)\]\] | False    | …                                                                                                                                                                                                                                                                  |
| user_id         | Optional\[str\]                               | False    | Unique account identifier provided by the partner’s Identity Provider/System assigned to the account owner by the partner. `user_id` is specific to the partner namespace. Used to track repeat purchases by the same user.                                        |

# Inheritance

object > [PydanticModel](PydanticModel.md) > CustomerAccount
