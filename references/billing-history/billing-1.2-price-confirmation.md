## Google Play Billing Library 1.2 Release

Version 1.2 of the Google Play Billing library is now available. This version contains the following changes.

### Summary of changes

- The Google Play Billing Library is now licensed under the [Android Software Development Kit License Agreement](<https://developer.android.com/studio/terms>).
- Added the `launchPriceChangeConfirmationFlow` API, which prompts users to review a pending change to a subscription price.
- Added support for a new proration mode, `DEFERRED`, when upgrading or downgrading a user's subscription.
- In the `BillingFlowParams` class, replaced `setSku()` with `setSkuDetails()`.
- Minor bug fixes and code optimizations.

#### Price change confirmation

You can now change the price of a subscription in Google Play Console and prompt users to review and accept the new price when they enter your app.

To use this API, create a `PriceChangeFlowParams` object by using the `skuDetails` of the subscription product, and then call `launchPriceChangeConfirmationFlow()`. Implement the `PriceChangeConfirmationListener` to handle the result when the price change confirmation flow finishes, as shown in the following code snippet:

**Kotlin**

```kotlin
val priceChangeFlowParams = PriceChangeFlowParams.newBuilder()
    .setSkuDetails(skuDetailsOfThePriceChangedSubscription)
    .build()

billingClient.launchPriceChangeConfirmationFlow(activity,
        priceChangeFlowParams,
        object : PriceChangeConfirmationListener() {
            override fun onPriceChangeConfirmationResult(responseCode: Int) {
                // Handle the result.
            }
        })
```

**Java**

```java
PriceChangeFlowParams priceChangeFlowParams =
        PriceChangeFlowParams.newBuilder()
    .setSkuDetails(skuDetailsOfThePriceChangedSubscription)
    .build();

billingClient.launchPriceChangeConfirmationFlow(activity,
        priceChangeFlowParams,
        new PriceChangeConfirmationListener() {
            @Override
            public void onPriceChangeConfirmationResult(int responseCode) {
                // Handle the result.
            }
        });
```

The price change confirmation flow displays a dialog containing the new pricing information, asking users to accept the new price. This flow returns a response code of type [`BillingClient.BillingResponse`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
