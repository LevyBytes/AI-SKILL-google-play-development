This version-specific example depends on [the library 6 catalog and client migration](library-6-catalog-and-setup.md). Check [present eligibility](version-eligibility.md) before using an older library.

**Kotlin**

```kotlin
val productList =
    listOf(
        QueryProductDetailsParams.Product.newBuilder()
            .setProductId("up_basic_sub")
            .setProductType(BillingClient.ProductType.SUBS)
            .build()
    )

val params = QueryProductDetailsParams.newBuilder().setProductList(productList).build()

billingClient.queryProductDetailsAsync(params) {
    billingResult,
    productDetailsList ->
    // Process the result
}
```

**Java**

```java
ImmutableList<Product> productList = ImmutableList.of(Product.newBuilder()
                                            .setProductId("up_basic_sub")
                                            .setProductType(ProductType.SUBS)
                                            .build());

QueryProductDetailsParams params = QueryProductDetailsParams.newBuilder()
    .setProductList(productList)
    .build();

billingClient.queryProductDetailsAsync(
        params,
        new ProductDetailsResponseListener() {
                public void onProductDetailsResponse(BillingResult billingResult, List<ProductDetails> productDetailsList) {
                    // Process the result
                }
        }
);
```

The callback for `queryProductDetailsAsync` returns a `List<ProductDetails>`. Each `ProductDetails` item contains the information about the product (ID, title, type, and so on). The main difference is that subscription products now also contain a `List<ProductDetails.SubscriptionOfferDetails>` that contains all offers available to the user.

Because previous versions of the Play Billing Library don't support the new objects (subscriptions, base plans, offers, and so on), the new system translates each subscription SKU into a single backward-compatible base plan and offer. Available one-time purchase products are also ported to a `ProductDetails` object. The offer details of a one-time purchase product can be accessed with the `getOneTimePurchaseOfferDetails()` method.

Rarely, some devices are unable to support `ProductDetails` and `queryProductDetailsAsync()`, usually due to outdated versions of [Google Play Services](<https://support.google.com/googleplay/answer/9037938>). To ensure proper support for this scenario, call [`isFeatureSupported()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isFeatureSupported(java.lang.String)>) for the [`PRODUCT_DETAILS`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.FeatureType#PRODUCT_DETAILS>) feature before calling `queryProductDetailsAsync`. If the response is [`OK`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#OK>), the device supports the feature and you can proceed with calling `queryProductDetailsAsync()`. If the response is [`FEATURE_NOT_SUPPORTED`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#FEATURE_NOT_SUPPORTED>), you can instead request the available backward-compatible products list with [`querySkuDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener)>). To learn more about how to use the backward compatibility features, see the [subscription catalog compatibility guide](<https://developer.android.com/google/play/billing/compatibility#play_billing_library_changes>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/migrate-gpblv6).
