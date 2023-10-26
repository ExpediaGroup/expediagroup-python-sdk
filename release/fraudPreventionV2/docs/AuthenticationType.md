[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [AuthenticationType](AuthenticationType.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AuthenticationType`

```python
AuthenticationType()
```

pydantic model AuthenticationType: The type of login authentication
method used by a user. For `authentication_type` ensure attributes
mentioned in dictionary below are set to corresponding values only.
`authentication_type` is an enum value with the following mapping with
`authentication_sub_type` attribute:

- authentication_type       :     authentication_sub_type

-

______________________________________________________________________

- `CREDENTIALS` : `EMAIL`

- `CREDENTIALS` :

- `PASSWORD_RESET` : `EMAIL`

- `SINGLE_SIGN_ON` : `EMAIL`

- `MULTI_FACTOR_AUTHENTICATION` : `EMAIL`

- `MULTI_FACTOR_AUTHENTICATION` : `PHONE`

- `SOCIAL` : `GOOGLE`

- `SOCIAL` : `FACEBOOK`

- `SOCIAL` : `APPLE`

## Attributes

| Name                        | Type | Required | Description |
| --------------------------- | ---- | -------- | ----------- |
| CREDENTIALS                 | Any  | True     | …           |
| MULTI_FACTOR_AUTHENTICATION | Any  | True     | …           |
| PASSWORD_RESET              | Any  | True     | …           |
| SINGLE_SIGN_ON              | Any  | True     | …           |
| SOCIAL                      | Any  | True     | …           |

# Inheritance

object > Enum > AuthenticationType
