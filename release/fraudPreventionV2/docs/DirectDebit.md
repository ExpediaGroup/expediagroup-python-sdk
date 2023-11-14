[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [DirectDebit](DirectDebit.md)

# class `expediagroup.sdk.fraudpreventionv2.model.DirectDebit`

```python
DirectDebit(
    routing_number: Optional[constr(max_length=15)],
    account_number: constr(max_length=100),
    mandate_type: Optional[MandateType],
    telephones: list[Telephone],
    method: Literal["DIRECT_DEBIT"],
)
```

pydantic model DirectDebit

## Attributes

| Name           | Type                                      | Required | Description                                                                                                                                                                                                                                                                 |
| -------------- | ----------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_number | constr(max_length=100)                    | True     | Cleartext (unencrypted) DirectDebit bank account number associated with the payment instrument.                                                                                                                                                                             |
| mandate_type   | Optional\[[MandateType](MandateType.md)\] | False    | The `mandate_type` is required if given `brand` as `SEPA_ELV` under `DirectDebit`. <br/>It is used for the wire transfer or direct debit transaction whose `routing_number` could not be provided or not supported. <br/>Allows values: <br/>- `ONE_OFF` <br/>- `RECURRING` |
| method         | Literal\[“DIRECT_DEBIT”\]                 | True     | …                                                                                                                                                                                                                                                                           |
| routing_number | Optional\[constr(max_length=15)\]         | False    | A code that identifies the financial institution for a specific bank account. `routing_number` is required if given `INTER_COMPANY` or `ELV` as `brand`.                                                                                                                    |
| telephones     | list\[[Telephone](Telephone.md)\]         | True     | Telephone(s) associated with direct debit payment provider.                                                                                                                                                                                                                 |

## Methods

### \_\_account_number_validator

```python
__account_number_validator()
```

# Inheritance

object > [PaymentGeneric](PaymentGeneric.md) > DirectDebit
