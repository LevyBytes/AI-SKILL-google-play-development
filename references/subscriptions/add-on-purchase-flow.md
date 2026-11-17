Subscription with add-ons lets you bundle multiple subscription products together that can be purchased, billed and managed together. Your existing product catalog subscriptions can be seamlessly offered as add-ons without any upfront specification or additional configuration. You can launch a purchase flow with multiple existing subscription products, and sell them as add-ons.

## Considerations

Consider the following points when using the subscription with add-ons feature:

- Subscription with add-ons is only supported for auto renewing base plans.
- All items in the purchase must have the same recurring billing period. For example, you can't have an annually billed subscription with monthly billed add-ons.
- You can have a maximum of 50 items in a subscription with add-ons purchase.
- This feature isn't available in South Korea (*KR*).

## Integrate with Play Billing Library

This section describes how to integrate the subscription with add-ons feature with the Play Billing Library (PBL). It assumes that you are familiar with the initial PBL integration steps such as, [adding the PBL dependency to your app](<https://developer.android.com/google/play/billing/integrate#dependency>), initializing the [BillingClient](<https://developer.android.com/google/play/billing/integrate#initialize>), and [connecting to Google Play](<https://developer.android.com/google/play/billing/integrate#connect-to-play>). This section focuses on the PBL integration aspects that are specific to subscription with add-ons.

### Launch a purchase flow

To launch a purchase flow for a subscription with add-ons, do the following steps:

1. Fetch all your subscription items by using the [`BillingClient.queryProductDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)>) method.
2. Set the [`ProductDetailsParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams#newBuilder()>) object for each item.

   The item represented by the [`ProductDetailsParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams#newBuilder()>) object, specifies both the [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) indicating the subscription item, and an [`offerToken`](<https://developer.android.com/google/play/billing/subscriptions>) selecting a specific subscription [`base plan`](<https://developer.android.com/google/play/billing/subscriptions>) or [`offer`](<https://developer.android.com/google/play/billing/subscriptions>).

   > **Note:** All items in the `ProductDetails` must be from the same app.
3. Specify the item details in the [`BillingFlowParams.Builder.setProductDetailsParamsList`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setProductDetailsParamsList(java.util.List%3Ccom.android.billingclient.api.BillingFlowParams.ProductDetailsParams%3E)>) method. The [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) class specifies the details of a purchase flow.

   > **Note:** The first item in the list is referred to as the base item, and the remaining items are referred to as add-ons. And every item in this list must be unique. In other words, you can't set two [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>) with the same [`productId`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails#getProductId()>) in the list.

   The following sample shows how to launch the billing flow for a subscription purchase with multiple items:

   #### Java

   ```java
      BillingClient billingClient = …;

       // ProductDetails obtained from queryProductDetailsAsync().
       ProductDetailsParams productDetails1 = ...;
       ProductDetailsParams productDetails2 = ...;
       ArrayList productDetailsList = new ArrayList<>();
       productDetailsList.add(productDetails1);
       productDetailsList.add(productDetails2);

       BillingFlowParams billingFlowParams =
           BillingFlowParams.newBuilder()
              .setProductDetailsParamsList(productDetailsList)
              .build();
       billingClient.launchBillingFlow(billingFlowParams);
   ```

   > **Note:** An in-app purchase will still be represented by the [`Purchase`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase>) object. And the [`getProducts()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getProducts()>) method returns entitlements for all the items the user has from this purchase.

#### Rules applicable for items in the purchase

- To ensure add-on renewal dates eventually align with the base item, Google Play may insert a prorated charge after any trial or intro pricing phases.
- [Offer eligibility](<https://support.google.com/googleplay/android-developer/answer/12154973>) will be evaluated separately for each item.

## Process purchases

Processing subscription with add-ons is the same as processing of a single subscription purchase as described in [Integrate the Google Play Billing Library into your app](<https://developer.android.com/google/play/billing/integrate#launch>). The only difference is that the user can receive multiple entitlements with a single purchase. A purchase of subscription with add-ons returns multiple items which can be retrieved using [`Purchase.getProducts()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getProducts>) in the Google Play Billing Library, and then the `lineItems` list in [`purchases.subscriptionsv2.get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) of the [Google Play Developer API](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>).

> **Note:** For each call of the [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) API, there is a limit of 50 items (active items + new items). If the cart contains more than 50 items, Google Play blocks the purchase flow.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscription-with-addons).
