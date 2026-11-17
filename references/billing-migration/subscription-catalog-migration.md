[Google Play's billing system](<https://developer.android.com/google/play/billing>) sells digital products and content in Android apps. The transition to base plans and offers changed subscription product definitions, in-app selling and backend management. New integrations should begin with [Getting ready](<https://developer.android.com/google/play/billing/getting-ready>).

For integrations built on the legacy subscription model, adopt base-plan and offer features while preserving existing subscriptions.

At the base-plan and offer transition, existing subscriptions, apps and backend integrations continued functioning without immediate migration changes. The new model could be adopted incrementally. Each major [Google Play Billing Library](<https://developer.android.com/reference/com/android/billingclient/classes>) release has a two-year support period; check the [current version and API deprecation requirements](<https://developer.android.com/google/play/billing/deprecation-faq>) before shipping. The original compatibility guarantee does not extend a deprecated API's shutdown cutoff.

The base-plan and offer model changes these parts of the integration:

- The new [**Google Play Console**](<https://play.google.com/console>) lets you create and manage subscriptions, base plans, and offers. This includes both new and migrated subscriptions.
- The [**Play Developer API**](<https://developers.google.com/android-publisher>) contains updates to support new Google Play Console UI functionality in API form. Notably, there is a new version of the [**Subscription Purchases API**](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>). Use this API to check subscription status and manage subscription purchases.
- The new [**Play Billing Library version 5**](<https://developer.android.com/google/play/billing/release-notes>) lets your app benefit from all the new subscription features. When you're ready to upgrade to version 5, follow the guidance in the [migration guide](<https://developer.android.com/google/play/billing/migrate-gpblv5>).

## Subscriptions configuration

### Managing subscriptions using Google Play Console

The base-plan and offer model changes how subscriptions appear in Google Play Console.

A single subscription can now have multiple base plans and offers. Previously-created subscription SKUs now appear in the Play Console as these new subscription, base plan, and offer objects. If you haven't already, see [Recent changes to subscriptions in Play Console](<https://support.google.com/googleplay/android-developer/answer/12124625>) for descriptions of the new objects, including their functionality and configuration. All of your pre-existing subscription products appear in the Google Play Console in this new format. Each SKU is now represented by a subscription object that contains a single base plan and backward-compatible offer, if applicable.

Since older integrations expected each subscription to include a single offer, represented by a [`SkuDetails`](<https://developer.android.com/reference/com/android/billingclient/api/SkuDetails>) object, each subscription can have a single backward-compatible base plan or offer. The backward-compatible base plan or offer is returned as part of a SKU for apps that are using the now-deprecated `querySkuDetailsAsync()` method. For more information on configuring and managing backward-compatible offers, see [Understand subscriptions](<https://support.google.com/googleplay/android-developer/answer/12154973>). After your app is using only `queryProductDetailsAsync()`, and after there are no earlier versions of your app still making purchases, you no longer need to use a backward-compatible offer.

### Managing subscriptions using Subscriptions Publishing API

The [Play Developer API](<https://developers.google.com/android-publisher#subscriptions>) contains new functionality for subscription purchases. The [`inappproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts>) API for SKU management continues to work as before, including handling one-time purchase products and subscriptions, so you don't need to make any immediate changes to maintain your integration.

However, it's important to note that the Google Play Console uses only the new subscription entities. **After you start editing your subscriptions in the Console, the [`inappproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts>) API can no longer be used for subscriptions**.

If your publishing integration uses the legacy subscription product model, converted subscriptions appear read-only in Google Play Console to protect existing integrations, and edits can produce a warning. Before editing those subscriptions in the Console, you should migrate the backend to the new publishing endpoints. [`monetization.subscriptions`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions>), [`monetization.subscriptions.basePlans`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans>) and [`monetization.subscriptions.basePlans.offers`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers>) manage subscriptions, base plans and offers. The following table maps `InAppProduct` fields to the new objects under `monetization.subscriptions`.

| InAppProduct | Subscription |
| --- | --- |
| `packageName` | `packageName` |
| `sku` | `productId` |
| `status` | `basePlans[0].state` |
| `prices` | basePlans[0].regionalConfigs.price |
| `listings` | listings |
| `defaultPrice` | No equivalence |
| `subscriptionPeriod` | basePlans[0].autoRenewingBasePlanType.billingPeriodDuration |
| `trialPeriod` | basePlans[0].offers[0].phases[0].regionalConfigs[0].free |
| `gracePeriod` | basePlans[0].autoRenewingBasePlanType.gracePeriodDuration |
| `subscriptionTaxesAndComplianceSettings` | taxAndComplianceSettings |

This required API update only applies to the Publishing API (SKU management).

## Play Billing Library changes

To support gradual migration, the Play Billing Library includes all the methods and objects available in previous versions. [`SkuDetails`](<https://developer.android.com/reference/com/android/billingclient/api/SkuDetails>) objects and functions like [`querySkuDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener)>) still exist so you can upgrade to use [new functionality](<https://developer.android.com/google/play/billing/migrate-gpblv5>) without having to also immediately update existing subscriptions code. You can also control which offers are available through these methods by marking them as backward-compatible.

In addition to keeping legacy methods, Play Billing Library 5 now includes a new `ProductDetails` object and a corresponding `queryProductDetailsAsync()` method to handle new entities and functionality. Existing in-app products (one-time purchases and consumables) are now also supported by `ProductDetails`.

For a subscription, `ProductDetails.getSubscriptionOfferDetails()` returns a list of all base plans and offers the user is eligible to purchase. This means that you can access all base plans and offers eligible for the user, regardless of backward-compatibility. `getSubscriptionOfferDetails()` returns `null` for non-subscription products. For one-time purchases, you can use `getOneTimePurchaseOfferDetails()`.

Play Billing Library 5 also includes both new and legacy methods for launching the purchase flow. If the `BillingFlowParams` object passed to [`BillingClient.launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,%20com.android.billingclient.api.BillingFlowParams)>) is configured using a `SkuDetails` object, the system extracts the offer information to sell from the backward-compatible base plan or offer that corresponds to the SKU. If the `BillingFlowParams` object passed to `BillingClient.launchBillingFlow()` is configured using `ProductDetailsParams` objects, which include `ProductDetails` and a `String` representing the specific offer token for the offer being purchased, the system then uses that information to identify the product being acquired by the user.

`queryPurchasesAsync()` returns all purchases owned by the user. To indicate the requested product type, you can pass in a `BillingClient.SkuType` value, as in earlier versions, or a `QueryPurchasesParams` object that contains a `BillingClient.ProductType` value that represents the new subscription entities.

We recommend [updating your apps](<https://developer.android.com/google/play/billing/migrate-gpblv5>) to version 5 of the library soon so you can start taking advantage of these new subscription features.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/compatibility).
