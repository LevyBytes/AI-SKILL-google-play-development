### Paused subscriptions

> **Note:** All subscriptions have pause enabled by default. You can disable pause from the [Google Play Console](<https://support.google.com/googleplay/android-developer/answer/140504#pause>).

You can reduce voluntary churn by enabling users to pause their subscription. When you enable the pause feature, users can choose to pause their subscription for a period of time between one week and three months, depending on the recurring period. This temporarily suspends the subscription.

| Subscription recurrence | Weekly | Monthly | Three-month | Six-month | Annual |
| --- | --- | --- | --- | --- | --- |
| Available pause lengths* | 1 week<br>2 weeks<br>3 weeks<br>4 weeks | 1 month<br>2 months<br>3 months | 1 month<br>2 months<br>3 months | 1 month<br>2 months<br>3 months | 1 month<br>2 months<br>3 months |

*Subject to change at any time.

A subscription pause takes effect only after the current billing period ends. While the subscription is paused, the user doesn't have access to the subscription, and they don't pay the renewal price. At the end of the pause period, the subscription resumes and Google attempts to renew the subscription. If the resume is successful, the subscription becomes active again. If the resume fails due to a payment issue, the user enters the account hold state as shown in figures 5 and 6:

![Image](<https://developer.android.com/static/images/google/play/billing/lifecycle/pause-1.png>)

**Figure 5.** A user pauses and then resumes their subscription.

![Image](<https://developer.android.com/static/images/google/play/billing/lifecycle/pause-2.png>)

**Figure 6.** A user pauses their subscription and then enters account hold.

A user can also choose to manually resume a subscription at any time during the pause period, as shown in figure 6. When a user resumes manually, the billing date changes to the manual resume date.

When a user's subscription is paused, the Play Billing Library doesn't return the subscription through the [`queryPurchasesAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>) method unless the `includeSuspendedSubscriptions` parameter is set to true in the `QueryPurchasesParams`. If the subscription is resumed, the `queryPurchasesAsync()` method returns it again.

Listen for RTDNs to be aware of when a user pauses their subscription. These notifications also allow you to notify your users in your app that they have paused their subscription and don't have access to it. You should also provide a way for the user to manually resume their subscription at any time by using a [deep link to Google Play](<https://developer.android.com/google/play/billing/subscriptions#use-deep>).

A [`SubscriptionNotification`](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) message with type `SUBSCRIPTION_PAUSE_SCHEDULE_CHANGED` is sent when your user initiates a pause of their subscription. At this time, the user should keep access to their subscription until the next renewal date, and the [subscription resource](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) contains `autoRenewEnabled = true`. The value of the `subscriptionState` field is `SUBSCRIPTION_STATE_ACTIVE` at this point.

A `SubscriptionNotification` message with type `SUBSCRIPTION_PAUSED` is sent when the pause goes into effect. When this happens, the user should lose access to their subscription, and the subscription resource contains `autoRenewEnabled = true`, and the `subscriptionState` field is set to `SUBSCRIPTION_STATE_PAUSED`. You can see when the subscription is expected to renew again by checking the [`PausedStateContext`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#pausedstatecontext>) object.

A `SubscriptionNotification` message with type `SUBSCRIPTION_RECOVERED` is sent if the subscription is resumed either automatically at the end of the pause period or if the user chose to manually resume the subscription.

A `SubscriptionNotification` message with type `SUBSCRIPTION_ON_HOLD` is sent if there was a payment failure while trying to resume the subscription after pause.

Both situations should be handled as described in [Account hold](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#account-hold>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/lifecycle/subscriptions).
