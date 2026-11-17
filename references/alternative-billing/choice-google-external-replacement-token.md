Google renders the choice screen and alternative payment happens outside the app (Scenario 2A). The connected flow includes [setup and eligibility](choice-google-external-setup.md), [reporting token](choice-google-external-reporting.md), [purchase launch and completion](choice-google-external-purchase.md), [replacement launch](choice-google-external-replacement-launch.md).

#### Subscription replacement in Scenario 2A

For subscriptions that were originally bought through the developer's website or a payment app after user choice, users requesting an upgrade or a downgrade should proceed through the developer's website or a payment app without going through the user choice experience again.

To do this, call [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) when the user requests an upgrade or a downgrade. Instead of specifying other params under the `SubscriptionUpdateParams` object, use [`setOriginalExternalTransactionId`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOriginalExternalTransactionId(java.lang.String)>), providing the external transaction ID for the original purchase. `DeveloperBillingOptionParams` must also be provided in this call. This does not display the user choice screen, given that the user choice for the original purchase is preserved for upgrades and downgrades. For example:

**Kotlin**

```kotlin
val externalTransactionId = "external_transaction_id"

// 1. Construct DeveloperBillingOptionParams indicating the billing program
val developerBillingOptionParams = DeveloperBillingOptionParams.newBuilder()
    .setBillingProgram(BillingProgram.BILLING_CHOICE)
    .build()

// 2. Build BillingFlowParams combining DeveloperBillingOptionParams and SubscriptionUpdateParams
val billingFlowParams = BillingFlowParams.newBuilder()
    .setProductDetailsParamsList(
        listOf(
            BillingFlowParams.ProductDetailsParams.newBuilder()
                // Fetched using queryProductDetailsAsync.
                .setProductDetails(productDetailsNewPlan)
                // offerIdToken can be found in ProductDetails=>SubscriptionOfferDetails.
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
```

**Java**

```java

String externalTransactionId = //... ;

// 1. Construct DeveloperBillingOptionParams indicating the billing program
DeveloperBillingOptionParams developerBillingOptionParams =
    DeveloperBillingOptionParams.newBuilder()
        .setBillingProgram(BillingClient.BillingProgram.BILLING_CHOICE)
        .build();

// 2. Add ProductDetailsParams
List productDetailsParamsList = new ArrayList<>();
productDetailsParamsList.add(
    ProductDetailsParams.newBuilder()
        // Fetched using queryProductDetailsAsync.
        .setProductDetails(productDetailsNewPlan)
        // offerIdToken can be found in ProductDetails=>SubscriptionOfferDetails
        .setOfferToken(offerTokenNewPlan)
        .build());

// 3. Build BillingFlowParams combining DeveloperBillingOptionParams and SubscriptionUpdateParams
BillingFlowParams billingFlowParams =
    BillingFlowParams.newBuilder()
        .setProductDetailsParamsList(productDetailsParamsList)
        .setSubscriptionUpdateParams(
            SubscriptionUpdateParams.newBuilder()
                .setOriginalExternalTransactionId(externalTransactionId)
                .build())
        .enableDeveloperBillingOption(developerBillingOptionParams)
        .build();


```

You must also generate a new external transaction token. For example:

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billingchoice/integration).
