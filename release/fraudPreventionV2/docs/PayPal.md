[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [PayPal](PayPal.md)
# class `expediagroup.sdk.fraudpreventionv2.model.PayPal`
```
PayPal(
    payer_id: constr(max_length=200),
    transaction_id: constr(max_length=200),
    merchant_order_code: Optional[constr(max_length=200)],
    method: Literal["PAYPAL"],
)
```

pydantic model PayPal



## Attributes
    
    
        
    
        
    
        
    
        
    

|         Name        |               Type               | Required |                                                                  Description                                                                  |
|---------------------|----------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| merchant_order_code | Optional[constr(max_length=200)] |  False   | Reference code passed to acquiring bank at the time of payment. This code is the key ID that ties back to payments data at the payment level. |
|        method       |        Literal["PAYPAL"]         |   True   |                                                                      ...                                                                      |
|       payer_id      |      constr(max_length=200)      |   True   |                                             Unique PayPal Customer Account identification number.                                             |
|    transaction_id   |      constr(max_length=200)      |   True   |                                          Unique transaction number to identify Auth calls at PayPal.                                          |










# Inheritance
object > [PaymentGeneric](PaymentGeneric.md) > PayPal