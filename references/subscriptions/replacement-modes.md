## Allow users to upgrade, downgrade, or change their subscription

You can provide existing subscribers with various options to change their subscription plan to better meet their needs:

- If you sell multiple subscription tiers, such as "basic" and "premium" subscriptions, you can allow users to switch tiers by purchasing a different subscription's base plan or offer.
- You can allow users to change their current billing period, such as switching from a monthly to an annual plan.
- You can also allow users to switch between auto-renewing and prepaid plans.

You can encourage any of these changes by providing subscription offers to provide a discount to eligible users. For example, you could create an offer providing a 50% discount on the first year when switching from a monthly to an annual plan, and limit this offer to users subscribed to a monthly plan who haven't purchased this offer. More information on offer eligibility criteria is available [in the Help Center](<https://support.google.com/googleplay/android-developer/answer/12154973?sjid=13996822054844635277-NA#offer_eligibility>)

Figure 3 shows an example app with three different plans:

![This app has three subscription tiers..](<https://developer.android.com/static/images/google/play/billing/plan_change_inapp.png>)

**Figure 3.** This app has three subscription tiers.

Your app could show a screen similar to figure 3, giving users options to change their subscription. In all cases, it should be clear to users what their current subscription plan is, and what options they have for changing it.

When users decide to upgrade, downgrade, or change their subscription, you specify a *replacement mode* that determines how the prorated value of the current paid billing period is applied, and when any entitlement change occurs.

### Replacement modes

The following table lists available replacement modes and example usage, and count of payments considered paid.

> **Note:** For installment subscriptions, all replacement modes are supported. Additionally, after a replacement occurs for installment subscriptions, it is possible that the first committed payment of the new plan will be recorded as paid depending on the replacement mode.

| Replacement mode | Description | Example usage | Committed payments recorded as paid (For installment subscription replacement) |
| --- | --- | --- | --- |
| `WITH_TIME_PRORATION` | The subscription item is upgraded or downgraded immediately. Any time remaining is adjusted based on the price difference, and credited toward the new subscription by pushing forward the next billing date. This is the default behavior. | Upgrade to a more expensive tier, without any immediate additional payment. | 0 |
| `CHARGE_PRORATED_PRICE` | The subscription item is upgraded immediately, and the billing cycle remains the same. The price difference for the remaining period is then charged to the user.**Note:** This option is available only for a subscription item upgrade, where the price per unit of time increases. | Upgrade to a more expensive tier, without changing the billing date. | 1 |
| `CHARGE_FULL_PRICE` | The subscription item is upgraded or downgraded immediately, and the user is charged full price for the new entitlement immediately. The remaining value from the previous subscription is either carried over for the same entitlement, or prorated for time when switching to a different entitlement. **Note:** If the new subscription has a free trial or introductory offer, the user is charged $0 or the price of the introductory offer, whichever applies, at the time of upgrade or downgrade. | Upgrade from shorter to longer billing period. | 1 (Note: 0 if the new subscription has a free trial.) |
| `WITHOUT_PRORATION` | The subscription item is upgraded or downgraded immediately, and the new price is charged when the subscription renews. The billing cycle remains the same. | Upgrade to a higher subscription tier while retaining any remaining free period. | 0 |
| `DEFERRED` | The subscription item is upgraded or downgraded only when the subscription renews, but the new purchase is issued immediately with the following two items: The existing item with auto renew disabled and expiry time set to the end of current billing cycle. The new entitlement which begins after the existing item expires. You can allow users to make additional changes if they want. For example, users can revert to the original plan or initiate a new deferred plan change. **Note:** For installment subscriptions, the plan change occurs at the start of the next payment date. | Downgrade to a less expensive tier. | 1 |
| `KEEP_EXISTING` | The payment schedule for the subscription item remains unchanged in the replacement. | Add or remove subscription item from a subscription with add-ons when a specific item should be unchanged. | N/A |

> **Note:** In Play Billing Library version 5 and lower, replacement modes were represented by `ProrationMode`. The new [`ReplacementMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode>) enum includes equivalent modes for all proration modes. `ReplacementMode.DEFERRED` includes some improvements to make it simpler to manage deferred changes of plan. The user experience is exactly the same. Read the [Replacement examples and behaviors](<https://developer.android.com/google/play/billing/subscriptions?hl=en#replacement-examples>) section to learn more.

To learn more about different upsell and winback applications of upgrade or downgrade offers, read the offers and promotions guide.

#### Set the replacement mode for a purchase

You can use different replacement modes for different types of subscription transitions, based on your preferences and business logic. This section explains how to set a replacement mode for a change in a subscription and the limitations that apply.

##### Resubscribe or switch plans within the same subscription

You can specify a default replacement mode in the Google Play Console. This setting lets you choose when to charge current subscribers if they purchase a different base plan or offer for the same subscription or resubscribe after a cancellation. The available options are *Charge immediately*, equivalent to `CHARGE_FULL_PRICE`, and *Charge at the next billing date*, equivalent to `WITHOUT_PRORATION`. These are the only relevant replacement modes when switching base plans within the same subscription.

For example, if you are implementing a winback offer for the same plan after the user cancels but before the subscription ends, you can process the new purchase as a regular purchase without indicating any values in `SubscriptionUpdateParams`. The system uses the default replacement mode you configured in the subscription and automatically handles the plan transition from the old purchase to the new purchase.

##### Switch plans across subscriptions, or override the default replacement mode

If the user is changing subscription *products* by purchasing a different subscription, or if you want to override the default replacement mode for any reason, you specify the proration rate *at runtime* as part of the purchase flow parameters.

To correctly provide [`ReplacementMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode>) in `SubscriptionProductReplacementParams` or `SubscriptionUpdateParams` as part of your runtime purchase flow configuration, note the following restrictions:

- When upgrading, downgrading, or initiating doing a same-subscription switch **to** a prepaid plan **from** either a prepaid plan, auto-renewing plan, or installment plan, the only allowed replacement mode is `CHARGE_FULL_PRICE`. If you specify any other replacement mode, the purchase fails and an error is shown to the user.
- When switching plans within the same subscription **to** an auto-renewing plan **from** either a prepaid plan or an auto-renewing plan, valid proration modes are `CHARGE_FULL_PRICE` and `WITHOUT_PRORATION`. If you specify any other proration mode, the purchase fails and an error is shown to the user.
- Switching plans within the same subscription product from an installments base plan to a non-installments base plan is not allowed.
- When using `KEEP_EXISTING` replacement mode in `SubscriptionProductReplacementParams` to keep an item's payment unchanged during replacement, the old product ID should be the same as the new product's product ID. The `KEEP_EXISTING` mode isn't supported in [`SubscriptionUpdateParams`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscriptions).
