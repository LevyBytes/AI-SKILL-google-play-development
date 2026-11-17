Google renders the choice screen and alternative payment happens outside the app (Scenario 2A). The connected flow includes [reporting token](choice-google-external-reporting.md), [purchase launch and completion](choice-google-external-purchase.md), [replacement token](choice-google-external-replacement-token.md), [replacement launch](choice-google-external-replacement-launch.md).

### Handle scenario 2A

Google renders the choice screen and the **alternate billing is handled outside** your app. Do the following steps to enable the billing choice in this scenario:

1. Call [`enableBillingProgram`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(com.android.billingclient.api.EnableBillingProgramParams)>) with [`EnableBillingProgramParams`](<https://developer.android.com/reference/com/android/billingclient/api/EnableBillingProgramParams>) when constructing your BillingClient instance, and then start the connection. For example:

   **Kotlin**

   [Complete kotlin example: Kotlin](<https://developer.android.com/google/play/billing/billingchoice/integration#kotlin>).

   **Java**

   ```java

   EnableBillingProgramParams params = EnableBillingProgramParams.newBuilder()
           .setBillingProgram(BillingProgram.BILLING_CHOICE)
           .setDeveloperProvidedBillingListener(developerProvidedBillingListener)
           .build();

   BillingClient billingClient = BillingClient.newBuilder(context)
           .setListener(purchasesUpdatedListener)
           .enablePendingPurchases(
                   PendingPurchasesParams.newBuilder()
                           .enableOneTimeProducts()
                           .build()
           )
           .enableBillingProgram(params)
           .build();

   ```
2. Verify the availability of the following:

   - Google rendered billing choice
   - External web link

   Call [`isBillingProgramAvailableAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)>) to check the program availability, and then call [`queryProductDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)>) to show available products. For example:

   **Kotlin**

   ```kotlin
   // Check the availability of the billing choice program asynchronously using coroutines
   val (billingResult, billingProgramAvailabilityDetails) =
       billingClient.isBillingProgramAvailable(BillingProgram.BILLING_CHOICE)

   // Ensure the billing program query succeeded
   if (billingResult.responseCode == BillingResponseCode.OK) {
       // Retrieve the availability details specific to the billing choice program
       val billingChoiceAvailabilityDetails =
           billingProgramAvailabilityDetails.billingChoiceAvailabilityDetails

       // Check if billing choice is available, renders via Google Play, and external link is supported
       if (billingChoiceAvailabilityDetails != null &&
           billingChoiceAvailabilityDetails.choiceScreenType == ChoiceScreenType.GOOGLE_RENDERED &&
           billingChoiceAvailabilityDetails.isExternalLinkAvailable
       ) {
           // Billing choice is available and external transaction links are supported. Query products and proceed.
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

               if (billingChoiceAvailabilityDetails != null
                       && billingChoiceAvailabilityDetails.getChoiceScreenType() == ChoiceScreenType.GOOGLE_RENDERED
                       && billingChoiceAvailabilityDetails.isExternalLinkAvailable()) {
                   // Billing choice is available and external transaction links are supported.
                   // Query products and proceed.
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
