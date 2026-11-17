The [program-specific client setup](user-choice-client-and-launch.md) establishes the connection and eligibility checks for this flow.

### Subscription cancellations and restorations

Users should be able to [cancel](<https://developer.android.com/google/play/billing/subscriptions#cancel>) their subscription at any time. When a user cancels a subscription, the termination of the entitlement may be deferred until the paid period ends. For example, if a user cancels a monthly subscription halfway through the month, they may continue to access the service for the remaining ~2 weeks until their access is removed. During this period, the subscription is still technically active, so the user can use the service.

It is not uncommon that users decide to reverse the cancellation during this active period. In this guide, this is called a *restoration*. The following sections describe how to handle restoration scenarios in your alternative billing API integration.

#### Subscriptions bought through an alternative billing system

If you have an external transaction ID for a canceled subscription, it's not necessary to call `launchBillingFlow()` to restore the subscription, so it shouldn't be used for this type of activation. If a user restores their subscription while still in the active period of a canceled subscription, no transaction occurs at that time; you can just continue reporting renewals when the current cycle expires and the next renewal occurs. This includes cases where the user receives a credit or special renewal price as part of the restoration (for example, a promotion to encourage the user to continue their subscription).

#### Subscriptions bought through Google Play's billing system

Generally, users can restore subscriptions on Google Play's billing system. For canceled subscriptions that were originally purchased on Google Play's billing system, the user may choose to undo the cancellation while the subscription is active through Google Play's [Resubscribe](<https://developer.android.com/google/play/billing/subscriptions#restore>) feature. In that case, you receive a `SUBSCRIPTION_RESTARTED` Real Time Developer Notification in your backend, and a new purchase token is **not** issued; the original token is used to continue the subscription. To learn how to manage restoration in Google Play's billing system, see [Restorations](<https://developer.android.com/google/play/billing/subscriptions#restore>) in the subscription management guide.

You can also trigger a restoration in Google Play's billing system from the app by calling `launchBillingFlow()`. See [Before subscription expiration - in-app](<https://developer.android.com/google/play/billing/subscriptions#before-in-app>) for an explanation of how to do this. In the case of users that went through the user choice flow for the original purchase (which was canceled but is still active), the system automatically detects their choice and displays the user interface for restoring these purchases. They are asked to confirm their re-purchase of the subscription through Google Play, but they don't need to go through the user choice flow again. A new purchase token is issued for the user in this case. Your backend receives a `SUBSCRIPTION_PURCHASED` Real Time Developer Notification, and the `linkedPurchaseToken` value for the new purchase status is set as in the case of an upgrade or downgrade, with the old purchase token for the subscription that was canceled.

### Resubscriptions

If a subscription completely expires, whether it is due to cancellation or payment decline without recovery (an expired account hold), then the user must *resubscribe* if they want to restart the entitlement.

Resubscribing can also be enabled through the app by processing it similarly to a standard signup. Users should be able to choose which billing system they want to use. `launchBillingFlow()` may be called in this case, as described in [Launch the user choice billing flow](<https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app?hl=en#launch-user-choice>).

## Test alternative billing

License testers should be used to test your alternative billing integration. You won't be invoiced for transactions that have been initiated by license tester accounts. See [Test in-app billing with application licensing](<https://support.google.com/googleplay/android-developer/answer/6062777>) for more information on configuring license testers.

## Next steps

Once you've finished in-app integration, you're ready to [integrate your backend](<https://developer.android.com/google/play/billing/outside-gpb-backend>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app).
