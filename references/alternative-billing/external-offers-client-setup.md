This guide describes how to integrate with the APIs to support external offers in eligible apps and regions. To learn more about the external offers program including eligibility requirements and geographic scope see [program requirements](<https://support.google.com/googleplay/android-developer/answer/14372887>).

## Play Billing Library setup

To use the external offers APIs, [add version 8.2.1 or higher of the Play Billing Library dependency](<https://developer.android.com/google/play/billing/getting-ready#dependency>) to your Android app. If you need to migrate from an earlier version, follow the instructions in the [migration guide](<https://developer.android.com/google/play/billing/migrate-gpblv8>) before you attempt to implement external offers.

## Connect to Google Play

The first steps in the integration process are the same as the ones described in the [billing integration guide](<https://developer.android.com/google/play/billing/integrate>), except you must call [`enableBillingProgram`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(int)>) to indicate that you want to use external offers when [initializing your `BillingClient`](<https://developer.android.com/google/play/billing/integrate#initialize>):

The following example demonstrates initializing a `BillingClient` with these modifications:

**Kotlin**

```kotlin
val billingClient = BillingClient.newBuilder(context)
    .enableBillingProgram(
        EnableBillingProgramParams.newBuilder()
            .setBillingProgram(BillingProgram.EXTERNAL_OFFER)
            .build()
    )
    .build()
```

**Java**

```java
private BillingClient billingClient = BillingClient.newBuilder(context)
    .enableBillingProgram(BillingProgram.EXTERNAL_OFFER)
    .build();
```

After you initialize the `BillingClient`, you need to [establish a connection to Google Play](<https://developer.android.com/google/play/billing/integrate#connect_to_google_play>) as described in the integration guide.

## Check availability

In order to confirm external offers are available to the current user, call [`isBillingProgramAvailableAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)>).

This API returns `BillingResponseCode.OK` if external offers are available. See [response handling](<https://developer.android.com/google/play/billing/external/integration?hl=en#response-handling>) for details on how your app should respond to other response codes.

**Kotlin**

```kotlin
billingClient.isBillingProgramAvailableAsync(
    BillingProgram.EXTERNAL_OFFER,
    object : BillingProgramAvailabilityListener {
        override fun onBillingProgramAvailabilityResponse(
            billingResult: BillingResult,
            billingProgramAvailabilityDetails: BillingProgramAvailabilityDetails
        ) {
            if (billingResult.responseCode != BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors,
                // handling external offers unavailable, etc.
                return
            }

            // External offers are available. Continue with steps in the
            // guide.
        }
    }
)
```

**Java**

```java

billingClient.isBillingProgramAvailableAsync(
  BillingProgram.EXTERNAL_OFFER,
  new BillingProgramAvailabilityListener() {
    @Override
    public void onBillingProgramAvailabilityResponse(
      BillingResult billingResult,
      BillingProgramAvailabilityDetails billingProgramAvailabilityDetails) {
        if (billingResult.getResponseCode() != BillingResponseCode.OK) {
            // Handle failures such as retrying due to network errors,
            // handling external offers being unavailable, etc.
            return;
        }
        // External offers are available. Continue with steps in the
        // guide.
      }
  });

```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/external/integration).
