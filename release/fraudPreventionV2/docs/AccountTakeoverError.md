[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [AccountTakeoverError](AccountTakeoverError.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AccountTakeoverError`

```
AccountTakeoverError(
    code: Code2,
    message: str,
)
```

pydantic model AccountTakeoverError: The object used to describe an
error, containing both human-readable and machine-readable information.

## Attributes

| Name    | Type              | Required | Description                                                                                                    |
| ------- | ----------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| code    | [Code2](Code2.md) | True     | Snake cased all caps error code interpreted from the HTTP status code that can programmatically be acted upon. |
| message | str               | True     | A human-readable explanation of the error, specific to this error occurrence.                                  |

# Inheritance

object > BaseModel > AccountTakeoverError
