[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [AccountUpdateRequestGeneric](AccountUpdateRequestGeneric.md)
# class `expediagroup.sdk.fraudpreventionv2.model.AccountUpdateRequestGeneric`
```
AccountUpdateRequestGeneric(
    type: Type1,
    risk_id: constr(max_length=200),
)
```

pydantic model AccountUpdateRequest: The `type` field value is used as a discriminator, with the following mapping:
* `MULTI_FACTOR_AUTHENTICATION_UPDATE`: `MultiFactorAuthenticationUpdate`
* `REMEDIATION_UPDATE`: `RemediationUpdate`



## Attributes
    
    
        
    
        
    

|   Name  |          Type          | Required |                                         Description                                          |
|---------|------------------------|----------|----------------------------------------------------------------------------------------------|
| risk_id | constr(max_length=200) |   True   | The `risk_id` provided by Expedia's Fraud Prevention Service in the `AccountScreenResponse`. |
|   type  |   [Type1](Type1.md)    |   True   |           The categorized type of account update event from the Partner's system.            |










# Inheritance
object > BaseModel > AccountUpdateRequestGeneric