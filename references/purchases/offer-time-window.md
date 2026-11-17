## Get the valid time window of an offer

You can use `OneTimePurchaseOfferDetails.getValidTimeWindow()` method to get the valid time window for an offer. This object contains the time window start and end time in milliseconds.

The following sample shows how to get the valid time window of an offer:

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
            if (oneTimePurchaseOfferDetails.getValidTimeWindow() != null) {
              // process the returned startTimeMillis and endTimeMillis.
              ValidTimeWindow validTimeWindow =
                  oneTimePurchaseOfferDetails.getValidTimeWindow();
              long startTimeMillis = validTimeWindow.getStartTimeMillis();
              long endTimeMillis = validTimeWindow.getEndTimeMillis();
              // …
            }
          }
        }
      }
    });
    
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers).
