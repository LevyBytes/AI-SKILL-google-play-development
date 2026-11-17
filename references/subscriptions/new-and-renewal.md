Subscription purchases can go through several different states throughout their lifecycle, depending on many factors including auto-renewal behavior, payment decline situations, and developer management actions.

## Handle lifecycle for auto-renewing subscriptions

When a user's subscription state changes, your backend server receives a [`SubscriptionNotification`](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) message.

![subs-auto-renew-state](<https://developer.android.com/static/images/google/play/billing/lifecycle/auto-renew-state-flow.svg>)

**Figure 1.** Lifecycle states and transition events for auto-renewing subscription purchases.

To update the state in your backend, call the [`purchases.subscriptionsv2.get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) API with the purchase token included in the notification. This endpoint provides the latest subscription state given a purchase token and is considered the source of truth for subscription management.

The purchase token is valid from subscription signup until 60 days after expiration. After this date, the purchase token is no longer valid to use to call the Google Play Developer API.

> **Note:** The [`purchases.subscriptions.get`](<https://developers.google.com/android-publisher/deprecated-apis/purchases.subscriptions/get>) method is deprecated and present for backward compatibility reasons. This method shouldn't be used to obtain subscription states for new integrations. If you have an existing integration that uses this method, see [API deprecations](<https://developer.android.com/google/play/billing/play-developer-apis-deprecations>) for alternatives. Other methods in the `purchases.subscriptions` endpoint are still in use.

### New auto-renewing subscription purchases

When a user purchases a subscription, a `SubscriptionNotification` message with type `SUBSCRIPTION_PURCHASED` is sent to your RTDN client. Whether you receive this notification or you register a new purchase in-app through [`PurchasesUpdatedListener`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener>) or [manually fetching purchases](<https://developer.android.com/google/play/billing/integrate#process>) in your app's `onResume()` method, you should process the new purchase in your secure backend. To do this, follow these steps:

1. Query the [`purchases.subscriptionsv2.get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) endpoint to get a [subscription resource](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) that contains the latest subscription state.
2. Make sure that the value of the [`subscriptionState`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionstate>) field is `SUBSCRIPTION_STATE_ACTIVE`.
3. [Verify the purchase](<https://developer.android.com/google/play/billing/security#verify>).
4. Give the user access to the content. The user account associated with the purchase can be identified with the [`ExternalAccountIdentifiers`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#externalaccountidentifiers>) object from the subscription resource if identifiers were set at purchase time using [`setObfuscatedAccountId`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedAccountId(java.lang.String)>) and [`setObfuscatedProfileId`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedProfileId(java.lang.String)>).

The `offerPhase` field in the `SubscriptionPurchaseLineItem` provides details about the current phase of the subscription, such as free trial or introductory price.

> **Note:** If you don't acknowledge a new subscription purchase within three days, the user automatically receives a refund, and Google Play revokes the purchase. If a purchase fails your verification or fraud checks and you choose not to grant entitlement, don't wait for the acknowledgment window to expire; withhold acknowledgment and immediately revoke and refund the subscription using [`purchases.subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) with `"fullRefund": {}` (see [Handle rejected or unfulfilled purchases](<https://developer.android.com/google/play/billing/integrate#rejected-purchases>)).

The Play Billing Library also includes a method to acknowledge a subscription, [`acknowledgePurchase()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#acknowledgepurchase>), and a method to check acknowledgement status, [`isAcknowledged()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#isacknowledged>). However, we recommend that you handle purchase processing in your backend for better security.

The subscription resource for new purchases looks similar to the following example:

[Complete json example: New auto-renewing subscription purchases](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#new-auto>).

### Subscription renewals

For non-installment, auto-renewing subscriptions, a `SUBSCRIPTION_RENEWED` notification is sent when the subscription renews. For installment subscriptions, a `SUBSCRIPTION_RENEWED` notification is sent each time the subscription is charged on its billing date. Make sure that the user is still entitled to the subscription and then update the subscription state with the new `expiryTime` provided in the [subscription resource](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) returned from the Google Play Developer API. The subscription resource looks similar to the following example:

[Complete json example: Subscription renewals](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#renewal>).

You don't need to acknowledge subscription renewals.

> **Note:** Renewals anchored to day 29, 30 or 31 move to day 28 when the next month has only 28 days, then stay on day 28 for the remaining subscription. Similarly, a subscription starting on day 31 renews on day 30 when the next month has 30 days, and continues to renew on day 30 thereafter.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/lifecycle/subscriptions).
