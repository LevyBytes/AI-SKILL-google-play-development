The [client connection](client-connection.md) supplies the `BillingClient` and listener. [Product queries](product-query.md) supply the product details used by the purchase flow.

## Launch the purchase flow

To start a purchase request from your app, call the [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchbillingflow>) method from your app's main thread. This method takes a reference to a [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) object that contains the relevant [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) object obtained from calling [`queryProductDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryproductdetailsasync)>). To create a `BillingFlowParams` object, use the [`BillingFlowParams.Builder`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder>) class.

**Kotlin**

```kotlin
// An activity reference from which the billing flow will be launched.
val activity : Activity = ...

val productDetailsParamsList = listOf(
    BillingFlowParams.ProductDetailsParams.newBuilder()
        // retrieve a value for productDetails by calling queryProductDetailsAsync()
        .setProductDetails(productDetails)
        // Get the offer token:
        // a. For one-time products, call ProductDetails.getOneTimePurchaseOfferDetailsList()
        // for a list of offers that are available to the user.
        // b. For subscriptions, call ProductDetails.getSubscriptionOfferDetails()
        // for a list of offers that are available to the user.
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

ImmutableList<BillingFlowParams.ProductDetailsParams> productDetailsParamsList =
    ImmutableList.of(
        BillingFlowParams.ProductDetailsParams.newBuilder()
             // retrieve a value for "productDetails" by calling queryProductDetailsAsync()
            .setProductDetails(productDetails)
            // Get the offer token:
            // a. For one-time products, call ProductDetails.getOneTimePurchaseOfferDetailsList()
            // for a list of offers that are available to the user.
            // b. For subscriptions, call ProductDetails.getSubscriptionOfferDetails()
            // for a list of offers that are available to the user.
            .setOfferToken(selectedOfferToken)
            .build()
    );

BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
    .setProductDetailsParamsList(productDetailsParamsList)
    .build();

// Launch the billing flow
BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);
```

The `launchBillingFlow()` method returns one of several response codes listed in [`BillingClient.BillingResponseCode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode>). Be sure to check this result to verify there were no errors launching the purchase flow. A `BillingResponseCode` of `OK` indicates a successful launch.

On a successful call to `launchBillingFlow()`, the system displays the Google Play purchase screen. Figure 1 shows a purchase screen for a subscription:

![the google play purchase screen shows a subscription that is available for purchase](<https://developer.android.com/static/images/google/play/billing/purchase-screen.png>)

**Figure 1.** The Google Play purchase screen shows a subscription that is available for purchase.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/integrate).
