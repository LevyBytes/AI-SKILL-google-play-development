This version-specific example depends on [the library 6 catalog and client migration](library-6-catalog-and-setup.md). Check [present eligibility](version-eligibility.md) before using an older library.

### Show products available to buy

To obtain all offers a user is eligible to purchase:

- Replace `SkuDetailsParams` with `QueryProductDetailsParams`
- Switch the `BillingClient.querySkuDetailsAsync()` call to use `BillingClient.queryProductDetailsAsync()`

Note that query results are now `ProductDetails` instead of `SkuDetails`. Each `ProductDetails` item contains the information about the product (ID, title, type, and so on). For subscription products, `ProductDetails` contains a `List<ProductDetails.SubscriptionOfferDetails>`, which is the list of the subscription offer details. For one-time purchase products, `ProductDetails` contains a `ProductDetails.OneTimePurchaseOfferDetails`. These can be used to decide which offers to show to the users.

The following example shows how your app might look before and after making these changes:

**Before**

**Kotlin**

```kotlin
val skuList = ArrayList<String>()

skuList.add("up_basic_sub")

val params = SkuDetailsParams.newBuilder()

params.setSkusList(skuList).setType(BillingClient.SkuType.SUBS).build()

billingClient.querySkuDetailsAsync(params) {
    billingResult,
    skuDetailsList ->
    // Process the result
}
```

**Java**

```java
List<String> skuList = new ArrayList<>();

skuList.add("up_basic_sub");

SkuDetailsParams.Builder params = SkuDetailsParams.newBuilder();

params.setSkusList(skuList).setType(SkuType.SUBS).build();

billingClient.querySkuDetailsAsync(params,
    new SkuDetailsResponseListener() {
        @Override
        public void onSkuDetailsResponse(BillingResult billingResult,
                List<SkuDetails> skuDetailsList) {
            // Process the result.
        }
    }
);
```

**After**

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/migrate-gpblv6).
