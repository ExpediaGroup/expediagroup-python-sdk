[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [DelayedFulfillment](DelayedFulfillment.md)

# class `expediagroup.sdk.fraudpreventionv2.model.DelayedFulfillment`

```python
DelayedFulfillment(
    is_available: Optional[bool],
    hold_duration_value: Optional[float],
    hold_duration_unit_of_measure: Optional[constr(max_length=100)],
    is_delayed_customer_confirmation: Optional[bool],
)
```

pydantic model DelayedFulfillment: This field holds details about
activity’s capabilities and execution details related to inventory hold
functionality.

## Attributes

| Name                             | Type                               | Required | Description                                                                                                                                                                                                                                                 |
| -------------------------------- | ---------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hold_duration_unit_of_measure    | Optional\[constr(max_length=100)\] | False    | This field indicates the unit of duration of the hold on an activity.                                                                                                                                                                                       |
| hold_duration_value              | Optional\[float\]                  | False    | This field indicates the duration of the hold on an activity.                                                                                                                                                                                               |
| is_available                     | Optional\[bool\]                   | False    | This field indicates if the fulfillment of an activity is possible or not.                                                                                                                                                                                  |
| is_delayed_customer_confirmation | Optional\[bool\]                   | False    | This field indicates whether customer order confirmation can be delayed. Customer will receive ticket number, voucher ID or any other type of confirmation until transaction is successfully completed or approved by an analyst during the review process. |

# Inheritance

object > [PydanticModel](PydanticModel.md) > DelayedFulfillment
