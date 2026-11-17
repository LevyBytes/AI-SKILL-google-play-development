### Test cases

Use these scenarios to verify the subscription integration. [Renewal test settings](subscription-renewal-tests.md) define the accelerated test periods.

#### Monthly subscription

| Time | User action | System event | Expected testing outcome |
| --- | --- | --- | --- |
| 12:00 pm | Sign up for an in-app subscription using your licensed test account and the payment method of "Test instrument, always approves" | Subscription started |  |
| 12:05 |  | Subscription renews |  |
| 12:10 |  | Subscription renews |  |
| 12:15 |  | Subscription renews |  |
| 12:20 |  | Subscription renews |  |
| 12:25 |  | Subscription renews |  |
| 12:30 |  | Subscription renews |  |
| 12:35 |  | Subscription ends (after 6 renewals) | User should lose access to in-app subscription content |

#### Monthly subscription with free trial

| Time | User action | System event | Expected testing outcome |
| --- | --- | --- | --- |
| 12:00 pm | Sign up for an in-app subscription using your licensed test account and the payment method of "Test instrument, always approves" | Subscription starts with free trial |  |
| 12:03 |  | Subscription renews |  |
| 12:08 |  | Subscription renews |  |
| 12:13 |  | Subscription renews |  |
| 12:18 |  | Subscription renews |  |
| 12:23 |  | Subscription renews |  |
| 12:28 |  | Subscription renews |  |
| 12:33 |  | Subscription ends (after 6 renewals) | User should lose access to in-app subscription content |

#### Yearly subscription with intro price

| Time | User action | System event | Expected testing outcome |
| --- | --- | --- | --- |
| 12:00 pm | Sign up for an in-app subscription using your licensed test account and the payment method of "Test instrument, always approves" | Subscription started at intro price |  |
| 12:30 |  | Subscription renews at regular price |  |
| 1:00 |  | Subscription renews |  |
| 1:30 |  | Subscription renews |  |
| 2:00 |  | Subscription renews |  |
| 2:30 |  | Subscription renews |  |
| 3:00 |  | Subscription renews |  |
| 3:30 |  | Subscription ends (after 6 renewals) | User should lose access to in-app subscription content |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/test).
