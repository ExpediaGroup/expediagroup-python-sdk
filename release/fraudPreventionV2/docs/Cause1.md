[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [Cause1](Cause1.md)
# class `expediagroup.sdk.fraudpreventionv2.model.Cause1`
```
Cause1(
    code: Optional[Code3],
    field: Optional[str],
    message: Optional[str],
)
```

pydantic model Cause1



## Attributes
    
    
        
    
        
    
        
    

|   Name  |             Type            | Required |                                      Description                                      |
|---------|-----------------------------|----------|---------------------------------------------------------------------------------------|
|   code  | Optional[[Code3](Code3.md)] |  False   |                                          ...                                          |
|  field  |        Optional[str]        |  False   | A JSON Path expression indicating which field, in the request body, caused the error. |
| message |        Optional[str]        |  False   |                                          ...                                          |










# Inheritance
object > BaseModel > Cause1