## Google Play Billing Library 2.0 Release

Version 2.0 of the Google Play Billing library is now available. This version contains the following changes.

### Purchases must be acknowledged within three days

> **Note:** This section describes a new requirement for acknowledging all purchases. If you are already consuming purchases using `consumeAsync()`, you don't need to make any further changes if you consume purchases within 3 days, as `consumeAsync()` automatically acknowledges a purchase. Failure to properly acknowledge purchases will result in purchases being refunded.

> **Note:** This requirement applies only to apps that use the Google Play Billing Library version 2.0 and newer. This requirement doesn't apply if you use an older version of the Google Play Billing Library, or if you use the AIDL API.

Google Play supports purchasing products from inside of your app (in-app) or outside of your app (out-of-app). In order for Google Play to ensure a consistent purchase experience regardless of where the user purchases your product, you must acknowledge all purchases received through the Google Play Billing Library as soon as possible after granting entitlement to the user. If you don't acknowledge a purchase within three days, the user automatically receives a refund, and Google Play revokes the purchase. For [pending transactions](<https://developer.android.com/google/play/billing/release-notes?hl=en#2_0_pending>) (new in version 2.0), the three-day window starts when the purchase has moved to the `PURCHASED` state and does not apply while the purchase is in a `PENDING` state.

For subscriptions, you must acknowledge any purchase that has a new purchase token. This means that all initial purchases, plan changes, and re-signups need to be acknowledged, but you don't need to acknowledge subsequent renewals. To determine if a purchase needs acknowledgment, you can check the acknowledgement field in the purchase.

The `Purchase` object now includes an [`isAcknowledged()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#isacknowledged>) method that indicates whether a purchase has been acknowledged. In addition, the Google Play Developer API includes acknowledgement boolean values for both [`Purchases.products`](<https://developers.google.com/android-publisher/api-ref/purchases/products>) and [`Purchases.subscriptions`](<https://developers.google.com/android-publisher/api-ref/purchases/subscriptions>). Before acknowledging a purchase, be sure to use these methods to determine if the purchase has already been acknowledged.

You can acknowledge a purchase by using one of the following methods:

- For consumable products, use `consumeAsync()`, found in the client API.
- For products that aren't consumed, use `acknowledgePurchase()`, found in the client API.
- A new `acknowledge()` method is also available in the Server API.

### BillingFlowParams.setSku() has been removed

The previously-deprecated `BillingFlowParams#setSku()` method has been removed in this release. Before rendering products in a purchase flow, you must now call [`BillingClient.querySkuDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryskudetailsasync>), passing the resulting [`SkuDetails`](<https://developer.android.com/reference/com/android/billingclient/api/SkuDetails>) object to [`BillingFlowParams.Builder.setSkuDetails()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setskudetails>).

> **Note:** Caching `SkuDetails` between user sessions is not recommended, as `SkuDetails` objects are valid only for a limited time before you must refresh them again by calling `querySkuDetailsAsync()`.

For code examples, see [Use the Google Play Billing Library](<https://developer.android.com/google/play/billing/billing_library_overview>).

### Developer payload is supported

Version 2.0 of the Google Play Billing library adds support for *developer payload*, arbitrary strings that can be attached to purchases. You can attach a developer payload parameter to a purchase, but only when the purchase is acknowledged or consumed. This is unlike developer payload in AIDL, where the payload could be specified when launching the purchase flow. Because purchases can now be initiated [from outside of your app](<https://developer.android.com/google/play/billing/release-notes?hl=en#2_0_acknowledge>), this change ensures that you always have an opportunity to add a payload to purchases.

To access the payload in the new library, `Purchase` objects now include a [`getDeveloperPayload()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getdeveloperpayload>) method.

> **Note:** You cannot modify a payload after it is assigned.

### Consistent offers

> **Note:** This feature is being tested, and general availability is not guaranteed.

When you offer a discounted SKU, Google Play now returns the original price of the SKU so that you can show users that they are receiving a discount.

[`SkuDetails`](<https://developer.android.com/reference/com/android/billingclient/api/SkuDetails>) contains two new methods for retrieving the original SKU price:

- [`getOriginalPriceAmountMicros()`](<https://developer.android.com/reference/com/android/billingclient/api/SkuDetails#getOriginalPriceAmountMicros()>)

  - returns the unformatted original price of the SKU before discount.
- [`getOriginalPrice()`](<https://developer.android.com/reference/com/android/billingclient/api/SkuDetails#getOriginalPrice()>)

  - returns the original price with additional currency formatting.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
