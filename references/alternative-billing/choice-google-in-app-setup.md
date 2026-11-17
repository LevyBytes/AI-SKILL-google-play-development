Google renders the choice screen and alternative payment happens inside the app (Scenario 1A). The connected flow includes [purchase launch and selection](choice-google-in-app-purchase.md), [subscription replacement](choice-google-in-app-replacement.md).

### Handle scenario 1A

Google renders the choice screen and the **alternate billing is handled within** your app. Do the following steps to enable the billing choice in this scenario:

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
2. Verify that the Google rendered billing choice is available for the user.

   Call [`isBillingProgramAvailableAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)>) to check the program availability, and then call [`queryProductDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)>) to show available products. For example:

   **Kotlin**

   ```kotlin
   val (billingResult, billingProgramAvailabilityDetails) = billingClient.isBillingProgramAvailable(BillingProgram.BILLING_CHOICE)

   if (billingResult.responseCode == BillingResponseCode.OK) {
       val billingChoiceAvailabilityDetails = billingProgramAvailabilityDetails.billingChoiceAvailabilityDetails
       if (billingChoiceAvailabilityDetails != null &&
           billingChoiceAvailabilityDetails.choiceScreenType == ChoiceScreenType.GOOGLE_RENDERED
       ) {
           // Billing choice is available. Query products and proceed.
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
                   billingChoiceAvailabilityDetails.getChoiceScreenType() == ChoiceScreenType.GOOGLE_RENDERED) {
                   // Billing choice is available. Query products and proceed.
               } else {
                   // Fallback to other available programs.
               }
           } else {
               // Fallback to other available programs.
           }
       }
   );

   ```

   **Note**: `billingProgramAvailabilityDetails` tells you if Google rendered or Developer rendered billing choice screen is available.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
