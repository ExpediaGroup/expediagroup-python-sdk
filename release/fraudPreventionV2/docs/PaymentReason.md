[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [PaymentReason](PaymentReason.md)
# class `expediagroup.sdk.fraudpreventionv2.model.PaymentReason`
```
PaymentReason(
)
```

pydantic model PaymentReason: The reason of payment. Possible values:
- `FULL` - If the amount is paid i full for the order
- `DEPOSIT` - The initial payment. Amount to be paid up front.
- `SCHEDULED` - The amount to be payment based on a schedule for the remaining portion of the booking amount.
- `SUBSEQUENT` - An additional amount paid that was not originally scheduled.
- `DEFERRED`



## Attributes
    
    
        
    
        
    
        
    
        
    
        
    

|    Name    | Type | Required | Description |
|------------|------|----------|-------------|
|  DEFERRED  | Any  |   True   |     ...     |
|  DEPOSIT   | Any  |   True   |     ...     |
|    FULL    | Any  |   True   |     ...     |
| SCHEDULED  | Any  |   True   |     ...     |
| SUBSEQUENT | Any  |   True   |     ...     |










# Inheritance
object > Enum > PaymentReason