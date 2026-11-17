### Revocations

A subscription can be revoked for a variety of reasons, including your backend revoking the subscription by using [`purchases.subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) or the purchase being charged back. In this situation, revoke the user's entitlement immediately. A `SubscriptionNotification` message with type `SUBSCRIPTION_REVOKED` is sent when this occurs. When you receive this notification, the [subscription resource](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) returned from the Google Play Developer API has the `subscriptionState` field set to `SUBSCRIPTION_STATE_EXPIRED`.

The subscription resource for a revoked purchase looks similar to the following example:

```json
{
  "kind": "androidpublisher#subscriptionPurchaseV2",
  ...
  "subscriptionState": "SUBSCRIPTION_STATE_EXPIRED",
  ...
  "lineItems": [
    {
      "productId": "sub_variant_plan01",
      "expiryTime": expiration_time,
      ...
    }
  ]
}
```

### Deferred subscriptions

There are a variety of reasons why you might want to extend a user's entitlement. For example, you might want to offer users free access as a special promotion, such as giving one week free for purchasing a movie or providing free access to customers as a gesture of goodwill.

You can use the [`purchases.subscriptionsv2.defer`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer>) API to defer the billing date for subscriptions (including subscriptions with add-ons). When you defer a subscription with add-ons, all items in the subscription are deferred by the same duration.

When you defer a subscription, a `SubscriptionNotification` message with type `SUBSCRIPTION_DEFERRED` is sent. During the deferral period, the user is subscribed to your content with full access but is not charged. The subscription renewal date is updated to reflect the new date.

For prepaid plans, you can use the defer billing API to defer the expiration time.

The subscription resource for a deferred subscription looks similar to the following example:

```json
{
  "kind": "androidpublisher#subscriptionPurchaseV2",
  ...
  "subscriptionState": "SUBSCRIPTION_STATE_ACTIVE",
  ...
  "lineItems": [
    {
      "productId": "sub_variant_plan01",
      "expiryTime": timestamp_in_future,
      ...
    }
  ],
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/lifecycle/subscriptions).
