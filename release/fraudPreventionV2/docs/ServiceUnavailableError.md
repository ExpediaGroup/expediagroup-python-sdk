[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [ServiceUnavailableError](ServiceUnavailableError.md)

# class `expediagroup.sdk.fraudpreventionv2.model.ServiceUnavailableError`

```
ServiceUnavailableError(
)
```

pydantic model ServiceUnavailableError: Indicates that the API is either
down for maintenance or overloaded and cannot fulfill the request at the
current time. This is a temporary error and retrying the same request
after a certain delay could eventually result in success. There will be
a Retry-After HTTP header in API response specifying how long to wait to
retry the request. If there is no Retry-After HTTP header then retry can
happen immediately. If the error persists after retrying with delay,
please reach out to <support team>."

# Inheritance

object > [AccountTakeoverError](AccountTakeoverError.md) >
ServiceUnavailableError
