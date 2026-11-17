##### Example 2: Retrieve discounted offer's absolute discount

The following example shows how to get the discounted offer's original full price and its absolute discount in micros. Note that the absolute discount in micros information is only returned for discounted offers. Either the absolute discount or percentage discount must be specified for a discount offer.

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
            long discountedOfferPriceMicros =
                oneTimePurchaseOfferDetails.getPriceAmountMicros();
            // process the returned fullPriceMicros and absolute DiscountAmountMicros.
            if (oneTimePurchaseOfferDetails.getFullPriceMicros() != null) {
              long fullPriceMicros = oneTimePurchaseOfferDetails.getFullPriceMicros();
            }
            if (oneTimePurchaseOfferDetails.getDiscountDisplayInfo() != null) {
              long discountAmountMicros =
                  oneTimePurchaseOfferDetails
                      .getDiscountDisplayInfo()
                      .getDiscountAmount()
                      .getDiscountAmountMicros();
            }
            // …
          }
        }
      }
    });
    
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers).
