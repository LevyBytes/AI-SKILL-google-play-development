## Limited quantity at the discount offer level

You can specify the maximum quantity limit at the discount offer level, that is applied only at the offer level. Here is an example to illustrate:

1. Super screensavers has 2 offers for the screensaver product: purchase option screensaver and discount screensaver.

   1. The purchase option screensaver doesn't have a limited quantity set up.
   2. The discount screensaver has the offer level maximum allowed quantity set to 3.
2. The screensaver product does not have product level maximum allowed quantity, so users can buy unlimited quantities of this product.
3. The user owns 1 discount screensaver, and they plan to buy another one with the discount screensaver.
4. When retrieving the available offers, the LimitedQuantityInfo for the purchase option screensaver is null and the remaining quantity value for the discount screensaver is 2.

The following sample shows how to get the limited quantity at the discount offer level:

#### Java

```java
billingClient.queryProductDetailsAsync(
    queryProductDetailsParams,
    new ProductDetailsResponseListener() {
      public void onProductDetailsResponse(
          BillingResult billingResult, QueryProductDetailsResult productDetailsResult) {
        // check billingResult
        // …
        // process productDetailsList returned by QueryProductDetailsResult
        for (ProductDetails productDetails : productDetailsResult.getProductDetailsList()) {
          for (OneTimePurchaseOfferDetails oneTimePurchaseOfferDetails :
              productDetails.getOneTimePurchaseOfferDetailsList()) {
            if (oneTimePurchaseOfferDetails.getLimitedQuantityInfo() != null) {
              // process the returned maximumQuantity and remainingQuantity.
              LimitedQuantityInfo limitedQuantityInfo =
                  oneTimePurchaseOfferDetails.getLimitedQuantityInfo();
              int maximumQuantity = limitedQuantityInfo.getMaximumQuantity();
              int remainingQuantity = limitedQuantityInfo.getRemainingQuantity();
              // …
            }
          }
        }
      }
    });
    
```

When users use up the maximum quantity redemptions for an offer, the offer isn't returned by the `getOneTimePurchaseOfferDetailsList()` method.

### Calculate redemption limit

The following example shows how to get the limited quantity information on a certain discount offer. You can get the maximum allowed quantity and the remaining quantity for the current user. Note that limited quantity feature is applicable for both the consumable and non-consumable one-time product offers. This feature is supported only at the offer level.

Google Play calculates the remaining quantity by subtracting the user's owned quantity from the maximum allowed quantity you have set up. When counting the user's owned quantity, Google Play considers consumed purchases or pending purchases. Purchases that were canceled, refunded or charged-back don't count towards the user's owned quantity. For example:

1. Super screensavers set up a discount offer with the maximum allowed quantity of one, so users can buy up to one discounted screensaver.
2. The user buys one of the discounted screensaver. If the user then tries to buy the second discounted screensaver, it will error out and the `PurchasesUpdatedListener` will get an ITEM_UNAVAILABLE response code.
3. The user asks for a refund of the originally purchased discounted screensaver, and successfully receives the refund. The user tries to buy one of the discounted screensaver, and the purchase will succeed.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers).
