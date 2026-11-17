## Google Play Billing Library 8.0.0 Release

Version 8.0.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- *In-app items* will now be referred to as *one-time products*.
- Multiple purchase options and offers for one-time products.

  You can now have multiple purchase options and offers for your one-time products. This provides you flexibility in how you sell your products and reduces the complexity of managing them.
- Improved the [`queryProductDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)>) method.

  Prior to PBL 8.0.0, the [`queryProductDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)>) method didn't return products that couldn't be fetched. This could be due to reasons such as the product is not found or no offers are available to the user. With PBL 8.0.0, unfetched products are returned with a new product-level status code that provides information about unfetched products. Note that there is a change in the signature of the [`ProductDetailsResponseListener.onProductDetailsResponse()`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetailsResponseListener#onProductDetailsResponse(com.android.billingclient.api.BillingResult,com.android.billingclient.api.QueryProductDetailsResult)>) which requires changes in your app. For more information, see [process the result](<https://developer.android.com/google/play/billing/integrate#process-the-result>).
- Automatic service reconnection.

  The new `BillingClient.Builder.enableAutoServiceReconnection()` builder parameter lets developers opt-in to automatic service reconnection, which simplifies connection management by handling reconnections to the Play Billing Service automatically and eliminating the need to manually call `startConnection()` in the event of a service disconnection. For more information, see [Automatically Re-establish a Connection](<https://developer.android.com/google/play/billing/integrate#automatic-service-reconnection>).
- Sub-response codes for the [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) method.

  The [BillingResult](<https://developer.android.com/reference/com/android/billingclient/api/BillingResult>) returned from [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) will now include a sub-response code field. This field will only be populated in some cases to provide a more specific reason for the failure. The sub-response field can have the following values:

  - `PAYMENT_DECLINED_DUE_TO_INSUFFICIENT_FUNDS` - Returned when the user's funds are less than the price of the item they are attempting to purchase.
  - `USER_INELIGIBLE` - Returned when the user doesn't meet the configured eligibility requirements for a subscription offer.
  - `NO_APPLICABLE_SUB_RESPONSE_CODE` - The default value, returned when no other sub-response code is applicable.
- Removed the `queryPurchaseHistory()` method.

  The `queryPurchaseHistory()` method that was previously marked as deprecated has now been removed. See [Query Purchase History](<https://developer.android.com/google/play/billing/query-purchase-history>) for details on what alternative APIs to use instead.
- Removed the `querySkuDetailsAsync()` method.

  The `querySkuDetailsAsync()` method that was previously marked as deprecated has now been removed. You should use [queryProductDetailsAsync](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)>) instead.
- Removed the `BillingClient.Builder.enablePendingPurchases()` method.

  The `enablePendingPurchases()` method with no parameters that was previously marked as deprecated has now been removed. You should use `enablePendingPurchases(PendingPurchaseParams params)` instead. Note that the deprecated `enablePendingPurchases()` is functionally equivalent to `enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())`.
- Removed the overloaded `queryPurchasesAsync()` method that takes a [skuType](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.SkuType>).

  The `queryPurchasesAsync(String skuType, PurchasesResponseListener listener)` method that was previously marked as deprecated has now been removed. Alternately, use [`queryPurchasesAsync(QueryPurchasesParams queryPurchasesParams, PurchasesResponseListener listener)`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,com.android.billingclient.api.PurchasesResponseListener)>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
