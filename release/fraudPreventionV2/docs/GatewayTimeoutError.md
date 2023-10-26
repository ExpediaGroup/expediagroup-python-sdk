[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [GatewayTimeoutError](GatewayTimeoutError.md)

# class `expediagroup.sdk.fraudpreventionv2.model.GatewayTimeoutError`

```python
GatewayTimeoutError()
```

pydantic model GatewayTimeoutError: Indicates that the API gateway has
issues completing the request on time. Request can be retried if it is
idempotent, If the issue persists, please reach out to support. For
non-idempotent requests, please reach out to <support team> to know the
status of your request before attempting retries.

# Inheritance

object > [AccountTakeoverError](AccountTakeoverError.md) >
GatewayTimeoutError
