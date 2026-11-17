This version-specific example depends on [the library 6 catalog and client migration](library-6-catalog-and-setup.md). Check [present eligibility](version-eligibility.md) before using an older library.

### Launch the offer purchase flow

Launching a purchase flow for an offer is very similar to launching a flow for a SKU. To start a purchase request using version 6, do the following:

- Instead of using `SkuDetails` for `BillingFlowParams`, use `ProductDetailsParams`.
- The offer details, such as offer ID, base plan ID, and more can be obtained using the `SubscriptionOfferDetails` object.

To purchase a product with the user's selected offer, get the `offerToken` of the selected offer and pass it into the `ProductDetailsParams` object.

Once you've created a `BillingFlowParams` object, launching the billing flow with the `BillingClient` remains the same.

The following example shows how your app might look before and after making these changes:

**Before**

**Kotlin**

```kotlin
// An activity reference from which the billing flow will be launched.
val activity : Activity = ...
// Retrieve a value for "skuDetails" by calling querySkuDetailsAsync().
val billingFlowParams = BillingFlowParams.newBuilder()
                            .setSkuDetails(skuDetails)
                            .build()

val billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)
```

**Java**

```java
// An activity reference from which the billing flow will be launched.
Activity activity = ...;
// Retrieve a value for "skuDetails" by calling querySkuDetailsAsync().
BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
        .setSkuDetails(skuDetails)
        .build();

BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)
```

**After**

**Kotlin**

```kotlin
// An activity reference from which the billing flow will be launched.
val activity : Activity = ...;

val productDetailsParamsList = listOf(
    BillingFlowParams.ProductDetailsParams.newBuilder()
        // retrieve a value for "productDetails" by calling queryProductDetailsAsync()
        .setProductDetails(productDetails)
        // For One-time product, "setOfferToken" method shouldn't be called.
        // For subscriptions, to get the offer token corresponding to the selected
        // offer call productDetails.subscriptionOfferDetails?.get(selectedOfferIndex)?.offerToken
        .setOfferToken(selectedOfferToken)
        .build()
)

val billingFlowParams = BillingFlowParams.newBuilder()
    .setProductDetailsParamsList(productDetailsParamsList)
    .build()

// Launch the billing flow
val billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)
```

**Java**

```java
// An activity reference from which the billing flow will be launched.
Activity activity = ...;

ImmutableList<ProductDetailsParams> productDetailsParamsList =
    ImmutableList.of(
        ProductDetailsParams.newBuilder()
             // retrieve a value for "productDetails" by calling queryProductDetailsAsync()
            .setProductDetails(productDetails)
            // For one-time products, "setOfferToken" method shouldn't be called.
            // For subscriptions, to get the offer token corresponding to the selected
            // offer call productDetails.getSubscriptionOfferDetails().get(selectedOfferIndex).getOfferToken()
            .setOfferToken(selectedOfferToken)
            .build()
    );

BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
    .setProductDetailsParamsList(productDetailsParamsList)
    .build();

// Launch the billing flow
BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/migrate-gpblv6).
