#### Installment subscription with an initial 12-month commitment period, followed by automatic monthly renewals

| Time | User action | System event | Expected testing outcome |
| --- | --- | --- | --- |
| 12:00 pm | Sign up for an in-app payment plan subscription using your licensed test account and the payment method of "Test instrument, always approves" | Subscription starts |  |
| 12:05 |  | Successful installment payment |  |
| 12:10 |  | Successful installment payment |  |
| 12:15 |  | Successful installment payment |  |
| 12:20 |  | Successful installment payment |  |
| 12:25 |  | Successful installment payment |  |
| 12:30 |  | Successful installment payment |  |
| 12:35 |  | Successful installment payment |  |
| 12:40 |  | Successful installment payment |  |
| 12:45 |  | Successful installment payment |  |
| 12:50 |  | Successful installment payment |  |
| 12:55 |  | Successful installment payment |  |
| 1:00 |  | Subscription renews (monthly auto-renewals) |  |
| 1:05 |  | Successful installment payment |  |
| 1:10 |  | Successful installment payment |  |
| 1:15 |  | Successful installment payment |  |
| 1:20 |  | Successful installment payment |  |
| 1:25 |  | Successful installment payment |  |
| 1:30 |  | Subscription ends (after 6 renewals) | User should lose access to in-app subscription content |

#### Installment subscription with an initial 6-month commitment period, followed by automatic renewal for the same duration (6 months)

| Time | User action | System event | Expected testing outcome |
| --- | --- | --- | --- |
| 12:00 pm | Sign up for an in-app payment plan subscription using your licensed test account and the payment method of "Test instrument, always approves" | Subscription starts |  |
| 12:05 |  | Successful installment payment |  |
| 12:10 |  | Successful installment payment |  |
| 12:15 |  | Successful installment payment |  |
| 12:20 |  | Successful installment payment |  |
| 12:25 |  | Successful installment payment |  |
| 12:30 |  | Subscription renews (repeating initial commitment period) |  |
| 12:35 |  | Successful installment payment |  |
| 12:40 |  | Successful installment payment |  |
| 12:45 |  | Successful installment payment |  |
| 12:50 |  | Successful installment payment |  |
| 12:55 |  | Successful installment payment |  |
| 1:00 |  | Subscription ends (after 6 renewals) | User should lose access to in-app subscription content |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/test).
