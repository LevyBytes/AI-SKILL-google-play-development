### Rent purchase option

The rent purchase option lets users access the one-time products for a specified time duration. You can specify the rental period and it's expiration. This document describes the steps to integrate the rent purchase option with the Play Billing Library (PBL).

> **Note:** You must grant user entitlement for your one-time products available on rent. For more information, see [Grant entitlement to the user](<https://developer.android.com/google/play/billing/integrate#granting-entitlement>).

#### Integrate rent purchase option with PBL

This section describes how to integrate the rent purchase option with the Play Billing Library (PBL). It assumes that you are familiar with the initial PBL integration steps such as, [adding the PBL dependency to your app](<https://developer.android.com/google/play/billing/integrate#dependency>), initializing the [BillingClient](<https://developer.android.com/google/play/billing/integrate#initialize>), and [connecting to Google Play](<https://developer.android.com/google/play/billing/integrate#connect_to_google_play>). This section focuses on the PBL integration aspects that are specific to the rent purchase option.

To configure products available for rent, you will need to use the new `monetization.onetimeproducts` service of the Play Developer API or the Play Developer Console UI. To use the service, you can call the REST API directly, or use the [Java client library](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient>).

#### Launch a purchase flow for the rent option

To launch a purchase flow for a rental offer, do the following steps:

1. Fetch the rent purchase option metadata by using the `ProductDetails.oneTimePurchaseOfferDetails.getRentalDetails()` method.

   The following sample shows how to get the rent purchase metadata:

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
           // Checks if the offer is a rent purchase option.
           if (oneTimePurchaseOfferDetails.getRentalDetails() != null) {
             // process the returned RentalDetails
             OneTimePurchaseOfferDetails.RentalDetails rentalDetails =
                 oneTimePurchaseOfferDetails.getRentalDetails();
             // Get rental period in ISO 8601 format.
             String rentalPeriod = rentalDetails.getRentalPeriod();
             // Get rental expiration period in ISO 8601 format, if present.
             if (rentalDetails.getRentalExpirationPeriod() != null) {
               String rentalExpirationPeriod = rentalDetails.getRentalExpirationPeriod();
             }
             // Get offer token
               String offerToken = oneTimePurchaseOfferDetails.getOfferToken();
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

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers).
