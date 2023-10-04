[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [Points](Points.md)
# class `expediagroup.sdk.fraudpreventionv2.model.Points`
```
Points(
    account_id: constr(max_length=200),
    method: Literal["POINTS"],
)
```

pydantic model Points



## Attributes
    
    
        
    
        
    

|    Name    |          Type          | Required |    Description     |
|------------|------------------------|----------|--------------------|
| account_id | constr(max_length=200) |   True   | Points account id. |
|   method   |   Literal["POINTS"]    |   True   |        ...         |










# Inheritance
object > [PaymentGeneric](PaymentGeneric.md) > Points