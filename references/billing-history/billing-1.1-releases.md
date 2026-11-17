## Play Billing Library 1.1 Release

Version 1.1 of the Google Play Billing library is now available. This version contains the following changes.

### Summary of changes

- Added support to specify a proration mode in [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) when upgrading/downgrading an existing subscription.
- The `replaceSkusProration` boolean flag in [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) is no longer supported. Use `replaceSkusProrationMode` instead.
- [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) now triggers a callback for failed responses.

### Behavior changes

Version 1.1 of the Google Play Billing library contains the following behavior changes.

#### Developers can set `replaceSkusProrationMode` in [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams>) class

A `ProrationMode` provides further details on the type of proration when upgrading or downgrading a user's subscription.

**Kotlin**

```kotlin
BillingFlowParams.newBuilder()
    .setSku(skuId)
    .setType(billingType)
    .setOldSku(oldSku)
    .setReplaceSkusProrationMode(replaceSkusProrationMode)
    .build()
```

**Java**

```java
BillingFlowParams.newBuilder()
    .setSku(skuId)
    .setType(billingType)
    .setOldSku(oldSku)
    .setReplaceSkusProrationMode(replaceSkusProrationMode)
    .build();
```

Google Play supports following proration modes:

| `IMMEDIATE_WITH_TIME_PRORATION` | Replacement takes effect immediately, and the new expiration time will be prorated and credited or charged to the user. This is the current default behavior. |
| --- | --- |
| `IMMEDIATE_AND_CHARGE_PRORATED_PRICE` | Replacement takes effect immediately, and the billing cycle remains the same. The price for the remaining period will be charged. **Note**: This option is only available for subscription upgrade. |
| `IMMEDIATE_WITHOUT_PRORATION` | Replacement takes effect immediately, and the new price will be charged on next recurrence time. The billing cycle stays the same. |

### `replaceSkusProration` is no longer supported in [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.html>) class

Developers used to be able to set a boolean flag to charge a prorated amount for a subscription upgrade request. Given that we are supporting `ProrationMode`, which contains more detailed proration instruction, this boolean flag is no longer supported.

### [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.html#launchBillingFlow(android.app.Activity,%20com.android.billingclient.api.BillingFlowParams)>) now triggers a callback for failed responses

The Billing Library will always trigger the [`PurhcasesUpdatedListener`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener>) callback and return a [`BillingResponse`](<https://developer.android.com/reference/com/android/billingclient/api/BillingResult>) asynchronously. The synchronous return value of [`BillingResponse`](<https://developer.android.com/reference/com/android/billingclient/api/BillingResult>) is kept as well.

### Bug fixes

- Properly exits early in async methods when service is disconnected.
- [`Builder`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder>) param objects no longer mutates built objects.
- Issue [68087141](<https://issuetracker.google.com/issues/68087141>): [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) now trigger callback for failed responses.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
