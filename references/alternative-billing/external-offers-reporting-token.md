The [program-specific client setup](external-offers-client-setup.md) establishes the connection and eligibility checks for this flow.

## Prepare an external transaction token

To report an external transaction to Google Play, you must have an external transaction token generated from the Play Billing Library. You can obtain this token by calling the [`createBillingProgramReportingDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)>) API. A new token must be generated immediately before directing the user outside the app for each external offer. Tokens must not be cached across transactions.

**Kotlin**

```kotlin
val params =
    BillingProgramReportingDetailsParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_OFFER)
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
            // Persist the transaction token in your backend. You may pass it
            // to the external website when calling the launchExternalLink API.
        }
    }
)
```

**Java**

```java
BillingProgramReportingDetailsParams params =
  BillingProgramReportingDetailsParams.newBuilder()
    .setBillingProgram(BillingProgram.EXTERNAL_OFFER)
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
        // Persist the transaction token in your backend. You may pass it
        // to the external website when calling the launchExternalLink API.
      }
});

```

Alternatively, you can query the suspend function [`createBillingProgramReportingDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)>) with [Kotlin extensions](<https://developer.android.com/google/play/billing/integrate#dependency>) so that you don't need to define a listener:

```kotlin
val createBillingProgramReportingDetailsResult =
    withContext(coroutineContext) {
        billingClient
            .createBillingProgramReportingDetails(params)
    }
// Process the result
```

## Response handling

When an error occurs, the methods `isBillingProgramAvailableAsync()`, `createBillingProgramReportingDetailsAsync()`, and `launchExternalLink()` might return responses other than `BillingResponseCode.OK`. Consider handling these response codes as follows:

- `ERROR`: This is an internal error. Don't proceed with the transaction or opening the external website. Retry by calling `launchExternalLink()` to display the information dialog to the user the next time you attempt to direct the user outside the app.
- `FEATURE_NOT_SUPPORTED`: The external offers APIs are not supported by the Play Store on the current device. Don't proceed with the transaction or opening the external website.
- `USER_CANCELED`: Don't proceed with opening the external website. Call `launchExternalLink()` again to display the information dialog to the user the next time you attempt to direct the user outside of the app.
- `BILLING_UNAVAILABLE`: The transaction is not eligible for external offers and therefore shouldn't proceed under this program. This is either because the user is not in an eligible country for this program or your account has not been successfully enrolled in the program. If it's the latter, check your enrollment status in the Play Developer Console.
- `DEVELOPER_ERROR`: There is an error with the request. Use the debug message to identify and correct the error before proceeding.
- `NETWORK_ERROR, SERVICE_DISCONNECTED, SERVICE_UNAVAILABLE`: These are transient errors that should be handled with an appropriate retry policy. In the case of `SERVICE_DISCONNECTED`, re-establish a connection with Google Play before retrying.

## Test external offers

License testers should be used to test your external offers integration. You won't be invoiced for transactions that have been initiated by license tester accounts. See [Test in-app billing with application licensing](<https://support.google.com/googleplay/android-developer/answer/6062777>) for more information on configuring license testers.

## Next steps

Once you've finished in-app integration, you're ready to [integrate your backend](<https://developer.android.com/google/play/billing/outside-gpb-backend>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/external/integration).
