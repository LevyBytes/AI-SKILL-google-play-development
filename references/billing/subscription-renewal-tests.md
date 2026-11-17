## Test subscription-specific features

The purchase flows for one-time products and subscriptions are similar, but subscriptions have additional scenarios, such as successful or declined subscription renewals. To test renewals, you can use the **Test card, always approves** and **Test card, always declines** payment methods that are available for license testers, as shown in figure 1. Use these payment instruments to test scenarios beyond the successful subscription scenario.

> **Caution:** The resubscribe and pause features are always enabled in license tester accounts even if they're disabled in the Play Console. Test these features in license testers, confirm that they work, and then enable them in the console for all users. To test your app's behavior when these features are disabled, you must use a non-license-tester account.

Similar to one-time products, verify that purchases are properly acknowledged as described in [processing purchases](<https://developer.android.com/google/play/billing/integrate#process>). For purchases from license testers, a purchase is refunded after 3 minutes if your app does not acknowledge the purchase, and you receive an email about the cancellation. You can also check the **Orders** tab in Google Play Console to see if an order was refunded after 3 minutes.

### Renewal periods

Test subscriptions renew more quickly than actual subscriptions, and test subscriptions can renew a maximum of six times, not counting free trials and introductory periods.

The following table lists the testing renewal times for subscriptions of various durations. These times are approximate. You may see small variations in the precise time of an event. To compensate for variation, call the API to view the current status after every subscription expiration date.

| **Production subscription period** | **Test subscription renewal** |
| --- | --- |
| 1 week | 5 minutes |
| 1 month | 5 minutes |
| 3 months | 10 minutes |
| 6 months | 15 minutes |
| 1 year | 30 minutes |

Time-based subscription features such as free trials are also shortened for testing. The following table identifies the testing time periods associated with time-based subscription features:

| **Feature** | **Test period** |
| --- | --- |
| Account hold | 10 minutes |
| Free trial | 3 minutes |
| Grace period | 5 minutes |
| Introductory price period | Same as subscription test period |
| Pause (1 month) | 5 minutes |
| Pause (2 months) | 10 minutes |
| Pause (3 months) | 15 minutes |
| Price step-up consent period<br><br> (applicable only for the South Korea (KR) region) | 3 minutes |
| Purchase acknowledgement | 5 minutes |

### Accelerate subscription state transition

You can also use Play Billing Lab and license testers to accelerate the [test subscriptions renewal periods](<https://developer.android.com/google/play/billing/test?hl=en#renewals>) to speed up your subscription testing or move the test subscription to grace period or account hold state to test [payment decline](<https://developer.android.com/google/play/billing/subscriptions#payment-declines>) scenarios with the following steps:

1. Click **Manage** on the **Subscription settings** card in the **Dashboard**.
2. Choose the active subscription you want to test.
3. Click the **Subscription state** drop-down menu.
4. Click the target state to update the subscription state.

![subscription state transition](<https://developer.android.com/static/images/google/play/billing/play-billing-lab-subscription-state-transition.png>)

**Figure 6.** Test subscription state transition.

Once you've selected the target subscription state in the drop-down menu, the test subscription state will update shortly afterward.

Note that:

- Test subscriptions must be acknowledged before using the Accelerate Subscription State Transition feature.
- Your payment method will automatically decline when you move the test subscription to grace period or account hold state. When you restore the test subscription, your payment method will restore to automatic approval.
- The subscription state transition process might take a few seconds to execute.
- When the subscription state transition is in progress, the subscription price change feature is not available.
- If you renew the test subscription when a price change is in effect, Play applies the new price if the user has accepted it. However, if the new price requires user acceptance and the user hasn't agreed to it yet, Play cancels the subscription.

### Trial Offers

With the Play Billing Lab trial offer testing feature, a license tester can test and use free trial or introductory offers an unlimited number of times by checking the **Test free trial or introductory offer** checkbox and applying the change. This removes the need to create multiple accounts to test a trial offer only available to new subscribers.

![test trial offers](<https://developer.android.com/static/images/google/play/billing/trial-offers-testing.png>)

**Figure 7.** Test trial offers.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/test).
