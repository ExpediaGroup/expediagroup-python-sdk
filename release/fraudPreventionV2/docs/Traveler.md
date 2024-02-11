[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Traveler](Traveler.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Traveler`

```python
Traveler(
    traveler_name: Name,
    email_address: Optional[EmailStr],
    telephones: Optional[list[Telephone]],
    primary: bool,
    age: Optional[float],
    birth_date: Optional[datetime],
    citizenship_country_code: Optional[constr(min_length=3, max_length=3, pattern=r"^[A-Z]{3}$")],
    traveler_id: Optional[constr(max_length=100)],
)
```

pydantic model Traveler

## Attributes

| Name                     | Type                                                                | Required | Description                                                                                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| age                      | Optional\[float\]                                                   | False    | Age of the traveler.                                                                                                                                                                           |
| birth_date               | Optional\[datetime\]                                                | False    | Date of birth for traveler, in ISO-8601 date and time format `yyyy-MM-ddTHH:mm:ss.SSSZ`.                                                                                                       |
| citizenship_country_code | Optional\[constr(min_length=3, max_length=3, pattern=r”[^1]{3}$“)\] | False    | The alpha-3 ISO country code of the traveler’s nationality.                                                                                                                                    |
| email_address            | Optional\[EmailStr\]                                                | False    | Email address associated with the traveler as supplied by the partner system.                                                                                                                  |
| primary                  | bool                                                                | True     | Indicator for one of the travelers who is the primary traveler. One traveler in each itinerary item must be listed as primary. By default, for a single traveler this should be set to `true`. |
| telephones               | Optional\[list\[[Telephone](Telephone.md)\]\]                       | False    | …                                                                                                                                                                                              |
| traveler_id              | Optional\[constr(max_length=100)\]                                  | False    | A unique identifier for travelers in the transaction.                                                                                                                                          |
| traveler_name            | [Name](Name.md)                                                     | True     | …                                                                                                                                                                                              |

# Inheritance

object > [PydanticModel](PydanticModel.md) > Traveler

[^1]: A-Z
