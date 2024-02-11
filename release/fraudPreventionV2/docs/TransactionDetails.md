[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.model](expediagroup.sdk.fraudpreventionv2.model.md)
/ [TransactionDetails](TransactionDetails.md)

# class `expediagroup.sdk.fraudpreventionv2.model.TransactionDetails`

```python
TransactionDetails(
    order_id: constr(max_length=50),
    current_order_status: CurrentOrderStatus,
    order_type: OrderType,
    travel_products: list[TravelProduct],
    travelers: list[Traveler],
    payments: Optional[list[Payment]],
)
```

pydantic model TransactionDetails

## Attributes

| Name                 | Type                                                                                                                                                                                                                                           | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| current_order_status | [CurrentOrderStatus](CurrentOrderStatus.md)                                                                                                                                                                                                    | True     | Status of the order:<br/>\_ `IN_PROGRESS` is used when order has not processed fully. For example, inventory has not yet been reserved, or payment has not yet been settled.<br/>\_ `COMPLETED` is used when an order has been processed fully. For example, inventory has been reserved, and the payment has been settled.                                                                                                                                         |
| order_id             | constr(max_length=50)                                                                                                                                                                                                                          | True     | Unique identifier assigned to the order by the partner. `order_id` is specific to the partner namespace.                                                                                                                                                                                                                                                                                                                                                            |
| order_type           | [OrderType](OrderType.md)                                                                                                                                                                                                                      | True     | Type of order. Possible `order_types`.<br/><br/>`CREATE` - Initial type of a brand new order.<br/><br/>`CHANGE` - If a `OrderPurchaseScreenRequest` has already been submitted for the initial booking with `order_type = CREATE`, but has now been modified and partner wishes to resubmit for Fraud screening then the `order_type = CHANGE`. Examples of changes that are supported are changes made to `check-in/checkout dates` or `price of a TravelProduct`. |
| payments             | Optional\[list\[Union\[[CreditCard](CreditCard.md), [PayPal](PayPal.md), [Points](Points.md), [GiftCard](GiftCard.md), [InternetBankPayment](InternetBankPayment.md), [DirectDebit](DirectDebit.md), [PaymentGeneric](PaymentGeneric.md)\]\]\] | False    | List of the form(s) of payment being used to purchase the order. One or more forms of payment can be used within an order. Information gathered will be specific to the form of payment.                                                                                                                                                                                                                                                                            |
| travel_products      | list\[Union\[[Rail](Rail.md), [Air](Air.md), [Cruise](Cruise.md), [Car](Car.md), [Hotel](Hotel.md), [Insurance](Insurance.md), [TravelProductGeneric](TravelProductGeneric.md)\]\]                                                             | True     | …                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| travelers            | list\[[Traveler](Traveler.md)\]                                                                                                                                                                                                                | True     | Individuals who are part of the travel party for the order. At minimum there must be at least `1` traveler.                                                                                                                                                                                                                                                                                                                                                         |

# Inheritance

object > [PydanticModel](PydanticModel.md) > TransactionDetails
