[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [MultiFactorAuthenticationUpdate](MultiFactorAuthenticationUpdate.md)
# class `expediagroup.sdk.fraudpreventionv2.model.MultiFactorAuthenticationUpdate`
```
MultiFactorAuthenticationUpdate(
    multi_factor_authentication_attempts: list[MultiFactorAuthenticationAttempt],
    type: Literal["MULTI_FACTOR_AUTHENTICATION_UPDATE"],
)
```

pydantic model MultiFactorAuthenticationUpdate: Information specific to a user's response to a Multi-Factor Authentication initiated by the Partner's system as a result of a fraud recommendation.



## Attributes
    
    
        
    
        
    

|                 Name                 |                                      Type                                     | Required |                               Description                               |
|--------------------------------------|-------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------|
| multi_factor_authentication_attempts | list[[MultiFactorAuthenticationAttempt](MultiFactorAuthenticationAttempt.md)] |   True   |                                   ...                                   |
|                 type                 |                 Literal["MULTI_FACTOR_AUTHENTICATION_UPDATE"]                 |   True   | The categorized type of account update event from the Partner's system. |










# Inheritance
object > [AccountUpdateRequestGeneric](AccountUpdateRequestGeneric.md) > MultiFactorAuthenticationUpdate