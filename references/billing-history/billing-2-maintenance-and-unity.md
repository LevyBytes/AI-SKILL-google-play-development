## Google Play Billing Library 2.2.1 Release

Version 2.2.1 of the Google Play Billing library is now available.

### Bug fixes

- Updated the default version of the Java Play Billing library that the Kotlin extension depends on.

## Google Play Billing Library 2.2.0 release and Unity support

Version 2.2.0 of the Google Play Billing provides functionality that helps developers ensure purchases are attributed to the correct user. These changes replace the need to build custom solutions based on developer payload. As part of this update, the developer payload functionality has been deprecated and will be removed in a future release. For more information, including recommended alternatives, see [Developer payload](<https://developer.android.com/google/play/billing/developer-payload>).

### Google Play Billing Billing Library 2 for Unity

In addition to the current Java and Kotlin versions of Google Play Billing Library 2, we released a version of the library for use with Unity. Game developers using the Unity in-app purchase API can upgrade now to take advantage of all Google Play Billing Library 2 features and to make the subsequent upgrades to future versions of the Google Play Billing Library easier.

To learn more, see [Use Google Play Billing with Unity](<https://developer.android.com/google/play/billing/unity>).

### Summary of changes

- Java Google Play Billing Library

  - In [`AcknowledgePurchaseParams`](<https://developer.android.com/reference/com/android/billingclient/api/AcknowledgePurchaseParams>), deprecated [`setDeveloperPayload()`](<https://developer.android.com/reference/com/android/billingclient/api/AcknowledgePurchaseParams.Builder#setDeveloperPayload(java.lang.String)>) and [`getDeveloperPayload()`](<https://developer.android.com/reference/com/android/billingclient/api/AcknowledgePurchaseParams#getDeveloperPayload()>) methods.
  - In [`ConsumeParams`](<https://developer.android.com/reference/com/android/billingclient/api/ConsumeParams>), deprecated [`setDeveloperPayload()`](<https://developer.android.com/reference/com/android/billingclient/api/ConsumeParams.Builder#setDeveloperPayload(java.lang.String)>) and [`getDeveloperPayload()`](<https://developer.android.com/reference/com/android/billingclient/api/ConsumeParams#getdeveloperpayload>) methods.
  - In [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder>), renamed [`setAccountId()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setAccountId(java.lang.String)>) to [`setObfuscatedAccountId()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedAccountId(java.lang.String)>), and documented length restriction of 64 characters and restriction disallowing Personally Identifiable Information (PII) in this field. [`setAccountId()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setaccountid>) has been marked as deprecated and will be removed in a future library version.
  - In `BillingFlowParams`, added [`setObfuscatedProfileId()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedprofileid>) which works similarly to [`setObfuscatedAccountId()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedAccountId(java.lang.String)>). For more information, see [Developer payload updates and alternatives](<https://developer.android.com/google/play/billing/developer-payload>).
  - In [`Purchase`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase>), added the [`getAccountIdentifiers()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getAccountIdentifiers()>) method to return the obfuscated account identifiers set in `BillingFlowParams`.
  - In [`BillingClient`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient>), the [`loadRewardedSku()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#loadRewardedSku(com.android.billingclient.api.RewardLoadParams,%20com.android.billingclient.api.RewardResponseListener)>) method has been marked deprecated as part of deprecating rewarded SKUs.

## Google Play Billing Library 2.1.0 Release and Kotlin Extension 2.1.0 Release

Version 2.1.0 of the Google Play Billing library and the new Kotlin extension are now available. The Play Billing Library Kotlin extension provides idiomatic API alternatives for Kotlin consumption, featuring better null-safety and coroutines. For code examples, see [Use the Google Play Billing Library](<https://developer.android.com/google/play/billing/billing_library_overview>).

This version contains the following changes.

### Summary of changes

- In [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>), deprecated `setOldSku(String oldSku)` and replaced with `setOldSku(String oldSku, String purchaseToken)`, to disambiguate when multiple accounts on the device own the same sku.

## Google Play Billing Library 2.0.3 Release

Version 2.0.3 of the Google Play Billing library is now available.

### Bug fixes

- Fixed a bug where `querySkuDetailsAsync()` would occasionally fail with code `DEVELOPER_ERROR` instead of returning a successful result.

## Google Play Billing Library 2.0.2 Release

Version 2.0.2 of the Google Play Billing library is now available. This release contains updates to the reference documentation and does not change library functionality.

## Google Play Billing Library 2.0.1 Release

Version 2.0.1 of the Google Play Billing library is now available. This version contains the following changes.

### Bug fixes

- Fixed a bug where debug messages were being returned as `null` in some cases.
- Fixed a potential memory leak issue.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
