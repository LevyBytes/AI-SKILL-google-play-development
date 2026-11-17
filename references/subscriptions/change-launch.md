### Trigger subscription changes in-app

Your app can offer users an upgrade or downgrade using the same steps as with [launching a purchase flow](<https://developer.android.com/google/play/billing/integrate#launch>). However, when upgrading or downgrading, you need to provide details of the current subscription, the future (upgraded or downgraded) subscription, and the replacement mode to use.

#### Use SubscriptionProductReplacementParams for replacement (preferred)

The following example shows how to update a subscription by using `SubscriptionProductReplacementParams`.

- The [`BillingFlowParams.ProductDetailsParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams>) object now has a `setSubscriptionProductReplacementParams()` method to specify product level replacement information.
- `SubscriptionProductReplacementParams` has two setter methods:

  - `setOldProductId:`This is the old product to be replaced by the product in current `ProductDetails.`
  - `setReplacementMode:`This is the item level replacement mode. The modes are essentially the same as `SubscriptionUpdateParams`, but the value mapping has been updated.
- The existing purchase level update params `BillingFlowParams.setSubscriptionUpdateParams()` should be constructed with `setOldPurchaseToken()`.
- Once `setSubscriptionProductReplacementParams()` is called for any of the `ProductDetailsParams`, `SubscriptionUpdateParams.setSubscriptionReplacementMode()` will have no effect.

The following code sample demonstrates how to change a subscription plan from (`old_product_1`, `old_product_2`) to (`product_1`, `product_2`, `product_3`). In this scenario, `product_1` replaces `old_product_1`, `product_2` replaces `old_product_2`, and `product_3` is added to the subscription immediately.

**Kotlin**

[Complete kotlin example: Kotlin](<https://developer.android.com/google/play/billing/subscriptions#kotlin>).

**Java**

```java
BillingClient billingClient = …;

int replacementModeForBasePlan =…;
int replacementModeForAddon =…;
// ProductDetails obtained from queryProductDetailsAsync().
ProductDetailsParams productDetails1 =
  ProductDetailsParams.newBuilder()
      .setSubscriptionProductReplacementParams(
           SubscriptionProductReplacementParams.newBuilder()
               .setOldProductId("old_product_id_1")
               .setReplacementMode(replacementModeForBasePlan))
               .build();
ProductDetailsParams productDetails2 =
  ProductDetailsParams.newBuilder()
      .setSubscriptionProductReplacementParams(
           SubscriptionProductReplacementParams.newBuilder()
               .setOldProductId("old_product_id_2")
               .setReplacementMode(replacementModeForAddon))
               .build();
ProductDetailsParams productDetails3 = ...;

ArrayList newProductDetailsList = new ArrayList<>();
newProductDetailsList.add(productDetails1);
newProductDetailsList.add(productDetails2);
newProductDetailsList.add(productDetails3);

BillingFlowParams billingFlowParams =
    BillingFlowParams.newBuilder()
        .setSubscriptionUpdateParams(
          SubscriptionUpdateParams.newBuilder()
              .setOldPurchaseToken(purchaseTokenOfExistingSubscription)
             .build())
        .setProductDetailsParamsList(productDetailsList)
        .build();

billingClient.launchBillingFlow(billingFlowParams);
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscriptions).
