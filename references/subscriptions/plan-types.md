This document describes how to handle subscription lifecycle events, such as renewals and expirations. It also describes additional subscription features such as offering promotions and allowing your users to manage their own subscriptions.

If you haven't configured subscription products for your app, see [Create and configure your products](<https://developer.android.com/google/play/billing/getting-ready#products>).

## Subscriptions overview

A *subscription* is a recurring transaction that grants specific entitlements to users. The entitlements represent a set of benefits users can access during a specified time period. For example, a subscription might entitle a user for a premium access.

Through *base plans* and *offers*, you can create multiple configurations for the same subscription product. For example, you can create an introductory offer for users who have never subscribed to your app. Similarly, you can create an upgrade offer for users who are already subscribed.

For a detailed overview of subscription products, base plans, and offers, see the documentation in the [Play Console Help Center](<https://support.google.com/googleplay/android-developer/answer/12154973>).

The Play Billing Library supports the following subscription types:

- Subscription - In this type, one item corresponding to one entitlement. For example, subscription to a music streaming service.
- Subscription with add-ons - In this type, one purchase can have several distinct entitlements bundled in a single purchase. For example, subscription to both music streaming service, and a video subscription. For information specific to subscription with add-ons, see [Subscriptions with add-ons](<https://developer.android.com/google/play/billing/subscription-with-addons>).

## Prepaid plans integration

Prepaid plans **do not** automatically renew upon expiration. To extend their subscription entitlement without interruption, the user must *top-up* a prepaid plan for the same subscription.

For top-ups, launch the billing flow as you would with the original purchase. You don't need to indicate that a purchase is a top-up.

Prepaid plan top-ups always use the `CHARGE_FULL_PRICE` replacement mode, and you don't need to set this mode explicitly. The user is immediately charged for a full billing period, and their entitlement is extended by the duration specified in the top-up.

After a top-up, the following fields in the [`Purchase`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase>) result object are updated to reflect the most recent top-up purchase:

- Order ID
- Purchase time
- Signature
- Purchase token
- Acknowledged

The following `Purchase` fields always contain the same data found in the original purchase:

- Package name
- Purchase state
- Products
- Auto renewing

### Prepaid purchase acknowledgement

Similar to auto-renewing subscriptions, you must acknowledge prepaid plans after purchase. Both the initial purchase and any top-ups need to be acknowledged. For more information, see [Processing purchases](<https://developer.android.com/google/play/billing/integrate#process>).

Due to the potential for short prepaid plan durations, it is important to acknowledge the purchase as soon as possible.

Prepaid plans with a duration of one week or longer must be acknowledged within three days.

Prepaid plans with a duration shorter than one week must be acknowledged within half the plan duration. For example, developers have 1.5 days to acknowledge a three-day prepaid plan.

> **Warning:** If a user on a prepaid plan purchases a top-up, and you do not acknowledge the purchase within the corresponding period, the top-up purchase is revoked, the remaining subscription is revoked and canceled, and the user is issued a refund.

## Installment subscriptions integration

An installment subscription is a type of subscription where users pay for the subscription in multiple installments over a period of time, rather than paying the entire subscription fee upfront.

Additional considerations for installment subscriptions:

- **Country availability**: Installment subscriptions feature is only available in Brazil, France, Italy, and Spain (check Console for latest availability).
- **Setting the price**: When setting the price for an installment subscription on the Console, the price represents the monthly payment amount. This, combined with the commitment period that is set, generates the total amount for the subscription in the purchase screen.
- **Commitment period**: The total duration of the initial subscription commitment, during which monthly payments are required. For example, if a base plan has a 15-month commitment period, the user will make 15 monthly payments over this period.
- **Renewals**: In the context of installment subscriptions, "renewal" signifies the conclusion of a commitment period, either initial commitment period or subsequent commitment period. Following the initial sign up, the first renewal occurs upon completion of the entire initial commitment period. Subsequent renewals occur after each subsequent commitment period is fulfilled. The renewal types for installment subscriptions can be "auto-renews monthly" or "auto-renews for the same duration". For "auto-renews monthly", there is no subsequent commitment and the plan behaves like a monthly subscription where each monthly subscription charge constitutes a renewal.
- **Billing period**: In the context of installment subscriptions, this refers to the recurring interval at which individual payments are made, as specified in the base plan.
- **Plan change vs. price change behaviors**: For price changes and cancellations, the commitment is firm. This means that if a user wants to cancel or a developer wants to change the price, the change takes effect at the end of a commitment period. For plan changes, the commitment is not firm. This means that the plan change does not have to wait until the end of a commitment period, it takes effect either immediately or on the next payment date based on the set replacement mode.
- **Same-subscription plan change**: Plan change from an installments base plan to a non-installments base plan of the same subscription product is not allowed.
- **Real-time developer notifications (RTDNs)**: A `SUBSCRIPTION_CANCELLATION_SCHEDULED` RTDN is sent immediately upon user-initiated cancellation when payments remain for the commitment period. The cancellation is pending and will only take effect at the end of the commitment period. Then, if not restored by the user, `SUBSCRIPTION_CANCELED` and `SUBSCRIPTION_EXPIRED` RTDNs are sent at the end of the commitment period.
- **Payouts / Revenue realization**: Developer payouts will happen as users make their monthly payments, subject to the same terms as all other subscriptions. Developers are not paid upfront when the user signs up for the installment subscription.
- **Missed payment collections**: If a user fails to make any installment subscription payments, neither Google nor Developer will attempt to collect any such missed or outstanding payments from the user, except that Google may periodically retry the payment during any applicable Grace Period or Account Hold period in accordance with its normal payment retry practices. Google won't be responsible to the Developer for any remaining unpaid installment payments.
- **Play Billing Library availability**: The `installmentDetails` field is only available for PBL 7 or later. For PBL 5 and later, the installment subscription is returned using `queryProductDetails()`, but the subscription won't include detailed installment information like committed payments count of the plan.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscriptions).
