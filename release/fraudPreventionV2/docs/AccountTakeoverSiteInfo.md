[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [AccountTakeoverSiteInfo](AccountTakeoverSiteInfo.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AccountTakeoverSiteInfo`

```
AccountTakeoverSiteInfo(
    locale: Optional[constr(regex=r"^([a-z]{2}-[A-Z]{2})$")],
    name: Optional[constr(max_length=200)],
    brand_name: constr(max_length=200),
    placement_name: Optional[PlacementName],
)
```

pydantic model AccountTakeoverSiteInfo: Information specific to the
Partner’s website through which a transaction was made.

## Attributes

| Name           | Type                                                   | Required | Description                                                                                                                                                                                                                                                                               |
| -------------- | ------------------------------------------------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| brand_name     | constr(max_length=200)                                 | True     | The trademark brand name that is displayed to a user on the website.                                                                                                                                                                                                                      |
| locale         | Optional\[constr(regex=r“^(\[a-z\]{2}-\[A-Z\]{2})$”)\] | False    | The locale of the website a user is accessing, which is separate from the user configured browser locale, in ISO 639-2 language code format and in ISO 3166-1 country code format.                                                                                                        |
| name           | Optional\[constr(max_length=200)\]                     | False    | Name of the website from which the event is generated.                                                                                                                                                                                                                                    |
| placement_name | Optional\[[PlacementName](PlacementName.md)\]          | False    | The categorized name of the page where a user initiated event is being evaluated.<br/>- `LOGIN` - Applicable if the user initiated this account event from a login web page.<br/>- `PASSWORD_RESET` - Applicable if the user initiated this account event from a password reset web page. |

# Inheritance

object > BaseModel > AccountTakeoverSiteInfo
