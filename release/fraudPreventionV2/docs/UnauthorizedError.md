[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [UnauthorizedError](UnauthorizedError.md)

# class `expediagroup.sdk.fraudpreventionv2.model.UnauthorizedError`

```
UnauthorizedError(
)
```

pydantic model UnauthorizedError: Indicates that the token sent in the
‘Authorization’ header is either invalid or missing. Please check the
value in the token field along with the token expiration time before
retrying.

# Inheritance

object > [Error](Error.md) > UnauthorizedError
