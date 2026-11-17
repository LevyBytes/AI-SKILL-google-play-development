2. Launch the billing flow.

   To start a purchase request from your app, call the [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchbillingflow>) method from your app's main thread. This method takes a reference to a [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) object that contains the relevant [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) object obtained from calling [`queryProductDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)>). To create a [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) object, use the `BillingFlowParams.Builder` class. Note that you must set the offer token corresponding to the offer selected by the user when creating the [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) object. If a user is eligible for the rent purchase option, they will receive an offer with RentalDetails and offerId in [`queryProductDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)>).

   The following sample shows how to launch the billing flow:

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

   The `offerToken` can be found as part of the `OneTimePurchaseOfferDetails`. When you show the offer to the user, make sure you configure the billing flow parameters with the correct offer token which you can get from the `oneTimePurchaseOfferDetails.getOfferToken()` method.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers).
