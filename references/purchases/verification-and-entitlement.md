The [client connection](client-connection.md) supplies the `BillingClient` and listener. [Product queries](product-query.md) supply the product details used by the purchase flow.

## Detect and process purchases

The detection and processing of a purchase described in this section is applicable to all types of purchases including out of app purchases like promotion redemptions.

Your app detect new purchases and completed [pending purchases](<https://developer.android.com/google/play/billing/integrate?hl=en#pending>) in one of the following ways:

1. When `onPurchasesUpdated` is called as a result of your app calling `launchBillingFlow` (as described in [purchase launch](launch-and-personalized-prices.md)) or if your app is running with an active Billing Library connection when there is a purchase made outside your app or a pending purchase is completed. For example, a family member approves a pending purchase on another device.
2. When your app calls queryPurchasesAsync to query the user's purchases.

For #1 `onPurchasesUpdated` will automatically be called for new or completed purchases as long as your app is running and has an active Google Play Billing Library connection. If your application is not running or your app doesn't have an active Google Play Billing library connection, `onPurchasesUpdated` won't be invoked. Remember, it is recommended for your app to try to keep an active connection as long as your app is in the foreground so that your app gets timely purchase updates.

For #2 you must call [BillingClient.queryPurchasesAsync()](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>) to ensure your app processes all purchases. It is recommended that you do this when your app successfully establishes a connection with the Google Play Billing Library (which is recommended when your app is launched or comes to the foreground as discussed in [initialize a BillingClient](<https://developer.android.com/google/play/billing/integrate?hl=en#initialize>). This can be accomplished by calling queryPurchasesAsync when receiving a successful result to [onServiceConnected](<https://developer.android.com/google/play/billing/integrate?hl=en#initialize>). Following this recommendation is critical to handle events and situations such as:

- **Network Issues during the purchase**: A user can make a successful purchase and receive confirmation from Google, but their device loses network connectivity before their device and your app receives notification of the purchase through the `PurchasesUpdatedListener`.
- **Multiple devices**: A user may buy an item on one device and then expect to see the item when they switch devices.
- **Handling purchases made outside your app**: Some purchases, such as promotion redemptions, can be made outside your app.
- **Handling purchase state transitions**: A user may complete payment for a PENDING purchase while your application is not running and expect to receive confirmation that they completed the purchase when they open your app.
- **Suspended subscriptions**: A subscription may become suspended during the [Subscription Lifecycle](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#new-auto>). [BillingClient.queryPurchasesAsync()](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>) will return suspended subscriptions only if the `includeSuspendedSubscriptions` parameter is set on `QueryPurchasesParams.Builder`. Suspended subscriptions are not returned in `PurchasesUpdatedListener`.

> **Note:** You can also choose to listen to Real-time Developer Notifications to learn about new purchases, completed pending purchases, and subscription lifecycle changes in real-time, even if the user is not using your app when the event occurs. This helps you keep your backend state in sync at all times. This is described in more detail in the backend integration section for [one-time purchases](<https://developer.android.com/google/play/billing/lifecycle/one-time#process>) and [subscriptions](<https://developer.android.com/google/play/billing/lifecycle/subscriptions#new-auto>).

Once your app detects a new or completed purchase then your app should:

- Verify the purchase.
- Grant content to the user for completed purchases.
- Notify the user.
- Notify Google that your app processed completed purchases.

Verification and entitlement are covered here; [consumption and acknowledgement](consumption-and-acknowledgement.md) and [rejected or pending purchases](rejected-and-pending-purchases.md) complete processing.

### Verify the purchase

Your app should always verify the legitimacy of purchases before granting benefits to a user. This can be done by following the guidelines described in [Verify purchases before granting entitlements](<https://developer.android.com/google/play/billing/security#verify>). Only after verifying the purchase should your app continue to process the purchase and grant entitlements to the user, which is discussed in the next section. If a purchase fails your verification, eligibility, or abuse checks, see [Handle rejected or unfulfilled purchases](<https://developer.android.com/google/play/billing/integrate?hl=en#rejected-purchases>).

### Grant entitlement to the user

Once your app has verified a purchase it can continue to grant the entitlement to the user and notify the user. Before granting entitlement, verify that your app is checking that the [purchase state](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getpurchasestate>) is [`PURCHASED`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase.PurchaseState>). If the purchase is in PENDING state, your app should notify the user that they still need to complete actions to complete the purchase before entitlement is granted. Only grant entitlement when the purchase transitions from PENDING to PURCHASED. Additional information can be found in [Handling pending transactions](<https://developer.android.com/google/play/billing/integrate?hl=en#pending>).

If you have attached user identifiers to the purchase as discussed in [attaching user identifiers](<https://developer.android.com/google/play/billing/integrate?hl=en#user-identifiers>) you can [retrieve](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getAccountIdentifiers()>) and use them to attribute to the correct user in your system. This technique is useful when reconciling purchases where your app may have lost context about which user a purchase is for. To protect against abuse, Google Play recommends that you verify these identifiers on your secure backend before granting entitlements. For more information, see [Verify purchases before granting entitlements](<https://developer.android.com/google/play/billing/security#verify>). Note, purchases made outside your app won't have these identifiers set. In this case your app can either grant the entitlement to the logged in user, or prompt the user to select a preferred account.

For [pre-orders](<https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers#pre-order>), the purchase is in PENDING state before the release time is reached. The preorder purchase will complete at the release time and change the state to PURCHASED without additional actions.

### Notify the User

After granting entitlement to the user, your app should show a notification to acknowledge the successful purchase. Because of the notification, the user is not confused as to whether the purchase completed successfully, which could result in the user stopping using your app, contacting user support, or complaining about it on social media. Be aware that your app may detect purchase updates at any time during your application lifecycle. For example, a parent approves a pending purchase on another device, in which case your app may want to delay notifying the user to an appropriate time. Some examples where a delay would be appropriate are:

- During the action part of a game or cutscenes, showing a message may distract the user. In this case, you must notify the user after the action part is over.
- During the initial tutorial and user setup parts of the game. For example, a user may have made a purchase outside your app before installing it. We recommend you notify new users of the reward immediately after they open the game or during initial user setup. If your app requires the user to create an account or logging in before granting entitlement to the user it is recommended to communicate to your user which steps to complete to claim their purchase. This is critical since purchases are refunded after 3 days if your app has not processed the purchase.

When notifying the user about a purchase, Google Play recommends the following mechanisms:

- Show an in-app dialog.
- Deliver the message to an in-app message box, and clearly stating that there is a new message in the in-app message box.
- Use an OS notification message.

The notification should notify the user about the benefit they received. For example, "You purchased 100 Gold Coins!". Additionally, if the purchase was a result of a benefit of a program such as Play Pass your app communicates this to the user. For example "Items received! You just got 100 Gems with Play Pass. Continue.". Each program may have guidance on the recommended text to display to users to communicate benefits.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/integrate).
