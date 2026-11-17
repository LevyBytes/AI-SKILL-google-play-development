Google renders the choice screen and alternative payment happens inside the app (Scenario 1A). The connected flow includes [setup and eligibility](choice-google-in-app-setup.md), [purchase launch and selection](choice-google-in-app-purchase.md).

### Billing choice during subscription replacement

For subscription replacement, the user choice screen shouldn't be shown given that the user choice for the original purchase is preserved for upgrades and downgrades.

If the **original purchase was processed through Google Play Billing**, you should call [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) with standard [Google Play Billing subscription replacement](<https://developer.android.com/google/play/billing/subscriptions#allow-users-change>) information.

However, if the original purchase was **processed through an alternative billing**, handling of subscription replacements slightly differ based on the scenarios.

#### Subscription replacement in Scenario 1A

Users requesting an upgrade or a downgrade should proceed through the developer's alternative billing system without going through the user choice experience again.

To do this, call [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) when the user requests an upgrade or a downgrade. Use `setOriginalExternalTransactionId` inside the `SubscriptionUpdateParams` object in the parameters to provide the external transaction ID for the original purchase. This does not display the user choice screen, given that the user choice for the original purchase is preserved for upgrades and downgrades. The call to [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) in this case generates a **new external transaction token** for the transaction that you can retrieve from the callback.

**Kotlin**

```kotlin
// The external transaction ID from the current
// alternative billing subscription.
val externalTransactionId = "external_transaction_id"

val developerBillingOptionParams = DeveloperBillingOptionParams.newBuilder()
    .setBillingProgram(BillingProgram.BILLING_CHOICE)
    .build()

val billingFlowParams = BillingFlowParams.newBuilder()
    .setProductDetailsParamsList(
        listOf(
            BillingFlowParams.ProductDetailsParams.newBuilder()
                // Fetched using queryProductDetailsAsync.
                .setProductDetails(productDetailsNewPlan)
                // offerIdToken can be found in
                // ProductDetails=>SubscriptionOfferDetails.
                .setOfferToken(offerTokenNewPlan)
                .build()
        )
    )
    .setSubscriptionUpdateParams(
        SubscriptionUpdateParams.newBuilder()
            .setOriginalExternalTransactionId(externalTransactionId)
            .build()
    )
    .enableDeveloperBillingOption(developerBillingOptionParams)
    .build()

val billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)

// When the user selects the alternative billing flow,
// the DeveloperProvidedBillingListener is triggered.
```

**Java**

```java

// The external transaction ID from the current
// alternative billing subscription.
String externalTransactionId = //... ;

DeveloperBillingOptionParams developerBillingOptionParams =
    DeveloperBillingOptionParams.newBuilder()
        .setBillingProgram(BillingProgram.BILLING_CHOICE)
        .build();

List<ProductDetailsParams> productDetailsParamsList = new ArrayList<>();
productDetailsParamsList.add(
    ProductDetailsParams.newBuilder()
        // Fetched using queryProductDetailsAsync.
        .setProductDetails(productDetailsNewPlan)
        // offerIdToken can be found in
        // ProductDetails=>SubscriptionOfferDetails
        .setOfferToken(offerTokenNewPlan)
        .build());

BillingFlowParams billingFlowParams =
    BillingFlowParams.newBuilder()
        .setProductDetailsParamsList(productDetailsParamsList)
        .setSubscriptionUpdateParams(
            SubscriptionUpdateParams.newBuilder()
                .setOriginalExternalTransactionId(externalTransactionId)
                .build())
        .enableDeveloperBillingOption(developerBillingOptionParams)
        .build();

BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);

// When the user selects the alternative billing flow,
// the DeveloperProvidedBillingListener is triggered.


```

When the upgrade or downgrade is complete, you need to [report a new transaction](<https://developer.android.com/google/play/billing/alternative#report-new>) using the external transaction token obtained through the previous call for the new subscription purchase.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
