The developer renders the choice screen and alternative payment happens inside the app (Scenario 1B). The connected flow includes [setup and eligibility](choice-developer-in-app-setup.md), [choice-screen information](choice-developer-in-app-ui.md), [subscription replacement](choice-developer-in-app-replacement.md).

4. Create an external transaction token with DeveloperBillingType set to **IN_APP**. For example:

   **Kotlin**

   ```kotlin
   // Build the parameters specifying the billing program and that the billing type is IN_APP.
   val params = BillingProgramReportingDetailsParams.newBuilder()
       .setBillingProgram(BillingProgram.BILLING_CHOICE)
       .setDeveloperBillingType(DeveloperBillingType.IN_APP)
       .build()

   // Call the suspending extension function to request the reporting details
   val (billingResult, billingProgramReportingDetails) =
       billingClient.createBillingProgramReportingDetails(params)

   if (billingResult.responseCode != BillingResponseCode.OK) {
       // Handle failures such as retrying due to network errors.
       return
   }

   // Extract the transaction token from the returned reporting details
   val transactionToken = billingProgramReportingDetails?.externalTransactionToken

   // Persist the external transaction token locally. Pass it to
   // DeveloperBillingOptionParams when launchBillingFlow is called.
   // It can also be used as part of your external website
   ```

   **Java**

   ```java

   BillingProgramReportingDetailsParams params =
       BillingProgramReportingDetailsParams.newBuilder()
           .setBillingProgram(BillingProgram.BILLING_CHOICE)
           .setDeveloperBillingType(DeveloperBillingType.IN_APP)
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
               // It can also be used as part of your external website
           }
       }
   );


   ```
5. When the user clicks Buy, call `showBillingProgramInformationDialog` to show an information dialog. For example, see [Information dialog for users](<https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app#information-dialog>). **BillingProgram and transactionToken** from step 4 must be set in the request.

   **Note**: Parental control is displayed for [supervised users](<https://support.google.com/families/answer/7106960>).
6. Launch your alternative billing choice screen if the result from the previous step is `OK`.
7. Handle the user selection of billing type as follows:

   - If the user selects Play Billing, call [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) following the [standard Play Billing guidance](<https://developer.android.com/google/play/billing/integrate#launch>). The billing result is returned to the [`PurchasesUpdatedListener`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener>) registered in step 1.
   - If the user selects your alternative billing, you must handle the transaction yourself and report it to Play using the token generated in step 4.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
