[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [BadRequestError](BadRequestError.md)

# class `expediagroup.sdk.fraudpreventionv2.model.BadRequestError`

```python
BadRequestError(
    causes: Optional[list[Cause]],
)
```

pydantic model BadRequestError: Indicates that a bad request occurred.
Typically it is an invalid parameter.

## Attributes

| Name   | Type                                  | Required | Description |
| ------ | ------------------------------------- | -------- | ----------- |
| causes | Optional\[list\[[Cause](Cause.md)\]\] | False    | …           |

# Inheritance

object > [Error](Error.md) > BadRequestError
