## Give rewarded purchases to users

If the Google Play Billing Library successfully loads the video associated with a rewarded product (that is, if the `RewardResponseListener` receives a `responseCode` of `BillingResponse.OK`), you can launch the billing flow.

> **Caution:** Don't start the billing flow if the `responseCode` isn't `BillingResponse.OK`, which happens if the video ad isn't available. That way, you don't show extra error dialogs, which maintains a good user experience.

You start playing ads for a rewarded product by calling [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchbillingflow>), as you do for [all other types of in-app products](<https://developer.android.com/google/play/billing/integrate#launch>). Even though the user isn't making a direct purchase to receive a rewarded product, you still need to enable the billing flow so that the user is able to obtain and use the product.

## Consume the purchase

To notify your billing client that a user has received and consumed a rewarded product, [handle the purchase](<https://developer.android.com/google/play/billing/integrate#process>) in your billing client listener's [`onPurchasesUpdated()`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener#onpurchasesupdated>) method. Note that rewarded purchases [need to be consumed](<https://developer.android.com/google/play/billing/integrate#notifying-google>).

## Test your rewarded products

To test how your app loads video ads and provides users with rewarded products, make use of *licensed testers*, who by default get test ads instead of real ones. To learn how to set up accounts for these testers, see [User-test a Google Play Billing app](<https://developer.android.com/google/play/billing/test#license-testers>).

Another method of testing is for you to use the `android.test.reward` product ID. This specific product is a reserved name in Google Play Billing, so you don't need to add it to your list of in-app products in the Play Console.

**Caution:**When testing your app's rewarded products, **don't use actual products**; otherwise, your account might be flagged as a spam or fraudulent account.

When you're done testing, however, make sure you replace `android.test.reward` with the product IDs for your actual rewarded products before you deploy your production app to end users.

## Diagram of rewarded product workflow

The following sequence diagram shows how the user, your app, and the Google Play Billing Library work together to show a video ad and grant the user access to a rewarded product:

![Sequence diagram showing rewarded products protocol](<https://developer.android.com/static/images/in-app-billing/rewarded-products-workflow.svg>)

**Figure 1.** Steps for completing a rewarded product purchase using Google Play Billing

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billing_rewarded_products).
