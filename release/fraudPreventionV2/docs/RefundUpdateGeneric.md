[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [RefundUpdateGeneric](RefundUpdateGeneric.md)
# class `expediagroup.sdk.fraudpreventionv2.model.RefundUpdateGeneric`
```
RefundUpdateGeneric(
    refund_status: RefundStatus,
    type: Literal["REFUND_UPDATE"],
)
```

pydantic model RefundUpdate: Refund related data. Update should be sent when refund is issued or settled. Amounts should include all fees and taxes.



## Attributes
    
    
        
    
        
    

|      Name     |               Type              | Required |                                                            Description                                                             |
|---------------|---------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------|
| refund_status | [RefundStatus](RefundStatus.md) |   True   | Identifies the refund status. Possible values are:<br/>-`ISSUED` - The refund was issued.<br/>-`SETTLED` - The refund was settled. |
|      type     |     Literal["REFUND_UPDATE"]    |   True   |                                                                ...                                                                 |










# Inheritance
object > [OrderPurchaseUpdateRequestGeneric](OrderPurchaseUpdateRequestGeneric.md) > RefundUpdateGeneric