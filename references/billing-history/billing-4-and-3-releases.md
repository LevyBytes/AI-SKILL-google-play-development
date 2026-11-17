## Google Play Billing Library 4.1 release

Version 4.1.0 of the Google Play Billing Library and Kotlin extensions are now available.

This version contains the following changes.

### Summary of changes

- Added [`BillingClient.showInAppMessages()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#showInAppMessages(android.app.Activity,%20com.android.billingclient.api.InAppMessageParams,%20com.android.billingclient.api.InAppMessageResponseListener)>) to help with handling subscription payment declines. To learn more about how to use in-app messaging for handling subscriptions payment declines, see [Handling payment declines](<https://developer.android.com/google/play/billing/subscriptions#payment-declines>).

## Google Play Billing Library 4.0 Release

Version 4.0.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- Added [`BillingClient.queryPurchasesAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(java.lang.String,%20com.android.billingclient.api.PurchasesResponseListener)>) to replace [`BillingClient.queryPurchases()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchases(java.lang.String)>) which will be removed in a future release.
- Added new subscription replacement mode [`IMMEDIATE_AND_CHARGE_FULL_PRICE`](<https://developer.android.com/google/play/billing/subscriptions#replacement-modes>).
- Added [`BillingClient.getConnectionState()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#getConnectionState()>) method to retrieve the Play Billing Library's connection state.
- Updated Javadoc and implementation to indicate which thread a method can be called on and which thread results are posted.
- Added [`BillingFlowParams.Builder.setSubscriptionUpdateParams()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setSubscriptionUpdateParams(com.android.billingclient.api.BillingFlowParams.SubscriptionUpdateParams)>) as a new way to initiate subscription updates. This replaces `BillingFlowParams#getReplaceSkusProrationMode`, `BillingFlowParams#getOldSkuPurchaseToken`, `BillingFlowParams#getOldSku`, `BillingFlowParams.Builder#setReplaceSkusProrationMode`, `BillingFlowParams.Builder#setOldSku` which have been removed.
- Added [`Purchase.getQuantity()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getQuantity()>) and [`PurchaseHistoryRecord.getQuantity()`](<https://developer.android.com/reference/com/android/billingclient/api/PurchaseHistoryRecord#getQuantity()>).
- Added [`Purchase#getSkus()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getSkus()>) and [`PurchaseHistoryRecord#getSkus()`](<https://developer.android.com/reference/com/android/billingclient/api/PurchaseHistoryRecord#getSkus()>). These replace `Purchase#getSku` and `PurchaseHistoryRecord#getSku` which have been removed.
- Removed `BillingFlowParams#getSku`, `BillingFlowParams#getSkuDetails` and `BillingFlowParams#getSkuType`.

## Google Play Billing Library 3.0.3 Release

Version 3.0.3 of the Google Play Billing Library, Kotlin extension, and Unity plugin are now available.

### Java and Kotlin Bug fixes

- Fix memory leak when [`endConnection()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#endConnection()>) is called.
- Fix issue when the Google Play Billing Library is used by apps which use the single task launch mode. A [`onPurchasesUpdated()`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener#onpurchasesupdated>) callback will be triggered when an app is resumed from the Android launcher and the billing dialog was visible prior to being suspended.

### Unity Bug fixes

- Update to Java version 3.0.3 to fix memory leak and resolve issue preventing purchases when an app is resumed from the Android launcher and the billing dialog was visible prior to being suspended.

## Google Play Billing Library 3.0.2 Release

Version 3.0.2 of the Google Play Billing Library and Kotlin extension are now available.

### Bug fixes

- Fixed a bug in the Kotlin extension where the coroutine fails with error "Already resumed".
- Fixed unresolved references when the Kotlin extension is used with the kotlinx.coroutines library version 1.4+.

## Google Play Billing Library 3.0.1 Release

Version 3.0.1 of the Google Play Billing Library and Kotlin extension are now available.

### Bug fixes

- Fixed a bug where if the app was killed and restored during the billing flow, `PurchasesUpdatedListener` may not be called with the purchase result.

## Google Play Billing Library 3.0 Release

Version 3.0.0 of the Google Play Billing Library, Kotlin extension, and Unity plugin are now available.

### Summary of changes

- Removed rewarded SKU support.
- Removed the `ChildDirected` and `UnderAgeOfConsent` parameters.
- Removed deprecated developer payload methods.
- Removed deprecated methods `BillingFlowParams.setAccountId()` and `BillingFlowParams.setDeveloperId()`.
- Removed deprecated methods `BillingFlowParams.setOldSkus(String oldSku)` and `BillingFlowParams.addOldSku(String oldSku)`.
- Added nullability annotations.

### Bug fixes

- [`SkuDetails.getIntroductoryPriceCycles()`](<https://developer.android.com/reference/com/android/billingclient/api/SkuDetails#getIntroductoryPriceCycles()>) now returns `int` instead of `String`.
- Fixed a bug where the billing flow would be treated as having extra params even if no extra params were set.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
