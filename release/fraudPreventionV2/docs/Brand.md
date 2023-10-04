[index](index.md) / [expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md) / [Brand](Brand.md)
# class `expediagroup.sdk.fraudpreventionv2.model.Brand`
```
Brand(
)
```

pydantic model Brand: The `brand` field value is the payment brand used for payment on this transaction.
For credit card payment method ensure attributes mentioned in dictionary below are set to corresponding values only.
Ensure to comply with the naming standards provided in below dictionary. For example, some Payment processors use “Japan Credit Bureau” but “JCB” should be used when calling Fraud API.
Incorrect `brand` - `card_type` combination will result in data quality issues and result in degraded risk recommendation.
'brand' is an enum value with the following mapping with CreditCard 'card_type' attribute:
*       brand                 :      card_type
* -------------------------------------------------------
* `AMERICAN_EXPRESS`          : `AMERICAN_EXPRESS`
* `DINERS_CLUB_INTERNATIONAL` : `DINERS_CLUB`
* `BC_CARD`                   : `DINERS_CLUB`
* `DISCOVER`                  : `DISCOVER`
* `BC_CARD`                   : `DISCOVER`
* `DINERS_CLUB_INTERNATIONAL` : `DISCOVER`
* `JCB`                       : `DISCOVER`
* `JCB`                       : `JCB`
* `MASTER_CARD`               : `MASTER_CARD`
* `MAESTRO`                   : `MASTER_CARD`
* `POSTEPAY_MASTERCARD`       : `MASTER_CARD`
* `SOLO`                      : `SOLO`
* `SWITCH`                    : `SWITCH`
* `MAESTRO`                   : `MAESTRO`
* `CHINA_UNION_PAY`           : `CHINA_UNION_PAY`
* `VISA`                      : `VISA`
* `VISA_DELTA`                : `VISA`
* `VISA_ELECTRON`             : `VISA`
* `CARTA_SI`                  : `VISA`
* `CARTE_BLEUE`               : `VISA`
* `VISA_DANKORT`              : `VISA`
* `POSTEPAY_VISA_ELECTRON`    : `VISA`
* `PAYPAL`                    :

'brand' with 'Points' payment_type is an enum value with following:
* `EXPEDIA_REWARDS`
* `AMEX_POINTS`
* `BANK_OF_AMERICA_REWARDS`
* `DISCOVER_POINTS`
* `MASTER_CARD_POINTS`
* `CITI_THANK_YOU_POINTS`
* `MERRILL_LYNCH_REWARDS`
* `WELLS_FARGO_POINTS`
* `DELTA_SKY_MILES`
* `UNITED_POINTS`
* `DISCOVER_MILES`
* `ALASKA_MILES`
* `RBC_REWARDS`
* `BILT_REWARDS`
* `ORBUCKS`
* `CHEAP_CASH`
* `BONUS_PLUS`
* `ULTIMATE_REWARDS`

'brand' with 'GiftCard' payment_type is an enum value with following:
* `GIFT_CARD`

'brand' with 'InternetBankPayment' payment_type is an enum value with following:
* `IBP`
* `LOCAL_DEBIT_CARD`
* `SOFORT`
* `YANDEX`
* `WEB_MONEY`
* `QIWI`
* `BITCOIN`

'brand' with 'DirectDebit' payment_type is an enum value with following:
* `ELV`
* `INTER_COMPANY`



## Attributes
    
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    

|            Name           | Type | Required | Description |
|---------------------------|------|----------|-------------|
|        ALASKA_MILES       | Any  |   True   |     ...     |
|      AMERICAN_EXPRESS     | Any  |   True   |     ...     |
|        AMEX_POINTS        | Any  |   True   |     ...     |
|  BANK_OF_AMERICA_REWARDS  | Any  |   True   |     ...     |
|          BC_CARD          | Any  |   True   |     ...     |
|        BILT_REWARDS       | Any  |   True   |     ...     |
|          BITCOIN          | Any  |   True   |     ...     |
|         BONUS_PLUS        | Any  |   True   |     ...     |
|          CARTA_SI         | Any  |   True   |     ...     |
|        CARTE_BLEUE        | Any  |   True   |     ...     |
|         CHEAP_CASH        | Any  |   True   |     ...     |
|      CHINA_UNION_PAY      | Any  |   True   |     ...     |
|   CITI_THANK_YOU_POINTS   | Any  |   True   |     ...     |
|      DELTA_SKY_MILES      | Any  |   True   |     ...     |
| DINERS_CLUB_INTERNATIONAL | Any  |   True   |     ...     |
|          DISCOVER         | Any  |   True   |     ...     |
|       DISCOVER_MILES      | Any  |   True   |     ...     |
|      DISCOVER_POINTS      | Any  |   True   |     ...     |
|            ELV            | Any  |   True   |     ...     |
|      EXPEDIA_REWARDS      | Any  |   True   |     ...     |
|         GIFT_CARD         | Any  |   True   |     ...     |
|            IBP            | Any  |   True   |     ...     |
|       INTER_COMPANY       | Any  |   True   |     ...     |
|            JCB            | Any  |   True   |     ...     |
|      LOCAL_DEBIT_CARD     | Any  |   True   |     ...     |
|          MAESTRO          | Any  |   True   |     ...     |
|        MASTER_CARD        | Any  |   True   |     ...     |
|     MASTER_CARD_POINTS    | Any  |   True   |     ...     |
|   MERRILL_LYNCH_REWARDS   | Any  |   True   |     ...     |
|          ORBUCKS          | Any  |   True   |     ...     |
|           PAYPAL          | Any  |   True   |     ...     |
|    POSTEPAY_MASTERCARD    | Any  |   True   |     ...     |
|   POSTEPAY_VISA_ELECTRON  | Any  |   True   |     ...     |
|            QIWI           | Any  |   True   |     ...     |
|        RBC_REWARDS        | Any  |   True   |     ...     |
|           SOFORT          | Any  |   True   |     ...     |
|            SOLO           | Any  |   True   |     ...     |
|           SWITCH          | Any  |   True   |     ...     |
|      ULTIMATE_REWARDS     | Any  |   True   |     ...     |
|       UNITED_POINTS       | Any  |   True   |     ...     |
|            VISA           | Any  |   True   |     ...     |
|        VISA_DANKORT       | Any  |   True   |     ...     |
|         VISA_DELTA        | Any  |   True   |     ...     |
|       VISA_ELECTRON       | Any  |   True   |     ...     |
|         WEB_MONEY         | Any  |   True   |     ...     |
|     WELLS_FARGO_POINTS    | Any  |   True   |     ...     |
|           YANDEX          | Any  |   True   |     ...     |










# Inheritance
object > Enum > Brand