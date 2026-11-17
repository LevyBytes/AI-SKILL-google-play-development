The developer renders the choice screen and alternative payment happens outside the app (Scenario 2B). The connected flow includes [setup and eligibility](choice-developer-external-setup.md), [choice-screen information](choice-developer-external-ui.md), [reporting token](choice-developer-external-reporting.md), [subscription replacement](choice-developer-external-replacement.md).

6. Handle the user selection of billing type as follows:

   - If the user selects Play Billing, call [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) following the [standard Play Billing guidance](<https://developer.android.com/google/play/billing/integrate#launch>). The billing result is returned to the [`PurchasesUpdatedListener`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener>) registered in step 1.

     Parental control is displayed for [supervised users](<https://support.google.com/families/answer/7106960>).
   - If the user selects your alternative billing, call launchExternalLink. For example:

     **Kotlin**

     ```kotlin
     // An activity reference from which the purchase flow will be launched.

     val params = LaunchExternalLinkParams.newBuilder()
         .setBillingProgram(BillingProgram.BILLING_CHOICE)
         .setExternalTransactionToken(transactionToken)
         // You can pass along the external transaction token from
         // BillingProgramReportingDetails as a URL parameter in the URI
         .setLinkUri(yourLinkUri)
         .setLinkType(LaunchExternalLinkParams.LinkType.LINK_TO_DIGITAL_CONTENT_OFFER)
         .setLaunchMode(
             LaunchExternalLinkParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP
         )
         .build()

     // Call launchExternalLink with a callback
     billingClient.launchExternalLink(activity, params) { billingResult ->
         if (billingResult.responseCode == BillingResponseCode.OK) {
             // Proceed with the rest of the purchase flow. If the user
             // purchases an item, be sure to report the transaction to Google
             // Play.
         } else {
             // Handle failures such as retrying due to network errors.
         }
     }
     ```

     **Java**

     ```java

     // An activity reference from which the purchase flow will be launched.
     Activity activity = ...;

     LaunchExternalLinkParams params = LaunchExternalLinkParams.newBuilder()
         .setBillingProgram(BillingProgram.BILLING_CHOICE)
         // You can pass along the external transaction token from
         // BillingProgramReportingDetails as a URL parameter in the URI
         .setLinkUri(yourLinkUri)
         .setLinkType(LaunchExternalLinkParams.LinkType.LINK_TO_DIGITAL_CONTENT_OFFER)
         .setLaunchMode(
             LaunchExternalLinkParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
         .setExternalTransactionToken(transactionToken)
         .build();

     LaunchExternalLinkResponseListener listener =
         new LaunchExternalLinkResponseListener() {
           @Override
           public void onLaunchExternalLinkResponse(BillingResult billingResult) {
             if (billingResult.getResponseCode() == BillingResponseCode.OK) {
               // Proceed with the rest of the purchase flow. If the user
               // purchases an item, be sure to report the transaction to Google
               // Play.
             } else {
               // Handle failures such as retrying due to network errors.
             }
           }
         };

     billingClient.launchExternalLink(activity, params, listener);

     ```
   - Pass the external transaction token from step 4 to [`LaunchExternalLinkParams`](<https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams>). If it returns OK, proceed with the transaction and report the transaction to Google Play.

     Parental control is displayed for [supervised users](<https://support.google.com/families/answer/7106960>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
