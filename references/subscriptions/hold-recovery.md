#### Account hold access and recovery

Figure 3 shows a timeline for a subscription that enters into account hold and then recovers when the user fixes their payment method.

![Image](<https://developer.android.com/static/images/google/play/billing/lifecycle/acct-hold-1.png>)

**Figure 3.** Timeline for a subscription that enters an account hold and recovers before it ends.

Similar to the previous example, Figure 4 shows a timeline for a subscription that first enters into a grace period before entering account hold, and then recovers while on hold.

![Image](<https://developer.android.com/static/images/google/play/billing/lifecycle/acct-hold-2.png>)

**Figure 4.** Timeline for a subscription that enters a grace period, then enters account hold, and finally recovers before the account hold ends.

It is important to remember the following points:

- Before a subscription enters into account hold, Google Play makes additional attempts to charge the payment method for up to 48 hours. The user retains subscription benefits during this period. After this retry period has elapsed, the subscription then enters into account hold, and the user should lose access to subscription benefits.
- The subscription enters into account hold directly when the subscription resumes from a paused state with a failed form of payment.
- When a subscription recovers from account hold, the renewal date resets.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/lifecycle/subscriptions).
