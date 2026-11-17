This document describes how to migrate from Google Play Billing Library 4 or 5 to Google Play Billing Library 6 and how to use new subscription capabilities.

For a full list of the changes in version 6.0.0, refer to the [release notes](<https://developer.android.com/google/play/billing/release-notes>).

## Overview

Google Play Billing Library 6 builds on the new subscription features introduced in version 5 and adds a few more improvements. These features allow you to sell subscriptions in more ways, reducing operational costs by eliminating the need to create and manage an ever-increasing number of SKUs.

For more information about the new features introduced with Play Billing Library 5, see [Recent changes to subscriptions in Play Console](<https://support.google.com/googleplay/android-developer/answer/12124625>).

## Backward-compatible Play Billing Library upgrade

Existing subscription products were automatically converted to the base-plan and offer model introduced with Play Billing Library 5. Those converted products already provide a catalog compatible with the newer library model, so no subscription product configuration change is required just to establish that compatibility. For conversion details, see *Working with older subscriptions* in the [Play Console Help article](<https://support.google.com/googleplay/android-developer/answer/12124625>).

### Previous versions of your app still work

If you have a backward-compatible subscription catalog, all existing versions of your app should still work as intended for those products. One-time product purchases should also continue working without issues in previous versions.

Versions of your app using deprecated methods (for example, [`querySkuDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener)>)) won't be able to sell any base plans or offers that are not backward compatible. You can read about backward-compatible offers in the relevant [Play Console Help Center article](<https://support.google.com/googleplay/android-developer/answer/12124625>).

### Upgrade to Play Billing Library 5 or 6

Play Billing Library 5 and 6 include the deprecated methods `querySkuDetailsAsync` and `BillingFlowParams.Builder.setSkuDetails` that takes [`SkuDetails`](<https://developer.android.com/reference/com/android/billingclient/api/SkuDetails>) as a billing flow parameter. This means that you can gradually move to Play Billing Library 6 by planning different stages of migration.

As a first step to migration, you can just [update the library version](<https://developer.android.com/google/play/billing/migrate-gpblv6?hl=en#update-google>), leave your catalog and backend as they are, and test your app while it still uses the deprecated methods. If you are not using `queryPurchases`, `launchPriceChangeFlow`, or `setVrPurchaseFlow`, it should still work as intended. Afterwards, you can iterate to fully adopt the [base-plan and offer subscription features](<https://developer.android.com/google/play/billing/compatibility>).

If you have previously adopted these features with a Google Play Billing Library 5 migration, you can proceed directly to the sections labeled [Update Google Play Billing Library](<https://developer.android.com/google/play/billing/migrate-gpblv6?hl=en#update-google>) and [Change a user's subscription purchases](<https://developer.android.com/google/play/billing/migrate-gpblv6?hl=en#change-user-purchases>). If you are starting from an earlier version or didn't fully adopt the new features yet, you can read the [full migration steps](<https://developer.android.com/google/play/billing/migrate-gpblv6?hl=en#steps>) that follow to learn how to adopt them.

## Full migration steps

### Create new subscriptions in your backend product catalog

Using the Play Developer Console or the Play Developer API, you can now configure a single subscription with multiple base plans, each with multiple offers. Subscription offers have flexible pricing models and eligibility options. You can create offers across the subscription lifecycle using a variety of auto-renewing and prepaid plans.

We recommend creating new products following the entity structure in the new subscription platform for your Play Billing Library 6 integration before migrating your app. You can consolidate duplicate products in your old catalog representing the same entitlement benefits under a single subscription and use base plan and offer configurations to represent all the options that you want to offer. For more information about this recommendation, see the *Working with older subscriptions* section of the [Play Console Help article](<https://support.google.com/googleplay/android-developer/answer/12124625>).

Leave automatically converted legacy subscription products unmodified so app versions using deprecated methods, such as [`querySkuDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener)>), can continue selling them without affecting those builds.

Automatically converted legacy subscription products were made read-only to avoid accidental changes that could break an existing integration. You can change these subscriptions, but doing so has implications for both frontend and backend integrations:

- On the frontend, app versions using [`querySkuDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener)>) to obtain subscription product details can only sell backward-compatible base plans and offers, and there can only be one backward-compatible base plan and offer combination, so if you add new plans or offers to the converted subscriptions, the new additional base plans or offers won't be able to be sold on these previous versions of your app.
- On the backend, if you edit your converted subscriptions in the Play Console UI, you won't be able to manage them with the [`inappproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts>) endpoint, if you were calling the endpoint for this purpose. You should also migrate to the new subscription purchase status endpoint ([`purchases.subscriptionsv2.get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>)) to manage purchases for these subscriptions, as the old purchase status endpoint ([`purchases.subscriptions.get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/get>)) only returns the data necessary to handle backward-compatible base plans and offers purchases. Read the [Manage subscription purchase status section](<https://developer.android.com/google/play/billing/migrate-gpblv6?hl=en#manage-subscription-status>) for more information.

### Manage your backend subscription catalog with the new API

If you manage your subscription product catalog automatically with the Google Play Developer API, you need to use the new subscription product definition endpoints to create and manage subscriptions, base plans, and offers. Read the [subscription catalog compatibility guide](<https://developer.android.com/google/play/billing/compatibility#managing-subscriptions>) to learn more about the product catalog API changes for this release.

To migrate an automatic product catalog management module for Google Play Billing subscriptions, replace the [`inappproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts>) API with the new Subscription Publishing API to manage and publish your subscription catalog. There are three new endpoints:

- [`Monetization.subscriptions`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions>) to manage subscription products.
- [`Monetization.basePlans`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans>) to manage base plans for subscriptions.
- [`Monetization.offers`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers>) to manage offers for base plans.

These new endpoints have all the necessary functionality to leverage all the new capabilities in your catalog: base plan and offer tags, regional targeting, prepaid plans, and more.

You should still use the [`inappproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts>) API to manage your in-app product catalog for one-time purchase products.

> **Note:** The [`inappproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts>) API for product management will continue to return subscription product details as before for converted subscriptions if you haven't made them editable in the Play Console. Once you start editing your subscriptions in the Console, the [`inappproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts>) API can no longer be used for subscriptions.

Versions of your app using deprecated methods (for example, [`querySkuDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener)>)) won't be able to sell any base plans or offers that are not backward compatible. You can read about backward-compatible offers in the [Play Console Help article](<https://support.google.com/googleplay/android-developer/answer/12124625>).

### Update Google Play Billing Library

Once you have created your new subscription products catalog, you can migrate your app to Google Billing Library 5. Replace the existing Play Billing Library dependency with the updated version to your app's `build.gradle` file.

```groovy
dependencies {
    def billingVersion = "6.0.0"

    implementation "com.android.billingclient:billing:$billingVersion"
}
```

Your project should build right away, even if you haven't modified any calls to methods; Play Billing Library 6 is backward compatible. The concept of a SKU is considered deprecated, but still present to make porting apps a simpler, more incremental process.

> **Note:** If you are migrating from Play Billing Library 5, you can skip to the [Change a user's subscription purchases](<https://developer.android.com/google/play/billing/migrate-gpblv6?hl=en#change-user-purchases>) section.

### Initialize the Billing Client and establish a connection to Google Play

The first steps to launch purchases from an Android app remain the same:

- [Initialize the Billing Client](<https://developer.android.com/google/play/billing/integrate#initialize>)
- [Establish a connection to Google Play](<https://developer.android.com/google/play/billing/integrate#connect_to_google_play>)

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/migrate-gpblv6).
