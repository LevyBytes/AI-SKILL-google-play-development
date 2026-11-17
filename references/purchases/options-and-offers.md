This document details the integration of your one-time products (OTPs) with the Play Billing Library. It further explains how to integrate various purchase options and offers related to your one-time products.

You can configure multiple purchase options and offers for your one-time products. For example, you can configure a buy purchase option and a pre-order offer for the same one-time product.

## Prerequisites

To configure multiple offers for one-time products, you must use the [`queryProductDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)>) API. The deprecated `querySkuDetailsAsync()` API isn't supported. For information on how to use [`queryProductDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)>) and the version of [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,%20com.android.billingclient.api.BillingFlowParams)>) that takes [`ProductDetailsParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams>) as input, see [migration steps](<https://developer.android.com/google/play/billing/migrate-gpblv6#steps>).

## Query the product details

If you have configured multiple offers or purchase options for your one-time product, the [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) object returned by the [`queryProductDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)>) method can have more than one available buy and (or) rent purchase option per one-time product. To get the list of all the eligible offers for each [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) object, use the `getOneTimePurchaseOfferDetailsList()` method. Only offers and purchase options for which the user is eligible will be returned as part of this list. Your code in the [`onProductDetailsResponse()`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetailsResponseListener#onProductDetailsResponse(com.android.billingclient.api.ProdctDetails.ProductDetailsResult)>) method should handle the returned offers.

> **Note:** If you continue to call the `getOneTimePurchaseOfferDetails()` method instead of the new `getOneTimePurchaseOfferDetailsList()` method, the backwards compatible purchase option offer is returned instead of all the eligible offers. By default, the first created buy purchase option is considered as backward compatible. However, if a backward compatible offer isn't available, the `QueryProductDetailsResult` will have an `UnfetchedProduct` object that has original requested product ID, product type, and the status code as `NO_ELIGIBLE_OFFER`.

## Launch the billing flow

To start a purchase request from your app, call the [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchbillingflow>) method from your app's main thread. This method takes a reference to a [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) object that contains the relevant [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) object obtained from calling [`queryProductDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)>). To create a [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) object, use the [`BillingFlowParams.Builder`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder>) class. Note that you must set the offer token corresponding to the offer selected by the user when creating the [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) object.

The following sample shows how to launch the purchase flow for a one-time product with multiple offers:

#### Java

```java
    
// An activity reference from which the billing flow will launch.
Activity activity = ...;
ImmutableList<ProductDetailsParams> productDetailsParamsList =
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

## Purchase options and offers

A purchase option lets you define how the entitlement is granted to a user, its price, and in which region the product is available. A single product can have multiple purchase options, which can represent where and how you sell your product.

Google Play supports the following purchase options for one-time products:

- Buy purchase option
- Rent purchase option

Offers refer to a pricing scheme that you can create for your one-time products. For example, you can create a discount offer for your one-time product.

Google Play supports the following purchase offers for one-time products:

- Pre-order offer (supported only for the buy purchase option)
- Discount offer (supported for both buy and rent purchase options)

### Buy purchase option

A buy purchase option represents a standard, outright purchase of the one-time product. It has an optional legacyCompatible field, indicating whether this purchase option will be available in older Play Billing Library (version 7 or older) flows that don't support the new model. For backwards compatibility, at least one buy purchase option should be marked as legacy compatible.

The steps for integrating both the buy and the rent purchase options with PBL are the same. To understand how to integrate the buy purchase option with PBL, see [Integrate rent purchase option with PBL](<https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers?hl=en#integrate-pbl>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers).
