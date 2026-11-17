### Grace period

> **Note:** By default, all auto-renewing base plans have grace period enabled. You can adjust the grace period length or disable it from the [Google Play Console](<https://support.google.com/googleplay/android-developer/answer/140504>). Specifying a length less than the default value may reduce the number of subscriptions recovered from payment declines.

If there are payment issues with a subscription renewal, Google notifies the user and periodically attempts to renew the subscription for some time before the subscription expires. This recovery period can consist of a grace period followed by an account hold period. During a grace period, the user should still have access to their subscription entitlement.

The [`queryPurchasesAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>) method continues to return purchases that are in the grace period. If your app relies solely on `queryPurchasesAsync` to check whether a user is entitled to a subscription, then your app should automatically handle grace periods, because these subscriptions are shown as active through the Play Billing Library.

Synchronizing subscription state with your backend lets you to be more aware of payment declines and gives you more context as you try to reduce involuntary churn. Listen for [`SubscriptionNotification`](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) messages with type `SUBSCRIPTION_IN_GRACE_PERIOD` to be notified when the user enters a grace period. While the user is in a grace period, the [subscription resource](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) contains `autoRenewEnabled = true`. Google Play dynamically extends the `expiryTime` value until the grace period has expired because entitlement should last until the user cancels or the grace period has lasted for its maximum length. The value of the `subscriptionState` field during this period is `SUBSCRIPTION_STATE_IN_GRACE_PERIOD`. The subscription resource looks similar to the following example:

```json
{
  "kind": "androidpublisher#subscriptionPurchaseV2",
  ...
  "subscriptionState": "SUBSCRIPTION_STATE_IN_GRACE_PERIOD",
  ...
  "lineItems": [
    {
      "productId": "sub_variant_plan01",
      "expiryTime": timestamp_in_future,
      "autoRenewingPlan": {
        "autoRenewEnabled": true
      }
    }
  ],
}
```

Play informs users that are in a grace period that their payment was declined and prompts them to fix their payment method issues in the Play Store. When a user enters a grace period, you should also encourage the user to fix their payment method in case the failure was involuntary. A straightforward way to do this is to use the [In-App Messaging API](<https://developer.android.com/google/play/billing/subscriptions#in-app-messaging>). If you call this API when the user opens your app, they are shown a Play message in a temporary snackbar informing the user that their payment has been declined. This message also includes a deep link for the user to fix their payment method on Google Play.

As soon as the user fixes their payment method, the subscription renews with its original renewal date, and you can handle the renewal as described in [Renewals](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#renewal>).

If the user does not fix their payment method during the grace period, the subscription enters [account hold](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#account-hold>), and they lose entitlement.

#### Grace period access and recovery

Figure 2 shows a timeline for a subscription that enters into a grace period and then recovers when the user fixes their payment method. After the grace period ends, the user should lose subscription benefits and go into account hold.

![Image](<https://developer.android.com/static/images/google/play/billing/lifecycle/grace-period.png>)

**Figure 2.** Timeline for a subscription that enters a grace period and recovers before it ends.

It is important to remember the following points:

- During a grace period, the user should retain access to subscription benefits.
- When a subscription recovers during a grace period, the renewal date does *not* reset.
- If you change the grace period, users who are currently in a grace period won't be impacted. Subscription renewals entering grace period after the change will have the new grace period reflected. For example, if you change the grace period from 7 days to 14 days, users who enter the grace period after the change will have the new 14-day grace period.
- The subscription remains in an active state and you won't receive a grace period RTDN until the silent grace period ends

### Silent grace period

You can set a grace period of 0 days, but Play will wait a minimum of 1 day to ensure sufficient time for payment retries. This silent grace period offers a safety net for payment processing. During this 24‑hour period the subscription remains in the [`ACTIVE` state](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions#state>).

The best way for you to stay in sync with subscription state changes is to listen and react to the real-time developer notifications (RTDN). Call the [`purchases.subscriptionsv2.get()`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) method at the RTDN time instead of the expiry time to get a more accurate status of the subscription.

Depending on the subscription status after the 24‑hour silent grace period, you should receive one of the following notifications:

- `SUBSCRIPTION_ON_HOLD` (if enabled)
- `SUBSCRIPTION_CANCELED` (if canceled)
- `SUBSCRIPTION_EXPIRED` (if expired)
- `SUBSCRIPTION_RENEWED` (if successfully renewed)

You can also call the `subscriptionV2.get()` method at any point after the 24‑hour silent grace period to get the latest status of the subscription.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/lifecycle/subscriptions).
