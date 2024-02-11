[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [Operations](Operations.md)

# class `expediagroup.sdk.fraudpreventionv2.model.Operations`

```python
Operations(
    verify: Optional[Verify],
    authorize: Optional[Authorize],
    authorize_reversal: Optional[AuthorizeReversal],
    capture: Optional[Capture],
    refunds: Optional[list[Refund]],
)
```

pydantic model Operations: All operations related to a payment
throughout its lifespan. An operation represents an event external to
Fraud Prevention Service that specifies to perform a payment operation.
Possible operation types include:

- `Verify`

- `Authorize`

- `AuthorizeReversal`

- `Capture`

- `Refund`

## Attributes

| Name               | Type                                                  | Required | Description |
| ------------------ | ----------------------------------------------------- | -------- | ----------- |
| authorize          | Optional\[[Authorize](Authorize.md)\]                 | False    | …           |
| authorize_reversal | Optional\[[AuthorizeReversal](AuthorizeReversal.md)\] | False    | …           |
| capture            | Optional\[[Capture](Capture.md)\]                     | False    | …           |
| refunds            | Optional\[list\[[Refund](Refund.md)\]\]               | False    | …           |
| verify             | Optional\[[Verify](Verify.md)\]                       | False    | …           |

# Inheritance

object > [PydanticModel](PydanticModel.md) > Operations
