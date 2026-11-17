## Country and region eligibility

You can choose the countries or regions where purchase option offer or discount offer will be available to users. Google Play will evaluate user eligibility based on Play country. When you configure regional availability for an offer, it will only be returned as part of `getOneTimePurchaseOfferDetailsList()` if the user is in a targeted country or region, otherwise it won't be part of the list of offers returned when you call `queryProductDetailsAsync()`.

> **Note:** Country or regional eligibility for a user may change between you displaying the eligible products for them and launching the purchase flow in some rare cases. For example, the user could change their country. Such a change may make the previously returned offer ineligible in the user's new country or region. Google Play will double check the user's country eligibility when the billing flow is launched to make sure country eligibility is enforced. If the user is not eligible, the `PurchasesUpdatedListener` will get an `ITEM_UNAVAILABLE` response code.

## Offer tags

The following sample shows how to retrieve the offer tags associated with an offer.

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
            // process the returned offer tags.
            ImmutableList<String> offerTags =
                oneTimePurchaseOfferDetails.getOfferTagsList();
            // …
          }
        }
      }
    });
    
    
```

### Inheritance of offer tags

You can set offer tags for either product, purchase option or discount offer. Discount offers inherit the offer tags from its purchase option offer. Similarly, if offer tags are specified at product level, both purchase option offer and discount offers inherit the product offer tags.

For example, Super screensavers has two offers for the screensaver product; purchase option screensaver and a discount screensaver.

- Super screensaver has the product offer tag `SSProductTag`.
- The purchase option screensaver has the offer tag `SSPurchaseOptionTag`.
- The discount screensaver has the offer tag `SSDiscountOfferTag`.

In this example, the `oneTimePurchaseOfferDetails.getOfferTagsList()` method for the purchase option offer returns `SSProductTag` and `SSPurchaseOptionTag`. For the discount offer, the method returns `SSProductTag`, `SSPurchaseOptionTag`, and `SSDiscountOfferTag`.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers).
