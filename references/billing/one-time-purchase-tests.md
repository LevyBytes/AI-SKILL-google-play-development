## Test one-time products

### Test consumable products

When testing consumable products, test a variety of situations, including the following:

- A successful purchase where the user receives an item. With a license tester, you can use the **Test instrument, always approves** payment method.
- A purchase where the payment method failed to be charged, and the user shouldn't receive the item. With a license tester you can use the **Test instrument, always declines** payment method.
- Ensure items can be purchased multiple times.

Verify that purchases are properly acknowledged as described in [processing purchases](<https://developer.android.com/google/play/billing/integrate#process>). For purchases from license testers, a purchase will be refunded after 3 minutes if your app does not acknowledge the purchase and you will receive an email about the cancellation. You can also check the **Orders** tab in the Google Play Console to see if an order was refunded after 3 minutes.

### Test non-consumable products

Non-consumables should be tested the same as consumables, but you should verify an item cannot be purchased again within your app. Be sure to verify purchase acknowledgement for both non-consumables and consumables (when applicable) since the logic to process each the two types of purchases vary.

> **Note:** To perform multiple test purchases for the same non-consumable product, you can [refund and revoke purchases using Google Play Console](<https://support.google.com/googleplay/android-developer/answer/2741495>).

### Test pending purchases

Test a pending purchase where the item should be granted when the purchase state becomes `PURCHASED`. License testers have access to two test instruments for delayed forms of payment where the payment automatically completes or cancels after a couple of minutes.

1. Make a purchase with a delayed form of payment **Slow test card, declines after a few minutes**, as shown in figure 3. Restart the app, validate that the purchase has not been granted.

   ![test a purchase with a declined slow test card](<https://developer.android.com/static/images/google/play/billing/test-delayed-payment-methods-decline.png>)

   **Figure 3.** Test a purchase with a declined slow test card.
2. Make a purchase with a delayed form of payment **Slow test card, approves after a few minutes**, as shown in figure 4. Wait a few minutes, validate that the purchase has been granted.

   ![test a purchase with an approved slow test card](<https://developer.android.com/static/images/google/play/billing/test-delayed-payment-methods-approve.png>)

   **Figure 4.** Test a purchase with an approved slow test card.

You can find more information at [Handling pending transactions](<https://developer.android.com/google/play/billing/integrate#pending>).

### Test user-initiated chargebacks

License testers have access to a test instrument that lets them simulate a user-initiated chargeback.

1. Make a purchase with the test instrument **Test card, approves then charges back**, as shown in figure 5. Soon afterwards, your system should be made aware of the test purchase being delivered and charged back through applicable surfaces. For example, you should receive a [PendingRefundReviewNotification](<https://developer.android.com/google/play/billing/rtdn-reference#pending-refund-review>) moments after making the purchase.

   ![test user-initiated chargebacks](<https://developer.android.com/static/images/google/play/billing/charge-then-charge-back-test-instrument.png>)

   **Figure 5.** Test a purchase with a test card that approves then charges back.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/test).
