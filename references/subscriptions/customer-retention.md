## Customer management

Using Real-time developer notifications, you can detect in real time when a user decides to cancel. When a user cancels, but before their subscription has expired, you can send them push notifications or in-app messages to ask them to resubscribe.

After a user has cancelled their subscription, you can try to win them back either in your app, or through the Play store. The following table describes various subscription scenarios along with associated winback actions and app requirements.

| Entry | Details | Details | Details | Details |
| --- | --- | --- | --- | --- |
|  | **Before subscription expiration** | **Before subscription expiration** | **After subscription expiration** | **After subscription expiration** |
|  | **In-app** | **In Play Store** | **In-app** | **In Play Store** |
| **Winback feature** | In-app subscription | Restore | In-app subscription | Resubscribe |
| **User goes through checkout flow** | Yes | No | Yes | Yes |
| **User subscription remains associated with the same SKU** | User can sign up for same or different SKU | Yes | User can sign up for same or different SKU | Yes |
| **Creates new purchase token** | Yes | No | Yes | Yes |
| **Enabled by default** | No | Yes, support required for all devs | No | Apps without Billing Library 2.0+: No<br> Apps with Billing Library 2.0+: Yes. Devs can opt-out in Console. |
| **When user is charged** | If using same SKU: end of current billing period.<br> If using different SKU: depends on proration mode. | End of current billing period | Immediately | Immediately |
| **Implementation required** | Provide a re-signup UI in your app | Detect change in subscription state<br> Deep-link to Play Store | Provide a re-signup UI in your app | Handle out-of-app purchases |

### Before subscription expiration - in-app

For subscriptions that have been canceled but have not yet expired, you can allow subscribers to restore their subscription within your app by applying the same in-app product purchase flow as for new subscribers. Ensure your UI reflects that the user has an existing subscription. For example, you might want to display the user's current expiration date and recurring price with a **Reactivate** button.

Most of the time, you will want to offer the user the same price and SKU they were already subscribed to, as follows:

- Initiate a new subscription purchase with the same SKU.
- The new subscription replaces the old one and renews on the same expiration date. The old subscription is immediately marked as expired.
- Example: Achilles resubscribes to the one-month Example Music App plan before its existing entitlement expires, at the same monthly price. The remaining credit is prorated into the new subscription, which becomes active immediately and retains the original renewal boundary.

If you would like to offer a different price (for example a new free trial or a winback discount), you can instead offer a different SKU to the user:

- Initiate an [upgrade or downgrade](<https://developer.android.com/google/play/billing/subscriptions?hl=en#allow-users-change>) with the different SKU using the replacement mode `WITHOUT_PRORATION`.
- The new subscription replaces the old one and renews on the same expiration date. The user is charged the price of the new SKU, including any introductory prices, on the original expiration date. If the old subscription was created using an obfuscated account ID, that same ID should be passed to the `BillingFlowParams` for upgrades and downgrades.
- Example: Before his existing Example Music App entitlement expires, Achilles resubscribes to an annual plan with an introductory price. The new subscription becomes active immediately; its introductory price is charged at the original entitlement's expiration boundary.
- If you decide to include a free trial or intro price in your winback SKU, ensure that the user is eligible by unchecking the **Allow one free trial per app** box in the Google Play Console, which restricts the user to getting one free trial per app.

When you receive the purchase token, [process the purchase](<https://developer.android.com/google/play/billing/integrate#process>) just as you would with a new subscription. Additionally, the Google Play Developer API returns a `linkedPurchaseToken` in the subscription resource. Be sure to [invalidate the token](<https://developer.android.com/google/play/billing/subs#upgrade-downgrade>) provided in the `linkedPurchaseToken` to ensure that the old token is not used to gain access to your services.

### Before subscription expiration - in Play Store

> **Note:** Supporting restore is required for all developers.

While the subscription is canceled but still active, users can restore the subscription in the Google Play subscriptions center by clicking **Resubscribe** (previously **Restore**). This keeps the same subscription and purchase token.

![subscriptions section in the google play store app showing a cancelled subscription with a resubscribe button](<https://developer.android.com/static/images/google/play/billing/resubscribe.jpg>)

**Figure 8.** *Account > Subscriptions* section in the Google Play Store app showing a cancelled subscription with a **Resubscribe** button.

For more information on restoring subscriptions, see [Restorations](<https://developer.android.com/google/play/billing/subscriptions?hl=en#restore>).

### After subscription expiration - in-app

You can allow expired subscribers to resubscribe within your app by applying the same in-app product purchase flow as for new subscribers. Note the following:

- To offer users a discount, you might want to offer a product ID with special pricing for your subscription, also called a *winback SKU*. You can provide the offer in your app, or you can notify the user of the offer outside of the app, such as in email.
- To start a winback subscription, launch the purchase flow in your Android app using the Google Play Billing Library. This is the same process as with a new subscription, but you can determine the SKU that is available to the user.
- If you decide to include a free trial or intro price in your winback SKU, ensure that the user is eligible by unchecking the **Allow one free trial per app** box in the Google Play Console, which restricts the user to getting one free trial per app.
- If the user resubscribes to the same SKU, they are no longer eligible for free trials or introductory price. Ensure that your UI reflects this.

When you receive the purchase token, [process the purchase](<https://developer.android.com/google/play/billing/integrate#process>) just as you would with a new subscription. You won't receive a `linkedPurchaseToken` in the subscription resource.

### After subscription expiration - in Play Store

> **Note:** Resubscribe from Play Store is only available to apps with Google Play Billing Library versions 2.0 and later.

> **Note:** All subscription SKUs for eligible apps have resubscribe enabled by default. You can opt out at any time by adjusting the SKU settings through the [Google Play Console](<https://support.google.com/googleplay/android-developer/answer/140504>).

If enabled, users can resubscribe to the same SKU for up to one year after expiration by clicking **Resubscribe** in the Google Play subscriptions center. This generates a new subscription and purchase token.

![subscriptions section in the google play store app showing a cancelled and expired subscription with resubscribe and remove buttons](<https://developer.android.com/static/images/google/play/billing/resubscribe-remove.jpg>)

**Figure 9.** *Account > Subscriptions* section in the Google Play Store app showing a cancelled and expired subscription with **Resubscribe** and **Remove** buttons.

Re-subscribing is considered an out-of-app purchase, so be sure to follow best practices for [properly acknowledging them from your backend](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#resubscribe_after_expiration>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscriptions).
