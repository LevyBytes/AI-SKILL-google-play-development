The developer renders the choice screen and alternative payment happens outside the app (Scenario 2B). The connected flow includes [setup and eligibility](choice-developer-external-setup.md), [reporting token](choice-developer-external-reporting.md), [external purchase](choice-developer-external-purchase.md), [subscription replacement](choice-developer-external-replacement.md).

3. Call the `getBillingChoiceInfoAsync` method to get the Play Billing banner and loyalty information.

   **Kotlin**

   ```kotlin
   // 1. Create the params required for the request
   val params = GetBillingChoiceInfoParams.newBuilder()
       .setBillingProgram(BillingProgram.BILLING_CHOICE)
       .setPlayBillingChoiceImageLayout(GetBillingChoiceInfoParams.ImageLayout.RECTANGULAR_FOUR_BY_ONE)
       .build()

   // 2. Call the suspend method on your billingClient instance
   val (billingResult, playBillingChoiceInfo) = billingClient.getBillingChoiceInfo(params)

   if (billingResult.responseCode == BillingResponseCode.OK && playBillingChoiceInfo != null) {
       // Access the URL of the image associated with the Play Billing Choice
       val imageUrl = playBillingChoiceInfo.playBillingChoiceImageUrl

       // Access the Play Loyalty string information, if available
       val loyaltyInfo = playBillingChoiceInfo.playBillingLoyaltyInfo

       // Populate your developer-rendered UI elements
       playBillingLoyaltyTextView.text = loyaltyInfo
       loadImage(imageUrl, playBillingImageView)
   } else {
       // Handle error scenarios
   }
   ```

   **Java**

   ```java

   // 1. Create the params required for the request
   GetBillingChoiceInfoParams params = GetBillingChoiceInfoParams.newBuilder()
       .setBillingProgram(BillingClient.BillingProgram.BILLING_CHOICE)
       .setPlayBillingChoiceImageLayout(GetBillingChoiceInfoParams.ImageLayout.RECTANGULAR_FOUR_BY_ONE)
       .build();
   // 2. Call the method asynchronously on your billingClient instance
   billingClient.getBillingChoiceInfoAsync(params, (billingResult, playBillingChoiceInfo) -> {
       if (billingResult.getResponseCode() == BillingResponseCode.OK && playBillingChoiceInfo != null) {
         // Access the URL of the image associated with the Play Billing Choice
           String imageUrl = playBillingChoiceInfo.getPlayBillingChoiceImageUrl();
           // Access the Play Loyalty string information, if available
           String loyaltyInfo = playBillingChoiceInfo.getPlayBillingLoyaltyInfo();

           // Populate your developer-rendered UI elements
           playBillingLoyaltyTextView.setText(loyaltyInfo);
             loadImage(imageUrl, playBillingImageView);
         } else {
             // Handle error scenarios
         }
   });

   ```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
