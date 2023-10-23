[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [PlacementName](PlacementName.md)

# class `expediagroup.sdk.fraudpreventionv2.model.PlacementName`

```
PlacementName(
)
```

pydantic model PlacementName: The categorized name of the page where a
user initiated event is being evaluated.

- `LOGIN` - Applicable if the user initiated this account event from a
  login web page.
- `PASSWORD_RESET` - Applicable if the user initiated this account
  event from a password reset web page.

## Attributes

| Name           | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| LOGIN          | Any  | True     | …           |
| PASSWORD_RESET | Any  | True     | …           |

# Inheritance

object > Enum > PlacementName
