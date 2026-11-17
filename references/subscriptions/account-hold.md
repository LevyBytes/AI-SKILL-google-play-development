### Account hold

> **Note:** By default, all auto-renewing base plans and installment plans have account hold enabled and the lengths are automatically calculated. The calculation will be 60 days minus any grace period duration. You can adjust the account hold length or disable it from the [Google Play Console](<https://support.google.com/googleplay/android-developer/answer/140504>). Specifying a length less than the default value may reduce the number of subscriptions recovered from payment declines.

If there are payment issues with a subscription renewal, after any [grace period](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#grace-period>) has ended, an account hold period begins. When a subscription enters account hold, you should block access to the subscription entitlement.

During account hold, you should continue to handle any [cancellations](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#cancel>), restorations, or [repurchases of your subscriptions](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#resubscribe>) as needed, because it's possible for the user to make these changes while the subscription is on hold.

RTDNs notify you when the user enters the account hold period, so you can inform them as soon as possible of why their access to the subscription was suspended. A straightforward way to do this is to use the [In-App Messaging API](<https://developer.android.com/google/play/billing/subscriptions#in-app-messaging>). Calling this API when your user opens the app will show the user a message in a temporary snackbar informing them that their payment has been declined. This message also includes a deep link for the user to fix their payment method on Google Play.

If your users can access subscription content outside of your app, they might discover that they have lost access on different surfaces. You might want to send a push notification or an email to the user to let them know that their subscription is no longer active due to payment decline.

The subscription is not returned by the [`queryPurchasesAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>) method during account hold, so if your app relies on this method to display existing purchases, you should support account hold by default.

With [real-time developer notifications](<https://developer.android.com/google/play/billing/getting-ready#configure-rtdn>), you receive a [`SubscriptionNotification`](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) message with type `SUBSCRIPTION_ON_HOLD` when a subscription enters account hold. Call the [`purchases.subscriptionsv2.get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) method from your secure backend server to retrieve the new subscription information. During account hold the `expiryTime` field of the [subscription resource](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) is set to a past timestamp, and the `subscriptionState` field is set to `SUBSCRIPTION_STATE_ON_HOLD`:

```json
{
  "kind": "androidpublisher#subscriptionPurchaseV2",
  ...
  "subscriptionState": "SUBSCRIPTION_STATE_ON_HOLD",
  ...
  "lineItems": [
    {
      "productId": "sub_variant_plan01",
      "expiryTime": timestamp_in_past,
      ...
    }
  ],
}
```

To restore access, users must fix their payment method. Play informs users in account hold of their payment decline, and you should also encourage them to fix their payment method.

After the user fixes their payment method, the subscription returns to an active state, and you must then restore access to the subscribed content. In this case, the purchase token is the same as it was before the account hold started because the same purchase is recovering, and you receive an RTDN with type `SUBSCRIPTION_RECOVERED`.

For installment subscriptions, payment declines and recoveries could occur for any individual payment attempt.

> **Note:** If a subscription is recovered from account hold, the billing date moves to the date of recovery.

After recovery, the Play Billing Library returns the subscription again through the `queryPurchasesAsync()` method. If you use this method to determine whether a user is entitled to a subscription, then your app should automatically handle the subscription recovering from account hold.

Listen for a [`SubscriptionNotification`](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) message with type `SUBSCRIPTION_RECOVERED` to be notified when a subscription is recovered and the user should regain access. If you query for a subscription after receiving this notification, the `expiryTime` field is set to a timestamp in the future and the `subscriptionState` field is set to `SUBSCRIPTION_STATE_ACTIVE` again:

```json
{
  "kind": "androidpublisher#subscriptionPurchaseV2",
  ...
  "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
  ...
  "lineItems": [
    {
      "productId": "sub_variant_plan01",
      "expiryTime": next_renewal_date,
      ...
    }
  ],
}
```

If the user does not fix their payment method before the end of the account hold period, you instead receive an RTDN with type `SUBSCRIPTION_CANCELED`. For instructions on handling a cancellation, see [Cancellations](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#cancel>). When you query for a subscription that was canceled in this way, the returned `expiryTime` field is set to a past timestamp:

```json
{
  "kind": "androidpublisher#subscriptionPurchaseV2",
  ...
  "subscriptionState": "SUBSCRIPTION_STATE_CANCELED",
  ...
  "lineItems": [
    {
      "productId": "sub_variant_plan01",
      "expiryTime": timestamp_in_past,
      ...
    }
  ],
}
```

Immediately after you are notified of the cancellation during account hold, you will also receive an RTDN with type `SUBSCRIPTION_EXPIRED` because the user is out of paid entitlement and the subscription has churned with the cancellation. You can [handle this expiration](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#expiration>) the way you normally would.

The user can regain access by repurchasing the same subscription plan or any other plan that you offer through the app during their account hold period from their original purchase. In that case, a new purchase token is issued and the new value is returned as part of a `SUBSCRIPTION_PURCHASED` event that represents this new instance.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/lifecycle/subscriptions).
