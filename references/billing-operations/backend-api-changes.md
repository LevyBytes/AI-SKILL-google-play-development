This document contains release notes for the Google Play Developer APIs.

## Chargeback review and cost responsibility

### New features

- **Updates to chargeback cost responsibility**: Google Play now supports a [collaborative chargeback](<https://developer.android.com/google/play/billing/provide-refund-and-chargeback-suggestions>) dispute process.

  - **Pending refund review notifications**: A new real-time developer notification (RTDN) type, [`PendingRefundReviewNotification`](<https://developer.android.com/google/play/billing/rtdn-reference#pending-refund-review>), is sent when a user requests a chargeback that requires your review. Pending reviews support only `CHARGEBACK` as the refund reason.
  - **ReviewRefund API**: You can evaluate these requests and respond within 24 hours by calling the new [`orders.reviewrefund`](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders/reviewrefund>) API. In the API call, you must provide a refund preference (such as `APPROVE`, `DECLINE`, or `NEUTRAL`) and any relevant purchase usage evidence (such as user IP address, cumulative consumption percentage, and coarse geographic location) to help Google Play dispute the chargeback.

## Pending order context and deprecations

### New features

- **Pending order ID**: The [SubscriptionPurchaseV2](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) API now includes `onHoldStateContext` and `inGracePeriodStateContext` fields. These fields provide additional details, such as the pending or failed order ID, when a subscription enters the `ON_HOLD` or `IN_GRACE_PERIOD` state due to a declined renewal payment.

### Deprecations

- Some subscription APIs are deprecated. Check the [subscription API deprecation groups and replacements](<https://developer.android.com/google/play/billing/play-developer-apis-deprecations>) and their current shutdown requirements.

## Add-on deferrals and offer phases

### New features

- **Subscription with add-ons deferral**: Previously, the Google Play Developer API allowed deferral of billing only for single subscriptions. The deferral functionality is now available for both single subscriptions and subscriptions with add-ons through the [`purchases.subscriptionsv2.defer`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer>) method. When you defer the billing date of a subscription with add-ons, the billing date for all items in the subscription are deferred by the specified duration.
- **OfferPhase**: The `OfferPhase` field is now available in the [SubscriptionPurchaseV2](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) API. This field provides the current offer phase of the subscription as one of prorated period, free trial, introductory price and base plan price.

## Resubscribe context and replacement details

### New features

- [Enhanced Resubscribe handling](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#resubscribe_after_expiration>).

  - The `outOfAppPurchaseContext` field is now available in [SubscriptionPurchaseV2](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>), which helps link resubscription purchases made from the Play Store by providing details from the expired subscription.
  - The [purchases.subscriptions.acknowledge](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/acknowledge>) method now accepts optional `externalAccountId` in the request body, which lets you associate the resubscription purchase with your user identifiers.
- `SubscriptionPurchaseLineItem.itemReplacement` field is now available in [SubscriptionPurchaseV2](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>), which offers details about the item being replaced, if applicable.
- The [Orders API](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders>) now includes `offerPhaseDetails` field, which provides more detailed information on the orders funding a prorated period.

## Cancellation and price step-up consent

### New features

- The [SubscriptionPurchaseV2](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) API now provides the [`cancel`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/cancel>) method.

  This method provides an enhancement over the existing [purchases.subscriptions.cancel](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/cancel>) functionality by introducing support for the `cancellationType` parameter in client libraries.
- [Price step-up consent](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#price-stepup-consent>) features are available:

  - A new field is added in the [SubscriptionPurchaseV2](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>): `SubscriptionPurchaseLineItem.auto_renewing_plan.price_step_up_consent_details`.
  - A new real time developer notification type [SUBSCRIPTION_PRICE_STEP_UP_CONSENT_UPDATED](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) is available.

## One-time purchase options

### New features

- The new [ProductPurchaseV2](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.productsv2>) API that supports [multiple purchase options and offers for one-time products](<https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers>) is available.

## Subscription refunds and order queries

### Deprecations

- Some of the subscription APIs are deprecated. For more information, see [Subscription API deprecation](<https://developer.android.com/google/play/billing/play-developer-apis-deprecations#may21-api-deprecation>).

### New features

- The following new fields are available in the [SubscriptionPurchaseV2](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>):

  - `SubscriptionPurchaseLineItem.latest_successful_order_id`
  - `PriceChangeState.CANCELED`
- The [`subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) method now provides the `item_based_refund` option.
- The [Orders](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders>) API now provides the [`get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders/get>) and [`batchGet`](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders/batchget>) methods.

### Other changes

- The *subscriptionId* parameter is optional in the [purchases.subscriptions](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions>) APIs.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/play-developer-apis-release-notes).
