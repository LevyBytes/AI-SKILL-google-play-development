This document describes how to integrate the Play Billing Library APIs to offer external payments in eligible apps. To learn more about this program, see [program requirements](<https://support.google.com/googleplay/android-developer/answer/16787536>).

## Play Billing Library setup

[Add the Play Billing Library dependency](<https://developer.android.com/google/play/billing/getting-ready#dependency>) to your Android app. To use the external payments APIs you need to use version 8.3 or higher. If you need to migrate from an earlier version, follow the instructions in the [migration guide](<https://developer.android.com/google/play/billing/migrate-gpblv8>) to upgrade before starting your integration.

## Initialize the billing client

The first steps in the integration process are the same as the ones described in the [Google Play Billing integration guide](<https://developer.android.com/google/play/billing/integrate>), with a few modifications when [initializing your BillingClient](<https://developer.android.com/google/play/billing/integrate#initialize>):

- You need to call a new [`enableBillingProgram(EnableBillingProgramParams)`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(com.android.billingclient.api.EnableBillingProgramParams)>) method to indicate that you want to offer external payments.
- You need to register an [`DeveloperProvidedBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener>) for handling cases where the user chooses to pay on your website or a payment app.

The following example demonstrates initializing a BillingClient with these modifications:

**Kotlin**

```kotlin
val purchasesUpdatedListener =
    PurchasesUpdatedListener { billingResult, purchases ->
        // Handle new Google Play purchase.
    }

val developerProvidedBillingListener =
    DeveloperProvidedBillingListener { details ->
        // Handle user selection for developer provided billing option.
    }

val billingClient = BillingClient.newBuilder(context)
    .setListener(purchasesUpdatedListener)
    .enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())
    .enableBillingProgram(
        EnableBillingProgramParams.newBuilder()
            .setBillingProgram(BillingProgram.EXTERNAL_PAYMENTS)
            .setDeveloperProvidedBillingListener(developerProvidedBillingListener)
            .build()
    )
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

private DeveloperProvidedBillingListener developerProvidedBillingListener =
    new DeveloperProvidedBillingListener() {
        @Override
        public void onUserSelectedDeveloperBilling(
            DeveloperProvidedBillingDetails details) {
            // Handle user selection for developer provided billing option.
        }
    };

private BillingClient billingClient = BillingClient.newBuilder(context)
    .setListener(purchasesUpdatedListener)
    .enablePendingPurchases()
    .enableBillingProgram(
        EnableBillingProgramParams.newBuilder()
            .setBillingProgram(BillingProgram.EXTERNAL_PAYMENTS)
            .setDeveloperProvidedBillingListener(developerProvidedBillingListener)
            .build())
    .build();
```

## Connect to Google Play

After you initialize the `BillingClient`, connect to Google Play as described in [Connect to Google Play](<https://developer.android.com/google/play/billing/integrate#connect_to_google_play>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/externalpaymentlinks/integration).
