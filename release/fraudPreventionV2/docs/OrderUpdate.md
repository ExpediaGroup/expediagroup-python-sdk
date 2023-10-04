[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [OrderUpdate](OrderUpdate.md)
# class `expediagroup.sdk.fraudpreventionv2.model.OrderUpdate`
```
OrderUpdate(
    order_status: Status,
    acquirer_reference_number: Optional[constr(max_length=200)],
    cancellation_reason: Optional[CancellationReason],
    type: Literal["ORDER_UPDATE"],
)
```

pydantic model OrderUpdate: Order related data that should be updated.



## Attributes
    
    
        
    
        
    
        
    
        
    

|            Name           |                          Type                         | Required |                                                                                                                                                                                            Description                                                                                                                                                                                             |
|---------------------------|-------------------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| acquirer_reference_number |            Optional[constr(max_length=200)]           |  False   | A unique number that tags a credit or debit card transaction when it goes from the merchant's bank through to the cardholder's bank.<br/>`acquirer_reference_number` is a required field only if `order_status` = `COMPLETED`<br/>Typically, merchants can get this number from their payment processors.<br/>This number is used when dealing with disputes/chargebacks on original transactions. |
|    cancellation_reason    | Optional[[CancellationReason](CancellationReason.md)] |  False   |                                                                                                                                                                                                ...                                                                                                                                                                                                 |
|        order_status       |                  [Status](Status.md)                  |   True   |                                                                                                                                                                                                ...                                                                                                                                                                                                 |
|            type           |                Literal["ORDER_UPDATE"]                |   True   |                                                                                                                                                                                                ...                                                                                                                                                                                                 |










# Inheritance
object > [OrderPurchaseUpdateRequestGeneric](OrderPurchaseUpdateRequestGeneric.md) > OrderUpdate