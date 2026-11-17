### Expirations

Once a subscription expires, the user should lose access to the subscription. A `SubscriptionNotification` message with type `SUBSCRIPTION_EXPIRED` is sent in that case. When you receive this notification, query the Google Play Developer API to get the latest [subscription resource](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>). After you confirm that the `subscriptionState` is `SUBSCRIPTION_STATE_EXPIRED`, remove the entitlement and register the purchase state as invalid in your backend. The subscription resource looks similar to the following example:

```json
{
  "kind": "androidpublisher#subscriptionPurchaseV2",
  ...
  "subscriptionState": "SUBSCRIPTION_STATE_EXPIRED",
  ...
  "lineItems": [
    {
      "productId": "sub_variant_plan01",
      "expiryTime": expiration_time_in_past,
      ...
    }
  ],
}
```

### Cancellations

A user can voluntarily cancel a subscription from the Play subscriptions center or have their subscription automatically canceled if they don't recover after being in [account hold](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#account-hold>). Developers can also trigger a cancellation with [`purchases.subscriptionsv2.cancel`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/cancel>) When a subscription is canceled, the user retains access to the content until the end of the current billing cycle. When the billing cycle ends, access should be revoked.

> **Note:** For installment subscriptions, user-initiated cancellation takes effect at the end of the current commitment period. Developer-initiated cancellation, using the [`purchases.subscriptionsv2.cancel`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/cancel>) API, where the `cancellationType` request parameter is set to `USER_REQUESTED_STOP_RENEWALS`, takes effect at the end of the current commitment period. However, setting the `cancellationType` request parameter to `DEVELOPER_REQUESTED_STOP_PAYMENTS`, stops the next payment.

Canceling a non-installment, auto-renewing subscription triggers a `SUBSCRIPTION_CANCELED` notification. When you receive this notification, the [subscription resource](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) returned from the Google Play Developer API has the `subscriptionState` field set to `SUBSCRIPTION_STATE_CANCELED`, and the `expiryTime` field contains the date when the user should lose access to the subscription. If that date is in the past, then the user should lose entitlement immediately. This could happen, for example, if a user cancels a subscription while on [account hold](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#account-hold>) due to a payment decline.

The subscription resource for a canceled purchase looks similar to the following example:

```json
{
  "kind": "androidpublisher#subscriptionPurchaseV2",
  ...
  "subscriptionState": "SUBSCRIPTION_STATE_CANCELED",
  ...
  "lineItems": [
    {
      "productId": "sub_variant_plan01",
      "expiryTime": expiration_time,
      ...
    }
  ],
}
```

For installment subscriptions, a `SUBSCRIPTION_CANCELLATION_SCHEDULED` notification gets sent upon a user-initiated cancellation when payments remain for the commitment period. The cancellation is pending and takes effect at the end of the current commitment period. When you receive this notification, the subscription resource returned from the Google Play Developer API has the subscriptionState field set to `SUBSCRIPTION_STATE_ACTIVE` because the installment subscription is still active until the end of the commitment period. However, there is an empty pendingCancellation object present. A `SUBSCRIPTION_CANCELED` notification gets sent followed by a `SUBSCRIPTION_EXPIRED` at the end of the commitment period.

The subscription resource for a installment subscription purchase that is pending cancellation looks similar to the following example:

```json
{
  "kind": "androidpublisher#subscriptionPurchaseV2",
  ...
  "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
  ...
  "lineItems": [
    {
      "productId": "sub_plan01",
      "expiryTime": expiration_time,
      "autoRenewingPlan": {
        "autoRenewEnabled": true,
        "recurringPrice": {
          "currencyCode": "USD",
          "units": "1",
          "nanos": 990000000
        },
        "installmentDetails": {
          "initialCommittedPaymentsCount": 6,
          "remainingCommittedPaymentsCount": 5,
          "pendingCancellation": {}
      ...
        }
      }
    }
  ],
}
```

You can look at the `canceledStateContext` field in the subscription resource to learn why the subscription was canceled (for example, whether the subscription was canceled by the user, by the system, or by you). If the subscription was canceled by the user, you can look at the `userInitiatedCancellation` field to learn why the user canceled the subscription. This can help inform communication strategies.

When a subscription is canceled but has not yet [expired](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#expiration>), it is still returned from [`queryPurchasesAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>). You might want to display a message in your app informing the user that their subscription was canceled and giving them the date of expiration.

> **Warning:** Don't remove access to a subscription from Google Play while the user is still entitled to the content. Removing access to content that a user is entitled to is a violation of [Google Play's subscriptions policy](<https://support.google.com/googleplay/android-developer/answer/9900533>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/lifecycle/subscriptions).
