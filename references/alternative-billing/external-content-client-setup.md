This document describes how to integrate the Play Billing Library APIs to offer external content links in eligible apps. This includes the ability to link users in the US outside your Play app to provide users with offers to in-app digital content and app downloads. To learn more about this program, see [program requirements](<https://support.google.com/googleplay/android-developer/answer/16470497>).

## Play Billing Library setup

[Add the Play Billing Library dependency](<https://developer.android.com/google/play/billing/getting-ready#dependency>) to your Android app. To use the [external links](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchExternalLink(android.app.Activity,com.android.billingclient.api.LaunchExternalLinkParams,com.android.billingclient.api.LaunchExternalLinkResponseListener)>) APIs you need to use version 8.2.1 or higher. If you need to migrate from an earlier version, follow the instructions in the [migration guide](<https://developer.android.com/google/play/billing/migrate-gpblv8>) before adding the external content links.

## Initialize the billing client

To initialize the billing client follow the same steps as described in [Initialize a `BillingClient`](<https://developer.android.com/google/play/billing/integrate#initialize>) with the following modifications:

- Don't enable the `PurchasesUpdatedListener` - this listener is not needed for external content links.
- Call `enableBillingProgram()` with `BillingProgram.EXTERNAL_CONTENT_LINK` to indicate that your app uses the external content links.

The following example shows initializing a `BillingClient` with these modifications:

**Kotlin**

```kotlin
val billingClient = BillingClient.newBuilder(context)
    .enableBillingProgram(
        EnableBillingProgramParams.newBuilder()
            .setBillingProgram(BillingProgram.EXTERNAL_CONTENT_LINK)
            .build()
    )
    .build()
```

**Java**

```java
private BillingClient billingClient = BillingClient.newBuilder(context)
    .enableBillingProgram(BillingProgram.EXTERNAL_CONTENT_LINK)
    .build();
```

## Connect to Google Play

After you initialize the `BillingClient`, connect to Google Play as described in [Connect to Google Play](<https://developer.android.com/google/play/billing/integrate#connect_to_google_play>).

## Check user eligibility

After you connect to Google Play, you must check if the user is eligible for the external content links program by calling the [`isBillingProgramAvailableAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)>) method. This method returns `BillingResponseCode.OK` if the user is eligible for external content links program. The following sample shows how to check the user eligibility for external content links:

**Kotlin**

```kotlin
billingClient.isBillingProgramAvailableAsync(
    BillingProgram.EXTERNAL_CONTENT_LINK,
    object : BillingProgramAvailabilityListener {
        override fun onBillingProgramAvailabilityResponse(
            billingResult: BillingResult,
            billingProgramAvailabilityDetails: BillingProgramAvailabilityDetails
        ) {
            if (billingResult.responseCode != BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors,
                // handling external content links unavailable, etc.
                return
            }

            // External content links are available. Prepare an external
            // transaction token.
        }
    }
)
```

**Java**

```java
billingClient.isBillingProgramAvailableAsync(
  BillingProgram.EXTERNAL_CONTENT_LINK,
  new BillingProgramAvailabilityListener() {
    @Override
    public void onBillingProgramAvailabilityResponse(
      int billingProgram, BillingResult billingResult) {
        if (billingResult.getResponseCode() != BillingResponseCode.OK) {
            // Handle failures such as retrying due to network errors,
            // handling external content links unavailable, etc.
            return;
        }

        // External content links are available. Prepare an external
        // transaction token.
      }

    });
```

See the [response handling](<https://developer.android.com/google/play/billing/externalcontentlinks/integration?hl=en#response-handling>) section for details on how your app should respond to other response codes. If you're [using Kotlin extensions](<https://developer.android.com/google/play/billing/integrate#dependency>), you can use Kotlin coroutines so you don't have to define a separate listener.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/externalcontentlinks/integration).
