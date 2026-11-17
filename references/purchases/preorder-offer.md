### Pre-order offer

> **EAP:** This product or feature is in the Early Access Program (EAP). Products and features in EAP are available "as is" and might have limited support. To access the EAP feature submit a request using the [One-time products EAP Interest Form](<https://docs.google.com/forms/d/e/1FAIpQLSfBsxfQg4a8uC7Ct9O4ssn121KE6l8TC4qh3ZvA5tJpFLycqw/viewform?usp=dialog>).

Pre-order lets you set up one-time products to be bought before the item is released. When a user pre-orders your product, they agree to pay for the item when the product is released, unless the user cancels the pre-order before the release date. On the release date, a buyer is charged and Play will notify them by email that the item is released.

This document describes the steps to integrate the pre-order purchase offer with the Play Billing Library (PBL).

#### Integrate pre-order offer with PBL

This section describes how to integrate the pre-order offer with the Play Billing Library (PBL). It assumes that you are familiar with the initial PBL integration steps such as, [adding the PBL dependency to your app](<https://developer.android.com/google/play/billing/integrate#dependency>), initializing the [BillingClient](<https://developer.android.com/google/play/billing/integrate#initialize>), and [connecting to Google Play](<https://developer.android.com/google/play/billing/integrate#connect_to_google_play>). This section focuses on the PBL integration aspects that are specific to the pre-order offer.

#### Launch a purchase flow for a pre-order offer

To launch a purchase flow for a pre-order offer, do the following steps:

1. Fetch the pre-order offer metadata by using the `ProductDetails.oneTimePurchaseOfferDetails.getPreorderDetails()` method. The following sample shows how to get the pre-order offer metadata:

   #### Java

   ```java
   billingClient.queryProductDetailsAsync(
   queryProductDetailsParams,
   new ProductDetailsResponseListener() {
     public void onProductDetailsResponse(
         BillingResult billingResult, QueryProductDetailsResult productDetailsResult) {
       // check billingResult
       // …
       // process productDetailsList returned by QueryProductDetailsResult
       for (ProductDetails productDetails : productDetailsResult.getProductDetailsList()) {
         for (OneTimePurchaseOfferDetails oneTimePurchaseOfferDetails :
             productDetails.getOneTimePurchaseOfferDetailsList()) {
           // Checks if the offer is a preorder offer.
           if (oneTimePurchaseOfferDetails.getPreorderDetails() != null) {
             // process the returned PreorderDetails
             OneTimePurchaseOfferDetails.PreorderDetails preorderDetails =
                 oneTimePurchaseOfferDetails.getPreorderDetails();
             // Get preorder release time in millis.
             long preorderReleaseTimeMillis = preorderDetails.getPreorderReleaseTimeMillis();
             // Get preorder presale end time in millis.
             long preorderPresaleEndTimeMillis = preorderDetails.getPreorderPresaleEndTimeMillis();
             // Get offer ID
               String offerId = oneTimePurchaseOfferDetails.getOfferId();
             // Get the associated purchase option ID
             if (oneTimePurchaseOfferDetails.getPurchaseOptionId() != null) {
               String purchaseOptionId = oneTimePurchaseOfferDetails.getPurchaseOptionId();
             }
           }
         }
       }
     }
   });
   ```
2. Launch the billing flow.

   To start a purchase request from your app, call the `launchBillingFlow()` method from your app's main thread. This method takes a reference to a [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) object that contains the relevant [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) object obtained from calling queryProductDetailsAsync(). To create a [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) object, use the `BillingFlowParams.Builder class`. Note that you must set the offer token corresponding to the offer selected by the user when creating the [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) object. If a user is eligible for the pre-order offer, they will receive an offer with PreorderDetails and offerId in the `queryProductDetailsAsync()` method.

   The following sample shows how to launch the billing flow:

   #### Java

   ```java
   // An activity reference from which the billing flow will launch.
   Activity activity = ...;
   ImmutableList productDetailsParamsList =
       ImmutableList.of(
       ProductDetailsParams.newBuilder()
            // retrieve a value for productDetails by calling queryProductDetailsAsync()
           .setProductDetails(productDetails)
           // to get an offer token, call
           // ProductDetails.getOneTimePurchaseOfferDetailsList() for a list of offers
           // that are available to the user
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
