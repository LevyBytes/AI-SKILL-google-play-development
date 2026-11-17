## Upgrade from PBL 6 to PBL 7

The following sections describe how to upgrade from PBL 6 to PBL 7.

### Update Google Play Billing Library

Update the Play Billing Library dependency version in your app's `build.gradle` file.

```groovy
dependencies {
    def billingVersion = 7.0.0

    implementation "com.android.billingclient:billing:$billingVersion"
}
```

Next, update your API references as described in the following sections.

### Handle subscription related API changes

The previously deprecated APIs `setOldSkuPurchaseToken`, `setReplaceProrationMode`, `setReplaceSkusProrationMode` have been removed.

- Update `setOldSkuPurchaseToken` to [`setOldPurchaseToken`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOldPurchaseToken>).
- Update `setReplaceProrationMode` to [`setSubscriptionReplacementMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode>).
- Update `setReplaceSkusProrationMode` to [`setSubscriptionReplacementMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode>).

### Handle removed alternative billing APIs

Removed `BillingClient.Builder.enableAlternativeBilling`, [`AlternativeBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/AlternativeBillingListener>), and [`AlternativeChoiceDetails`](<https://developer.android.com/reference/com/android/billingclient/api/AlternativeChoiceDetails>). Use [`BillingClient.Builder.enableUserChoiceBilling()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableUserChoiceBilling(com.android.billingclient.api.UserChoiceBillingListener)>) with [`UserChoiceBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/UserChoiceBillingListener>) and [`UserChoiceDetails`](<https://developer.android.com/reference/com/android/billingclient/api/UserChoiceDetails>) in the listener callback instead.

### Optional changes

PBL 7 includes two new optional APIs.

#### Support pending purchases for prepaid plans

See the [Handle Subscriptions and Pending Transactions](<https://developer.android.com/google/play/billing/subscriptions#pending>) guide.

#### Virtual installment subscriptions

See the [Installment Subscriptions Integration](<https://developer.android.com/google/play/billing/subscriptions#installments>) guide for information on how to integrate these changes into your app.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/migrate-gpblv7).
