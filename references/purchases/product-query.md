## Show products available to buy

After you have established a connection to Google Play, you are ready to query for your available products and display them to your users.

Querying for product details is an important step before displaying your products to your users, as it returns localized product information. For subscriptions, verify your product display [follows all Play policies](<https://play.google.com/about/developer-content-policy/>).

To query for one-time product details, call the [`queryProductDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)>) method. This method can return multiple offers based on your one-time product configuration. For more information, see [Multiple purchase options and offers for one-time products](<https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers>).

To handle the result of the asynchronous operation, you must also specify a listener which implements the [`ProductDetailsResponseListener`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetailsResponseListener>) interface. You can then override [`onProductDetailsResponse`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetailsResponseListener#onProductDetailsResponse(com.android.billingclient.api.ProdctDetails.ProductDetailsResult)>), which notifies the listener when the query finishes, as shown in the following example:

**Kotlin**

```kotlin
val queryProductDetailsParams =
    QueryProductDetailsParams.newBuilder()
        .setProductList(
            listOf(
                Product.newBuilder()
                    .setProductId("product_id_example")
                    .setProductType(ProductType.SUBS)
                    .build()
            )
        )
        .build()

billingClient.queryProductDetailsAsync(queryProductDetailsParams) {
        billingResult,
        queryProductDetailsResult ->
    if (billingResult.responseCode == BillingResponseCode.OK) {
        for (productDetails in queryProductDetailsResult.productDetailsList) {
            // Process successfully retrieved product details here.
        }

        for (unfetchedProduct in queryProductDetailsResult.unfetchedProductList) {
            // Handle any unfetched products as appropriate.
        }
    }
}
```

**Java**

```java
QueryProductDetailsParams queryProductDetailsParams =
QueryProductDetailsParams.newBuilder()
    .setProductList(
        ImmutableList.of(
            Product.newBuilder()
                .setProductId("product_id_example")
                .setProductType(ProductType.SUBS)
                .build()))
    .build();

billingClient.queryProductDetailsAsync(
queryProductDetailsParams,
new ProductDetailsResponseListener() {
    public void onProductDetailsResponse(BillingResult billingResult,
            QueryProductDetailsResult queryProductDetailsResult) {
        if (billingResult.getResponseCode() == BillingResponseCode.OK) {
           for (ProductDetails productDetails : queryProductDetailsResult.getProductDetailsList()) {
             // Process successfully retrieved product details here.
           }

           for (UnfetchedProduct unfetchedProduct : queryProductDetailsResult.getUnfetchedProductList()) {
             // Handle any unfetched products as appropriate.
           }
        }
    }
}
)
```

When querying for product details, pass an instance of [`QueryProductDetailsParams`](<https://developer.android.com/reference/com/android/billingclient/api/QueryProductDetailsParams>) that specifies a list of product ID strings created in Google Play Console along with a `ProductType`. The `ProductType` can be either `ProductType.INAPP` for one-time products or `ProductType.SUBS` for subscriptions.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/integrate).
