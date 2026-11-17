> **Note:** Manual reporting of alternative billing with user choice is being sunset. Please find more details about migration deadlines [here](<https://support.google.com/googleplay/android-developer/answer/13821247>) . To learn about what transactions need to be migrated and how to migrate see [Migrating from manual reporting](<https://developer.android.com/google/play/billing/alternative/backend#migrating-manual>) for more information.

This guide describes how to integrate the APIs to offer alternative billing with user choice in your app.

## Play Billing Library setup

[Add the Play Billing Library dependency](<https://developer.android.com/google/play/billing/getting-ready#dependency>) to your Android app. To use the alternative billing APIs you need to use version 5.2 or higher. If you need to migrate from an earlier version, follow the instructions in the [migration guide](<https://developer.android.com/google/play/billing/migrate-gpblv5>) before you attempt to implement alternative billing.

## Connect to Google Play

> **Note:** In Play Billing Library 6.1 alternative billing was renamed to user choice billing to distinguish alternative billing with user choice from alternative billing only (i.e. without user choice). As a result, API and class names such as enableAlternativeBilling have been switched to enableUserChoiceBilling. APIs and classes with the old naming still exist for backwards compatibility and will be removed in a subsequent release.

The first steps in the integration process are the same as the ones described in the [Google Play Billing integration guide](<https://developer.android.com/google/play/billing/integrate>), with a few modifications when [initializing your BillingClient](<https://developer.android.com/google/play/billing/integrate#initialize>):

- You need to call a new method to indicate that you want to offer the user a choice of billing options: [`enableUserChoiceBilling`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableUserChoiceBilling(com.android.billingclient.api.UserChoiceBillingListener)>).
- You need to register an [`UserChoiceBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/UserChoiceBillingListener>) for handling cases where the user chooses alternative billing.

The following example demonstrates initializing a `BillingClient` with these modifications:

**Kotlin**

```kotlin
val purchasesUpdatedListener =
    PurchasesUpdatedListener { billingResult, purchases ->
        // Handle new Google Play purchase.
    }

val userChoiceBillingListener =
    UserChoiceBillingListener { userChoiceDetails ->
        // Handle alternative billing choice.
    }

val billingClient = BillingClient.newBuilder(context)
    .setListener(purchasesUpdatedListener)
    .enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())
    .enableUserChoiceBilling(userChoiceBillingListener)
    .build()
```

**Java**

```java
private PurchasesUpdatedListener purchasesUpdatedListener = new PurchasesUpdatedListener() {
    @Override
    public void onPurchasesUpdated(BillingResult billingResult, List<Purchase> purchases) {
        // Handle new Google Play purchase.
    }
};

private UserChoiceBillingListener userChoiceBillingListener = new UserChoiceBillingListener() {
    @Override
    public void userSelectedAlternativeBilling(
        UserChoiceDetails userChoiceDetails) {
        // Handle new Google Play purchase.
    }
};

private BillingClient billingClient = BillingClient.newBuilder(context)
    .setListener(purchasesUpdatedListener)
    .enablePendingPurchases()
    .enableUserChoiceBilling(userChoiceBillingListener)
    .build();
```

After you initialize the `BillingClient`, you need to [establish a connection to Google Play](<https://developer.android.com/google/play/billing/integrate#connect_to_google_play>) as described in the integration guide.

## Display available products

You can [display available products to the user](<https://developer.android.com/google/play/billing/integrate#show-products>) in the same way as with a Google Play billing system integration. When your user has seen the products available for purchase and selects one to buy, launch the user choice billing flow as described in the following section.

## Launch the user choice billing flow

> **Note:** If you are offering user choice billing through alternative billing APIs, the user experience requirements will be met by integrating with and using the client-side APIs. You will not need to separately follow the interim user experience guidelines ([for South Korea](<https://developer.android.com/google/play/billing/alternative/interim-ux/billing-choice>), [for other eligible markets](<https://developer.android.com/google/play/billing/alternative/interim-ux/user-choice>)).

Launch the user choice billing flow by calling `launchBillingFlow()`. This works the same as [launching a purchase flow](<https://developer.android.com/google/play/billing/integrate#launch>) with a Google Play billing system integration: you provide a `ProductDetails` instance and an `offerToken` corresponding to the product and the offer that the user wants to acquire. If the user chooses Google Play's billing system, this information is used to continue the purchase flow.

When developers call `launchBillingFlow()`, the Google Play billing system performs the following check:

- The system checks if the user's [Google Play country](<https://support.google.com/googleplay/answer/7431675>) is a country that supports alternative billing with user choice (i.e. a supported country). If the user's Google Play country is supported, Google Play checks whether alternative billing has been enabled based on the configuration of the `BillingClient`.

  - If alternative billing with user choice has been enabled, the purchase flow shows the [user choice UX](<https://developer.android.com/google/play/billing/alternative#user-experience>).
  - If alternative billing with user choice is **not** enabled, the purchase flow shows the standard Google Play billing system UX, without user choice.
- If the user's Google Play country is **not** a supported country, the purchase flow shows the standard Google Play billing system UX, without user choice.

|  | User's Play country is a supported country | User's Play country is not a supported country |
| --- | --- | --- |
| enableUserChoiceBilling called during BillingClient setup | User sees user choice UX | User sees standard Google Play billing system UX |
| enableUserChoiceBilling not called during BillingClient setup | User sees standard Google Play billing system UX | User sees standard Google Play billing system UX |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app).
