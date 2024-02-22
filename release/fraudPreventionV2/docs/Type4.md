[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Type4](Type4.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Type4`

```python
Type4()
```

pydantic model Type4: The categorized type of device used by a user.
Possible values are:

- `WEBSITE` - Applicable if the user initiated this event from a web
  browser on a desktop computer.
- `PHONE_WEB` - Applicable if the user initiated this event from a web
  browser on a phone.
- `TABLET_WEB` - Applicable if the user initiated this event from a web
  browser on a tablet.
- `PHONE_APP` - Applicable if the user initiated this event from an app
  on a phone.
- `TABLET_APP` - Applicable if the user initiated this event from an app
  on a tablet.

## Attributes

| Name       | Type | Required | Description |
| ---------- | ---- | -------- | ----------- |
| PHONE_APP  | Any  | True     | …           |
| PHONE_WEB  | Any  | True     | …           |
| TABLET_APP | Any  | True     | …           |
| TABLET_WEB | Any  | True     | …           |
| WEBSITE    | Any  | True     | …           |

# Inheritance

object > Enum > Type4
