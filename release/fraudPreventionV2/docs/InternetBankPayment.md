[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [InternetBankPayment](InternetBankPayment.md)

# class `expediagroup.sdk.fraudpreventionv2.model.InternetBankPayment`

```python
InternetBankPayment(
    bank_id: constr(max_length=15),
    bank_branch_code: constr(max_length=15),
    telephones: list[Telephone],
    method: Literal["INTERNET_BANK_PAYMENT"],
)
```

pydantic model InternetBankPayment

## Attributes

| Name             | Type                               | Required | Description                                                                                                                      |
| ---------------- | ---------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------- |
| bank_branch_code | constr(max_length=15)              | True     | A code that identifies the bank branch for internet bank payment(IBP).                                                           |
| bank_id          | constr(max_length=15)              | True     | The bank_id provided by the internet bank payment(IBP) provider (DRWP aka NetGiro) for the bank used for processing the payment. |
| method           | Literal\[“INTERNET_BANK_PAYMENT”\] | True     | …                                                                                                                                |
| telephones       | list\[[Telephone](Telephone.md)\]  | True     | Telephone(s) associated with internet bank payment(IBP) provider.                                                                |

# Inheritance

object > [PaymentGeneric](PaymentGeneric.md) > InternetBankPayment
