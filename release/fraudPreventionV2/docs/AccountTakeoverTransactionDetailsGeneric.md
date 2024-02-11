[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/
[AccountTakeoverTransactionDetailsGeneric](AccountTakeoverTransactionDetailsGeneric.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AccountTakeoverTransactionDetailsGeneric`

```python
AccountTakeoverTransactionDetailsGeneric(
    type: Type3,
    transaction_date_time: datetime,
    transaction_id: constr(max_length=200),
    current_user_session: Optional[CurrentUserSession],
)
```

pydantic model AccountTakeoverTransactionDetails: The `transaction_type`
field value is used as a discriminator, with the following mapping:

- `LOGIN`: `LoginTransactionDetails`

## Attributes

| Name                  | Type                                                    | Required | Description                                                                                                                           |
| --------------------- | ------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| current_user_session  | Optional\[[CurrentUserSession](CurrentUserSession.md)\] | False    | …                                                                                                                                     |
| transaction_date_time | datetime                                                | True     | The local date and time the transaction occured in the Partner’s system, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`. |
| transaction_id        | constr(max_length=200)                                  | True     | Unique identifier to identify a transaction attempt in the Partner’s system.                                                          |
| type                  | [Type3](Type3.md)                                       | True     | The categorized type of account event related to a user’s action.                                                                     |

# Inheritance

object > [PydanticModel](PydanticModel.md) >
AccountTakeoverTransactionDetailsGeneric
