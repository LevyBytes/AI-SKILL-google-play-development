## Managing subscription status

This section describes the primary changes to the backend components of a Google Play billing system integration that need to be implemented for migration to version 5.

### Real Time Developer Notifications

Soon the [`SubscriptionNotification`](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) object will no longer contain a *subscriptionId*. If you are relying on this field to identify the subscription product, you should update to obtain this information from the subscription status by using [`purchases.subscriptionsv2:get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) after you receive the notification. Each [`SubscriptionPurchaseLineItem`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionpurchaselineitem>) element in the *lineItems* collection that is returned as part of the purchase status will include the corresponding *productId*.

### Subscriptions Purchases API: getting subscription status

The legacy Subscriptions Purchases endpoint [`purchases.subscriptions:get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions>) supports backward-compatible subscription purchases but **does not** support the new base-plan and offer functionality. Verify its [current deprecation and shutdown requirements](<https://developer.android.com/google/play/billing/play-developer-apis-deprecations>) before relying on it.

In the new version of the Subscriptions Purchases API, use [`purchases.subscriptionsv2:get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) to obtain subscription purchase status. This API is compatible with migrated subscriptions, new subscriptions (both prepaid and auto-renewing), and purchases of all types. You can use this endpoint to check for subscription status when receiving notifications. The returned object, `SubscriptionPurchaseV2`, contains new fields, but it still includes legacy data that is needed to continue supporting existing subscriptions.

#### SubscriptionPurchaseV2 fields for prepaid plans

New fields have been added to support prepaid plans, which are extended by the user instead of automatically renewing. All fields apply to prepaid plans as they do for auto-renewing subscriptions, with the following exceptions:

- **[New field] `lineItems[0].prepaid_plan.allowExtendAfterTime`**: denotes when a user will be allowed to buy another top-up to extend their prepaid plan, as a user is allowed to have only one unconsumed top-up at a time.
- **[New field] `SubscriptionState`**: specifies the subscription object state. For prepaid plans, this value is always either `ACTIVE`, `PENDING`, or `CANCELED`.
- **`lineItems[0].expiryTime`**: This field is always present for prepaid plans.
- **`paused_state_context`**: This field is never present, as prepaid plans cannot pause.
- **`lineItems[0].auto_renewing_plan`**: Not present for prepaid plans.
- **`canceled_state_context`**: Not present for prepaid plans, as this field applies only to users who actively cancel a subscription.
- **`lineItems[0].productId`**: This field replaces `subscriptionId` from previous versions.

#### SubscriptionPurchaseV2 fields for recurring subscriptions

`purchases.subscriptionsv2` contains new fields that provide more detail about new subscription objects. The following table shows how fields from the legacy subscription endpoint map to corresponding fields in `purchases.subscriptionsv2`.

| SubscriptionPurchase | SubscriptionPurchaseV2 |
| --- | --- |
| `countryCode` | `regionCode` |
| `orderId` | `latestOrderId` |
| (no equivalent field) | `lineItems.offerPhase` (identifies current phase: free trial, intro price, proration, base price) |
| (no equivalent field) | `lineItems` (list of [SubscriptionPurchaseLineItem](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionpurchaselineitem>)) that represents the products acquired with the purchase |
| (no equivalent field) | `lineItems.offerDetails.basePlanId` |
| (no equivalent field) | `lineItems.offerDetails.offerId` |
| (no equivalent field) | `lineItems.offerDetails.offerTags` |
| `startTimeMillis` | `startTime` |
| `expiryTimeMillis` | `lineItems.expiryTime` (each subscription acquired in the purchase has its own `expiryTime`) |
| (no equivalent field) | `subscriptionState` (indicates the [state of the subscription](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionstate>)) |
| (no equivalent field) | `pausedStateContext` (only present if the subscription status is `SUBSCRIPTION_STATE_PAUSED`) |
| `autoResumeTimeMillis` | `pausedStateContext.autoResumeTime` |
| (no equivalent field) | `canceledStateContext` (only present if the subscription status is `SUBSCRIPTION_STATE_CANCELED`) |
| (no equivalent field) | `testPurchase` (only present in licensed tester purchases) |
| `autoRenewing` | `lineItems.autoRenewingPlan.autoRenewEnabled` |
| `priceCurrenceCode`, `priceAmountMicros` | `lineItems.autoRenewingPlan.recurringPrice` |
| `introductoryPriceInfo` | `lineItems.offerPhase.introductoryPrice`<br> This information can also be found in the `offer` for each of the subscriptions purchased. |
| developerPayload | (no equivalent field) developer payload has been deprecated |
| paymentState | (no equivalent field)<br> You can infer the payment state from `subscriptionState`: Payment is pending: `SUBSCRIPTION_STATE_PENDING` (new purchases with pending transaction) `SUBSCRIPTION_STATE_IN_GRACE_PERIOD` `SUBSCRIPTION_STATE_ON_HOLD` Payment has been received: `SUBSCRIPTION_STATE_ACTIVE` Free trial: `lineItems.offerPhase.freeTrial` Deferred upgrade / downgrade: `SUBSCRIPTION_STATE_PENDING` |
| `cancelReason`, `userCancellationTimeMillis`, `cancelSurveyResult` | `canceledStateContext` |
| `linkedPurchaseToken` | `linkedPurchaseToken` (no change) |
| `purchaseType` | Test: through `testPurchase`<br> Promotion: `signupPromotion` |
| `priceChange` | `lineItems.autoRenewingPlan.priceChangeDetails` |
| `profileName`, `emailAddress`, `givenName`, `familyName`, `profileId` | [`subscribeWithGoogleInfo`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscribewithgoogleinfo>) |
| `acknowledgementState` | `acknowledgementState (no change)` |
| `promotionType`, `promotionCode` | `signupPromotion` |
| `externalAccountId`, `obfuscatedExternalAccountId`, `obfuscatedExteranlProfileId` | `externalAccountIdentifiers` |

### Other subscription management functions

While [`purchases.subscriptions:get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/get>) has been upgraded to [`purchases.subscriptionsv2:get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>), the rest of the developer subscription management functions remain unchanged for now in the `purchases.subscriptions` endpoint, so you can continue using [`purchases.subscriptions:acknowledge`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/acknowledge>), [`purchases.subscriptions:cancel`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/cancel>), [`purchases.subscriptions:defer`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/defer>), [`purchases.subscriptions:refund`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/refund>), and [`purchases.subscriptions:revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/revoke>) as you did before.

### Pricing API

Use the [`monetization.convertRegionPrices`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization/convertRegionPrices>) endpoint to calculate regional prices as you would through the Play Console. This method accepts a single price in any Play-supported currency and returns converted prices (including the default rate of tax where applicable) for all regions where Google Play supports purchases.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/compatibility).
