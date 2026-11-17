### Discount offer

This section describes how you can configure discount offers for your one-time products.

There are four different parameters you can configure in a one-time product discount offer:

- Discounted offer price: Specifies details about either the percentage discounted off or absolute price off the original price.
- Countries or Regions eligibility: Specifies the availability of one-time product offers in a country or a region.
- Purchase limit (optional): Lets you to determine how many times a user can redeem the same offer. If a user exceeds the purchase limit, the user will be ineligible for the offer.
- Limited time (optional): Specifies the time period in which the offer is available. Outside of the time period, the offer is ineligible for purchase.

#### Retrieve discounted offer price information

For a discounted offer, you can retrieve the percentage of discount or the absolute discount offered.

##### Example 1: Retrieve discounted offer's percentage discount

The following sample shows how to get the discounted offer's original full price and its percentage discount. Note that the percentage discount information is only returned for discounted offers.

#### Java

```java
billingClient.queryProductDetailsAsync(
    queryProductDetailsParams,
    new ProductDetailsResponseListener() {
      public void onProductDetailsResponse(
          BillingResult billingResult, QueryProductDetailsResult productDetailsResult){
        // check billingResult
        // …
        // process productDetailsList returned by QueryProductDetailsResult
        for (ProductDetails productDetails : productDetailsResult.getProductDetailsList()) {
          for (OneTimePurchaseOfferDetails oneTimePurchaseOfferDetails :
              productDetails.getOneTimePurchaseOfferDetailsList()) {
            long discountedOfferPriceMicros =
                oneTimePurchaseOfferDetails.getPriceAmountMicros();
            // process the returned fullPriceMicros and percentageDiscount.
            if (oneTimePurchaseOfferDetails.getFullPriceMicros() != null) {
              long fullPriceMicros = oneTimePurchaseOfferDetails.getFullPriceMicros();
            }
            if (oneTimePurchaseOfferDetails.getDiscountDisplayInfo() != null) {
              long percentageDiscount =
                  oneTimePurchaseOfferDetails
                      .getDiscountDisplayInfo()
                      .getPercentageDiscount();
            }
            // …
          }
        }
      }
    });
    
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers).
