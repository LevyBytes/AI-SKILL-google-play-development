### Upgrades, downgrades, and resubscribe

When a user upgrades, downgrades, or [signs up after cancellation from your app before the subscription expires](<https://developer.android.com/google/play/billing/subscriptions#before-in-app>), the old subscription is invalidated and a [new subscription](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#new-auto>) is created with a new purchase token.

In addition, the [subscription resource](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions>) returned from the Google Play Developer API contains a `linkedPurchaseToken` field that indicates the old purchase from which the user upgraded, downgraded, or resubscribed. You can use the purchase token in that field to look up the old subscription and identify the existing user account so that you can associate the new purchase with the same account.

When a user signs up again from your app for the same base plan before their subscription expires, Google Play generates an order for $0.00 for the new purchase. The user isn't charged at sign-up, because they've already paid for the current billing period. Regular billing resumes on the original renewal date. The $0.00 order appears in **Order management** in Play Console and in your financial reports. It doesn't mean that the user received a free trial or a promotional discount.

Before offering upgrade, downgrade, or resubscribe options to a user in your app, you must acknowledge the existing subscription. Any plan change or resubscribe is blocked if the existing subscription is still pending acknowledgement.

If the user successfully purchases the upgrade, downgrade, or resubscribe, this is a new purchase which you must acknowledge. The recommended way to do this is to use the [Google Play Developer API](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/acknowledge>). The subscription resource looks similar to the following example:

```json
{
  "kind": "androidpublisher#subscriptionPurchaseV2",
  ...
  "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
  "linkedPurchaseToken": old_purchase_token,
  ...
  "lineItems": [
    {
      "productId": "sub_variant_plan01",
      "expiryTime": next_renewal_date,
      "autoRenewingPlan": {
        "autoRenewEnabled": true
      }
    }
  ],
}
```

### Price changes

See the [price change best practices guide](<https://developer.android.com/google/play/billing/price-changes>) to learn about changing auto-renewing subscription prices and notifying users when appropriate.

When a price change is added and for any updates to the price change status, you will receive the `SUBSCRIPTION_PRICE_CHANGE_UPDATED` RTDN. You can query the [purchases.subscriptionsv2.get](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) endpoint to get a [subscription resource](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) which will contain price change details for each item in the subscription.

When price changes are applied to existing subscribers as *opt-in*, you will received an RTDN if the user takes action to confirm or reject the new price.

#### Handle user confirmation of an opt-in price change

When a user accepts your subscription price increase, you receive a [SubscriptionNotification](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) message with type `SUBSCRIPTION_PRICE_CHANGE_UPDATED`.

> **Note:** For subscriptions without addons `SUBSCRIPTION_PRICE_CHANGE_CONFIRMED` notifications will also be sent. However, this notification is deprecated. For more information, see [Deprecations](<https://developer.android.com/google/play/billing/play-developer-apis-deprecations#may21-api-deprecation>).

#### Handle renewals after price change is applied

With a price decrease, or when the subscription price increase renews, you will receive a `SubscriptionNotification` message with type `SUBSCRIPTION_RENEWED`. Treat this notification like any other [renewal](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#renewal>).

#### Handle cases where an opt-in price increase is not accepted

If a user hasn't accepted your opt-in price increase before they need to renew at the higher price, they are automatically unsubscribed and you receive a [SubscriptionNotification](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) message with type `SUBSCRIPTION_CANCELED`. Handle this event as described in [Cancellations](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#cancel>).

Users can also cancel their subscriptions for an opt-out price increase following the same mechanism.

### Price step-up consent (applicable only for KR region)

Due to new South Korean (KR) regulations, subscription users in the KR region must consent to any price step-ups that will occur after their free trial or introductory period ends.

To help you comply with the regulation, Play will notify users in the KR region about the consent requirement and will also store the consent response from the users. Subscriptions are automatically canceled for users who don't provide consent before the higher price takes effect. In addition to the notifications sent from Play, you can also send your custom price step-up notifications to your users, and can provide [link to specific management page](<https://developer.android.com/google/play/billing/subscriptions#link-specific>) in your notifications.

When the consent period has begun or the user has provided consent, you will receive a [SubscriptionNotification](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) message with type `SUBSCRIPTION_PRICE_STEP_UP_CONSENT_UPDATED`.

> **Note:** If the consent period starts at signup (for example, a 7-day free trial), the consent-start RTDN is suppressed to avoid duplicate notifications. You will only receive `SUBSCRIPTION_PURCHASED` upon purchase, followed by `SUBSCRIPTION_PRICE_STEP_UP_CONSENT_UPDATED` once the user actually provides consent.

#### Difference between price step-up and price change

A `price step-up` refers to an increase in the subscription price, due to a transition from one offer phase to another. For example, a subscription moving from a free trial to a regular price. You can use the `offerPhase` field in the subscription resource to identify the current phase of the subscription.

However, a `price change` refers to price updates initiated by you (developer) for the base plan price for a subscription. For example, opt-in price increase or opt-out price increase.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/lifecycle/subscriptions).
