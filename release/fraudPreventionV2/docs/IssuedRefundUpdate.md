[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [IssuedRefundUpdate](IssuedRefundUpdate.md)
# class `expediagroup.sdk.fraudpreventionv2.model.IssuedRefundUpdate`
```
IssuedRefundUpdate(
    refund_details: Optional[IssuedRefundUpdateDetails],
    refund_status: Literal["ISSUED"],
)
```

pydantic model IssuedRefundUpdate: Data related to the issued refund that should be updated.



## Attributes
    
    
        
    
        
    

|      Name      |                                 Type                                | Required |                                                            Description                                                             |
|----------------|---------------------------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------|
| refund_details | Optional[[IssuedRefundUpdateDetails](IssuedRefundUpdateDetails.md)] |  False   |                                                                ...                                                                 |
| refund_status  |                          Literal["ISSUED"]                          |   True   | Identifies the refund status. Possible values are:<br/>-`ISSUED` - The refund was issued.<br/>-`SETTLED` - The refund was settled. |










# Inheritance
object > [RefundUpdateGeneric](RefundUpdateGeneric.md) > IssuedRefundUpdate