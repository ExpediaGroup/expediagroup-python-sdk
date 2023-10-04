[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [OrderPurchaseScreenResponse](OrderPurchaseScreenResponse.md)
# class `expediagroup.sdk.fraudpreventionv2.model.OrderPurchaseScreenResponse`
```
OrderPurchaseScreenResponse(
    risk_id: Optional[constr(max_length=200)],
    decision: Optional[FraudDecision],
)
```

pydantic model OrderPurchaseScreenResponse



## Attributes
    
    
        
    
        
    

|   Name   |                     Type                    | Required |                                     Description                                      |
|----------|---------------------------------------------|----------|--------------------------------------------------------------------------------------|
| decision | Optional[[FraudDecision](FraudDecision.md)] |  False   |                                         ...                                          |
| risk_id  |       Optional[constr(max_length=200)]      |  False   | Unique identifier assigned to the transaction by Expedia's Fraud Prevention Service. |










# Inheritance
object > BaseModel > OrderPurchaseScreenResponse