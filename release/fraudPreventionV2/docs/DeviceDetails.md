[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [DeviceDetails](DeviceDetails.md)

# class `expediagroup.sdk.fraudpreventionv2.model.DeviceDetails`

```
DeviceDetails(
    source: Optional[constr(max_length=50)],
    device_box: Optional[constr(max_length=16000)],
    ip_address: constr(
        regex=r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$"
    ),
)
```

pydantic model DeviceDetails

## Attributes

| Name       | Type                                  | Required        | Description                                               |
| ---------- | ------------------------------------- | --------------- | --------------------------------------------------------- |
| device_box | Optional\[constr(max_length=16000)\]  | False           | Device related information retrieved from TrustWidget.    |
| ip_address | constr(<br/> regex=r“^(?:(?:25\[0-5\] | 2\[0-4\]\[0-9\] | \[01\]?\[0-9\]\[0-9\]?).){3}(?:25\[0-5\]                  |
| source     | Optional\[constr(max_length=50)\]     | False           | Source of the device_box. Default value is `TrustWidget`. |

# Inheritance

object > BaseModel > DeviceDetails
