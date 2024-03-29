[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Telephone](Telephone.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Telephone`

```python
Telephone(
    type: Optional[TelephoneType],
    platform_type: Optional[TelephonePlatformType],
    country_access_code: constr(max_length=3, pattern=r"^[0-9]{1,3}$"),
    area_code: constr(max_length=20, pattern=r"^[0-9]{1,20}$"),
    phone_number: constr(max_length=50, pattern=r"^[0-9]{1,50}$"),
    extension_number: Optional[constr(max_length=20, pattern=r"^[0-9]{1,20}$")],
    preference_rank: Optional[float],
    last_verified_date_time: Optional[datetime],
    verified_flag: Optional[bool],
)
```

pydantic model Telephone: Group of attributes intended to hold
information about phone number associated with the transaction. A user
can have one to many phone numbers (home, work, mobile, etc.).

## Attributes

| Name      | Type                                          | Required | Description                                                                                                                                  |
| --------- | --------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| area_code | constr(max_length=20, pattern=r”[^1]{1,20}$") | True     | A number prefixed to an individual telephone number: used in making long-distance calls. Does not include symbols, spaces, or leading zeros. |

```
                | country_access_code     | constr(max_length=3, pattern=r"^[0-9]{1,3}$“)                                                                                                                                                                                                                           | True     | Numeric digit between 1 to 3 characters used to represent the country code for international dialing. Does not include symbols, spaces, or leading zeros.                   |
```

| extension_number | Optional\[constr(max_length=20, pattern=r”[^2]{1,20}$")\]   | False    | The number used to reach an individual once a phone connection is established. Does not include symbols, spaces, or leading zeros.                                                          |\
| last_verified_date_time | Optional\[datetime\]                                          | False    | Local date and time user validated possession of their phone number via a text or voice multi factor authentication challenge, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`. |\
| phone_number            | constr(max_length=50, pattern=r"^\[0-9\]{1,50}$“)                                                                                                                                                                                                                         | True     | A number that is dialed on a telephone, without the country or area codes, to reach a particular person, business, etc. Does not include symbols, spaces, or leading zeros. |
| platform_type    | Optional\[[TelephonePlatformType](TelephonePlatformType.md)\]                                                                                                                                                                                                                                      | False    | …                                                                                                                                                                           |
| preference_rank  | Optional\[float\]                                                                                                                                                                                                                                                                                  | False    | Ranking of order of user preference for contact via text (if type is Mobile) or voice. `0` means no preference. `1` is the primary phone, `2` is the secondary phone, etc.  |
| type             | Optional\[[TelephoneType](TelephoneType.md)\]                                                                                                                                                                                                                                                      | False    | …                                                                                                                                                                           |
| verified_flag    | Optional\[bool\]                                                                                                                                                                                                                                                                                   | False    | Flag indicating whether user passed validation of possession of their phone number via a text or voice multi factor authentication challenge.                               |

# Inheritance

object > [PydanticModel](PydanticModel.md) > Telephone

[^1]: 0-9

[^2]: 0-9
