The [program-specific client setup](alternative-only-client-setup.md) establishes the connection and eligibility checks for this flow.

## Reporting transactions to Google Play

> **Note:** See response handling for instructions on how to handle errors from this API.

All transactions made through an alternative billing system **must be reported to Google Play by calling the Google Play Developer API from your backend within 24 hours**, providing an `externalTransactionToken` which is obtained using the API described below. A new externalTransactionToken should be generated for each one-time purchase, each new subscription, and for any upgrade/downgrades to an existing subscription. To learn how to report a transaction once an `externalTransactionToken` is obtained see the [backend integration guide](<https://developer.android.com/google/play/billing/outside-gpb-backend>).

**Kotlin**

```kotlin
billingClient.createAlternativeBillingOnlyReportingDetailsAsync(object :
    AlternativeBillingOnlyReportingDetailsListener {
    override fun onAlternativeBillingOnlyTokenResponse(
        billingResult: BillingResult,
        alternativeBillingOnlyReportingDetails: AlternativeBillingOnlyReportingDetails?
    ) {
        if (billingResult.responseCode != BillingResponseCode.OK) {
            // Handle failures such as retrying due to network errors.
            return
        }

        val externalTransactionToken =
            alternativeBillingOnlyReportingDetails?.externalTransactionToken

        // Send transaction token to backend and report to Google Play.
    }
})
```

**Java**

```java

billingClient.createAlternativeBillingOnlyReportingDetailsAsync(
    new AlternativeBillingOnlyReportingDetailsListener() {
        @Override
        public void onAlternativeBillingOnlyTokenResponse(
            BillingResult billingResult,
            @Nullable AlternativeBillingOnlyReportingDetails
                alternativeBillingOnlyReportingDetails) {
            if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors.
                return;
            }

            String transactionToken =
                alternativeBillingOnlyReportingDetails
                .getExternalTransactionToken();

            // Send transaction token to backend and report to Google Play.
        }
    });
```

## Response handling

The above methods `isAlternativeBillingOnlyAvailableAsync()`, `showAlternativeBillingOnlyInformationDialog()`, and `createAlternativeBillingOnlyReportingDetailsAsync()` may return non-BillingResponseCode.OK responses in the case of errors. The recommended handling of the errors is described below:

- `ERROR`: This is an internal error. Don't proceed with the transaction. Retry again by calling `showAlternativeBillingOnlyInformationDialog()` to display the information dialog to the user the next time the user attempts to make a purchase.
- `FEATURE_NOT_SUPPORTED`: The alternative billing APIs are not supported by the Play Store on the current device. Don't proceed with the transaction.
- `USER_CANCELED`: Don't proceed with the transaction. Call `showAlternativeBillingOnlyInformationDialog()` again to display the information dialog to the user the next time the user attempts to make a purchase.
- `BILLING_UNAVAILABLE`: The transaction is not eligible for alternative billing only and therefore shouldn't proceed under this program. This is either because the user is not in an eligible country for this program or your account has not been successfully enrolled in the program. If it's the latter, check your enrollment status in the Play Developer Console.
- `DEVELOPER_ERROR`: There is an error with the request. Use the debug message to identify and correct the error before proceeding.
- `NETWORK_ERROR, SERVICE_DISCONNECTED, SERVICE_UNAVAILABLE`: These are transient errors that should be retried. In the case of `SERVICE_DISCONNECTED` re-establish a connection with Google Play before retrying.

## Test alternative billing

License testers should be used to test your alternative billing integration. You won't be invoiced for transactions that have been initiated by license tester accounts. See [Test in-app billing with application licensing](<https://support.google.com/googleplay/android-developer/answer/6062777>) for more information on configuring license testers.

## Next steps

Once you've finished in-app integration, you're ready to [integrate your backend](<https://developer.android.com/google/play/billing/outside-gpb-backend>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app).
