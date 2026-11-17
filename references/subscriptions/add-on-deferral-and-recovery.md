## Defer billing

You can advance the next billing date for a subscription with add-ons using the [`Purchases.subscriptionsv2:defer`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer>) method.

When you defer a subscription with add-ons, all items in the subscription are deferred by the same duration. During the deferral period, the user retains full access to all items but is not charged. The renewal date for all items is updated to the new date.

This can be useful for promotions or customer goodwill gestures. Billing can be deferred by as little as one day and up to one year per API call. You can call the API multiple times to extend the deferral before the new billing date arrives.

A `SUBSCRIPTION_DEFERRED` real-time developer notification is triggered when this action is taken.

## Item expiration during payment decline

For a purchase of subscription with add-ons, certain renewals may only need to extend a subset of item entitlements, without affecting items with a future expiry date.

Regardless of which items are involved in a renewal, if the renewal payment is declined, the overall subscription purchase will enter grace period and account hold as described in the following documentation.

### Recovery period selection

As grace period itself still grants the user entitlement, upon a purchase of subscription with add-ons, renewal payment is declined, the item with the *minimum* grace period over all active items is selected, and its grace period and account hold period as the recovery period is applied for this renewal.

Active items includes items that were active in the purchase of a subscription with add-ons just prior to the renewal attempt, excludes any newly added items (which won't be entitled until after recovery), and excludes any items that are no longer active due to removal or turndown.

The account hold setting of the item with the minimum grace period selected is applied. If there are more than one items with the minimum grace period, but different account hold periods, the longest account hold period is applied.

### Grace period

When a subscription renewal payment is declined, the subscription purchase will enter grace period state. During the grace period, the user will continue to have access to all active items from the previous renewal period. After the grace period, if the payment method hasn't been fixed, the entire subscription purchase goes into account hold. If any other items reach their renewal date during grace period, a new charge attempt will be initiated for those items once the subscription recovers from payment decline.

### Account hold

While the subscription purchase is in account hold, access to all subscription items is suspended until payment recovers.

If the subscription in account hold is recovered, the subscription purchase continues existing as is. If the subscription is not recovered, the items in payment decline will expire, and access to the other items will be resumed for the remainder of their billing periods.

Example:

- A user with monthly *My Base Plan* adds a $10-per-month *Add on plan* with a seven-day free trial during a 31-day billing month. Neither item has a grace period; both have a 30-day account hold period.
- When the trial ends, Play attempts a $2.90 prorated charge (10*9/31). The payment method has expired, so the subscription enters payment decline at that point.

When the subscription enters account hold due to payment decline, the user does not have access to any of the items in the subscription with add-ons. The remaining time for the items that are not being renewed will be given back to users when the subscription exits account hold, either because payment has been recovered or canceled.

In that example, payment decline starts the account hold period.

- If payment recovers three days later, before the broader renewal boundary, access to both *My Base Plan* and *Add on plan* resumes immediately. The next billing boundary moves three days later to account for the suspended entitlement.
- If payment has not recovered after 30 days, the subscription is canceled as described in this example. Access to *Add on plan* ends, while access to *My Base Plan* resumes for its unused paid entitlement.

In this example, you must get the updated `expiryTime` for ALL items in the subscription with add-ons, as some items may resume their entitlement after the grace period and account hold.

## Financial reporting and reconciliation

Use the [Earnings report](<https://support.google.com/googleplay/android-developer/answer/6135870>) to reconcile your active subscriptions with transactions on Play. Each transaction line item has an order ID. With purchases representing several items, the [Earnings and Estimated sales reports](<https://support.google.com/googleplay/android-developer/answer/2482017>) will include separate rows for each transaction such as charge, fee, tax, and refund, for each item involved.

For dashboards in the Play Console:

- The revenue statistics presented in the **Financial reporting** section of the console are broken down by items.
- Order management reflects purchase of subscription with add-ons, and show itemized lists of what was purchased. From order management, you may cancel or refund a user's purchase.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscription-with-addons).
