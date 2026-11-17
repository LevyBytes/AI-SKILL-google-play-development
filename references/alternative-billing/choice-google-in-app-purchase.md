Google renders the choice screen and alternative payment happens inside the app (Scenario 1A). The connected flow includes [setup and eligibility](choice-google-in-app-setup.md), [subscription replacement](choice-google-in-app-replacement.md).

3. Call [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) to trigger the purchase flow when the user clicks Buy. If billing choice is available, pass [`DeveloperBillingOptionParams`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperBillingOptionParams>) to [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>). For example:

   **Kotlin**

   ```kotlin
   val developerBillingOptionParams = DeveloperBillingOptionParams.newBuilder()
       .setBillingProgram(BillingProgram.BILLING_CHOICE)
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
           .build();
   BillingFlowParams billingFlowParams =
       BillingFlowParams.newBuilder()
           .setProductDetailsParamsList(productDetailsParamsList)
           .enableDeveloperBillingOption(developerBillingOptionParams)
           .build();

   BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);

   ```

   **Note**: Parental control is displayed for [supervised users](<https://support.google.com/families/answer/7106960>).
4. Handle the user selection of billing type as follows:

   - If the user selects Play Billing, the billing result is returned to the [`PurchasesUpdatedListener`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener>) registered in step 1.
   - If the user selects your alternative billing, the billing result is returned to the [`DeveloperProvidedBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener>) registered in step 1. The returned [`DeveloperProvidedBillingDetails`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails>) contains an `externalTransactionToken` in this case. The token will be used for transaction reporting.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
