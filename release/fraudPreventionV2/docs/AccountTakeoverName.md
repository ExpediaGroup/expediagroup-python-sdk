[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [AccountTakeoverName](AccountTakeoverName.md)

# class `expediagroup.sdk.fraudpreventionv2.model.AccountTakeoverName`

```python
AccountTakeoverName(
    last_name: constr(max_length=200),
    first_name: constr(max_length=200),
    middle_name: Optional[constr(max_length=200)],
    title: Optional[constr(max_length=200)],
    suffix: Optional[constr(max_length=50)],
)
```

pydantic model AccountTakeoverName: Group of attributes intended to hold
information about a customer or traveler’’s name for the account.

## Attributes

| Name        | Type                               | Required | Description                                                                                                                                                                      |
| ----------- | ---------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| first_name  | constr(max_length=200)             | True     | Given, or first name, of the person.                                                                                                                                             |
| last_name   | constr(max_length=200)             | True     | Surname, or last name, of the person.                                                                                                                                            |
| middle_name | Optional\[constr(max_length=200)\] | False    | Middle name of the person.                                                                                                                                                       |
| suffix      | Optional\[constr(max_length=50)\]  | False    | Generational designations (e.g. Sr, Jr, III) or values indicate that the individual holds a position, educational degree, accreditation, office, or honor (e.g. PhD, CCNA, OBE). |
| title       | Optional\[constr(max_length=200)\] | False    | Title of the person for name (e.g. Mr., Ms. etc).                                                                                                                                |

# Inheritance

object > BaseModel > AccountTakeoverName
