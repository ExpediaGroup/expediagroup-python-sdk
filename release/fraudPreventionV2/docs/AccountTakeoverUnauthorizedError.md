[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/
[AccountTakeoverUnauthorizedError](AccountTakeoverUnauthorizedError.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AccountTakeoverUnauthorizedError`

```python
AccountTakeoverUnauthorizedError()
```

pydantic model AccountTakeoverUnauthorizedError: Indicates that the
token sent in the ‘Authorization’ header is either invalid or missing.
Please check the value in the token field along with the token
expiration time before retrying.

# Inheritance

object > [AccountTakeoverError](AccountTakeoverError.md) >
AccountTakeoverUnauthorizedError
