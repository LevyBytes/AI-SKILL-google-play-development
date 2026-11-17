## Issue refunds and revocations

There are many situations where you may want to issue a refund for or revoke access to a subscription or one-time purchase.

### Fully refund an order by order ID

With the [`orders.refund`](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund>) API, you can issue full refunds for any order within three years of purchase. The `orders.refund` method receives a revoke parameter indicating whether or not access should be revoked in addition to providing the refund.

If you issue a revocation with the refund call for a subscription purchase, the subscription is immediately terminated and it triggers both a `SUBSCRIPTION_REVOKED` Real Time Developer Notification and a `VoidedPurchaseNotification` (recorded in the [Voided Purchases API](<https://developers.google.com/android-publisher/voided-purchases>)). Read the subscription lifecycle management guide [Revocations section](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#revoke>) to learn how to handle these events.

Example:

1. To celebrate the beginning of the new world cup, the e-sports app Football-Not-Soccer decides to raffle off free virtual jerseys for all users who purchase new team kits in the first 24 hours.
2. Football-Not-Soccer uses the [`orders.refund`](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund>) API without passing a revoke parameter to refund the jersey purchases to the winners.

> **Note:** Access to a subscription can only be revoked for subscriptions with current entitlement. When using the `revoke` parameter while refunding an order, make sure the order is the latest associated with the subscription. If it is not , the refund will be successful, but the subscription won't be revoked. If your use case requires revoking access to an active subscription, Use the [`purchases.subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) API with the purchase ID instead of the refund API with a revoke parameter.

### Revoke and refund a subscription by purchase token

For certain use cases you might need to revoke access to a user's subscription and provide a refund. Play Billing offers revocation methods including full refunds and prorated refunds through the [`subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) API. With this endpoint, you can specify [`revocationContext`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke#revocationcontext>) to determine how the refund is calculated.

Taking this action triggers both a `SUBSCRIPTION_REVOKED` Real Time Developer Notification and a `VoidedPurchaseNotification`, and is recorded in the [Voided Purchases API](<https://developers.google.com/android-publisher/voided-purchases>). Your app should handle these cancellations as described in [Revocations](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#revoke>).

Example:

- Purchase with purchase token `1a2b3c4d5e6f7g8h9i0j`
- Application with the package name `com.your.app`
- Intent of issuing a prorated refund

HTTP POST request:

```textonly
https://androidpublisher.googleapis.com/androidpublisher/v3/applications/com.your.app/purchases/subscriptionsv2/tokens/1a2b3c4d5e6f7g8h9i0j:revoke
```

Request body:

```json
{
  "revocationContext": {
    "proratedRefund": {}
  }
}
```

#### Full refunds

If you need to terminate a subscription and refund the full amount of the current billing period, issue a full refund. Use the [`purchases.subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) function, and set `"fullRefund": {}` as the refund type.

Example:

1. Maria has an auto-renewing 30-day subscription to SuperMovies streaming monthly plan. Maria encountered some technical issues that prevent her from accessing the content. She contacts customer service on day 3 of her billing cycle stating that she never got access to the subscription.
2. Customer service locates Maria's subscription purchase details in their system and triggers a call to [`purchases.subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) requesting a full refund.
3. Customer service tells Maria she should get 100% of her subscription price refunded and she is not subscribed to the plan anymore.

#### Prorate refunds

If you need to terminate a subscription and partially refund the remaining entitlement time, issue a prorated refund. Use the [`purchases.subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) function, and set `"proratedRefund": {}` as the refund type.

Prorated refunds are supported for both auto-renewing subscriptions and prepaid plans with a duration of at least one week.

Example:

1. Maria has an auto-renewing 30-day subscription to SuperMovies streaming monthly plan. She has happily used the service for some time. Maria contacts customer service on day 15 of her billing cycle stating that she is moving abroad and won't be able to use the service anymore starting the next day.
2. Customer service locates Maria's subscription purchase details in their system and triggers a call to [`purchases.subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) requesting a prorated refund.
3. Customer service tells Maria she should get about 50% of her subscription price refunded and that access to the service terminated immediately.

> **Note:** The [`purchases.subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) API is a replacement and improvement of the legacy [`purchases.subscription.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/revoke>). The main difference is that the new method allows partial refunds while the legacy is capable of only full refunds. Be aware that a user refund is based on the value of the latest order.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/manage-purchases).
