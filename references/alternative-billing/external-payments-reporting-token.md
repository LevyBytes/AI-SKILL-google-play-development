The [program-specific client setup](external-payments-client-setup.md) establishes the connection and eligibility checks for this flow.

## Prepare an external transaction token

To report an external transaction to Google Play, you must have an external transaction token generated from the Play Billing Library. A new external transaction token must be generated each time the user visits an external website or app through the external payments API. This can be done by calling the [`createBillingProgramReportingDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)>) API. The token should be generated immediately before launchBillingFlow is called.

**Kotlin**

```kotlin
val params =
    BillingProgramReportingDetailsParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_PAYMENTS)
        .build()

billingClient.createBillingProgramReportingDetailsAsync(
    params,
    object : BillingProgramReportingDetailsListener {
        override fun onCreateBillingProgramReportingDetailsResponse(
            billingResult: BillingResult,
            billingProgramReportingDetails: BillingProgramReportingDetails?
        ) {
            if (billingResult.responseCode != BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors.
                return
            }
            val externalTransactionToken =
                billingProgramReportingDetails?.externalTransactionToken
            // Persist the external transaction token locally. Pass it to
            // the external website using DeveloperBillingOptionParams when
            // launchBillingFlow is called.
        }
    }
)
```

**Java**

```java
BillingProgramReportingDetailsParams params =
    BillingProgramReportingDetailsParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_PAYMENTS)
        .build();

billingClient.createBillingProgramReportingDetailsAsync(
  params,
  new BillingProgramReportingDetailsListener() {
    @Override
    public void onCreateBillingProgramReportingDetailsResponse(
      BillingResult billingResult,
      @Nullable BillingProgramReportingDetails
        billingProgramReportingDetails) {
        if (billingResult.getResponseCode() != BillingResponseCode.OK) {
            // Handle failures such as retrying due to network errors.
            return;
        }

        String transactionToken =
          billingProgramReportingDetails.getExternalTransactionToken();

        // Persist the external transaction token locally. Pass it to
        // the external website using DeveloperBillingOptionParams when
        // launchBillingFlow is called.
      }
});
```

If you're [using Kotlin extensions](<https://developer.android.com/google/play/billing/integrate#dependency>), you can use Kotlin coroutines so you don't have to define a separate listener.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/externalpaymentlinks/integration).
