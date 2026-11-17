> **Note:** Manual reporting of alternative billing only is being sunset. Please find more details about migration deadlines [here](<https://support.google.com/googleplay/android-developer/answer/13821247>) . To learn about what transactions need to be migrated and how to migrate see [Migrating from manual reporting](<https://developer.android.com/google/play/billing/alternative/backend#migrating-manual>) for more information.

This guide describes how to integrate the APIs to offer alternative billing only (i.e. without user choice) in eligible apps. To learn more about these programs including eligibility requirements and geographic scope see [About Alternative Billing](<https://developer.android.com/google/play/billing/alternative>).

## Play Billing Library setup

[Add the Play Billing Library dependency](<https://developer.android.com/google/play/billing/getting-ready#dependency>) to your Android app. To use the alternative billing APIs you need to use version 6.1 or higher.

## Connect to Google Play

> **Note:** When using alternative billing only, your app does not need to provide a `PurchasesUpdatedListener` which is used for listening to transactions made through Google Play's Billing system.

The first steps in the integration process are the same as the ones described in the [Google Play Billing integration guide](<https://developer.android.com/google/play/billing/integrate>), with a few modifications when [initializing your BillingClient](<https://developer.android.com/google/play/billing/integrate#initialize>):

- You need to call a new method to indicate that your app uses only an alternative billing system: [`enableAlternativeBillingOnly`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableAlternativeBillingOnly()>).

The following example demonstrates initializing a `BillingClient` with these modifications:

**Kotlin**

```kotlin
var billingClient = BillingClient.newBuilder(context)
    .enableAlternativeBillingOnly()
    .build()
```

**Java**

```java
private BillingClient billingClient = BillingClient.newBuilder(context)
    .enableAlternativeBillingOnly()
    .build();
```

After you initialize the `BillingClient`, you need to [establish a connection to Google Play](<https://developer.android.com/google/play/billing/integrate#connect_to_google_play>) as described in the integration guide.

## Checking Availability

> **Note:** See response handling section for instructions on how to handle errors from this API.

Your app should confirm alternative billing only is available by calling [`isAlternativeBillingOnlyAvailableAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isAlternativeBillingOnlyAvailableAsync(com.android.billingclient.api.AlternativeBillingOnlyAvailabilityListener)>).

This API will return [BillingResponseCode.OK](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#OK>) if alternative billing only is available. Refer to [response handling](<https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app?hl=en#response-handling>) for details on how your app should respond to other response codes.

**Kotlin**

```kotlin
billingClient.isAlternativeBillingOnlyAvailableAsync(object :
    AlternativeBillingOnlyAvailabilityListener {
    override fun onAlternativeBillingOnlyAvailabilityResponse(
        billingResult: BillingResult
    ) {
        if (billingResult.responseCode != BillingResponseCode.OK) {
            // Handle failures such as retrying due to network errors,
            // handling alternative billing only being unavailable, etc.
            return
        }

        // Alternative billing only is available. Continue with steps in
        // the guide.
    }
})
```

**Java**

```java

billingClient.isAlternativeBillingOnlyAvailable(
    new AlternativeBillingOnlyAvailabilityListener() {
        @Override
        public void onAlternativeBillingOnlyAvailabilityResponse(
            BillingResult billingResult) {
            if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                 // Handle failures such as retrying due to network errors,
                 // handling alternative billing only being unavailable,
                 // etc.
                return;
            }

            // Alternative billing only is available. Continue with steps in
            // the guide.
        }
    });
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app).
