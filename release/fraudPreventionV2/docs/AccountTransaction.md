[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [AccountTransaction](AccountTransaction.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AccountTransaction`

```
AccountTransaction(
    site_info: AccountTakeoverSiteInfo,
    device_details: AccountTakeoverDeviceDetails,
    customer_account: AccountTakeoverCustomerAccount,
    transaction_details: AccountTakeoverTransactionDetails,
)
```

pydantic model AccountTransaction: Information for an account
transaction.

## Attributes

| Name                | Type                                                                                                                                                    | Required | Description |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ----------- |
| customer_account    | [AccountTakeoverCustomerAccount](AccountTakeoverCustomerAccount.md)                                                                                     | True     | …           |
| device_details      | [AccountTakeoverDeviceDetails](AccountTakeoverDeviceDetails.md)                                                                                         | True     | …           |
| site_info           | [AccountTakeoverSiteInfo](AccountTakeoverSiteInfo.md)                                                                                                   | True     | …           |
| transaction_details | Union\[[LoginTransactionDetails](LoginTransactionDetails.md), [AccountTakeoverTransactionDetailsGeneric](AccountTakeoverTransactionDetailsGeneric.md)\] | True     | …           |

# Inheritance

object > BaseModel > AccountTransaction
