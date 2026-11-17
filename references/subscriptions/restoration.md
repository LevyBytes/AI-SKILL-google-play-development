### Resubscribe

For auto-renewing subscription base plans, the Google Play Store may display a **Resubscribe** button. This button allows users to regain access to a subscription. It may not appear for various reasons, for example when a subscription expired a long time ago.

> **Note:** For license testers, the **Resubscribe** button is always enabled regardless of the setting in the Google Play Console. To test your app's behavior when resubscribe is disabled, use a non-license-tester account.

![Image](<https://developer.android.com/static/images/google/play/billing/lifecycle/restoration.png>)

**Figure 7.** *Account > Subscriptions* section of the Google Play Store app showing a canceled subscription with a **Resubscribe** button.

Although the button is always labeled **Resubscribe**, its functionality depends upon the subscription state.

While a subscription is canceled but not yet expired, the user is still subscribed and receiving subscription benefits. If the user taps Resubscribe, the cancelation is effectively undone, and the subscription continues to renew. This action is known as *restore* in Play developer documentation and APIs.

After an auto-renewing subscription has expired, you can allow users to purchase the same subscription base plan. This action is known *resubscribe* in Play developer documentation and APIs. You can configure this option for each base plan in the [Play Console](<https://support.google.com/googleplay/android-developer/answer/140504#zippy=%2Ccreate-and-activate-a-base-plan>) or using the API.

#### Restore prior to expiration

> **Note:** All developer apps are required to support Restore.

If your app relies solely on the [`queryPurchasesAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>) method to determine whether a user is entitled to a subscription, then your app should automatically handle restorations because the `queryPurchasesAsync()` method continues to return canceled purchases before their expiration dates. A restored subscription continues to renew as if it were not canceled.

If your app synchronizes subscription state with a backend, you should listen for a [`SubscriptionNotification`](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) message with the type `SUBSCRIPTION_RESTARTED`. After you receive this RTDN, your app can respond to the notification, record that the subscription is now set to renew, and stop displaying restoration messages in your app. The subscription resource looks similar to the following example:

```json
{
  "kind": "androidpublisher#subscriptionPurchaseV2",
  ...
  "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
  ...
  "lineItems": [
    {
      "productId": "sub_variant_plan01",
      "expiryTime": next_renewal_date
      ...
    }
  ],
}
```

> **Note:** A restored subscription uses the same purchase token from when the subscription was canceled. All cancellation fields are cleared from the subscription resource.

Restoring a subscription doesn't generate a new order. If you see a $0.00 order for a subscription that the user previously canceled, the user likely signed up again from your app before the subscription expired. For more information, see [Upgrades, downgrades, and resubscribe](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#upgrades-downgrades>).

#### Resubscribe after expiration

If an auto-renewing base plan is configured using the Google Play Console or API to allow Resubscribe, users can re-purchase an expired subscription in the Google Play Store.

These are new purchases. Google Play issues a brand new purchase token, and your backend receives an RTDN with type `SUBSCRIPTION_PURCHASED`. The purchase status for this type of out-of-app purchase does not include a `linkedPurchaseToken` associated with the original purchase in that case, because the original subscription expired completely.

To ensure accurate user association for the re-purchased subscriptions and prevent automatic refunds for unacknowledged purchases, you must acknowledge the re-purchase on your backend server:

1. Call [`purchases.subscriptionsv2.get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) with the new purchase token from the RTDN. The response for this type of out-of-app purchase includes the [`outOfAppPurchaseContext`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#OutOfAppPurchaseContext>) field, present exclusively for unacknowledged resubscription purchases. This field provides:

   - `expiredExternalAccountIdentifiers`: An [`ExternalAccountIdentifiers`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#externalaccountidentifiers>) object containing the `obfuscatedAccountId` and `obfuscatedProfileId` fields that were configured for the *previous* expired subscription, if they were set.
   - `expiredPurchaseToken`: The purchase token of the last expired subscription.

   Use either of these identifiers to look up and link the new purchase to the correct user account in your backend.
2. Call [`purchases.subscriptions.acknowledge`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/acknowledge>) to acknowledge the purchase.

   - Optionally, you can send the user's `obfuscatedAccountId` and `obfuscatedProfileId` if you had configured them using [`setObfuscatedAccountId`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedAccountId(java.lang.String)>) and [`setObfuscatedProfileId`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setObfuscatedProfileId(java.lang.String)>) during the in-app billing flow.

This server-side approach lets you acknowledge the purchase within three days from the date of purchase, even if the user doesn't open your app.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/lifecycle/subscriptions).
