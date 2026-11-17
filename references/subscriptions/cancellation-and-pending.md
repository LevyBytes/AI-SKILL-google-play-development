## Handle cancellations and pending states

This section explains how to handle subscriptions that are cancelled or revoked, as well as how to manage subscriptions that enter a pending state during the purchase process.

### Cancel or revoke

You can use the [Google Play Developer API](<https://developers.google.com/android-publisher/api-ref/purchases/subscriptions>) to [cancel](<https://developers.google.com/android-publisher/api-ref/purchases/subscriptions/cancel>) or [revoke](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) a subscription. This functionality is also available in the [Google Play Console](<https://support.google.com/googleplay/android-developer/answer/2741495>).

- **Cancel**: Users can cancel a subscription on Google Play. You can also provide an option for users to cancel in your app or on your website. Your app should handle these cancellations as described in [Cancellations](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#cancel>).
- **Revoke**: When you revoke, the user immediately loses access to the subscription. This can be used if, for example, there was a technical error that prevented the user from accessing your product, and the user does not want to continue using the product. Your app should handle these cancellations as described in [Revocations](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#revoke>).

The following table illustrates the differences between cancel and revoke.

|  | **Stops renewal** | **Revoke access** |
| --- | --- | --- |
| **[Cancel](<https://developers.google.com/android-publisher/api-ref/purchases/subscriptions/cancel>)** | **Yes** | No |
| **[Revoke](<https://developers.google.com/android-publisher/api-ref/purchases/subscriptions/revoke>)** | **Yes** | **Yes** |

### Handle subscription pending transactions

> **Note:** Pending transactions are only available for purchasing prepaid plan with Google Play Billing Library versions 7.0 and higher. You need to support and enable pending transactions **explicitly**.

[Pending transactions](<https://developer.android.com/google/play/billing/integrate#pending>) can happen in initial purchase, top-up, upgrade or downgrade. The subscription purchase starts with the `SUBSCRIPTION_STATE_PENDING` state before transitioning to `SUBSCRIPTION_STATE_ACTIVE`. If the transaction is expired or canceled by the user, it goes to `SUBSCRIPTION_STATE_PENDING_PURCHASE_EXPIRED`. You must and should only update the user's entitlement after the transaction is completed.

Subscription state change for initial purchase with pending transactions is straightforward. Your app receives a `Purchase` with `PENDING` state when the user initiates a pending transaction. When the transaction is completed, your app receives the `Purchase` again with state updated to `PURCHASED`. A `SubscriptionNotification` message with type `SUBSCRIPTION_PURCHASED` is sent to your RTDN client. Follow the normal process to verify the purchase, give the user access to the content and acknowledge the purchase. If the transaction expires or is canceled, a `SubscriptionNotification` message with type `SUBSCRIPTION_PENDING_PURCHASE_CANCELED` is sent to your RTDN client. In such cases, the user should never have gained access to the content.

Top-up, upgrade or downgrade with pending transactions involves state changes for both the old and new subscriptions. When the user initiates a pending top-up, upgrade or downgrade transaction, your app receives a `Purchase` for the old subscription with a `PendingPurchaseUpdate` object. At this time, the user is still owning the old subscription and has not gained the new subscription yet. Calling `getProducts()` and `getPurchaseToken()` on the `PendingPurchaseUpdate` object returns the product ids and purchase token of the new subscription. When the transaction is completed, your app receives a `Purchase` with the top-level purchase token set for the new subscription and the state set to `PURCHASED`. A `SubscriptionNotification` message with type `SUBSCRIPTION_PURCHASED` is sent to your RTDN client. Only at this time, you should replace the old purchase token with the new purchase token and update the user's access to the content. If the transaction expires or is canceled, a `SubscriptionNotification` message with type `SUBSCRIPTION_PENDING_PURCHASE_CANCELED` is sent to your RTDN client. In such cases, the user should still have access to the content of the old subscription.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscriptions).
