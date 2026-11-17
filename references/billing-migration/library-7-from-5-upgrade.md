This document describes how to migrate from Google Play Billing Library 5 or 6 to Google Play Billing Library 7 and how to integrate with the new optional subscription capabilities.

For a full list of the changes in version 7.0.0, refer to the [release notes](<https://developer.android.com/google/play/billing/release-notes>).

## Overview

Google Play Billing Library 7 improves payment handling for existing subscription features. These optional improvements add support for paying with installment plans as well as support for pending purchases for prepaid subscriptions.

## Backward-compatible Play Billing Library upgrade

All new Google Play Billing Library 7 APIs are optional, and developers don't need to implement any API changes to update.

To migrate, you need to update API references and remove certain APIs from your app as described in the release notes and later in this migration guide.

## Upgrade from PBL 5 to PBL 7

The following sections describe how to upgrade from PBL 5 to PBL 7.

### Update Google Play Billing Library

Update the Play Billing Library dependency version in your app's `build.gradle` file.

```groovy
dependencies {
    def billingVersion = 7.0.0

    implementation "com.android.billingclient:billing:$billingVersion"
}
```

Next, update your API references as described in the following sections.

### Change a user's subscription purchases

Play Billing Library 5 and earlier used [`ProrationMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProrationMode>) to apply changes to a user's subscription purchases, such as upgrades or downgrades. This API has been removed and replaced with [`ReplacementMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode>).

### Handle subscription price changes

The previously deprecated `launchPriceConfirmationFlow` API has been removed. For alternatives, see the [price changes guide](<https://developer.android.com/google/play/billing/price-changes>).

### Handle subscription related API changes

The previously deprecated APIs `setOldSkuPurchaseToken`, `setReplaceProrationMode`, `setReplaceSkusProrationMode` have been removed.

- Update `setOldSkuPurchaseToken` to [`setOldPurchaseToken`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOldPurchaseToken>).
- Update `setReplaceProrationMode` to [`setSubscriptionReplacementMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode>).
- Update `setReplaceSkusProrationMode` to [`setSubscriptionReplacementMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setSubscriptionReplacementMode>).

### Handle Play Billing Library errors

A new `NETWORK_ERROR` code indicates problems with the network connection between the user's device and the Google Play system.

The `SERVICE_TIMEOUT` and `SERVICE_UNAVAILABLE` codes were also updated.

For more information, see [Handle BillingResult response codes](<https://developer.android.com/google/play/billing/errors>).

### Handle pending transactions

The Play Billing Library no longer creates an order ID for pending purchases. For these purchases, the order ID is populated after the purchase is moved to the [`PURCHASED`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase.PurchaseState#PURCHASED>) state. Make sure that your integration expects an order ID only after a transaction has fully completed. You can still use the purchase token for your records.

For more information about handling pending purchases, see the Play Billing Library [integration guide](<https://developer.android.com/google/play/billing/integrate>) and the [purchase lifecycle management guide](<https://developer.android.com/google/play/billing/lifecycle>).

### Handle removed alternative billing APIs

Removed `BillingClient.Builder.enableAlternativeBilling`, [`AlternativeBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/AlternativeBillingListener>), and [`AlternativeChoiceDetails`](<https://developer.android.com/reference/com/android/billingclient/api/AlternativeChoiceDetails>). Use [`BillingClient.Builder.enableUserChoiceBilling()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enableUserChoiceBilling(com.android.billingclient.api.UserChoiceBillingListener)>) with [`UserChoiceBillingListener`](<https://developer.android.com/reference/com/android/billingclient/api/UserChoiceBillingListener>) and [`UserChoiceDetails`](<https://developer.android.com/reference/com/android/billingclient/api/UserChoiceDetails>) in the listener callback instead.

This update is a renaming of the deprecated APIs with no behavior changes.

### Optional changes

PBL 7 includes two new optional APIs.

#### Support pending purchases for prepaid plans

See the [Handle Subscriptions and Pending Transactions](<https://developer.android.com/google/play/billing/subscriptions#pending>) guide.

#### Virtual installment subscriptions

See the [Installment Subscriptions Integration](<https://developer.android.com/google/play/billing/subscriptions#installments>) guide.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/migrate-gpblv7).
