This document contains release notes for the Google Play Billing Library.

## Google Play Billing Library 9.1.0 Release

Version 9.1.0 of the Google Play Billing Library and Kotlin extensions are now available.

### Summary of changes

- New APIs for [Billing Choice](<https://developer.android.com/google/play/billing/billingchoice>):

  - Added [`BillingClient.getBillingChoiceInfoAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#getBillingChoiceInfoAsync(com.android.billingclient.api.GetBillingChoiceInfoParams,com.android.billingclient.api.BillingChoiceInfoResponseListener)>) to retrieve information about billing choices available to the user.
  - Added [`BillingChoiceInfo`](<https://developer.android.com/reference/com/android/billingclient/api/BillingChoiceInfo>) class which contains the response details, including image URLs and loyalty information.
  - Added [`GetBillingChoiceInfoParams`](<https://developer.android.com/reference/com/android/billingclient/api/GetBillingChoiceInfoParams>) to configure the request.
  - Added [`BillingChoiceInfoResponseListener`](<https://developer.android.com/reference/com/android/billingclient/api/BillingChoiceInfoResponseListener>) to receive the callback.
  - Added Kotlin extension `BillingClient.getBillingChoiceInfo()` suspend function.
  - Added [`BillingClient.showBillingProgramInformationDialog()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#showBillingProgramInformationDialog(android.app.Activity,com.android.billingclient.api.BillingProgramInformationDialogParams,com.android.billingclient.api.BillingProgramInformationDialogListener)>) to show an information dialog for a billing program.
  - Added [`BillingProgramInformationDialogParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingProgramInformationDialogParams>) to configure the dialog.
  - Added [`BillingProgramInformationDialogListener`](<https://developer.android.com/reference/com/android/billingclient/api/BillingProgramInformationDialogListener>) to receive the callback.
  - Added [`BillingProgramAvailabilityDetails.BillingChoiceAvailabilityDetails`](<https://developer.android.com/reference/com/android/billingclient/api/BillingProgramAvailabilityDetails.BillingChoiceAvailabilityDetails>) to provide details about billing choice availability.
  - Added [`ChoiceScreenType`](<https://developer.android.com/reference/com/android/billingclient/api/BillingProgramAvailabilityDetails.BillingChoiceAvailabilityDetails.ChoiceScreenType>) to specify the type of choice screen.

## Google Play Billing Library 9.0.0 Release

Version 9.0.0 of the Google Play Billing Library and Kotlin extensions are now available. See the [PBL 9 migration guide](<https://developer.android.com/google/play/billing/migrate-pbl-latest>) if you want to migrate from the previous versions of PBL.

### Summary of changes

- **Updated error codes for blocked Play Store activity**: Error codes for blocked Play Store apps have been updated. For instances where the Play Store app is blocked by the system (for example, in OEM-customized kids mode), the response code has changed from `ERROR` to `BILLING_UNAVAILABLE`. Additionally, the `BillingResult` for such cases now provides a *Play Store is blocked* debug message.

  > **Note:** For this feature to work, you need [AndroidX.core library](<https://developer.android.com/jetpack/androidx/releases/core#1.9.0>) version 1.9 or later.
- **Nullability update for developer-provided billing**: The [`DeveloperProvidedBillingDetails.getLinkUri()`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails#getLinkUri()>) method has been updated to be `@Nullable`. This change supports scenarios where the direct link URI for external payments is unavailable during the payment selection stage.

  To handle this change safely, ensure your integration code handles both `null` and empty string (`""`) values from the [`DeveloperProvidedBillingDetails.getLinkUri()`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails#getLinkUri()>) method before parsing or launching browser intents.
- Updated `targetSdkVersion` to 35.
- You can now use [in-app messaging](<https://developer.android.com/google/play/billing/subscriptions#in-app-messaging>) to notify users of an upcoming opt-in price increase. This lets users confirm the price increase without leaving the app. The message for an outstanding opt-in price increase is shown starting on the first day the user can accept the price increase, and the message is shown a maximum of once every 7 days.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
