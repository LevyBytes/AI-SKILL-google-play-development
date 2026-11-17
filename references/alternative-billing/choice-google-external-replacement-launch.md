Google renders the choice screen and alternative payment happens outside the app (Scenario 2A). The connected flow includes [setup and eligibility](choice-google-external-setup.md), [reporting token](choice-google-external-reporting.md), [purchase launch and completion](choice-google-external-purchase.md), [replacement token](choice-google-external-replacement-token.md).

**Kotlin**

```kotlin
val params =
    BillingProgramReportingDetailsParams.newBuilder()
        .setBillingProgram(BillingProgram.BILLING_CHOICE)
        .setDeveloperBillingType(DeveloperBillingType.EXTERNAL_LINK)
        .build()

val (billingResult, billingProgramReportingDetails) =
    billingClient.createBillingProgramReportingDetails(params)

if (billingResult.responseCode != BillingResponseCode.OK) {
    // Handle failures such as retrying due to network errors.
    return
}

val externalTransactionToken =
    billingProgramReportingDetails?.externalTransactionToken
// Persist the external transaction token locally. Pass it to
// the external website using DeveloperBillingOptionParams when
// launchBillingFlow is called.
```

**Java**

```java

BillingProgramReportingDetailsParams params =
    BillingProgramReportingDetailsParams.newBuilder()
        .setBillingProgram(BillingProgram.BILLING_CHOICE)
        .setDeveloperBillingType(DeveloperBillingType.EXTERNAL_LINK)
        .build();

billingClient.createBillingProgramReportingDetailsAsync(
    params,
    new BillingProgramReportingDetailsListener() {
      @Override
      public void onCreateBillingProgramReportingDetailsResponse(
          BillingResult billingResult,
          @Nullable BillingProgramReportingDetails billingProgramReportingDetails) {
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

After generating the new token, you must call the [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) method to launch the purchase flow.

When the upgrade or downgrade is complete, you need to [report a new transaction](<https://developer.android.com/google/play/billing/outside-gpb-backend>) using the external transaction token obtained through the previous call for the new subscription purchase.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
