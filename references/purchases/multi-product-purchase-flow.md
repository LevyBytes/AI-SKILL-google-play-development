This document describes how you can integrate your app with the multi-product feature of Play Billing Library (PBL).

The multi-product for one-time product (OTP) feature lets you combine several one-time products into a single unit. These bundled products can then be purchased, billed, and managed collectively. You can also create [discount offers](<https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers#discount-offers>) for these bundled OTPs to incentivize product purchases.

## Considerations

When you create one-time product bundles, note the following considerations:

- You can't have subscriptions in a one-time product bundle.
- You can't have a combination of digital content and service in the same one-time product bundle.
- The bundled one-time products must be available for immediate download. For example, a one-time product bundle can't have a pre-order purchase because it's not available for immediate download.
- The multi-product for one-time products doesn't support the [rent purchase option](<https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers#rent-option>).

## Integrate with Play Billing Library

This section assumes that you are familiar with the initial PBL integration steps such as, [adding the PBL dependency to your app](<https://developer.android.com/google/play/billing/integrate#dependency>), initializing the [BillingClient](<https://developer.android.com/google/play/billing/integrate#initialize>), and [connecting to Google Play](<https://developer.android.com/google/play/billing/integrate#connect-to-play>). This section focuses on the PBL integration aspects that are specific to the multi-product OTP purchases.

### Launch a purchase flow

To launch a purchase flow for multi-product one-time products, do the following steps:

1. Create a product list having all the one-time products by using the [QueryProductDetailsParams.Builder.setProductList](<https://developer.android.com/reference/com/android/billingclient/api/QueryProductDetailsParams.Builder#setProductList(java.util.List%3Ccom.android.billingclient.api.QueryProductDetailsParams.Product%3E)>) method.
2. Fetch all your one-time products by using the [`BillingClient.queryProductDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)>) method.

   The following sample shows how to fetch all your one-time products:

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
       ImmutableList productDetailsList = productDetailsResult.getProductDetailsList();
       for (ProductDetails productDetails : productDetailsList) {
         for (OneTimePurchaseOfferDetails oneTimePurchaseOfferDetails :
             productDetails.getOneTimePurchaseOfferDetailsList()) {
                // …
         }
       }
     }
   });
   ```
3. Set the [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams.Builder#setProductDetails(com.android.billingclient.api.ProductDetails)>) object for each one-time product.

   > **Note:** All one-time products in the `ProductDetails` must be from the same app.
4. Specify the one-time product details in the [`BillingFlowParams.Builder.setProductDetailsParamsList`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setProductDetailsParamsList(java.util.List%3Ccom.android.billingclient.api.BillingFlowParams.ProductDetailsParams%3E)>) method. The [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) class specifies the details of a purchase flow.

   The following sample shows how to launch the billing flow for a multi-product OTP purchase:

   #### Java

   ```java
   BillingClient billingClient =
      BillingClient.newBuilder()
       // set other options
       .build();
   // ProductDetails obtained from queryProductDetailsAsync().
   ProductDetails productDetails1 = ...;
   ProductDetails productDetails2 = ...;
   ArrayList productDetailsList = new ArrayList<>();
   productDetailsList.add(productDetails1);
   productDetailsList.add(productDetails2);
   BillingFlowParams billingFlowParams =
   BillingFlowParams.newBuilder()
       .setProductDetailsParamsList(productDetailsList)
       .build();
   billingClient.launchBillingFlow(billingFlowParams);
   ```

   > **Note:** An in-app purchase will still be represented by the [`Purchase`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase>) object, but this object will also be associated with all the products acquired in the transaction.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/multi-product-for-one-time-product).
