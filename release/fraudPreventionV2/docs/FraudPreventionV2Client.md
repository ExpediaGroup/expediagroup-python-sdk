[index](index.md) /
[expediagroup.sdk.fraudpreventionv2.client](expediagroup.sdk.fraudpreventionv2.client.md)
/ [FraudPreventionV2Client](FraudPreventionV2Client.md)

# class `expediagroup.sdk.fraudpreventionv2.client.FraudPreventionV2Client`

```python
FraudPreventionV2Client(
    client_config: ClientConfig,
)
```

Fraud Prevention V2 API Client.

## Methods

### screen_account

```python
screen_account(
    body: AccountScreenRequest,
)
```

#### Parameters

| Name | Type                                            | Required | Description                                                                                                                                                                                                                                                                                                                                               |
| ---- | ----------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body | [AccountScreenRequest](AccountScreenRequest.md) | True     | The Account Screen API gives a Fraud recommendation for an account transaction. A recommendation can be ACCEPT, CHALLENGE, or REJECT. A transaction is marked as CHALLENGE whenever there are insufficient signals to recommend ACCEPT or REJECT. These CHALLENGE incidents are manually reviewed, and a corrected recommendation is made asynchronously. |

### notify_with_account_update

```python
notify_with_account_update(
    body: AccountUpdateRequest,
)
```

#### Parameters

| Name | Type                                                                                                                                                                                     | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body | Union\[[MultiFactorAuthenticationUpdate](MultiFactorAuthenticationUpdate.md), [RemediationUpdate](RemediationUpdate.md), [AccountUpdateRequestGeneric](AccountUpdateRequestGeneric.md)\] | True     | The Account Update API is called when there is an account lifecycle transition such as a challenge outcome, account restoration, or remediation action completion. For example, if a user’s account is disabled, deleted, or restored, the Account Update API is called to notify Expedia Group about the change. The Account Update API is also called when a user responds to a login Multi-Factor Authentication based on a Fraud recommendation. |

### screen_order

```python
screen_order(
    body: OrderPurchaseScreenRequest,
)
```

#### Parameters

| Name | Type                                                        | Required | Description                                                                                                                                                                                                                                                                                                                      |
| ---- | ----------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body | [OrderPurchaseScreenRequest](OrderPurchaseScreenRequest.md) | True     | The Order Purchase API gives a Fraud recommendation for a transaction. A recommendation can be Accept, Reject, or Review. A transaction is marked as Review whenever there are insufficient signals to recommend Accept or Reject. These incidents are manually reviewed, and a corrected recommendation is made asynchronously. |

### notify_with_order_update

```python
notify_with_order_update(
    body: OrderPurchaseUpdateRequest,
)
```

#### Parameters

| Name | Type                                                                                                                                                                                                                                                                                                                                                                                       | Required | Description                                                                                                                                                                                                                                                                                                                                                               |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| body | Union\[[OrderUpdate](OrderUpdate.md), [ChargebackFeedback](ChargebackFeedback.md), [InsultFeedback](InsultFeedback.md), Union\[[IssuedRefundUpdate](IssuedRefundUpdate.md), [SettledRefundUpdate](SettledRefundUpdate.md), [RefundUpdateGeneric](RefundUpdateGeneric.md)\], [PaymentUpdate](PaymentUpdate.md), [OrderPurchaseUpdateRequestGeneric](OrderPurchaseUpdateRequestGeneric.md)\] | True     | For example, if the customer cancels the reservation, changes reservation in any way, or adds additional products or travelers to the reservation, the Order Purchase Update API is called to notify Expedia Group about the change.<br/><br/>The Order Purchase Update API is also called when the merchant cancels or changes an order based on a Fraud recommendation. |

# Inheritance

object > FraudPreventionV2Client
