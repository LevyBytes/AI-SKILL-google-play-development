The developer renders the choice screen and alternative payment happens outside the app (Scenario 2B). The connected flow includes [choice-screen information](choice-developer-external-ui.md), [reporting token](choice-developer-external-reporting.md), [external purchase](choice-developer-external-purchase.md), [subscription replacement](choice-developer-external-replacement.md).

### Handle scenario 2B

Developer renders the choice screen and the **alternate billing is handled outside** the app. Do the following steps to enable the billing choice in this scenario:

1. Call [`enableBillingProgram`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(com.android.billingclient.api.EnableBillingProgramParams)>) without the [`DeveloperProvidedBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener>) in [`EnableBillingProgramParams`](<https://developer.android.com/reference/com/android/billingclient/api/EnableBillingProgramParams>) when constructing a BillingClient instance, and then start the connection. For example:

   **Kotlin**

   [Complete kotlin example: Kotlin](<https://developer.android.com/google/play/billing/billingchoice/integration#kotlin_3>).

   **Java**

   ```java

   EnableBillingProgramParams params = EnableBillingProgramParams.newBuilder()
           .setBillingProgram(BillingProgram.BILLING_CHOICE)
           .build();

   BillingClient billingClient = BillingClient.newBuilder(context)
           .setListener(purchasesUpdatedListener)
           .enablePendingPurchases()
           .enableBillingProgram(params)
           .build();

   ```
2. Verify the availability of the following:

   - Google rendered billing choice
   - External web link

   Call [`isBillingProgramAvailableAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)>) to check the program availability, and then call [`queryProductDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)>) to show available products. For example:

   **Kotlin**

   ```kotlin
   // Check the availability of the billing choice program asynchronously using a coroutine
   val (billingResult, billingProgramAvailabilityDetails) =
       billingClient.isBillingProgramAvailable(BillingProgram.BILLING_CHOICE)

   // Ensure the response code is OK
   if (billingResult.responseCode == BillingResponseCode.OK) {
       // Retrieve the billing choice availability details
       val billingChoiceAvailabilityDetails =
           billingProgramAvailabilityDetails.billingChoiceAvailabilityDetails

       // Check if billing choice details are available, choice screen is developer-rendered,
       // and external transaction links are supported.
       if (billingChoiceAvailabilityDetails != null &&
           billingChoiceAvailabilityDetails.choiceScreenType == ChoiceScreenType.DEVELOPER_RENDERED &&
           billingChoiceAvailabilityDetails.isExternalLinkAvailable
       ) {
           // Billing choice is available and external transaction links are supported.
           // Query products and proceed.
       } else {
           // Fallback to other available programs.
       }
   } else {
       // Fallback to other available programs.
   }
   ```

   **Java**

   ```java

   // ...

   billingClient.isBillingProgramAvailableAsync(
       BillingProgram.BILLING_CHOICE,
       (billingResult, billingProgramAvailabilityDetails) -> {
           if (billingResult.getResponseCode() == BillingResponseCode.OK) {
               BillingChoiceAvailabilityDetails billingChoiceAvailabilityDetails =
                   billingProgramAvailabilityDetails.getBillingChoiceAvailabilityDetails();
               if (billingChoiceAvailabilityDetails != null &&
                   billingChoiceAvailabilityDetails.getChoiceScreenType() == ChoiceScreenType.DEVELOPER_RENDERED &&
                   billingChoiceAvailabilityDetails.isExternalLinkAvailable()) {
                   // Billing choice is available and external transaction links are supported. Query products and proceed.
               } else {
                   // Fallback to other available programs.
               }
           } else {
               // Fallback to other available programs.
           }
       }
   );

   ```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
