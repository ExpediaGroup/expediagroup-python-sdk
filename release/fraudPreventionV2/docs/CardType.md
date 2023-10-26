[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [CardType](CardType.md)

# class `expediagroup.sdk.fraudpreventionv2.model.CardType`

```python
CardType()
```

pydantic model CardType: The ‘card_type’ field value is an enum value
which is associated with the payment method of the specific payment
instrument. For credit card payment method ensure attributes mentioned
in dictionary below are set to corresponding values only. Ensure to
comply with the naming standards provided in below dictionary. For
example, some Payment processors use “Japan Credit Bureau” but “JCB”
should be used when calling Fraud API. Incorrect `card_type` - `brand`
combination will result in data quality issues and result in degraded
risk recommendation. ‘card_type’ is an enum value with the following
mapping with Payment `brand` attribute:

- card_type            :          brand

-

______________________________________________________________________

- `AMERICAN_EXPRESS` : `AMERICAN_EXPRESS`

- `DINERS_CLUB` : `DINERS_CLUB_INTERNATIONAL`

- `DINERS_CLUB` : `BC_CARD`

- `DISCOVER` : `DISCOVER`

- `DISCOVER` : `BC_CARD`

- `DISCOVER` : `DINERS_CLUB_INTERNATIONAL`

- `DISCOVER` : `JCB`

- `JCB` : `JCB`

- `MASTER_CARD` : `MASTER_CARD`

- `MASTER_CARD` : `MAESTRO`

- `MASTER_CARD` : `POSTEPAY_MASTERCARD`

- `SOLO` : `SOLO`

- `SWITCH` : `SWITCH`

- `MAESTRO` : `MAESTRO`

- `CHINA_UNION_PAY` : `CHINA_UNION_PAY`

- `UATP` : `UATP`

- `UATP` : `UATP_SUPPLY`

- `UATP` : `AIR_PLUS`

- `UATP` : `UA_PASS_PLUS`

- `VISA` : `VISA`

- `VISA` : `VISA_DELTA`

- `VISA` : `VISA_ELECTRON`

- `VISA` : `CARTA_SI`

- `VISA` : `CARTE_BLEUE`

- `VISA` : `VISA_DANKORT`

- `VISA` : `POSTEPAY_VISA_ELECTRON`

## Attributes

| Name             | Type | Required | Description |
| ---------------- | ---- | -------- | ----------- |
| AMERICAN_EXPRESS | Any  | True     | …           |
| CHINA_UNION_PAY  | Any  | True     | …           |
| DINERS_CLUB      | Any  | True     | …           |
| DISCOVER         | Any  | True     | …           |
| JCB              | Any  | True     | …           |
| MAESTRO          | Any  | True     | …           |
| MASTER_CARD      | Any  | True     | …           |
| SOLO             | Any  | True     | …           |
| SWITCH           | Any  | True     | …           |
| UATP             | Any  | True     | …           |
| VISA             | Any  | True     | …           |

# Inheritance

object > Enum > CardType
