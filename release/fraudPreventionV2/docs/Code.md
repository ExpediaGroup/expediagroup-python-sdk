[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Code](Code.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Code`

```python
Code()
```

pydantic model Code: Snake cased all caps error code interpreted from
the HTTP status code that can programmatically be acted upon.

## Attributes

| Name                                    | Type | Required | Description |
| --------------------------------------- | ---- | -------- | ----------- |
| BAD_GATEWAY                             | Any  | True     | …           |
| BAD_REQUEST                             | Any  | True     | …           |
| FORBIDDEN                               | Any  | True     | …           |
| GATEWAY_TIMEOUT                         | Any  | True     | …           |
| INTERNAL_SERVER_ERROR                   | Any  | True     | …           |
| NOT_FOUND                               | Any  | True     | …           |
| ORDER_PURCHASE_UPDATE_NOT_FOUND         | Any  | True     | …           |
| RETRYABLE_ORDER_PURCHASE_SCREEN_FAILURE | Any  | True     | …           |
| RETRYABLE_ORDER_PURCHASE_UPDATE_FAILURE | Any  | True     | …           |
| TOO_MANY_REQUESTS                       | Any  | True     | …           |
| UNAUTHORIZED                            | Any  | True     | …           |

# Inheritance

object > Enum > Code
