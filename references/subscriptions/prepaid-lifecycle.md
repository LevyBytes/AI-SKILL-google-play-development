## Handle lifecycle for prepaid plans

As with auto-renewing subscriptions, you must acknowledge prepaid plans after each [new purchase](<https://developer.android.com/google/play/billing/lifecycle/subscriptions?hl=en#new-auto>). In the case of prepaid plans, you must fully process both the initial purchase and any top-ups, because the user has to go through the purchase flow every time.

Due to the potential for short prepaid plan durations, it's important to acknowledge the purchase as soon as possible. Prepaid plans with a duration of one week or longer must be acknowledged within 3 days. Prepaid plans with a duration shorter than one week must be acknowledged within half of the plan duration. For example, developers have 1.5 days to acknowledge purchase of a three-day prepaid plan.

> **Warning:** If a user on a prepaid plan purchases a top-up and you do not acknowledge the purchase within the corresponding timeframe, the top-up purchase is revoked, the remaining subscription is revoked and canceled, and the user is issued a refund.

![Image](<https://developer.android.com/static/images/google/play/billing/lifecycle/prepaid-states.svg>)

**Figure 8.** Lifecycle states and transition events for subscription purchases.

A [`SubscriptionNotification`](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) message with type `SUBSCRIPTION_PURCHASED` is sent to your RTDN client whenever a prepaid plan subscription is purchased, including every top-up. Call the [`purchases.subscriptionsv2.get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) method to check for the latest prepaid plan subscription state.

A new purchase token is issued for top-up purchases, and you receive the previous purchase token in the `linkedPurchaseToken` field as part of the new subscription purchase state. The purchase token is valid from subscription signup until 60 days after expiration. After this date, the purchase token is no longer valid to use to call the Google Play Developer API.

The subscription resource for a prepaid plan purchase looks similar to the following example:

[Complete json example: Handle lifecycle for prepaid plans](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#prepaid>).

You can see when the entitlement ends in the `expiryTime` field. Top-up purchases increase the entitlement time by accumulating it. That means that if the user tops up before their original entitlement ends, the new time is added on top of their previous expiration date.

You might want to display a message in your app informing the user that their prepaid subscriptions can be extended with a top-up. To know when a user will be able to top-up, check the `allowExtendAfterTime` field in the subscription resource.

Prepaid plans don't auto-renew, so they can't be canceled. If a user wants to cancel a prepaid plan, they can let it reach its expiration date.

### SubscriptionPurchaseV2 fields for prepaid plans

New fields have been added to support prepaid plans, which are extended by the user instead of automatically renewing. All fields apply to prepaid plans as they do for auto-renewing subscriptions, with the following exceptions:

- **[New field] lineItems[0].prepaid_plan.allowExtendAfterTime**: denotes when a user will be allowed to buy another top-up to extend their prepaid plan, as a user is allowed to have only one unconsumed top-up at a time.
- **[New field] SubscriptionState**: specifies the subscription object state. For prepaid plans, this value is always either `ACTIVE`, `PENDING`, or `CANCELED`.
- **lineItems[0].expiryTime**: This field is always present for prepaid plans.
- **paused_state_context**: This field is never present, as prepaid plans cannot pause.
- **lineItems[0].auto_renewing_plan**: Not present for prepaid plans.
- **canceled_state_context**: Not present for prepaid plans, as this field applies only to users who actively cancel a subscription.
- **lineItems[0].productId**: This field replaces `subscriptionId` from previous versions.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/lifecycle/subscriptions).
