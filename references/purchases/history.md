`queryPurchaseHistory()` was deprecated in Play Billing Library 7. This page describes the recommended alternatives for use cases your app may have relied on `queryPurchaseHistory()` for.

## Process purchases

To retrieve purchases for processing, use [`queryPurchasesAsync(QueryPurchasesParams, PurchasesResponseListener)`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,com.android.billingclient.api.PurchasesResponseListener)>).

See the [Detect and process purchases](<https://developer.android.com/google/play/billing/integrate#process>) section of the integration guide for more details.

## Handle voided purchases

To fetch voided or canceled purchases, use the [voided purchases](<https://developers.google.com/android-publisher/voided-purchases>) server developer API.

## Track historical purchases

If your app would like to track a user's purchase history, your app should keep track of the history on your app's backend.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/query-purchase-history).
