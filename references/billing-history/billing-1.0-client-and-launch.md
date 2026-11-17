## Google Play Billing Library 1.0 Release

Version 1.0 of the Google Play Billing library is now available. This version contains the following changes.

### Important changes

- Embedded billing permission inside library's manifest. It's not necessary to add the `com.android.vending.BILLING` permission inside Android manifest anymore.
- New builder added to [`BillingClient.Builder`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder.html>) class.
- Introduced builder pattern for [`SkuDetailsParams`](<https://developer.android.com/reference/com/android/billingclient/api/SkuDetailsParams.html>) class to be used on methods to query SKUs.
- Several API methods were updated for consistency (the same return argument names and order).

### Behavior changes

Version 1.0 of the Google Play Billing library contains the following behavior changes.

#### BillingClient.Builder class

[`BillingClient.Builder`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder.html>) is now initialized via the newBuilder pattern:

**Kotlin**

```kotlin
billingClient = BillingClient.newBuilder(context).setListener(this).build()
```

**Java**

```java
billingClient = BillingClient.newBuilder(context).setListener(this).build();
```

#### launchBillingFlow method is now called using a BillingFlowParams class

To initiate the billing flow for a purchase or subscription, the [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) method receives a [`BillingFlowParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.html>) instance initialized with parameters specific to the request:

**Kotlin**

```kotlin
BillingFlowParams.newBuilder().setSku(skuId)
        .setType(billingType)
        .setOldSku(oldSku)
        .build()

// Then, use the BillingFlowParams to start the purchase flow
val responseCode = billingClient.launchBillingFlow(builder.build())
```

**Java**

```java
BillingFlowParams.newBuilder().setSku(skuId)
                              .setType(billingType)
                              .setOldSku(oldSku)
                              .build();

// Then, use the BillingFlowParams to start the purchase flow
int responseCode = billingClient.launchBillingFlow(builder.build());
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
