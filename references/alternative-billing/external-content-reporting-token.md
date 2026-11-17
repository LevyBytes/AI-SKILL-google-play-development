The [program-specific client setup](external-content-client-setup.md) establishes the connection and eligibility checks for this flow.

## Prepare an external transaction token

Next, you must generate an external transaction token from the Play Billing Library. A new external transaction token must be generated each time the user visits an external website through the external links API. This can be done by calling the [`createBillingProgramReportingDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)>) API. The token should be generated immediately before the user is linked out.

**Note**: The external transaction token should never be cached and you should generate a new token each time the user is linked out.

**Kotlin**

```kotlin
val params =
    BillingProgramReportingDetailsParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_CONTENT_LINK)
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
            // Persist the external transaction token locally. Pass it to the
            // external website when launchExternalLink is called.
        }
    }
)
```

**Java**

```java
BillingProgramReportingDetailsParams params =
    BillingProgramReportingDetailsParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_CONTENT_LINK)
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

        // Persist the external transaction token locally. Pass it to the
        // external website when launchExternalLink is called.
      }
  });
```

If you're [using Kotlin extensions](<https://developer.android.com/google/play/billing/integrate#dependency>), you can use Kotlin coroutines so you don't have to define a separate listener.

## Response handling

When an error occurs, the methods `isBillingProgramAvailableAsync()`, and `createBillingProgramReportingDetailsAsync()`, and `onLaunchExternalLinkResponse()` might provide a `BillingResponseCode` other than `BillingResponseCode.OK`. Consider handling these response codes as follows:

- `ERROR`: This is an internal error. Don't proceed with the transaction or opening the external website. Retry by calling the API again or by calling `launchExternalLink()` the next time you attempt to direct the user outside the app.
- `FEATURE_NOT_SUPPORTED`: The external content link APIs are not supported by the Play Store on the current device. Don't proceed with the transaction or opening the external website.
- `USER_CANCELED`: Don't proceed with opening the external website. Call `launchExternalLink()` again the next time you attempt to direct the user outside of the app.
- `BILLING_UNAVAILABLE`: The transaction is not eligible for external content links and therefore don't proceed under this program. This is either because the user is not in an eligible country for this program or your account has not been successfully enrolled in the program. If it's the latter, check your enrollment status in the Play Developer Console.
- `DEVELOPER_ERROR`: There is an error with the request. Use the debug message to identify and correct the error before proceeding.
- `NETWORK_ERROR, SERVICE_DISCONNECTED, SERVICE_UNAVAILABLE`: These are transient errors that should be handled with an appropriate retry policy. In the case of `SERVICE_DISCONNECTED`, re-establish a connection with Google Play before retrying.

## Test external content links

License testers should be used to test your external offers integration. You won't be invoiced for transactions that have been initiated by license tester accounts. See [Test in-app billing with application licensing](<https://support.google.com/googleplay/android-developer/answer/6062777>) for more information on configuring license testers.

## Next steps

After you've finished in-app integration, you're ready to [integrate your backend](<https://developer.android.com/google/play/billing/outside-gpb-backend>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/externalcontentlinks/integration).
