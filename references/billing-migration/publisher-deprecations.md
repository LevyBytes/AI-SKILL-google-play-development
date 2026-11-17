This document lists the Google Play Developer APIs and the related features which are in a deprecation period.

## Cancellation, deferral and offer-phase migration

The APIs and features in this group are deprecated. Check the [official deprecation schedule](<https://developer.android.com/google/play/billing/play-developer-apis-deprecations>) for their exact shutdown and extension cutoffs. You may request an eligible extension by submitting a support ticket through [Play Console > Help](<https://play.google.com/console/u/0/developers/help-and-support>).

> **Note:** Newer [client libraries](<https://developers.google.com/android-publisher/libraries>) stop including these APIs according to the published schedule; existing libraries can still access them until their shutdown cutoff. Verify both the library-removal and service-shutdown requirements in the [official schedule](<https://developer.android.com/google/play/billing/play-developer-apis-deprecations>).

### Deprecated subscription APIs

This section lists the API deprecations.

| API | Available replacement |
| --- | --- |
| [subscriptions.cancel](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/cancel>) | [subscriptionsv2.cancel](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/cancel>) |
| [subscriptions.defer](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/defer>) | [subscriptionsv2.defer](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer>) |
| [Order.lineItems.subscriptionDetails.offer_phase](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders#Order>) | [Order.lineItems.subscriptionDetails.offer_phase_details](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders#Order>) |

## Purchase status, refund and revocation migration

The APIs and features in this group are deprecated. Check the [official deprecation schedule](<https://developer.android.com/google/play/billing/play-developer-apis-deprecations>) for their exact shutdown and extension cutoffs. You may request an eligible extension by submitting a support ticket through [Play Console > Help](<https://play.google.com/console/u/0/developers/help-and-support>).

> **Note:** Newer [client libraries](<https://developers.google.com/android-publisher/libraries>) stop including these APIs according to the published schedule; existing libraries can still access them until their shutdown cutoff. Verify both the library-removal and service-shutdown requirements in the [official schedule](<https://developer.android.com/google/play/billing/play-developer-apis-deprecations>).

### Deprecated subscription APIs

This section lists the API deprecations.

| API | Available replacement |
| --- | --- |
| [subscriptions.get](<https://developers.google.com/android-publisher/deprecated-apis/purchases.subscriptions/get>) | [subscriptionsv2.get](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) |
| [subscriptions.refund](<https://developers.google.com/android-publisher/deprecated-apis/purchases.subscriptions/refund>) | Call [subscriptionsv2.get](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) to get SubscriptionPurchaseLineItem. latest_successful_order_id, and then call [Orders.refund](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund>) to refund the orders. |
| [subscriptions.revoke](<https://developers.google.com/android-publisher/deprecated-apis/purchases.subscriptions/revoke>) | [subscriptionsv2.revoke](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) |
| [SubscriptionPurchaseV2. latestOrderId](<https://developers.google.com/android-publisher/deprecated-apis/latestOrderId.subscription.purchasev2>) | [SubscriptionPurchaseLineItem. latest_successful_order_id](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionpurchaselineitem>) |
| RealTimeDeveloperNotification. SubscriptionNotification.subscriptionId | No replacement |
| [RealTimeDeveloperNotification. SubscriptionNotification. notificationType SUBSCRIPTION_PRICE_CHANGE_CONFIRMED](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) | SUBSCRIPTION_PRICE _CHANGE_UPDATED |

### SubscriptionPurchaseV2 fields for recurring subscriptions

`purchases.subscriptionv2` contains new fields that provide more detail about new subscription objects. The following table shows how fields from the legacy subscription endpoint map to corresponding fields in `purchases.subscriptionv2`.

| SubscriptionPurchase | SubscriptionPurchaseV2 |
| --- | --- |
| `countryCode` | `regionCode` |
| `orderId` | `lineItems.latestSuccessfulOrderId`<br> You can get the pending order ID from `inGracePeriodStateContext.renewalDeclined.pendingOrderId` or `onHoldStateContext.renewalDeclined.pendingOrderId`. |
| `startTimeMillis` | `startTime` |
| `expiryTimeMillis` | `lineItems.expiryTime` (each subscription acquired in the purchase has its own `expiryTime`) |
| `autoResumeTimeMillis` | `pausedStateContext.autoResumeTime` |
| `autoRenewing` | `lineItems.autoRenewingPlan.autoRenewEnabled` |
| `priceCurrencyCode`, `priceAmountMicros` | `lineItems.autoRenewingPlan.recurringPrice` |
| `introductoryPriceInfo` | `lineItems.offerPhase.introductoryPrice`<br> This information can also be found in the `offer` for each of the subscriptions purchased. |
| `developerPayload` | (no equivalent field) developer payload has been deprecated |
| `paymentState` | (no equivalent field)<br> You can infer the payment state from `subscriptionState`: Payment is pending: `SUBSCRIPTION_STATE_PENDING` (new purchases with pending transaction) `SUBSCRIPTION_STATE_IN_GRACE_PERIOD` `SUBSCRIPTION_STATE_ON_HOLD` Payment has been received: `SUBSCRIPTION_STATE_ACTIVE` Free trial: `lineItems.offerPhase.freeTrial` Deferred upgrade / downgrade: `lineItems.deferredItemReplacement` |
| `cancelReason`, `userCancellationTimeMillis`, `cancelSurveyResult` | `canceledStateContext` |
| `linkedPurchaseToken` | `linkedPurchaseToken` (no change) |
| `purchaseType` | Test: through `testPurchase`<br> Promotion: `signupPromotion` |
| `priceChange` | `lineItems.autoRenewingPlan.priceChangeDetails` |
| `profileName`, `emailAddress`, `givenName`, `familyName`, `profileId` | `subscribeWithGoogleInfo` |
| `acknowledgementState` | `acknowledgementState (no change)` |
| `promotionType`, `promotionCode` | `signupPromotion` |
| `externalAccountId`, `obfuscatedExternalAccountId`, `obfuscatedExternalProfileId` | `externalAccountIdentifiers` |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/play-developer-apis-deprecations).
