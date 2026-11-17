## Non-Retriable BillingResult responses

You can't recover from these errors using retry logic.

### [FEATURE_NOT_SUPPORTED](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#FEATURE_NOT_SUPPORTED>)

#### Problem

This non-retriable error indicates that the Google Play Billing feature is not supported on the user's device, likely due to an old Play Store version.

For example, perhaps some of your users' devices don't support in-app messaging.

#### Possible mitigation

Use [`BillingClient.isFeatureSupported`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isFeatureSupported(java.lang.String)>) to check feature support before making the call to the Play Billing Library.

```kotlin
when {
    billingClient.isReady -> {
        val billingResult =
            billingClient.isFeatureSupported(BillingClient.FeatureType.IN_APP_MESSAGING)
        if (billingResult.responseCode == BillingClient.BillingResponseCode.OK) {
            // use Feature
        }
    }
}
```

### [USER_CANCELED](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#USER_CANCELED>)

#### Problem

The user has clicked out of the billing flow UI.

#### Possible resolution

This is informational only and can fail gracefully.

### [ITEM_UNAVAILABLE](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ITEM_UNAVAILABLE>)

#### Problem

The Google Play Billing subscription or one-time purchase product is not available for purchase for this user.

#### Possible mitigation

Make sure your app refreshes the product details using [`queryProductDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)>) as recommended. Take into account how often your product catalog changes on the Play Console configuration to implement extra refreshes if needed. Only attempt to sell products on Google Play Billing that return the right information using [`queryProductDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryProductDetailsAsync(com.android.billingclient.api.QueryProductDetailsParams,%20com.android.billingclient.api.ProductDetailsResponseListener)>). Check the product eligibility configuration for any inconsistencies. For example, you might be querying for a product that is only available for a region other than the one the user is trying to purchase. To be available for purchase, a product needs to be active, its app needs to be published, and its app needs to be available in the user's country.

Sometimes, in particular during testing, everything is correct in the product configuration, but users still see this error. This might be due to a propagation delay of the product details across Google's servers. Try again later.

### [DEVELOPER_ERROR](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#DEVELOPER_ERROR>)

#### Problem

This is a fatal error that indicates you're improperly using an API. For example, supplying incorrect parameters to [`BillingClient.launchBillingFlow`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,%20com.android.billingclient.api.BillingFlowParams)>) can cause this error.

#### Possible resolution

Make sure that you are correctly using the different Play Billing Library calls. Also, check the debug message for more info about the error.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/errors).
