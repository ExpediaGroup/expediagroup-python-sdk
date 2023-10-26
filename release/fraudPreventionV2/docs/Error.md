[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Error](Error.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Error`

```python
Error(
    code: Code,
    message: str,
)
```

pydantic model Error: The object used to describe an error, containing
both human-readable and machine-readable information.

## Attributes

| Name    | Type            | Required | Description                                                                                                    |
| ------- | --------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| code    | [Code](Code.md) | True     | Snake cased all caps error code interpreted from the HTTP status code that can programmatically be acted upon. |
| message | str             | True     | A human-readable explanation of the error, specific to this error occurrence.                                  |

# Inheritance

object > BaseModel > Error
