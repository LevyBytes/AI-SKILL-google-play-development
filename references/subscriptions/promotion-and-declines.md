## Promote your subscription

You can create promotion codes to give selected users an extended free trial to an existing subscription. To learn more, see [Promo codes](<https://developer.android.com/google/play/billing/promo>).

For free trials, Google Play verifies that the user has a valid payment method before starting the free trial. Some users may see this verification as a hold or charge on their payment method. This hold or charge is temporary and is later reversed or refunded.

After the trial period ends, the user's payment method is charged for the full subscription amount.

If a user cancels a subscription at any time during the free trial, the subscription remains active until the end of the trial, and they aren't charged when the free trial period ends.

## Defer billing for a subscriber

You can extend the entitlement period for a subscription by using the [`subscriptionsv2.defer`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer>) method. When you defer a subscription with add-ons, all items in the subscription are deferred by the same duration. During the deferral period, the user is subscribed to your content with full access but is not charged. The subscription renewal date is updated to reflect the new date.

For prepaid plans, you can use the defer billing API to defer the expiration time.

Deferred billing lets you do the following:

- Give users free access as a special offer, such as giving one week free for purchasing a movie.
- Give free access to customers as a gesture of goodwill.

Billing can be deferred by as little as one day and by as long as one year per API call. To defer the billing even further, you can call the API again before the new billing date arrives.

Example: Darcy normally pays £1.25 per month for Fishing Quarterly. After she completes a survey, the publisher rewards her with six free weeks by deferring the next payment for that duration. She keeps full access without a charge during the extension. At the deferred billing boundary she pays the normal £1.25 for the next month, and subsequent monthly renewals use that new boundary.

When deferring, you might want to notify the user by email or within the app to notify them that their billing date has changed.

## Handle payment declines

If there are payment issues with a subscription renewal, Google will periodically attempt to renew the subscription for some time before canceling. This recovery period can consists of a grace period, followed by an account hold period. During this time, Google sends the user emails and notifications prompting them to update their payment method.

Upon payment decline, the subscription enters a [grace period](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#grace-period>) if one is configured. During the grace period, you should ensure the user still has access to the subscription entitlements.

After any grace period has ended, the subscription enters an [account hold](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#account-hold>) period. During account hold, you should ensure the user does not have access to the subscription entitlements.

You can specify the length of each auto-renewing base plan's grace period and account hold in the Google Play Console. Specifying lengths less than the default values may reduce the number of subscriptions recovered from payment declines.

To maximize the likelihood of subscription recovery during a payment decline, you can inform your user of a payment issue and ask them to fix it.

You can either do this yourself, as described in the [grace period](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#grace-period>) and [account hold](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#account-hold>) sections, or you can implement the in-app messaging API, where Google shows a message to users in your app.

When there is a payment issue, Google Play can display a notification to your users. To facilitate this, you can use the in-app messaging feature to inform them about any pending payments. If you have enabled in-app messaging, message for payment issues is shown during grace period and account hold once per day. This provides users an opportunity to fix their payment without leaving the app. For more information, see [in-app messaging](<https://developer.android.com/google/play/billing/subscriptions?hl=en#in-app-messaging>).

> **Note:** You can use [Play Billing Lab Subscription State Transition](<https://developer.android.com/google/play/billing/test#subscription-state-transition>) feature to test payment decline scenarios.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscriptions).
