[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [PaymentThreeDSCriteria](PaymentThreeDSCriteria.md)
# class `expediagroup.sdk.fraudpreventionv2.model.PaymentThreeDSCriteria`
```
PaymentThreeDSCriteria(
    probable_flag: Optional[bool],
    transaction_model: Optional[constr(max_length=200)],
)
```

pydantic model PaymentThreeDSCriteria: Payment ThreeDS criteria attributes.



## Attributes
    
    
        
    
        
    

|        Name       |               Type               | Required |                                         Description                                          |
|-------------------|----------------------------------|----------|----------------------------------------------------------------------------------------------|
|   probable_flag   |          Optional[bool]          |  False   | This is a flag passed that indicates that this transaction could potentially go through 3DS. |
| transaction_model | Optional[constr(max_length=200)] |  False   |                          Model used to process payment transaction.                          |










# Inheritance
object > BaseModel > PaymentThreeDSCriteria