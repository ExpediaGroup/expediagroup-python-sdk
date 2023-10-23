[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [RemediationUpdateAction](RemediationUpdateAction.md)

# class `expediagroup.sdk.fraudpreventionv2.model.RemediationUpdateAction`

```python
RemediationUpdateAction(
    action_name: ActionName,
    status: Status2,
    update_end_date_time: Optional[datetime],
)
```

pydantic model RemediationUpdateAction: Information specific to the
remediation action initiated by the Partner’s system to a user.

## Attributes

| Name                 | Type                        | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | --------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| action_name          | [ActionName](ActionName.md) | True     | The categorized remediation action initiated by the Partner’‘s system to a user. Possible values are:<br/>- `PASSWORD_RESET` - Applicable if this event is the result of a password reset by the Partner’‘s system.<br/>- `DISABLE_ACCOUNT` - Applicable if this event is the result of disabling an account by the Partner’‘s system.<br/>- `TERMINATE_ALL_SESSIONS` - Applicable if this event is the result of terminating all active user sessions of an account by the Partner’’s system. |
| status               | [Status2](Status2.md)       | True     | The status of the remediation action.<br/> - `SUCCESS` - Applicable if the Partner’‘s system was successfully able to perform the remediation action.<br/> - `FAILED` - Applicable if the Partner’’s system failed to perform the remediation action.                                                                                                                                                                                                                                          |
| update_end_date_time | Optional\[datetime\]        | False    | The local date and time the remediation action to a user ended in the Partner’s system, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.                                                                                                                                                                                                                                                                                                                                           |

# Inheritance

object > BaseModel > RemediationUpdateAction
