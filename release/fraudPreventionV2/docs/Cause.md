[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Cause](Cause.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Cause`

```python
Cause(
    code: Optional[Code1],
    field: Optional[str],
    message: Optional[str],
)
```

pydantic model Cause

## Attributes

| Name    | Type                          | Required | Description                                                                           |
| ------- | ----------------------------- | -------- | ------------------------------------------------------------------------------------- |
| code    | Optional\[[Code1](Code1.md)\] | False    | …                                                                                     |
| field   | Optional\[str\]               | False    | A JSON Path expression indicating which field, in the request body, caused the error. |
| message | Optional\[str\]               | False    | …                                                                                     |

# Inheritance

object > BaseModel > Cause
