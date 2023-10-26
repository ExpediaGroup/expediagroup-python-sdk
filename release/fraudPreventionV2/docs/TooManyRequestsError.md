[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [TooManyRequestsError](TooManyRequestsError.md)

# class `expediagroup.sdk.fraudpreventionv2.model.TooManyRequestsError`

```python
TooManyRequestsError()
```

pydantic model TooManyRequestsError: Indicates that the API cannot
fulfill the request because server resources have been exhausted.
Perhaps the client has sent too many requests in a given amount of time
or has reached some specific quota. Please check the rate limits for the
product and adjust as necessary before retries. If you believe the rate
limit was incorrect or if you need a different rate limit, please reach
out to the <support team> regarding the next steps.

# Inheritance

object > [AccountTakeoverError](AccountTakeoverError.md) >
TooManyRequestsError
