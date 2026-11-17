Google Play calls `onPurchasesUpdated()` to deliver the result of the purchase operation to a listener that implements the `PurchasesUpdatedListener` interface. The listener is specified using the `setListener()` method when you [initialized your client](<https://developer.android.com/google/play/billing/integrate?hl=en#initialize>).

You must implement `onPurchasesUpdated()` to handle possible response codes. The following example shows how to override `onPurchasesUpdated()`:

**Kotlin**

```kotlin
override fun onPurchasesUpdated(billingResult: BillingResult, purchases: List<Purchase>?) {
    if (billingResult.responseCode == BillingResponseCode.OK && purchases != null) {
        for (purchase in purchases) {
            // Process the purchase as described in the next section.
        }
    } else if (billingResult.responseCode == BillingResponseCode.USER_CANCELED) {
        // Handle an error caused by a user canceling the purchase flow.
    } else {
        // Handle any other error codes.
    }
}
```

**Java**

```java
@Override
void onPurchasesUpdated(BillingResult billingResult, List<Purchase> purchases) {
  if (billingResult.getResponseCode() == BillingResponseCode.OK
      && purchases != null) {
      for (Purchase purchase : purchases) {
          // Process the purchase as described in the next section.
      }
  } else if (billingResult.getResponseCode() == BillingResponseCode.USER_CANCELED) {
      // Handle an error caused by a user canceling the purchase flow.
  } else {
      // Handle any other error codes.
  }
}
```

A successful purchase generates a Google Play purchase success screen similar to figure 2.

![Google Play purchase confirmation display.](<https://developer.android.com/static/images/google/play/billing/purchase-success.png>)

**Figure 2.** Google Play's purchase success screen.

A successful purchase also generates a purchase token, which is a unique identifier that represents the user and the product ID for the one-time product they purchased. Your apps can store the purchase token locally, though we strongly recommend passing the token to your secure backend server where you can then verify the purchase and protect against fraud. This process is further described in [Detecting and Processing Purchases](<https://developer.android.com/google/play/billing/integrate?hl=en#process>).

The user is also emailed a receipt of the transaction containing an Order ID or a unique ID of the transaction. Users receive an email with a unique Order ID for each one-time product purchase, and also for the initial subscription purchase and subsequent recurring automatic renewals. You can use the Order ID to manage refunds in the Google Play Console.

### Indicate a personalized price

If your app can be distributed to users in the European Union, use the `setIsOfferPersonalized()` method when calling `launchBillingFlow` to disclose to users that an item's price was personalized using automated decision-making.

![The Google Play purchase screen indicating that the price was customized for the user.](<https://developer.android.com/static/images/google/play/billing/personalized-pricing.png>)

**Figure 3.** The Google Play purchase screen indicating that the price was customized for the user.

You must consult Art. 6 (1) (ea) CRD of the Consumer Rights Directive [2011/83/EU](<https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02011L0083-20220528>) to determine if the price you are offering to users is personalized.

`setIsOfferPersonalized()` takes a boolean input. When `true`, the Play UI includes the disclosure. When `false`, the UI omits the disclosure. The default value is `false`.

See the [Consumer Help Center](<https://support.google.com/googleplay?p=customized_pricing>) for more information.

### Attach user identifiers

When you launch the purchase flow your app can attach any user identifiers you have for the user making the purchase using [obfuscatedAccountId](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedAccountId(java.lang.String)>) or [obfuscatedProfileId](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedProfileId(java.lang.String)>). An example identifier could be an obfuscated version of the user's login in your system. Setting these parameters can help Google [detect fraud](<https://developer.android.com/google/play/billing/security#fraud>). Additionally, it can help you ensure that purchases are attributed to the right user as discussed in [granting entitlements to users](<https://developer.android.com/google/play/billing/integrate?hl=en#granting-entitlement>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/integrate).
