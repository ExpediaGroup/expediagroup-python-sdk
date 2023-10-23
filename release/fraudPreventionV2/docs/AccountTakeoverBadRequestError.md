[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [AccountTakeoverBadRequestError](AccountTakeoverBadRequestError.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AccountTakeoverBadRequestError`

```
AccountTakeoverBadRequestError(
    causes: Optional[list[Cause1]],
)
```

pydantic model AccountTakeoverBadRequestError: Indicates that a bad
request occurred. Typically it is an invalid parameter.

## Attributes

| Name   | Type                                    | Required | Description |
| ------ | --------------------------------------- | -------- | ----------- |
| causes | Optional\[list\[[Cause1](Cause1.md)\]\] | False    | …           |

# Inheritance

object > [AccountTakeoverError](AccountTakeoverError.md) >
AccountTakeoverBadRequestError
