   ### Upgrade from

   The following table lists the APIs that are removed in PBL 9, and the corresponding alternate APIs that you must use in your app.

   | Previously deprecated API removed | Alternate API to use |
   | --- | --- |
   | BillingClient.SkuType | [BillingClient.ProductType](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.ProductType>). The INAPP and SUBS product type constants remain functionally similar to the deprecated SKU type constants. |
   | SkuDetails | [ProductDetails](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>). This is the new data model that supports the one-time products. |
   | SkuDetailsParams | Use [QueryProductDetailsParams](<https://developer.android.com/reference/com/android/billingclient/api/QueryProductDetailsParams>) with [queryProductDetailsAsync](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)>). |
   | SkuDetailsResponseListener | Use [ProductDetailsResponseListener](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetailsResponseListener>) with [queryProductDetailsAsync](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)>). |
   | QueryPurchaseHistoryParams | Use [queryProductDetailsAsync](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)>) for active or pending purchases. Track consumed purchases on your backend servers. Use the server-side [Voided Purchases API](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.voidedpurchases>) for canceled or voided purchases. |
   | getSkuDetailsList and setSkuDetailsList | Use [BillingFlowParams.Builder.setProductDetailsParamsList](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setProductDetailsParamsList(java.util.List%3Ccom.android.billingclient.api.BillingFlowParams.ProductDetailsParams%3E)>) |
4. (Recommended) Enable automatic service reconnection.

   The Play Billing Library can attempt to automatically re-establish the service connection if an API call is made while the service is disconnected. For more information, see [Enable automatic service reconnection](<https://developer.android.com/google/play/billing/integrate#automatic-service-reconnection>).
5. Handle new sub-response codes.

   The [BillingResult](<https://developer.android.com/reference/com/android/billingclient/api/BillingResult>) returned from [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) will now include a sub-response code field. This field will only be populated in some cases to provide a more specific reason for the failure. The sub-response field can have the following values:

   - `PAYMENT_DECLINED_DUE_TO_INSUFFICIENT_FUNDS` - Returned when the user's funds are less than the price of the item they are attempting to purchase.
   - `USER_INELIGIBLE` - Returned when the user doesn't meet the configured eligibility requirements for a subscription offer.
   - `NO_APPLICABLE_SUB_RESPONSE_CODE` - The default value, returned when no other sub-response code is applicable.

   **Migration step**: Update your `PurchasesUpdatedListener` or equivalent result handling to recognize and respond to these specific sub-response codes to provide a better user experience. For example, prompt the user to fix payment methods or show a specific error message.
6. Error-code reclassification awareness.

   For instances where the Play Store app is blocked by the system (for example, in OEM-customized kids mode), the response code from PBL has changed from `ERROR` to `BILLING_UNAVAILABLE`.

   **Migration step**: Ensure your error handling logic accommodates this change and doesn't rely on receiving a generic error in these specific scenarios.

   > **Note:** For this feature to work, you need [AndroidX.core library](<https://developer.android.com/jetpack/androidx/releases/core#core_and_core-ktx_version_190_2>) version 1.9 or later.
7. Handle [`DeveloperProvidedBillingDetails.getLinkUri()`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails#getLinkUri()>) nullability.

   If you use `DeveloperProvidedBillingDetails` as part of an external payments integration, `getLinkUri()` is now `@Nullable`.

   **Migration step**: To handle this change safely, ensure your integration code handles both `null` and empty string (`""`) values from the [`DeveloperProvidedBillingDetails.getLinkUri()`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails#getLinkUri()>) method before parsing or launching browser intents. For example:

   **Kotlin**

   ```kotlin
   val linkUri = details.linkUri
   if (!linkUri.isNullOrEmpty()) {
       val intent = Intent(Intent.ACTION_VIEW, linkUri.toUri())
       context.startActivity(intent)
   }
   ```

   **Java**

   ```java
   String linkUri = details.getLinkUri();
   if (!android.text.TextUtils.isEmpty(linkUri)) {
     Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(linkUri));
     context.startActivity(intent);
   }
   ```
8. Optional changes.

   - Support pending purchases for prepaid plans. For more information, see [Handle Subscriptions and Pending Transactions](<https://developer.android.com/google/play/billing/subscriptions#pending>).
   - Virtual installment subscriptions. For more information, see [Installment Subscriptions Integration](<https://developer.android.com/google/play/billing/subscriptions#installments>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/migrate-gpblv9).
