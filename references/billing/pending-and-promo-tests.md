## Test pending transactions

You should test pending transactions are handled correctly and entitlements are updated accordingly when the purchase state becomes `PURCHASED`. License testers have access to two test instruments for delayed forms of payment where the payment automatically completes or cancels after a couple of minutes.

1. Make a purchase with a delayed form of payment **Slow test card, declines after a few minutes**, as shown in figure 9. Restart the app, validate that the purchase has not been granted.

   ![test a purchase with a declined slow test card](<https://developer.android.com/static/images/google/play/billing/test-delayed-payment-methods-decline.png>)

   **Figure 9.** Test a purchase with a declined slow test card.
2. Make a purchase with a delayed form of payment **Slow test card, approves after a few minutes**, as shown in figure 10. Wait a few minutes, validate that the purchase has been granted.

   ![test a purchase with an approved slow test card](<https://developer.android.com/static/images/google/play/billing/test-delayed-payment-methods-approve.png>)

   **Figure 10.** Test a purchase with an approved slow test card.

## Test promo codes

You can use the Google Play Console to [create codes for your own testing](<https://support.google.com/googleplay/android-developer/answer/6321495>). Keep in mind that you may only create 500 promo codes per quarter across all managed products in an app.

You should test the following promo code redemption scenarios:

- When the promo code is entered in the purchase dialog that was launched within your app.
- When the promo code is redeemed in the Google Play Store app.
- When the promo code is redeemed at [https://play.google.com/store](<https://play.google.com/store>) using the **Redeem** button in the left-hand navigation.

Within these scenarios, you should test redeeming codes in as many ways as possible. Perform the following tests at a minimum:

- Redemption before the app is installed.
- Redemption while the app is running in the foreground. Note that for this test, you need another device to test using the Google Play Store app. Be sure to test redemptions from different screens in your app.
- Redemption with [multi-window mode](<https://developer.android.com/guide/topics/ui/multi-window>), where both your app and the Google Play Store app are being displayed at the same time.

For each test, make sure that the item is correctly detected and that the user is notified.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/test).
