[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [DirectDebit](DirectDebit.md)

# class `expediagroup.sdk.fraudpreventionv2.model.DirectDebit`

```python
DirectDebit(
    routing_number: constr(max_length=15),
    account_number: constr(max_length=100),
    telephones: list[Telephone],
    method: Literal["DIRECT_DEBIT"],
)
```

pydantic model DirectDebit

## Attributes

| Name           | Type                              | Required | Description                                                                                     |
| -------------- | --------------------------------- | -------- | ----------------------------------------------------------------------------------------------- |
| account_number | constr(max_length=100)            | True     | Cleartext (unencrypted) DirectDebit bank account number associated with the payment instrument. |
| method         | Literal\[“DIRECT_DEBIT”\]         | True     | …                                                                                               |
| routing_number | constr(max_length=15)             | True     | A code that identifies the financial institution for a specific bank account.                   |
| telephones     | list\[[Telephone](Telephone.md)\] | True     | Telephone(s) associated with direct debit payment provider.                                     |

## Methods

### dict

```python
dict()
```

# Inheritance

object > [PaymentGeneric](PaymentGeneric.md) > DirectDebit
