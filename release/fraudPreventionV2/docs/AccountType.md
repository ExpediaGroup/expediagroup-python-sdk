[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [AccountType](AccountType.md)
# class `expediagroup.sdk.fraudpreventionv2.model.AccountType`
```
AccountType(
)
```

pydantic model AccountType: Identifies if the customer account is known to the client. Possible values are:

-`GUEST` - Applicable if the partner maintains record to distinguish whether the transaction was booked via a guest account.

-`STANDARD` - Default account type.



## Attributes
    
    
        
    
        
    

|   Name   | Type | Required | Description |
|----------|------|----------|-------------|
|  GUEST   | Any  |   True   |     ...     |
| STANDARD | Any  |   True   |     ...     |










# Inheritance
object > Enum > AccountType