[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [RemediationUpdate](RemediationUpdate.md)
# class `expediagroup.sdk.fraudpreventionv2.model.RemediationUpdate`
```
RemediationUpdate(
    remediation_update_actions: list[RemediationUpdateAction],
    type: Literal["REMEDIATION_UPDATE"],
)
```

pydantic model RemediationUpdate: Information specific to remediation actions initiated by the Partner's system to a user as a result of a fraud recommendation.



## Attributes
    
    
        
    
        
    

|            Name            |                             Type                            | Required |                               Description                               |
|----------------------------|-------------------------------------------------------------|----------|-------------------------------------------------------------------------|
| remediation_update_actions | list[[RemediationUpdateAction](RemediationUpdateAction.md)] |   True   |                                   ...                                   |
|            type            |                Literal["REMEDIATION_UPDATE"]                |   True   | The categorized type of account update event from the Partner's system. |










# Inheritance
object > [AccountUpdateRequestGeneric](AccountUpdateRequestGeneric.md) > RemediationUpdate