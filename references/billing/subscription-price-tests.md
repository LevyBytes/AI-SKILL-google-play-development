### Price changes

You can also use Play Billing Lab and license testers to test [subscription price changes](<https://developer.android.com/google/play/billing/price-changes>) without affecting other active subscribers with the following steps:

1. Click **Manage** on the **Subscription settings** card in the **Dashboard**.
2. Choose the active subscription you want to test.
3. Enter the new price.
4. Select or unselect the **User opt-out** checkbox per your test requirement.
5. Click **Apply**.

![test subscription price change](<https://developer.android.com/static/images/google/play/billing/play-billing-lab-price-change.png>)

**Figure 8.** Test subscription price change.

After applying your changes, the price is updated starting from the next renewal only for the tester. Other active subscribers won't be affected. All the license testers rules apply to the test subscription. The tester can then test their app for downstream processes triggered by the price change, such as price change notifications.

Keep the following considerations in mind when planning test periods:

- Due to a small renewal duration for license testers, it's possible that a price migration made from the console won't register for license testers. To ensure that price change notifications and emails can be tested, developers should defer billing by at least one hour after triggering a price change.
- Price decreases don't have a notification period. Users are notified of a price decrease soon after cohort migration. This is unchanged when testing.
- For price increases, test notification times are calculated the same as with actual increases:

  - The user is first charged at the first billing anniversary following a mandatory notification period.
  - Notification times are calculated backward from the first charge date.
  - The final notification is always 1 minute before the charge, regardless of billing period.

The following table shows test billing and notification periods for several actual billing periods:

| **Actual base plan billing period** | **Test billing period** | **Test notification period (opt-in and opt-out regions with 30 day notice)** | **Test notification period (opt-out regions with 60 day notice)** |
| --- | --- | --- | --- |
| 1 week | 5 minutes | 5 minutes | 10 minutes |
| 1 month | 5 minutes | 5 minutes | 10 minutes |
| 3 months | 10 minutes | 3 minutes | 6 minutes |
| 6 months | 15 minutes | 2 minutes | 4 minutes |
| 1 year | 30 minutes | 3 minutes | 6 minutes |

### Price step-up consent

> **Note:** The price step-up consent feature is available only to the subscriptions in the South Korea (KR) region.

Information related to a price step-up that requires user consent will be available to you in the [`purchases.subscriptionsv2.get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) API.

Google Play sends two push and email price step-up notifications to the relevant users (including license testers) before the step-up is live. The notification period for testing is as follows:

| **Notification schedule** | **Test notification period** |
| --- | --- |
| First notification | 3 minutes |
| Second (final) notification | 1 minute |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/test).
