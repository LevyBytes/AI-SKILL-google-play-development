## Google Play Billing Library 6.2.1 Release

Version 6.2.1 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- Fixed a bug in [`BillingClient.showAlternativeBillingOnlyInformationDialog()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#showAlternativeBillingOnlyInformationDialog(android.app.Activity,%20com.android.billingclient.api.AlternativeBillingOnlyInformationDialogListener)>) where the [`AlternativeBillingOnlyInformationDialogListener`](<https://developer.android.com/reference/com/android/billingclient/api/AlternativeBillingOnlyInformationDialogListener>) may not be called in certain cases when the dialog completes.

## Google Play Billing Library 6.2.0 Release

Version 6.2.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- Added APIs to support [external offers](<https://developer.android.com/google/play/billing/external>)

  - Added [`BillingClient.Builder.enableExternalOffer()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableExternalOffer()>) to enable the ability to provide external offers.
  - Added [`BillingClient.isExternalOfferAvailableAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isExternalOfferAvailableAsync(com.android.billingclient.api.ExternalOfferAvailabilityListener)>) to check the availability of providing external offers functionality.
  - Added [`BillingClient.showExternalOfferInformationDialog()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#showExternalOfferInformationDialog(android.app.Activity,%20com.android.billingclient.api.ExternalOfferInformationDialogListener)>) to show an information dialog to users before leading users outside the app.
  - Added [`BillingClient.createExternalOfferReportingDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createExternalOfferReportingDetailsAsync(com.android.billingclient.api.ExternalOfferReportingDetailsListener)>) to create a payload required to report transactions made through external offers.

## Google Play Billing Library 6.1.0 Release

Version 6.1.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- Added APIs to support [alternative billing only (i.e. without user choice)](<https://developer.android.com/google/play/billing/alternative>)

  - Added [`BillingClient.Builder.enableAlternativeBillingOnly()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableAlternativeBillingOnly()>) to functionally enable the ability to offer alternative billing only.
  - Added [`BillingClient.isAlternativeBillingOnlyAvailableAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isAlternativeBillingOnlyAvailableAsync(com.android.billingclient.api.AlternativeBillingOnlyAvailabilityListener)>) to check the availability of offering alternative billing only.
  - Added [`BillingClient.showAlternativeBillingOnlyInformationDialog()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#showAlternativeBillingOnlyInformationDialog(android.app.Activity,%20com.android.billingclient.api.AlternativeBillingOnlyInformationDialogListener)>) to show an information dialog to inform users when alternative billing only is being used.
  - Added [`BillingClient.createAlternativeBillingOnlyReportingDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createAlternativeBillingOnlyReportingDetailsAsync(com.android.billingclient.api.AlternativeBillingOnlyReportingDetailsListener)>) to create a payload required to report transactions made through alternative billing only.
- Updated the user choice billing APIs

  - Added [`UserChoiceBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/UserChoiceBillingListener>) to replace [AlternativeBillingListener](<https://developer.android.com/reference/com/android/billingclient/api/AlternativeBillingListener>) which has been marked as deprecated.
  - Added [`UserChoiceDetails`](<https://developer.android.com/reference/com/android/billingclient/api/UserChoiceDetails>) to replace [`AlternativeChoiceDetails`](<https://developer.android.com/reference/com/android/billingclient/api/AlternativeChoiceDetails>) which has been marked as deprecated.
  - Added [`BillingClient.Builder.enableUserChoiceBilling()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableUserChoiceBilling(com.android.billingclient.api.UserChoiceBillingListener)>) to replace [`BillingClient.Builder.enableAlternativeBilling()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableAlternativeBilling(com.android.billingclient.api.AlternativeBillingListener)>) which has been marked as deprecated.
- Added [`BillingClient.getBillingConfigAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#getBillingConfigAsync(com.android.billingclient.api.GetBillingConfigParams,%20com.android.billingclient.api.BillingConfigResponseListener)>) to retrieve Google Play country.

## Google Play Billing Library 6.0.1 Release

Version 6.0.1 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

Update Play Billing Library to be compatible with Android 14.

## Google Play Billing Library 6.0 Release

Version 6.0.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- Added new [`ReplacementMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode>) enum to replace [`ProrationMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProrationMode>).

  Note that `ProrationMode` is still available for backward compatibility reasons.
- Removed order ID for [`PENDING`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase.PurchaseState#PENDING()>) purchases.

  Previously, the order ID would always be created even if the purchase was pending. Starting with version 6.0.0, an order ID will not be created for pending purchases, and for these purchases, the order ID will be populated after the purchase is moved to the [`PURCHASED`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase.PurchaseState#PURCHASED()>) state.
- Removed `queryPurchases` and `launchPriceConfirmationFlow` methods.

  The `queryPurchases` and `launchPriceConfirmationFlow` methods that have previously been marked as deprecated have now been removed in Play Billing Library 6.0.0. Developers should use [`queryPurchasesAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>) instead of `queryPurchases`. For `launchPriceConfirmationFlow` alternatives, see [Price changes](<https://developer.android.com/google/play/billing/price-changes>).
- Added new network error response code.

  A new network error response code, [`NETWORK_ERROR`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#NETWORK_ERROR()>), has been added starting with PBL version 6.0.0. This code is returned when an error occurs due to a network connection issue. These network connection errors were previously reported as `SERVICE_UNAVAILABLE`.
- Updated [`SERVICE_UNAVAILABLE`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_UNAVAILABLE()>) and [`SERVICE_TIMEOUT`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_TIMEOUT()>).

  Starting with PBL version 6.0.0, errors due to timeout in processing will be returned as `SERVICE_UNAVAILABLE` instead of the current `SERVICE_TIMEOUT`.

  The behavior does not change in earlier versions of PBL.
- Removed [`SERVICE_TIMEOUT`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_TIMEOUT()>).

  Starting with PBL version 6.0.0, `SERVICE_TIMEOUT` will no longer be returned. Previous versions of PBL will still return this code.
- Added additional logging.

  The Play Billing Library 6 release includes additional logging, which provides insight into API usage (such as success and failure) and service connection issues. This information will be used to improve the performance of the Play Billing Library and provide better support for errors.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
