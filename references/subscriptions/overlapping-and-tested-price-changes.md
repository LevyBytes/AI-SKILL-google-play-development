## Accidental price increases

This section describes the various scenarios for handling an accidental price change.

- **Opt-in increase** - If you've accidentally initiated an opt-in price increase, reverse the change immediately by making another price change back to the original price.

  Change the base plan price back to the original price and navigate to the legacy price points page to initiate a price decrease to the original price. Existing subscribers are not notified about the accidental price change if the price is reverted within seven days. If the price is reverted back to the old price after seven days, the price change will be canceled for any users who have not paid the new price. The price change is cancelled after the [payment authorization](<https://support.google.com/googleplay/answer/2476088>) period of up to five days. Based on renewal dates, some users may have already received the opt-in email notice.
- **Opt-out increase** - You can cancel an accidental opt-out increase by reverting the price back to the original price. Change the base plan price back to the original price and navigate to the legacy price points page to initiate a price decrease to the original price. Depending on when the price is reverted if a user has not already paid the higher price, their price increase would be canceled after the [payment authorization](<https://support.google.com/googleplay/answer/2476088>) period of up to five days. Based on renewal dates, some users may have already received the price increase notice emails.
- **Price decreases** - You can cancel a price decrease by reverting the subscription's price back to its original value by using the Google Play Console. Change the base plan price back to the original price and navigate to the legacy price points page to initiate a price increase to the original price. Developers can initiate either opt-in or opt-out (if eligible) to cancel the price decrease. If using opt-out, it would be counted toward the frequency. Google Play determines whether the cancellation is effective for a given user's next renewal based on the timing of this reversion relative to their individual renewal date.

  - A price decrease cancellation is valid if the period between reverting the price to its original value and a user's expected renewal time at the new price exceeds the relevant country-specific notification window (30 or 60 days). The user's next subscription renewal occurs at the original, higher price.
  - A price decrease cancellation is invalid if the period between reverting the price to its original value and a user's expected renewal time at the new price is shorter or equal to the relevant country-specific notification window (30 or 60 days). The user will instead go through the price increase process after being charged the lower price at least once upon the next renewal. The user will then get notified about a price increase. Depending on the mode selected during the price migration users would need to accept the price increase for opt-in price increase or would receive the notifications about an opt out increase. Any frequency and amount limitations for opt out increase would apply in this case.

## Handle overlapping price changes

Make sure that you only do one price change at a time. However, if you perform a price change multiple times, impacted users need to agree only to the latest price change. For example, if you've ended a legacy price cohort with an opt-in price increase, changed the price again, and then performed another opt-in price increase, affected users no longer need to respond to the first price increase because only the second price increase now applies. This behaviour applies for legacy price opt-in and opt-out price increases and price decreases.

When you start a new price migration for an item that has an older price migration in progress, Google Play handles it as follows:

- Old price migration is canceled.

  Google Play stops the old price migration. In the `SubscriptionPurchaseV2` API, you'll see the old price change details marked as `CANCELED`. You'll also receive a `SUBSCRIPTION_PRICE_CHANGE_UPDATED` RTDN.
- New Price Migration takes over.

  Immediately after, Google Play starts the new price migration. This will appear in `SubscriptionPurchaseV2` as either `OUTSTANDING` (for opt-in increases) or `CONFIRMED` (for opt-out increases or price decreases). You'll receive another `SUBSCRIPTION_PRICE_CHANGE_UPDATED` RTDN for the item.
- The user gets the new price.

  The user will now be moved to the new price migration, and they won't complete the previous price change. And the user receives the standard notification period for the new price.

## Test price changes

Don't change subscription prices for products owned by active subscribers for testing purposes.

You can use the [Play Billing Lab app](<https://play.google.com/store/apps/details?id=com.google.android.apps.play.billingtestcompanion>) and license testers to test subscription price changes without affecting other active subscribers.

See the [testing guide](<https://developer.android.com/google/play/billing/test#price-changes>) to learn more about testing price changes.

## Examples

The [opt-in examples](opt-in-price-examples.md) and [opt-out or price step-up examples](opt-out-and-step-up-price-examples.md) demonstrate the relevant price-change scenarios.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/price-changes).
