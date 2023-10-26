[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [OrderPurchaseTransaction](OrderPurchaseTransaction.md)

# class `expediagroup.sdk.fraudpreventionv2.model.OrderPurchaseTransaction`

```python
OrderPurchaseTransaction(
    site_info: SiteInfo,
    device_details: DeviceDetails,
    customer_account: CustomerAccount,
    transaction_details: TransactionDetails,
)
```

pydantic model OrderPurchaseTransaction

## Attributes

| Name                | Type                                        | Required | Description |
| ------------------- | ------------------------------------------- | -------- | ----------- |
| customer_account    | [CustomerAccount](CustomerAccount.md)       | True     | …           |
| device_details      | [DeviceDetails](DeviceDetails.md)           | True     | …           |
| site_info           | [SiteInfo](SiteInfo.md)                     | True     | …           |
| transaction_details | [TransactionDetails](TransactionDetails.md) | True     | …           |

# Inheritance

object > BaseModel > OrderPurchaseTransaction
