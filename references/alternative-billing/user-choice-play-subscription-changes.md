The [program-specific client setup](user-choice-client-and-launch.md) establishes the connection and eligibility checks for this flow.

#### Subscriptions bought through Google Play's billing system

Similarly, users that bought their current subscription through Google Play's billing system after user choice should be shown the [upgrade or downgrade flow in Google Play's billing system](<https://developer.android.com/google/play/billing/subscriptions#change>). The following instructions describe how you would launch the purchase flow for an upgrade or downgrade through Google Play's billing system:

1. Identify the `offerToken` of the selected offer for the new plan:

   **Kotlin**

   ```kotlin
   val offerTokenNewPlan = productDetailsNewPlan.getSubscriptionOfferDetails()
       ?.getOrNull(selectedOfferIndex)
       ?.offerToken
       ?: ""
   ```

   **Java**

   ```java
   String offerTokenNewPlan = productDetailsNewPlan
           .getSubscriptionOfferDetails(selectedOfferIndex)
           .getOfferToken();
   ```
2. Send the correct information to Google Play's billing system to process the new purchase, including the purchase token for the existing subscription:

   **Kotlin**

   ```kotlin
   val billingFlowParams =
       BillingFlowParams.newBuilder()
           .setProductDetailsParamsList(
               listOf(
                   BillingFlowParams.ProductDetailsParams.newBuilder()
                       // Fetched using queryProductDetailsAsync
                       .setProductDetails(productDetailsNewPlan)
                       .setSubscriptionProductReplacementParams(
                           SubscriptionProductReplacementParams.newBuilder()
                               .setReplacementMode(
                                   SubscriptionProductReplacementParams.ReplacementMode.CHARGE_FULL_PRICE
                               )
                               .setOldProductId("old_product_id")
                               .build()
                       )
                       // offerIdToken can be found in
                       // ProductDetails=>SubscriptionOfferDetails.
                       .setOfferToken(offerTokenNewPlan)
                       .build()
               )
           )
           .setSubscriptionUpdateParams(
               BillingFlowParams.SubscriptionUpdateParams.newBuilder()
                   // purchaseToken can be found in
                   // Purchase#getPurchaseToken
                   .setOldPurchaseToken(oldToken)
                   .build()
           )
           .build()

   val billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)
   ```

   **Java**

   ```java
   BillingFlowParams billingFlowParams =
       BillingFlowParams.newBuilder()
           .setProductDetailsParamsList(
               ImmutableList.of(
                   ProductDetailsParams.newBuilder()
                       // Fetched using queryProductDetailsAsync
                       .setProductDetails(productDetailsNewPlan)
                       // offerIdToken can be found in
                       // ProductDetails=>SubscriptionOfferDetails.
                       .setOfferToken(offerTokenNewPlan)
                       .build()
               )
           )
           .setSubscriptionUpdateParams(
               SubscriptionUpdateParams.newBuilder()
                   // purchaseToken can be found in
                   // Purchase#getPurchaseToken
                   .setOldPurchaseToken(oldToken)
                   .setReplaceProrationMode(BillingFlowParams.ProrationMode.IMMEDIATE_AND_CHARGE_FULL_PRICE)
                   .build()
           )
           .build();

   BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);
   ```

This purchase proceeds in Google Play's billing system, and your app receives the `PurchasesUpdatedListener.onPurchaseUpdated` call with the result of the purchase. If the purchase was successful, the `onPurchaseUpdated()` method also receives the new purchase information, and your backend receives a `SUBSCRIPTION_PURCHASED` Real Time Developer Notification. When pulling the status for the new purchase, a `linkedPurchaseToken` attribute links to the old subscription purchase so that you can retire it [as recommended](<https://medium.com/androiddevelopers/implementing-linkedpurchasetoken-correctly-to-prevent-duplicate-subscriptions-82dfbf7167da>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app).
