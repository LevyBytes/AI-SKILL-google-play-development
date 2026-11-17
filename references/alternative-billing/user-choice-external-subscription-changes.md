The [program-specific client setup](user-choice-client-and-launch.md) establishes the connection and eligibility checks for this flow.

## Handle changes in subscription

> **Note:** Manual reporting of alternative billing with user choice is being sunset. Please find more details about migration deadlines [here](<https://support.google.com/googleplay/android-developer/answer/13821247>) . To learn about what transactions need to be migrated and how to migrate see [Migrating from manual reporting](<https://developer.android.com/google/play/billing/alternative/backend#migrating-manual>) for more information.

For developers using alternative billing with user choice, purchases need to be either processed through Google Play's billing system or reported with an `externalTransactionId`, depending on the user's choice. Changes to existing subscriptions that were processed through the user choice flow can be made through the same billing system until expiration.

This section describes how to handle some common subscription change scenarios.

### Upgrade and downgrade flows

Subscription plan changes including upgrade and downgrade flows should be handled differently depending on whether the subscription was originally bought through Google Play's billing system or through an alternative billing system.

Add-ons that depend on an existing subscription, share the same payment method, and align recurring charges are handled as upgrades. For other add-ons, users should be able to choose which billing system they want to use. Initiate a new purchase experience by using `launchBillingFlow()`, as described in [Launch the user choice billing flow](<https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app?hl=en#launch-user-choice>).

#### Subscriptions bought through an alternative billing system

For subscriptions that were originally bought through the developer's alternative billing system after user choice, users requesting an upgrade or a downgrade should proceed through the developer's alternative billing system without going through the user choice experience again.

To do this, call `launchBillingFlow()` when the user requests an upgrade or a downgrade. Instead of specifying a `SubscriptionUpdateParams` object in the parameters, use `setOriginalExternalTransactionId`, providing the external transaction ID for the original purchase. This does **not** display the user choice screen, given that the user choice for the original purchase is preserved for upgrades and downgrades. The call to `launchBillingFlow()` in this case generates a **new external transaction token** for the transaction that you can retrieve from the callback.

> **Note:** In Play Billing Library 6.1 alternative billing was renamed to user choice billing to distinguish alternative billing with user choice from alternative billing only (i.e. without choice). As a result, API and class names such as enableAlternativeBilling have been switched to enableUserChoiceBilling. APIs and classes with the old naming still exist for backwards compatibility and will be removed in a subsequent release.

**Kotlin**

```kotlin
// The external transaction ID from the current
// alternative billing subscription.
val externalTransactionId = "your_external_transaction_id"

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
        BillingFlowParams.SubscriptionUpdateParams.newBuilder()
            .setOriginalExternalTransactionId(externalTransactionId)
            .build()
    )
    .build()

val billingResult = billingClient.launchBillingFlow(activity, billingFlowParams)

// When the user selects the alternative billing flow,
// the UserChoiceBillingListener is triggered.
```

**Java**

```java
// The external transaction ID from the current
// alternative billing subscription.
String externalTransactionId = //... ;

BillingFlowParams billingFlowParams =
    BillingFlowParams.newBuilder()
        .setProductDetailsParamsList(
            ImmutableList.of(
                ProductDetailsParams.newBuilder()
                    // Fetched using queryProductDetailsAsync.
                    .setProductDetails(productDetailsNewPlan)
                    // offerIdToken can be found in
                    // ProductDetails=>SubscriptionOfferDetails
                    .setOfferToken(offerTokenNewPlan)
                    .build()
                )
            )
        .setSubscriptionUpdateParams(
            SubscriptionUpdateParams.newBuilder()
                .setOriginalExternalTransactionId(externalTransactionId)
                .build()
            )
        .build();

BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);

// When the user selects the alternative billing flow,
// the UserChoiceBillingListener is triggered.
```

When the upgrade or downgrade is completed in the alternative billing system, you need to [report a new transaction](<https://developer.android.com/google/play/billing/alternative#report-new>) using the external transaction token obtained through the previous call for the new subscription purchase.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app).
