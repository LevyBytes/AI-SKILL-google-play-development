## Google Play Billing Library 5.2.1 Release

Version 5.2.1 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

Update Play Billing Library to be compatible with Android 14.

## Google Play Billing Library 5.2 Release

Version 5.2.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- Added classes to support alternative billing flows on mobile/tablet for users in South Korea:

  - [`AlternativeBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/AlternativeBillingListener>)
  - [`AlternativeChoiceDetails`](<https://developer.android.com/reference/com/android/billingclient/api/AlternativeChoiceDetails>)
  - [`AlternativeChoiceDetails.Product`](<https://developer.android.com/reference/com/android/billingclient/api/AlternativeChoiceDetails.Product>)
- Added [`BillingFlowParams.SubscriptionUpdateParams.Builder.setOriginalExternalTransactionId()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOriginalExternalTransactionId(java.lang.String)>) method to specify the external transaction id of the originating subscription.
- Added [`BillingClient.Builder.enableAlternativeBilling()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableAlternativeBilling(com.android.billingclient.api.AlternativeBillingListener)>) method to allow users in South Korea to select an alternative billing option.

## Google Play Billing Library 5.1 Release

Version 5.1.0 of the Google Play Billing Library and Kotlin extensions are now available.

This version contains the following changes.

### Summary of changes

- Added [`ProductDetails.SubscriptionOfferDetails.getOfferId()`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails.SubscriptionOfferDetails#getOfferId()>) method to retrieve the offer ID.
- Added [`ProductDetails.SubscriptionOfferDetails.getBasePlanId()`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails.SubscriptionOfferDetails#getBasePlanId()>) method to retrieve the base plan ID.
- Updated the `targetSdkVersion` to 31.

## Google Play Billing Library 5.0 Release

Version 5.0.0 of the Google Play Billing Library and Kotlin extensions are now available.

This version contains the following changes.

### Summary of changes

- Introduced a new model for subscriptions, including new entities that enable you to create multiple offers for a single subscription product. For more information, see the [migration guide](<https://developer.android.com/google/play/billing/migrate-gpblv5>).
- Added [`BillingClient.queryProductDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)>) to replace `BillingClient.querySkuDetailsAsync()`.
- Added `setIsOfferPersonalized()` method for EU personalized pricing disclosure requirements. To learn more about how to use this method, see [Indicate a personalized price](<https://developer.android.com/google/play/billing/integrate#personalized-price>).
- Removed `queryPurchases()`, which was previously deprecated and replaced by queryPurchasesAsync introduced in Google Play Billing Library 4.0.0.
- `launchPriceChangeFlow` has been deprecated and will be removed in a future release. To learn more about alternatives, see [Launch a price change confirmation flow](<https://developer.android.com/google/play/billing/price-changes>).
- Removed [`setVrPurchaseFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setVrPurchaseFlow(boolean)>), which was previously used when instantiating a purchase flow. In previous versions, this method redirected the user to complete the purchase on their Android-powered device. Once you remove this method, users will complete the purchase through the standard purchase flow.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
