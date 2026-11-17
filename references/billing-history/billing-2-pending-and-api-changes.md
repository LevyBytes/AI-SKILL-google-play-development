### Pending transactions

With version 2.0 of the Google Play Billing library, you *must* support purchases where additional action is required before granting entitlement. For example, a user might choose to purchase your in-app product at a physical store using cash. This means that the transaction is completed outside of your app. In this scenario, you should grant entitlement only after the user has completed the transaction.

To enable pending purchases, call [`enablePendingPurchases()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enablependingpurchases>) as part of initializing your app.

Use [`Purchase.getPurchaseState()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getpurchasestate>) to determine whether the purchase state is `PURCHASED` or `PENDING`. Note that you should grant entitlement only when the state is `PURCHASED`. You should check for `Purchase` status updates by doing the following:

1. When starting your app, call [`BillingClient.queryPurchases()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querypurchases>) to retrieve the list of unconsumed products associated with the user.
2. Call `Purchase.getPurchaseState()` on each returned `Purchase` object.
3. Implement the [`onPurchasesUpdated()`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener#onpurchasesupdated>) method to respond to changes to `Purchase` objects.

In addition, the Google Play Developer API includes a `PENDING` state for [`Purchases.products`](<https://developers.google.com/android-publisher/api-ref/purchases/products>). Pending transactions are not supported for subscriptions.

This release also introduces a new real-time developer notification type, `OneTimeProductNotification`. This notification type contains a single message whose value is either `ONE_TIME_PRODUCT_PURCHASED` or `ONE_TIME_PRODUCT_CANCELED`. This notification type is sent only for purchases associated with delayed forms of payment, such as cash.

When acknowledging pending purchases, be sure to acknowledge only when the purchase state is `PURCHASED` and not `PENDING`.

> **Note:** Pending transactions can be tested using license testers. In addition to two test credit cards, license testers have access to two new test instruments for delayed forms of payment which automatically complete or cancel after a couple of minutes. While testing your application, you should verify that your application does not grant entitlement or acknowledge the purchase immediately after purchasing with either of these two new instruments. When purchasing using the new test instrument that automatically completes, you should verify that your application grants entitlement and acknowledges the purchase once the purchase completes.

### API changes

Version 2.0 of the Google Play Billing library contains several API changes to support new features and clarify existing functionality.

#### consumeAsync

[`consumeAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#consumeasync>) now takes a [`ConsumeParams`](<https://developer.android.com/reference/com/android/billingclient/api/ConsumeParams>) object instead of a `purchaseToken`. `ConsumeParams` contains the `purchaseToken` as well as an optional developer payload.

The previous version of `consumeAsync()` has been removed in this release.

#### queryPurchaseHistoryAsync

To minimize confusion, [`queryPurchaseHistoryAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchaseHistoryAsync(java.lang.String,%20com.android.billingclient.api.PurchaseHistoryResponseListener)>) now returns a [`PurchaseHistoryRecord`](<https://developer.android.com/reference/com/android/billingclient/api/PurchaseHistoryRecord>) object instead of a `Purchase` object. The `PurchaseHistoryRecord` object is the same as a `Purchase` object, except that it reflects only the values returned by `queryPurchaseHistoryAsync()` and does not contain the `autoRenewing`, `orderId`, and `packageName` fields. Note that nothing has changed with the returned data: `queryPurchaseHistoryAsync()` returns the same data as before.

#### BillingResult return values

APIs that previously returned a `BillingResponse` integer value now return a [`BillingResult`](<https://developer.android.com/reference/com/android/billingclient/api/BillingResult>) object. `BillingResult` contains the `BillingResponse` integer as well as a debug string that you can use to diagnose errors. The debug string uses an en-US locale and is not meant to be shown to end users.

### Bug fixes

- [`SkuDetails.getIntroductoryPriceAmountMicros()`](<https://developer.android.com/reference/com/android/billingclient/api/SkuDetails#getIntroductoryPriceAmountMicros()>) now returns a `long` instead of a `String`.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
