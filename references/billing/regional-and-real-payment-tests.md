## Test the purchase experience in different regions

You can test the purchase experience in different regions with the [Play Billing Lab](<https://developer.android.com/google/play/billing/test?hl=en#play-billing-lab>) app. To use the Play Billing Lab, you must be a license tester. Use the following steps to test:

1. Register the app billing user as a license tester.
2. Log into Play Billing Lab app with the same user.
3. Select the required country and apply the change in Play Billing Lab.
4. Launch the purchase flow in the app under testing.

   ![test purchase experience in different regions](<https://developer.android.com/static/images/google/play/billing/play-billing-lab-country.png>)

   **Figure 11.** Test purchase experience in different regions.

[Play Billing Lab](<https://developer.android.com/google/play/billing/test?hl=en#play-billing-lab>) lets you test offer regional eligibility and the user experience in any region, regardless of where you are physically testing.

> **Note:** Gmail accounts created for testing purposes shouldn't be used to make purchases using real instruments on Google Play. This includes other apps and purchases such as Google Books.

## Test the purchase experience using real payment methods

You can test the purchase experience with real payment methods with the [Play Billing Lab](<https://developer.android.com/google/play/billing/test?hl=en#play-billing-lab>) Android app.

> **Note:**
>
> - You need permissions to access this feature. Contact your Google Play Business Development manager to opt in.
> - You lose all other license tester features and Play Billing Lab configurations when you enable testing for real payment methods. Request a [refund](<https://support.google.com/googleplay/android-developer/answer/2741495>) for each purchase, or you will be charged a [service fee](<https://support.google.com/googleplay/android-developer/answer/11131145>).

Use the following steps to test real payment methods:

1. Register the Google Account user as a license tester.
2. Log into the Play Billing Lab app with the same user.
3. Enable real payment methods in the Play Billing Lab app.
4. Restart and launch the purchase flow in the app under testing.

## Spend limits for unpublished apps

Apps that are in the draft stage or published to the internal test track, are subject to spend limits.

Google Play enforces limits on the following:

- **Daily transactions:** The number of transactions a user can make per day across all unpublished apps.
- **Per-order value:** The maximum amount for an individual transaction.
- **Daily total spend:** The cumulative daily expenditure for a user across all unpublished apps.

These limits reset every 24 hours.

If a user exceeds any of these limits while testing your app, they will see an error message in the purchase cart, and the transaction will be blocked.

> **Note:** If your testing requires higher limits, ensure your app is published to a [closed, open, or production track](<https://support.google.com/googleplay/android-developer/answer/9859751>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/test).
