[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [AccountTakeoverDeviceDetails](AccountTakeoverDeviceDetails.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AccountTakeoverDeviceDetails`

```python
AccountTakeoverDeviceDetails(
    source: Optional[constr(max_length=50)],
    device_box: str,
    ip_address: constr(
        pattern=r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$"
    ),
    user_agent: str,
    type: Optional[Type4],
)
```

pydantic model AccountTakeoverDeviceDetails: Information specific to the
Partner’s device through which a transaction was made.

## Attributes

| Name       | Type                                                                                                                                                                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| device_box | str                                                                                                                                                                                             | True     | Device related information retrieved from TrustWidget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ip_address | constr(<br/> pattern=r”^(?:(?:25\[0-5\]\|2\[0-4\]\[0-9\]\|\[01\]?\[0-9\]\[0-9\]?).){3}(?:25\[0-5\]\|2\[0-4\]\[0-9\]\|\[01\]?\[0-9\]\[0-9\]?)$\|^(?:\[A-F0-9\]{1,4}:){7}\[A-F0-9\]{1,4}$“<br/> ) | True     | IP address of the device used for this event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| source     | Optional\[constr(max_length=50)\]                                                                                                                                                               | False    | Source of the device_box. Default value is `TrustWidget`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| type       | Optional\[[Type4](Type4.md)\]                                                                                                                                                                   | False    | The categorized type of device used by a user. Possible values are:<br/>- `WEBSITE` - Applicable if the user initiated this event from a web browser on a desktop computer.<br/>- `PHONE_WEB` - Applicable if the user initiated this event from a web browser on a phone.<br/>- `TABLET_WEB` - Applicable if the user initiated this event from a web browser on a tablet.<br/>- `PHONE_APP` - Applicable if the user initiated this event from an app on a phone.<br/>- `TABLET_APP` - Applicable if the user initiated this event from an app on a tablet. |
| user_agent | str                                                                                                                                                                                             | True     | The application type, operating system, software vendor, or software version of the originating request.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

# Inheritance

object > [PydanticModel](PydanticModel.md) >
AccountTakeoverDeviceDetails
