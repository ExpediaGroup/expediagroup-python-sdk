[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [InventorySource](InventorySource.md)
# class `expediagroup.sdk.fraudpreventionv2.model.InventorySource`
```
InventorySource(
)
```

pydantic model InventorySource: Identifies the business model through which the supply is being sold. Merchant/Agency.
* `MERCHANT` is used when Partner is the merchant of record for this order.
* `AGENCY` is used when this order is through an agency booking.



## Attributes
    
    
        
    
        
    

|   Name   | Type | Required | Description |
|----------|------|----------|-------------|
|  AGENCY  | Any  |   True   |     ...     |
| MERCHANT | Any  |   True   |     ...     |










# Inheritance
object > Enum > InventorySource