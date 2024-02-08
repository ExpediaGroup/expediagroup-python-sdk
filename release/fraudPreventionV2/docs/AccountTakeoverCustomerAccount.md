[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [AccountTakeoverCustomerAccount](AccountTakeoverCustomerAccount.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AccountTakeoverCustomerAccount`

```python
AccountTakeoverCustomerAccount(
    user_id: constr(max_length=200),
    account_type: AccountType1,
    account_role: Optional[AccountRole],
    name: Optional[AccountTakeoverName],
    username: constr(max_length=200),
    email_address: EmailStr,
    telephones: Optional[list[Telephone]],
    address: Optional[Address],
    registered_time: datetime,
    active_flag: bool,
    loyalty_member_id: Optional[constr(max_length=200)],
)
```

pydantic model AccountTakeoverCustomerAccount: Information about a
user’s account.

## Attributes

| Name              | Type                                                      | Required | Description                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------- | --------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_role      | Optional\[[AccountRole](AccountRole.md)\]                 | False    | Identifies the account role and associated permissions of a user’’s account. Possible values are:<br/>- `USER`: Basic account with no special privileges.<br/>- `MANAGER`: Account with additional privileges, such as the ability to make bookings for others.<br/>- `ADMIN`: Account with higher privileges than a manager, including the ability to grant manager access to other users. |
| account_type      | [AccountType1](AccountType1.md)                           | True     | Identifies the account type of a user’’s account. Possible values are:<br/>- `INDIVIDUAL` - Applicable if this account is for an individual traveler.<br/>- `BUSINESS` - Applicable if this account is for a business or organization account used by suppliers or Partners.                                                                                                                |
| active_flag       | bool                                                      | True     | Indicator for if this account is an active account or not.                                                                                                                                                                                                                                                                                                                                  |
| address           | Optional\[[Address](Address.md)\]                         | False    | …                                                                                                                                                                                                                                                                                                                                                                                           |
| email_address     | EmailStr                                                  | True     | Email address for the account owner.                                                                                                                                                                                                                                                                                                                                                        |
| loyalty_member_id | Optional\[constr(max_length=200)\]                        | False    | Unique loyalty identifier for a user.                                                                                                                                                                                                                                                                                                                                                       |
| name              | Optional\[[AccountTakeoverName](AccountTakeoverName.md)\] | False    | …                                                                                                                                                                                                                                                                                                                                                                                           |
| registered_time   | datetime                                                  | True     | The local date and time that the customer first registered on the Partner’s site, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.                                                                                                                                                                                                                                              |
| telephones        | Optional\[list\[[Telephone](Telephone.md)\]\]             | False    | …                                                                                                                                                                                                                                                                                                                                                                                           |
| user_id           | constr(max_length=200)                                    | True     | Unique account identifier provided by the Partner’s Identity Provider/System assigned to the account owner by the partner. `user_id` is specific to the Partner’s namespace. Used to track repeat account activity by the same user.                                                                                                                                                        |
| username          | constr(max_length=200)                                    | True     | Username of the account.                                                                                                                                                                                                                                                                                                                                                                    |

# Inheritance

object > [PydanticModel](PydanticModel.md) >
AccountTakeoverCustomerAccount
