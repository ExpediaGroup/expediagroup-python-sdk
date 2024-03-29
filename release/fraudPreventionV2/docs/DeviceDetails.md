[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [DeviceDetails](DeviceDetails.md)

# class `expediagroup.sdk.fraudpreventionv2.model.DeviceDetails`

```python
DeviceDetails(
    source: Optional[constr(max_length=50)],
    device_box: Optional[str],
    ip_address: constr(
        pattern=r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$"
    ),
)
```

pydantic model DeviceDetails

## Attributes

| Name       | Type                                                                                                                                                                                            | Required | Description                                               |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------- |
| device_box | Optional\[str\]                                                                                                                                                                                 | False    | Device related information retrieved from TrustWidget.    |
| ip_address | constr(<br/> pattern=r”^(?:(?:25\[0-5\]\|2\[0-4\]\[0-9\]\|\[01\]?\[0-9\]\[0-9\]?).){3}(?:25\[0-5\]\|2\[0-4\]\[0-9\]\|\[01\]?\[0-9\]\[0-9\]?)$\|^(?:\[A-F0-9\]{1,4}:){7}\[A-F0-9\]{1,4}$“<br/> ) | True     | IP address of the device used for booking.                |
| source     | Optional\[constr(max_length=50)\]                                                                                                                                                               | False    | Source of the device_box. Default value is `TrustWidget`. |

# Inheritance

object > [PydanticModel](PydanticModel.md) > DeviceDetails
