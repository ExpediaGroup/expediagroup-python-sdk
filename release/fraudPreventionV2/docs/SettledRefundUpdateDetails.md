[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [SettledRefundUpdateDetails](SettledRefundUpdateDetails.md)
# class `expediagroup.sdk.fraudpreventionv2.model.SettledRefundUpdateDetails`
```
SettledRefundUpdateDetails(
    refund_settlement_date_time: datetime,
    refund_deposit_date_time: datetime,
    acquirer_reference_number: constr(max_length=200),
    settlement_id: constr(max_length=200),
    refund_settled_amount: Amount,
)
```

pydantic model SettledRefundUpdateDetails: Data that describes settled refund that should be updated.



## Attributes
    
    
        
    
        
    
        
    
        
    
        
    

|             Name            |          Type          | Required |                                                                                                                                                Description                                                                                                                                                |
|-----------------------------|------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  acquirer_reference_number  | constr(max_length=200) |   True   | A unique number that tags a credit or debit card transaction when it goes from the merchant's bank through to the cardholder's bank.<br/>Typically, merchants can get this number from their payment processors.<br/>This number is used when dealing with disputes/chargebacks on original transactions. |
|   refund_deposit_date_time  |        datetime        |   True   |                                                                                                                Date and time when the refund was deposited to the original form of payment.                                                                                                               |
|    refund_settled_amount    |  [Amount](Amount.md)   |   True   |                                                                                                                                                    ...                                                                                                                                                    |
| refund_settlement_date_time |        datetime        |   True   |                                                                      Date and time when the 3rd party payment processor confirmed that a previously submitted payment refund has settled at the participating financial institutions.                                                                     |
|        settlement_id        | constr(max_length=200) |   True   |                                                                             Unique settlement identifier specific to the payment processor for the settlement transaction generated for a previously submitted payment refund.                                                                            |










# Inheritance
object > BaseModel > SettledRefundUpdateDetails