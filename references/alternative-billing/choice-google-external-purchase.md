Google renders the choice screen and alternative payment happens outside the app (Scenario 2A). The connected flow includes [setup and eligibility](choice-google-external-setup.md), [reporting token](choice-google-external-reporting.md), [replacement token](choice-google-external-replacement-token.md), [replacement launch](choice-google-external-replacement-launch.md).

4. Call [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) to trigger the purchase flow when the user clicks Buy. If billing choice is available for the user, perform the following:

   1. Pass [`DeveloperBillingOptionParams`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperBillingOptionParams>) to [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>).
   2. Pass the external transaction token from step 3 to `DeveloperBillingOptionParams`.

   For example:

   **Kotlin**

   ```kotlin
   // Build the developer billing option parameters with the external link URI,
   // the transaction token, and browser/app launch mode.
   val developerBillingOptionParams =
       DeveloperBillingOptionParams.newBuilder()
           .setBillingProgram(BillingProgram.BILLING_CHOICE)
           .setLinkUri(Uri.parse("https://www.example.com/external/purchase"))
           .setExternalTransactionToken(transactionToken)
           .setLaunchMode(
               DeveloperBillingOptionParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP
           )
           .build()
   val billingFlowParams = BillingFlowParams.newBuilder()
       .setProductDetailsParamsList(productDetailsParamsList)
       .enableDeveloperBillingOption(developerBillingOptionParams)
       .build()
   val billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)
   ```

   **Java**

   ```java

   DeveloperBillingOptionParams developerBillingOptionParams =
       DeveloperBillingOptionParams.newBuilder()
           .setBillingProgram(BillingProgram.BILLING_CHOICE)
           .setLinkUri(Uri.parse("https://www.example.com/external/purchase"))
           .setExternalTransactionToken(transactionToken)
           .setLaunchMode(
             DeveloperBillingOptionParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
           .build();

   ```

   **Note**: Parental control is displayed for [supervised users](<https://support.google.com/families/answer/7106960>).
5. Handle the user selection of billing type as follows:

   - If the user selects Play Billing, call [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) following the [standard Play Billing guidance](<https://developer.android.com/google/play/billing/integrate#launch>). The billing result is returned to the [`PurchasesUpdatedListener`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener>) registered in step 1.
   - If the user selects your alternative billing, the billing result is returned to the [`DeveloperProvidedBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener>) registered in step

     1. The returned [`DeveloperProvidedBillingDetails`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails>) contains the `externalTransactionToken` that was passed to `DeveloperBillingOptionParams` in step 4 if it is a valid token.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
