[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [GiftCard](GiftCard.md)

# class `expediagroup.sdk.fraudpreventionv2.model.GiftCard`

```python
GiftCard(
    card_number: constr(regex=r"^[0-9A-Za-z]{4,16}$", max_length=16),
    card_holder_name: constr(max_length=200),
    pin: constr(regex=r"^[0-9]{4,8}$", max_length=8),
    method: Literal["GIFT_CARD"],
)
```

pydantic model GiftCard

## Attributes

| Name             | Type                                        | Required | Description                   |
| ---------------- | ------------------------------------------- | -------- | ----------------------------- |
| card_holder_name | constr(max_length=200)                      | True     | The name of gift card holder. |
| card_number      | constr(regex=r”[^1]{4,16}$", max_length=16) | True     | Gift card number.             |

## Methods

### dict

```python
dict()
```

# Inheritance

object > [PaymentGeneric](PaymentGeneric.md) > GiftCard

[^1]: 0-9A-Za-z
