## Google Play Billing Library 1.2.2 Release

Version 1.2.2 of the Google Play Billing library is now available. This version contains the following changes.

### Bug fixes

- Fixed a threading issue introduced in v1.2.1. Background calls no longer block the main thread.

### Other changes

- Although using the main thread is still recommended, you can now instantiate the Google Play Billing Library from a background thread.
- Instantiation has been fully migrated to the background thread to reduce the chance of causing ANRs.

## Play Billing Library 1.2.1 Release

Version 1.2.1 of the Google Play Billing library is now available. This version contains the following changes.

### Major changes

- Added support for [rewarded products](<https://developer.android.com/google/play/billing/billing_rewarded_products>). For more information on monetization options, see [Add rewarded-product-specific features](<https://developer.android.com/distribute/best-practices/earn/monetization-options>).

### Other changes

- Added public constructors for `PurchasesResult` and `SkuDetailsResult` to make testing easier.
- `SkuDetails` objects can use a new method, `getOriginalJson()`.
- All AIDL service calls are now handled by background threads.

### Bug fixes

- Null callback listeners are no longer passed into public APIs.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
