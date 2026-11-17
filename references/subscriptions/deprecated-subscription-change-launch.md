#### Set SubscriptionUpdateParams for replacement (deprecated)

> **Note:** Starting with the PBL 8.1 release, [`SubscriptionUpdateParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams>) is deprecated. Alternately, use `SubscriptionProductReplacementParams` to specify the replacement parameters.

The following example shows how to update a subscription by using `SubscriptionUpdateParams`.

**Kotlin**

```kotlin
val offerToken = productDetails
        .getSubscriptionOfferDetails(selectedOfferIndex)
        .getOfferToken()

val billingParams = BillingFlowParams.newBuilder().setProductDetailsParamsList(
       listOf(
           BillingFlowParams.ProductDetailsParams.newBuilder()
               .setProductDetails(productDetails)
               .setOfferToken(offerToken)
               .build()
       )
       ).setSubscriptionUpdateParams(
           BillingFlowParams.SubscriptionUpdateParams.newBuilder()
               .setOldPurchaseToken("old_purchase_token")
               .setSubscriptionReplacementMode(
                 BillingFlowParams.ReplacementMode.CHARGE_FULL_PRICE
               )
               .build()
       ).build()

billingClient.launchBillingFlow(
    activity,
    billingParams
   )
// ...
```

**Java**

```java
String offerToken = productDetails
    .getSubscriptionOfferDetails(selectedOfferIndex)
    .getOfferToken();

BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
    .setProductDetailsParamsList(
        ImmuableList.of(
            ProductDetailsParams.newBuilder()
                // fetched via queryProductDetailsAsync
                .setProductDetails(productDetails)
                // offerToken can be found in
                // ProductDetails=>SubscriptionOfferDetails
                .setOfferToken(offerToken)
                .build()))
    .setSubscriptionUpdateParams(
        SubscriptionUpdateParams.newBuilder()
            // purchaseToken can be found in Purchase#getPurchaseToken
            .setOldPurchaseToken("old_purchase_token")
            .setSubscriptionReplacementMode(ReplacementMode.CHARGE_FULL_PRICE)
            .build())
    .build();

BillingResult billingResult = billingClient.launchBillingFlow(activity, billingFlowParams);
// ...
```

#### Replacement recommendations

The following table shows diferrent proration scenarios along with what we recommend for each scenario:

| Scenario | Recommended replacement mode | Result |
| --- | --- | --- |
| Upgrading to a more expensive tier | `CHARGE_PRORATED_PRICE` | The user receives access immediately while keeping the same billing period. |
| Downgrading to a less expensive tier | `DEFERRED` | The user already paid for the more expensive tier, so they keep access until the next billing date. |
| Upgrading while in a free trial, keeping the trial | `WITHOUT_PRORATION` | The user upgrades to a higher tier for the remainder of the trial period without extra charge. |
| Upgrading while in a free trial - ending access to the free trial | `CHARGE_PRORATED_PRICE` | The user receives access to the new tier immediately, the remaining value of the free trial is carried over. The carried over value is calculated based on base plan pricing. |
| Keeping payment schedule of some subscription items unchanged while adding or removing other subscription items from Subscription with add-ons. | `KEEP_EXISTING` | The user keeps paying the old price for the unchanged item. New items are added immediately. Other old items can be replaced by specifying a replacement mode or removed. |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscriptions).
