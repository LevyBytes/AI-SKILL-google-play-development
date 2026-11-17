### Query with Kotlin extensions

If you're [using Kotlin extensions](<https://developer.android.com/google/play/billing/integrate?hl=en#dependency>), you can query for one-time product details by calling the `queryProductDetails()` extension function.

`queryProductDetails()` leverages Kotlin coroutines so that you don't need to define a separate listener. Instead, the function suspends until the querying completes, after which you can process the result:

```kotlin
suspend fun processPurchases() {
    val productList = listOf(
        QueryProductDetailsParams.Product.newBuilder()
            .setProductId("product_id_example")
            .setProductType(BillingClient.ProductType.SUBS)
            .build()
    )
    val params = QueryProductDetailsParams.newBuilder()
    params.setProductList(productList)

    // leverage queryProductDetails Kotlin extension function
    val productDetailsResult = withContext(Dispatchers.IO) {
        billingClient.queryProductDetails(params.build())
    }

    // Process the result.
}
```

Rarely, some devices are unable to support `ProductDetails` and `queryProductDetailsAsync()`, usually due to outdated versions of [Google Play Services](<https://support.google.com/googleplay/answer/9037938>). To provide proper support for this scenario, learn how to use backwards compatibility features in the [Play Billing Library 7 migration guide](<https://developer.android.com/google/play/billing/migrate-gpblv7#showing-products>).

### Process the result

The Google Play Billing Library stores the query results in a [`QueryProductDetailsResult`](<https://developer.android.com/reference/com/android/billingclient/api/QueryProductDetailsResult>) object. [`QueryProductDetailsResult`](<https://developer.android.com/reference/com/android/billingclient/api/QueryProductDetailsResult>) contains a `List` of [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) objects. You can then call a variety of methods on each `ProductDetails` object in the list to view relevant information about a successfully fetched one-time product, such as its price or description. To view the available product detail information, see the list of methods in the [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) class.

[`QueryProductDetailsResult`](<https://developer.android.com/reference/com/android/billingclient/api/QueryProductDetailsResult>) also contains a `List` of [`UnfetchedProduct`](<https://developer.android.com/reference/com/android/billingclient/api/UnfetchedProduct>) objects. You can then query each UnfetchedProduct to get a status code corresponding to the fetch failure reason. To view the available unfetched product information, see the list of methods in the [`UnfetchedProduct`](<https://developer.android.com/reference/com/android/billingclient/api/UnfetchedProduct>) class.

Before offering an item for sale, check that the user does not already own the item. If the user has a consumable that is still in their item library, they must consume the item before they can buy it again.

Before offering a subscription, verify that the user is not already subscribed. Also note the following:

- For subscriptions, the `queryProductDetailsAsync()` method returns subscription product details and a maximum of 50 user eligible offers per subscription. If the user attempts to purchase an ineligible offer (for example, if the app is displaying an outdated list of eligible offers), Play informs the user that they are ineligible, and the user can choose to purchase the base plan instead.
- For one-time products, the `queryProductDetailsAsync()` method returns only the user eligible offers. If the user attempts to purchase an offer for which they're ineligible (for example, if the user has reached the purchase quantity limit), Play informs the user that they are ineligible, and the user can choose to purchase its purchase option offer instead.

> **Note:** Caching [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) objects is **not** recommended, as stale objects can cause [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchbillingflow>) failures.

> **Note:** Some Android devices might have an older version of the Google Play Store app that doesn't support certain products types, such as subscriptions. Before your app enters the billing flow, you can call [`isFeatureSupported()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isfeaturesupported>) to determine whether the device supports the products you want to sell. For a list of product types that can be supported, see [`BillingClient.FeatureType`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.FeatureType>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/integrate).
