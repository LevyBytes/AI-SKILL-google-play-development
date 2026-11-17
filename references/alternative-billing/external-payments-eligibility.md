The [program-specific client setup](external-payments-client-setup.md) establishes the connection and eligibility checks for this flow.

## Check user eligibility

After you connect to Google Play, you can check if the user is eligible for the external payments program by calling the [`isBillingProgramAvailableAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)>) method. This method returns [`BillingResponseCode.OK`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#OK()>) if the user is eligible. The following sample demonstrates how to check eligibility:

**Kotlin**

```kotlin
billingClient.isBillingProgramAvailableAsync(
    BillingProgram.EXTERNAL_PAYMENTS,
    object : BillingProgramAvailabilityListener {
        override fun onBillingProgramAvailabilityResponse(
            billingResult: BillingResult,
            billingProgramAvailabilityDetails: BillingProgramAvailabilityDetails
        ) {
            if (billingResult.responseCode != BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors,
                // handling external payments unavailable, etc.
                return
            }

            // External payments are available. Can proceed with generating an
            // external transaction token.
        }
    }
)
```

**Java**

```java
billingClient.isBillingProgramAvailableAsync(
  BillingProgram.EXTERNAL_PAYMENTS,
  new BillingProgramAvailabilityListener() {
    @Override
    public void onBillingProgramAvailabilityResponse(
      int billingProgram, BillingResult billingResult) {
        if (billingResult.getResponseCode() != BillingResponseCode.OK) {
            // Handle failures such as retrying due to network errors,
            // handling external payments unavailable, etc.
            return;
        }

        // External payments are available. Can proceed with generating an external transaction token.
      }

    });
```

See the [response handling](<https://developer.android.com/google/play/billing/externalpaymentlinks/integration?hl=en#response-handling>) section for details on how your app should respond to other response codes. If you're [using Kotlin extensions](<https://developer.android.com/google/play/billing/integrate#dependency>), you can use Kotlin coroutines so you don't have to define a separate listener.

## Display available products

You can [display available products to the user](<https://developer.android.com/google/play/billing/integrate#show-products>) in the same way as with a Google Play billing system integration. When your user has seen the products available for purchase and selects one to buy, launch the external payments flow as described in the [launching the external payments flow section](<https://developer.android.com/google/play/billing/externalpaymentlinks/integration?hl=en#launching-external>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/externalpaymentlinks/integration).
