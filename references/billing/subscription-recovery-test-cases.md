#### Monthly subscription with grace period; user recovers

| Time | User action | System event |
| --- | --- | --- |
| 12:00 pm | Sign up for an in-app subscription using your licensed test account and the payment method of "Test instrument always approves" | Subscription started |
| 12:01 | Go to the Google Play app, **Account > Subscriptions**, click your test subscription, and change payment method to "Test instrument, always declines" |  |
| 12:05 | Subscription payment declines and user enters grace period |  |
| 12:08 | Go to the **Account > Subscriptions** section of the Google Play app, click your test subscription, and change payment method to "Test instrument, always approves" | Subscription recovered and exit grace period |
| 12:10 |  | Subscription renews |
| 12:15 |  | Subscription renews |
| 12:20 |  | Subscription renews |
| 12:25 |  | Subscription renews |
| 12:30 |  | Subscription renews |
| 12:35 |  | Subscription renews |
| 12:40 |  | Subscription ends (after 6 renewals) |

#### Monthly subscription with grace period and account hold; user involuntarily churns

| Time | User action | System event | Expected testing outcome |
| --- | --- | --- | --- |
| 12:00 pm | Sign up for an in-app subscription using your licensed test account and the payment method of "Test instrument always approves" | Subscription started |  |
| 12:01 | Go to the **Account > Subscriptions** section of the Google Play app, click your test subscription, and change payment method to "Test instrument, always declines" |  |  |
| 12:05 |  | Payment declined; enter grace period |  |
| 12:10 |  | Exit grace period; enter account hold | User should lose access to in-app subscription content |
| 12:20 |  | Subscription is canceled due to involuntary churn |  |

#### Yearly subscription with grace period and account hold; user recovers during account hold

| Time | User action | System event | Expected testing outcome |
| --- | --- | --- | --- |
| 12:00 pm | Sign up for an in-app subscription using your licensed test account and the payment method of "Test instrument always approves" | Subscription started |  |
| 12:01 | Go to the **Account > Subscriptions** section of the Google Play app, click your test subscription, and change payment method to "Test instrument, always declines" |  |  |
| 12:30 |  | Payment declined; enter grace period |  |
| 12:35 |  | Exit grace period; enter account hold | User should lose access to in-app subscription content |
| 12:45 | Go to the **Account > Subscriptions** section of the Google Play app, click your test subscription, and change payment method to "Test instrument, always approves" | Subscription is recovered, renews, and exits account hold | User should regain access to in-app subscription content |
| 1:15 |  | Subscription renews |  |
| 1:45 |  | Subscription renews |  |
| 2:15 |  | Subscription renews |  |
| 2:45 |  | Subscription renews |  |
| 3:15 |  | Subscription renews |  |
| 3:45 |  | Subscription ends (after 6 renewals) |  |

#### Yearly subscription with grace period and account hold; user involuntarily churns

| Time | User action | System event | Expected testing outcome |
| --- | --- | --- | --- |
| 12:00 pm | Sign up for an in-app subscription using your licensed test account and the payment method of "Test instrument always approves" | Subscription started |  |
| 12:01 | Go to the **Account > Subscriptions** section of the Google Play app, click your test subscription, and change payment method to "Test instrument, always declines" |  |  |
| 12:30 |  | Payment declined; enter grace period |  |
| 12:35 |  | Exit grace period; enter account hold | User should lose access to in-app subscription content |
| 12:45 |  | Subscription is canceled due to involuntary churn |  |

#### Monthly subscription with account hold and no grace period; user recovers

| Time | User action | System event | Expected testing outcome |
| --- | --- | --- | --- |
| 12:00 pm | Sign up for an in-app subscription using your licensed test account and the payment method of "Test instrument always approves" | Subscription started |  |
| 12:01 | Go to the **Account > Subscriptions** section of the Google Play app, click your test subscription, and change payment method to "Test instrument, always declines" |  |  |
| 12:05 |  | Payment declined; enter account hold | User should lose access to in-app subscription content |
| 12:15 | Go to the **Account > Subscriptions** section of the Google Play app, click your test subscription, and change payment method to "Test instrument, always approves" | Subscription is recovered, renews, and exits account hold | User should regain access to in-app subscription content |
| 12:20 |  | Subscription renews |  |
| 12:25 |  | Subscription renews |  |
| 12:30 |  | Subscription renews |  |
| 12:35 |  | Subscription renews |  |
| 12:40 |  | Subscription renews |  |
| 12:45 |  | Subscription ends (after 6 renewals) |  |

#### Monthly subscription with account hold and no grace period; user involuntarily churns

| Time | User action | System event | Expected testing outcome |
| --- | --- | --- | --- |
| 12:00 pm | Sign up for an in-app subscription using your licensed test account and the payment method of "Test instrument always approves" | Subscription started |  |
| 12:01 | Go to the **Account > Subscriptions** section of the Google Play app, click your test subscription, and change payment method to "Test instrument, always declines" |  |  |
| 12:05 |  | Payment declined; enter account hold | User should lose access to in-app subscription content |
| 12:15 |  | Subscription is canceled due to involuntary churn |  |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/test).
