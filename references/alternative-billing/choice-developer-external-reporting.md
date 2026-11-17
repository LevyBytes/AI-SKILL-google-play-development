The developer renders the choice screen and alternative payment happens outside the app (Scenario 2B). The connected flow includes [setup and eligibility](choice-developer-external-setup.md), [choice-screen information](choice-developer-external-ui.md), [external purchase](choice-developer-external-purchase.md), [subscription replacement](choice-developer-external-replacement.md).

4. Call [`createBillingProgramReportingDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)>) to create an external transaction token when the user shows the intention to buy. For example:

   **Kotlin**

   ```kotlin
   // Build the parameters for creating reporting details
   val params =
       BillingProgramReportingDetailsParams.newBuilder()
           .setBillingProgram(BillingProgram.BILLING_CHOICE)
           .setDeveloperBillingType(DeveloperBillingType.EXTERNAL_LINK)
           .build()

   // Call the suspend function to create billing program reporting details
   val (billingResult, billingProgramReportingDetails) =
       billingClient.createBillingProgramReportingDetails(params)

   // Handle response failure cases
   if (billingResult.responseCode != BillingResponseCode.OK) {
       // Handle failures such as retrying due to network errors.
       return
   }

   // Retrieve the external transaction token
   val transactionToken =
       billingProgramReportingDetails?.externalTransactionToken

   // Persist the external transaction token locally. Pass it to
   // DeveloperBillingOptionParams when launchBillingFlow is called.
   // It can also be used as part of your external website
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
               @Nullable BillingProgramReportingDetails billingProgramReportingDetails
           ) {
               if (billingResult.getResponseCode() != BillingResponseCode.OK) {
                   // Handle failures such as retrying due to network errors.
                   return;
               }

               String transactionToken =
                   billingProgramReportingDetails.getExternalTransactionToken();

               // Persist the external transaction token locally. Pass it to
               // DeveloperBillingOptionParams when launchBillingFlow is called.
               // It can also be used as part of your external website.
           }
       }
   );

   ```
5. Launch your alternative choice screen when the user clicks Buy.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
