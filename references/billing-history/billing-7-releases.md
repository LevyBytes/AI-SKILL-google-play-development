## Google Play Billing Library 7.1.1 Release

Version 7.1.1 of the Google Play Billing Library and Kotlin extensions are now available.

### Bug fixes

- Fixed a bug in Play Billing Library 7.1.0 related to [testing `BillingResult` response codes](<https://developer.android.com/google/play/billing/test-response-codes>).

## Google Play Billing Library 7.1.0 Release

Version 7.1.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- Improved thread safety related to connection status and management.
- Introduced partial changes for testing [`BillingResult`](<https://developer.android.com/reference/com/android/billingclient/api/BillingResult>) response codes which is fully released in Play Billing Library 7.1.1. To test your integration using this feature, you'll need to upgrade to Play Billing Library 7.1.1. A bug exists that will only impact applications with [billing overrides testing enabled](<https://developer.android.com/google/play/billing/test-response-codes#enable-billing-overrides-testing>) and does not affect regular usage. For more information, see [Test `BillingResult` response codes](<https://developer.android.com/google/play/billing/test-response-codes>).

## Google Play Billing Library 7.0.0 Release

Version 7.0.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- Added APIs to support installment subscriptions.

  - Added [`ProductDetails.InstallmentPlanDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails.InstallmentPlanDetails>) for installment base plans that users are eligible to purchase. This API helps your app identify the installment plan and its commitment setup to provide related information to the user. To learn more, see our [subscription installments guide](<https://developer.android.com/google/play/billing/subscriptions#installments>).
- Added [`PendingPurchasesParams`](<https://developer.android.com/reference/com/android/billingclient/api/PendingPurchasesParams>) and [`BillingClient.Builder.enablePendingPurchases(PendingPurchaseParams)`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enablePendingPurchases(com.android.billingclient.api.PendingPurchasesParams)>) to replace [`BillingClient.Builder.enablePendingPurchases()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enablePendingPurchases()>), which has been deprecated in this release.

  - The deprecated `enablePendingPurchases()` is functionally equivalent to `enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())`.
- Added APIs to support pending transactions for subscription prepaid plans:

  - Use [`PendingPurchasesParams.Builder.enablePrepaidPlans()`](<https://developer.android.com/reference/com/android/billingclient/api/PendingPurchasesParams.Builder#enablePrepaidPlans()>) along with [`BillingClient.Builder.enablePendingPurchases(PendingPurchaseParams)`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enablePendingPurchases(com.android.billingclient.api.PendingPurchasesParams)>) to enable pending transactions for subscription prepaid plans. When adding support, be sure that your app also correctly manages subscription lifecycles. To learn more see our [pending purchases guide](<https://developer.android.com/google/play/billing/subscriptions#pending>).
  - Added [`Purchase.PendingPurchaseUpdate`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase.PendingPurchaseUpdate>) and [`Purchase.getPendingPurchaseUpdate()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getPendingPurchaseUpdate()>) for retrieving the pending top-up or upgrade or downgrade to an existing subscription.
- Removed [`BillingClient.Builder.enableAlternativeBilling()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableAlternativeBilling(com.android.billingclient.api.AlternativeBillingListener)>), [`AlternativeBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/AlternativeBillingListener>), and [`AlternativeChoiceDetails`](<https://developer.android.com/reference/com/android/billingclient/api/AlternativeChoiceDetails>).

  - Developers should use [`BillingClient.Builder.enableUserChoiceBilling()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableUserChoiceBilling(com.android.billingclient.api.UserChoiceBillingListener)>) with [`UserChoiceBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/UserChoiceBillingListener>) and [`UserChoiceDetails`](<https://developer.android.com/reference/com/android/billingclient/api/UserChoiceDetails>) in the listener callback instead.
- Removed [`BillingFlowParams.ProrationMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProrationMode>), [`BillingFlowParams.SubscriptionUpdateParams.Builder.setReplaceProrationMode()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setReplaceProrationMode(int)>), and [`BillingFlowParams.SubscriptionUpdateParams.Builder.setReplaceSkusProrationMode()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setReplaceSkusProrationMode(int)>).

  - Developers should use [`BillingFlowParams.SubscriptionUpdateParams.ReplacementMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode>) with [`BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode(int)`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode(int)>) instead.
- Removed [`BillingFlowParams.SubscriptionUpdateParams.Builder#setOldSkuPurchaseToken()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOldSkuPurchaseToken(java.lang.String)>).

  - Developers should use [`BillingFlowParams.SubscriptionUpdateParams.Builder#setOldPurchaseToken(java.lang.String)`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOldPurchaseToken(java.lang.String)>) instead.
- [`BillingClient.queryPurchaseHistoryAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchaseHistoryAsync(com.android.billingclient.api.QueryPurchaseHistoryParams,com.android.billingclient.api.PurchaseHistoryResponseListener)>) has been deprecated and will be removed in a future release. Developers should use the following alternatives instead:

  - Acknowledged and pending purchases: Use [`BillingClient.queryPurchasesAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>) to fetch the active purchases.
  - Consumed purchases: Developers should keep track of consumed purchases on their own servers.
  - Canceled purchases: Use the [voided-purchases](<https://developers.google.com/android-publisher/voided-purchases>) developer API.
  - For more details, see [Query Purchase History](<https://developer.android.com/google/play/billing/query-purchase-history>)
- [`BillingFlowParams.ProductDetailsParams.setOfferToken()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams.Builder#setOfferToken(java.lang.String)>) now throws an exception when developers specify an empty `offerToken`.
- Updated `minSdkVersion` to 21 and `targetSdkVersion` to 34.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
