The developer renders the choice screen and alternative payment happens inside the app (Scenario 1B). The connected flow includes [choice-screen information](choice-developer-in-app-ui.md), [reporting token and purchase handling](choice-developer-in-app-reporting.md), [subscription replacement](choice-developer-in-app-replacement.md).

### Handle scenario 1B

Developer renders the choice screen and the **alternate billing is handled within** your app. Do the following steps to enable the billing choice in this scenario:

1. Call [`enableBillingProgram`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(com.android.billingclient.api.EnableBillingProgramParams)>) without the [`DeveloperProvidedBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener>) in [`EnableBillingProgramParams`](<https://developer.android.com/reference/com/android/billingclient/api/EnableBillingProgramParams>) when constructing a `BillingClient` instance, and then start the connection. For example:

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
2. Verify that the developer rendered billing choice is available for the user.

   Call [`isBillingProgramAvailableAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)>) to check the program availability, and then call [`queryProductDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,com.android.billingclient.api.ProductDetailsResponseListener)>) to show available products. For example:

   **Kotlin**

   ```kotlin
   val (billingResult, billingProgramAvailabilityDetails) =
       billingClient.isBillingProgramAvailable(BillingProgram.BILLING_CHOICE)

   if (billingResult.responseCode == BillingResponseCode.OK) {
       val billingChoiceAvailabilityDetails =
           billingProgramAvailabilityDetails.billingChoiceAvailabilityDetails

       if (billingChoiceAvailabilityDetails != null &&
           billingChoiceAvailabilityDetails.choiceScreenType == ChoiceScreenType.DEVELOPER_RENDERED
       ) {
           // Billing choice is available. Query products and proceed.
           // You can inspect details such as:
           // - billingChoiceAvailabilityDetails.choiceScreenType
           // - billingChoiceAvailabilityDetails.isExternalLinkAvailable
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
                       && billingChoiceAvailabilityDetails.getChoiceScreenType() == ChoiceScreenType.DEVELOPER_RENDERED) {
                   // Billing choice is available. Query products and proceed.
                   // You can inspect details such as:
                   // - billingChoiceAvailabilityDetails.getChoiceScreenType()
                   // - billingChoiceAvailabilityDetails.isExternalLinkAvailable()
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
