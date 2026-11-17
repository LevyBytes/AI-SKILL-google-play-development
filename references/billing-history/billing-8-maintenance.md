## Google Play Billing Library 8.3.0 Release

Version 8.3.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- New APIs for [external payments](<https://developer.android.com/google/play/billing/externalpaymentlinks>):

  - Added classes to support external payments flow:

    - [`BillingProgram.EXTERNAL_PAYMENTS`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingProgram#EXTERNAL_PAYMENTS()>)
    - [`EnableBillingProgramParams`](<https://developer.android.com/reference/com/android/billingclient/api/EnableBillingProgramParams>)
    - [`DeveloperBillingOptionParams`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperBillingOptionParams>)
    - [`DeveloperProvidedBillingDetails`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails>)
    - [`DeveloperProvidedBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener>)
  - Added [`enableBillingProgram(EnableBillingProgramParams)`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(com.android.billingclient.api.EnableBillingProgramParams)>) to enable external payments.
  - Added [`BillingFlowParams.Builder.enableDeveloperBillingOption`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#enableDeveloperBillingOption(com.android.billingclient.api.DeveloperBillingOptionParams)>) to launch the external payments flow.
- Improved error categorization for external payment flow drop-offs:

  - If a user navigates away from the purchase flow to complete payment on an external app (such as an e-wallet) and abandons the transaction without returning, the response code returned to the client is now `BillingResponseCode.USER_CANCELED` (1) with debug message `BILLING_ACTIVITY_PAUSED` (previously defaulted to `BillingResponseCode.ERROR` (6)).

## Google Play Billing Library 8.2.1 Release

Version 8.2.1 of the Google Play Billing Library and Kotlin extensions are now available.

### Bug fixes

- Fixed a bug in [`isBillingProgramAvailableAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)>) and [`createBillingProgramReportingDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)>). Update to version 8.2.1 to use these APIs introduced in 8.2.0.

## Google Play Billing Library 8.2.0 Release

Version 8.2.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- New APIs for [external content links](<https://developer.android.com/google/play/billing/externalcontentlinks>) and [external offers](<https://developer.android.com/google/play/billing/external>):

  - Added [`enableBillingProgram`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableBillingProgram(int)>) to setup the `BillingClient` for these programs.
  - Added [`isBillingProgramAvailableAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isBillingProgramAvailableAsync(int,com.android.billingclient.api.BillingProgramAvailabilityListener)>) to determine user eligibility.
  - Added [`createBillingProgramReportingDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)>) to create the external transaction token that must be used for reporting.
  - Added [`launchExternalLink`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchExternalLink(android.app.Activity,com.android.billingclient.api.LaunchExternalLinkParams,com.android.billingclient.api.LaunchExternalLinkResponseListener)>) to initiate the external link to a digital content offer or an app download.
- Changes to the [external offers program](<https://developer.android.com/google/play/billing/external>):

  - There are policy changes for the external offers program. See [program changes](<https://support.google.com/googleplay/android-developer/answer/16505463>) for details. To understand how to launch external offer flows with the new APIs, see the [integration guide](<https://developer.android.com/google/play/billing/external/integration>).
  - Deprecated the [`BillingClient.Builder.enableExternalOffer`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableExternalOffer()>) API.
  - Deprecated the [`isExternalOfferAvailableAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isExternalOfferAvailableAsync(com.android.billingclient.api.ExternalOfferAvailabilityListener)>) API.
  - Deprecated the [`createExternalOfferReportingDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createExternalOfferReportingDetailsAsync(com.android.billingclient.api.ExternalOfferReportingDetailsListener)>) API.
  - Deprecated the [`showExternalOfferInformationDialog`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#showExternalOfferInformationDialog(android.app.Activity,com.android.billingclient.api.ExternalOfferInformationDialogListener)>) API.

## Google Play Billing Library 8.1.0 Release

Version 8.1.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- Suspended subscriptions

  A new parameter has been added to the [`BillingClient.queryPurchasesAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,com.android.billingclient.api.PurchasesResponseListener)>) method to include suspended subscriptions when querying for subscriptions. Suspended subscriptions are still attributed to the user, but are not active, either because the user paused the subscription or their renewal payment method was declined.

  The [`Purchase`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase>) object returned in the listener will return `isSuspended() = true` for any suspended subscriptions. In this case, you shouldn't grant access to the purchased subscription, and instead guide the user to the [subscriptions center](<https://play.google.com/store/account/subscriptions>) where the user can manage their payment methods or pause state to re-activate their subscription.
- Updates to [subscriptions](<https://developer.android.com/google/play/billing/subscriptions>):

  - The [`BillingFlowParams.ProductDetailsParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProductDetailsParams>) object now has the `setSubscriptionProductReplacementParams()` method in which you can specify product level replacement information.
  - The `SubscriptionProductReplacementParams` object has two setter methods:

    - `setOldProductId`: The old product that needs to be replaced by the product in current [`ProductDetails`](<https://developer.android.com/reference/com/android/billingclient/api/ProductDetails>).
    - `setReplacementMode`: This is the item level replacement mode. The modes are essentially the same as SubscriptionUpdateParams, but the value mapping has been updated. A new replacement mode `KEEP_EXISTING` is introduced that lets you keep the existing payment schedule unchanged for an item.
  - [SubscriptionUpdateParams setSubscriptionReplacementMode](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode(int)>) will be deprecated. You should use `SubscriptionProductReplacementParams.setReplacementMode` instead.
- Updated `minSdkVersion` to 23.
- Enabled [pre-order APIs for one-time products](<https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers#pre-order>)

  The `ProductDetails.oneTimePurchaseOfferDetails.getPreorderDetails()` API that gets the pre-order details is now available for use.
- Google Play Billing Library now supports [Kotlin version 2.2.0](<https://kotlinlang.org/docs/whatsnew22.html>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
