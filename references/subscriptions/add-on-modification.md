## Modify subscriptions with add-ons

Any changes to your subscription with add-ons, results in an upgrade or a downgrade. For more information, see [upgrade or downgrade subscriptions](<https://developer.android.com/google/play/billing/subscriptions#allow-users-change>).

To change or restore an existing purchase of subscription with add-ons in your app, you must call the [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) API with additional parameters, and ensure the following:

- Always call `setOldPurchaseToken` with the purchase token of the current subscription purchase.
- To upgrade, downgrade, or crossgrade an item, call `SubscriptionProductReplacementParams.setReplacementMode` to specify how the plan change should be handled between the old and the new purchase item. Otherwise, there is no need to set `SubscriptionProductReplacementParams`.
- When the base item isn't changed, you can still call `SubscriptionProductReplacementParams.setSubscriptionReplacementMode` to apply a specific replacement behavior. For the applicable rules in this case, see [Resubscribe or switch plans within the same subscription](<https://developer.android.com/google/play/billing/subscriptions#resubscribe_or_switch_plans_within_the_same_subscription>).
- New add-ons will apply immediately with a prorated charge to align the next renewal date with the base item in the subscription.
- Removed add-ons will expire at the end of their current billing periods.
- When launching the billing flow, you will need to specify all active items in the subscription with add-ons excluding those to be removed, along with any new add-ons.

The following sample shows how to call the [`launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) API when changing an existing purchase of subscription with add-ons:

#### Java

```java
BillingClient billingClient = …;

int replacementMode =…;

// ProductDetails obtained from queryProductDetailsAsync().
ProductDetailsParams productDetails1 = ...;
ProductDetailsParams productDetails2 = ...;
ProductDetailsParams productDetails3 = ...;

ArrayList newProductDetailsList = new ArrayList<>();
newProductDetailsList.add(productDetails1);
newProductDetailsList.add(productDetails1);
newProductDetailsList.add(productDetails1);

BillingFlowParams billingFlowParams =
    BillingFlowParams.newBuilder()
        .setSubscriptionUpdateParams(
          SubscriptionUpdateParams.newBuilder()
              .setOldPurchaseToken(purchaseTokenOfExistingSubscription)
              // No need to set if change does not affect the base item.
             .setSubscriptionReplacementMode(replacementMode)
             .build())
        .setProductDetailsParamsList(productDetailsList)
        .build();

billingClient.launchBillingFlow(billingFlowParams);
```

### Subscription modification scenarios

The following table lists the various modification scenarios for subscription with add-ons, and the corresponding behaviour.

#### When using SubscriptionProductReplacementParams

| Existing items | Modified items | Do you need to set the replacement mode in SubscriptionProductReplacementParams? | Behavior |
| --- | --- | --- | --- |
| A (base item), B | A (base item) | Yes (use `KEEP_EXISTING`) | Item B is scheduled for deferred removal. Item A is retained. Users would retain their current pricing for item A including any remainder of introductory payments they got at signup time. |
| A | A (base item), B | Yes (use `KEEP_EXISTING` for A) | Item B is added immediately with a prorated charge. Item A is retained. Users would retain their current pricing for item A including any remainder of introductory payments they got at signup time. |
| A (base item), B | A (base item), C | Yes (use `KEEP_EXISTING` for A) | B is scheduled for deferred removal. C is added immediately with a prorated charge. Item A is retained. Users would retain their current pricing for item A including any remainder of introductory payments they got at signup time. |
| A (base item), B | B (base item) | No | A is scheduled for a deferred removal. |
| A (base item), B | C (base item) | Yes | The replacement for A -> C depends on `SubscriptionProductReplacementParams replacementMode` B is scheduled for deferred removal. |
| A (base item), B | C (base item), B | Yes | The replacement for A -> C depends on `SubscriptionProductReplacementParams replacementMode`. To keep item B unchanged, set its replacement mode as `KEEP_EXISTING`. |
| A (base item), B | C (base item), D | Yes | The replacement for A -> C depends on `SubscriptionProductReplacementParams replacementMode`. B is scheduled for deferred removal. D is added immediately with a prorated charge. |
| A (base item), B | A (base item), C | Yes | The replacement for A -> A and B -> C depends on the replacement mode provided in `SubscriptionProductReplacementParams replacementMode` in each `ProductDetailsParams`. To keep item A unchanged set its replacement mode as `KEEP_EXISTING`. |
| A (base item), B, C | D (base item), B, C | Yes | The replacement for A->D and B->B, C->C depends on the replacement mode provided in `SubscriptionProductReplacementParams replacementMode` in each `ProductDetailsParams`. To keep items B and C unchanged, set their replacement mode as `KEEP_EXISTING`. |

#### When using SubscriptionUpdateParams

| Existing items | Modified items | Do you need to set the replacement information? | Behavior |
| --- | --- | --- | --- |
| A (base item), B | A (base item) | No | Item B is scheduled for deferred removal. Item A's behaviour depends on the [Base plan and offer changes](<https://support.google.com/googleplay/android-developer/answer/12154973>) setting of the base plan. The pricing for item A is updated to the latest price and users may lose any introductory payments they got during signup based on offer eligibility criteria. |
| A | A (base item), B | No | Item B is added immediately with a prorated charge. Item A's behaviour depends on the [Base plan and offer changes](<https://support.google.com/googleplay/android-developer/answer/12154973>) setting of the base plan. The pricing for item A is updated to the latest price and users may lose any introductory payments they got during signup based on offer eligibility criteria. |
| A (base item), B | A (base item), C | No | B is scheduled for deferred removal. C is added immediately with a prorated charge. Item A's behaviour depends on the [Base plan and offer changes](<https://support.google.com/googleplay/android-developer/answer/12154973>) setting of the base plan. |
| A (base item), B | B (base item) | No | A is scheduled for a deferred removal. |
| A (base item), B | C (base item) | Yes | The replacement for A -> C depends on `setSubscriptionReplacementMode` (deprecated in PBL 8.1). B is scheduled for deferred removal. |
| A (base item), B | C (base item), B | Yes | The replacement for A -> C depends on `setSubscriptionReplacementMode` (deprecated in PBL 8.1). |
| A (base item), B | C (base item), D | Yes | The replacement for A -> C depends on `setSubscriptionReplacementMode` (deprecated in PBL 8.1). B is scheduled for deferred removal. D is added immediately with a prorated charge. |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscription-with-addons).
