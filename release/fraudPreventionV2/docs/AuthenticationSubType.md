[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [AuthenticationSubType](AuthenticationSubType.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AuthenticationSubType`

```python
AuthenticationSubType()
```

pydantic model AuthenticationSubType: The sub type of login
authentication method used by a user. For `authentication_sub_type`
ensure attributes mentioned in dictionary below are set to corresponding
values only. `authentication_sub_type` is an enum value with the
following mapping with `authentication_type` attribute:

- authentication_sub_type   :     authentication_type

-

______________________________________________________________________

- `EMAIL` : `CREDENTIALS`

- `EMAIL` : `PASSWORD_RESET`

- `EMAIL` : `SINGLE_SIGN_ON`

- `EMAIL` : `MULTI_FACTOR_AUTHENTICATION`

- `PHONE` : `MULTI_FACTOR_AUTHENTICATION`

- `GOOGLE` : `SOCIAL`

- `FACEBOOK` : `SOCIAL`

- `APPLE` : `SOCIAL`

- ```
                                : `CREDENTIALS`
  ```

## Attributes

| Name     | Type | Required | Description |
| -------- | ---- | -------- | ----------- |
| APPLE    | Any  | True     | …           |
| EMAIL    | Any  | True     | …           |
| FACEBOOK | Any  | True     | …           |
| GOOGLE   | Any  | True     | …           |
| PHONE    | Any  | True     | …           |

# Inheritance

object > Enum > AuthenticationSubType
