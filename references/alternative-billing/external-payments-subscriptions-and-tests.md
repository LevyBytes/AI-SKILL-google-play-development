The [program-specific client setup](external-payments-client-setup.md) establishes the connection and eligibility checks for this flow.

## Handle changes in subscription

For developers using external payments, purchases need to be either processed through Google Play's billing system or reported with an `externalTransactionId`, depending on the user's choice. Changes to existing subscriptions that were processed through the developer's website can be made through the same billing system until expiration.

This section describes how to handle some common subscription change scenarios.

### Upgrade and downgrade flows

Subscription plan changes including upgrade and downgrade flows should be handled differently depending on whether the subscription was originally bought through Google Play's billing system or through the developer's website.

Add-ons that depend on an existing subscription, share the same payment method, and align recurring charges are handled as upgrades. For other add-ons, users should be able to choose which billing system they want to use. Initiate a new purchase experience by using `launchBillingFlow()`, as described in [launching the external payments flow](<https://developer.android.com/google/play/billing/externalpaymentlinks/integration?hl=en#launching-external>).

### Subscriptions bought through the developer's website or a payment app

For subscriptions that were originally bought through the developer's website or a payment app after user choice, users requesting an upgrade or a downgrade should proceed through the developer's website or a payment app without going through the user choice experience again.

To do this, call `launchBillingFlow()` when the user requests an upgrade or a downgrade. Instead of specifying other params under the `SubscriptionUpdateParams` object, use [`setOriginalExternalTransactionId()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.Builder#setOriginalExternalTransactionId(java.lang.String)>), providing the external transaction ID for the original purchase.

`DeveloperBillingOptionParams` must also be provided in this call. This does not display the user choice screen, given that the user choice for the original purchase is preserved for upgrades and downgrades. You must generate a new external transaction token for this transaction as described [here](<https://developer.android.com/google/play/billing/externalpaymentlinks/integration?hl=en#prepare-external>).

When the upgrade or downgrade is completed using the developer's website or a payment app, you need to [report a new transaction](<https://developer.android.com/google/play/billing/outside-gpb-backend>) using the external transaction token obtained through the previous call for the new subscription purchase.

### Subscriptions bought through Google Play's billing system

Similarly, users that bought their current subscription through Google Play's billing system after user choice should be shown go through the [standard Google Play Billing flow](<https://developer.android.com/google/play/billing/subscriptions#change>). `DeveloperBillingOptionParams` must not be set in the call to `launchBillingFlow`.

### Subscription cancellations and restorations

Users should be able to [cancel](<https://developer.android.com/google/play/billing/subscriptions#cancel>) their subscription at any time. When a user cancels a subscription, the termination of the entitlement may be deferred until the paid period ends. For example, if a user cancels a monthly subscription halfway through the month, they may continue to access the service for the remaining ~2 weeks until their access is removed. During this period, the subscription is still technically active, so the user can use the service.

It is not uncommon that users decide to reverse the cancellation during this active period. In this guide, this is called a restoration. The following sections describe how to handle restoration scenarios in your external payments API integration.

#### Subscriptions bought through the developer's website

If you have an external transaction ID for a canceled subscription, it's not necessary to call `launchBillingFlow()` to restore the subscription, so it shouldn't be used for this type of activation. If a user restores their subscription while still in the active period of a canceled subscription, no transaction occurs at that time; you can just continue reporting renewals when the current cycle expires and the next renewal occurs. This includes cases where the user receives a credit or special renewal price as part of the restoration (for example, a promotion to encourage the user to continue their subscription).

#### Subscriptions bought through Google Play's billing system

Generally, users can restore subscriptions on Google Play's billing system. For canceled subscriptions that were originally purchased on Google Play's billing system, the user may choose to undo the cancellation while the subscription is active through Google Play's [Resubscribe](<https://developer.android.com/google/play/billing/subscriptions#restore>) feature. In that case, you receive a SUBSCRIPTION_RESTARTED Real Time Developer Notification in your backend, and a new purchase token is not issued; the original token is used to continue the subscription. To learn how to manage restoration in Google Play's billing system, see [Restorations](<https://developer.android.com/google/play/billing/subscriptions#restore>) in the subscription management guide.

You can also trigger a restoration in Google Play's billing system from the app by calling `launchBillingFlow()`. See [Before subscription expiration - in-app](<https://developer.android.com/google/play/billing/subscriptions#before-in-app>) for an explanation of how to do this. In the case of users that went through the user choice flow for the original purchase (which was canceled but is still active), the system automatically detects their choice and displays the user interface for restoring these purchases. They are asked to confirm their re-purchase of the subscription through Google Play, but they don't need to go through the user choice flow again. A new purchase token is issued for the user in this case. Your backend receives a SUBSCRIPTION_PURCHASED Real Time Developer Notification, and the linkedPurchaseToken value for the new purchase status is set as in the case of an upgrade or downgrade, with the old purchase token for the subscription that was canceled.

### Resubscriptions

If a subscription completely expires, whether it is due to cancellation or payment decline without recovery (an expired account hold), then the user must resubscribe if they want to restart the entitlement.

Resubscribing can also be enabled through the app by processing it similarly to a standard signup. Users should be able to choose which billing system they want to use. `launchBillingFlow()` may be called in this case, as described in [launching the external payments flow](<https://developer.android.com/google/play/billing/externalpaymentlinks/integration?hl=en#launching-external>).

## Response handling

When an error occurs, the methods `isBillingProgramAvailableAsync()` , `createBillingProgramReportingDetailsAsync()`, `launchBillingFlow()` might provide a `BillingResponseCode` other than `BillingResponseCode.OK`. Consider handling these response codes as follows:

- [`BillingResponseCode.ERROR`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#ERROR()>): This is an internal error. Don't proceed with the transaction or opening the external website. Retry by calling the API again.
- [`BillingResponseCode.FEATURE_NOT_SUPPORTED`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#FEATURE_NOT_SUPPORTED()>): The external payments APIs are not supported by the Play Store on the current device. Don't proceed with the transaction or opening the external website.
- [`BillingResponseCode.DEVELOPER_ERROR`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#DEVELOPER_ERROR()>): There is an error with the request. Use the debug message to identify and correct the error before proceeding.
- [`BillingResponseCode.USER_CANCELED`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#USER_CANCELED()>): Don't proceed with opening the external website or app. Call `launchBillingFlow()` again to display the information dialog to the user the next time you attempt to direct the user outside of the app.
- [`BillingResponseCode.BILLING_UNAVAILABLE`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#BILLING_UNAVAILABLE()>): The transaction is not eligible for external payments and therefore developer billing won't be available under this program. This is either because the user is not in an eligible country for this program or your account has not been successfully enrolled in the program. If it's the latter, check your enrollment status in the Play Developer Console.
- [`BillingResponseCode.NETWORK_ERROR`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#NETWORK_ERROR()>), [`BillingResponseCode.SERVICE_DISCONNECTED`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_DISCONNECTED()>), [`BillingResponseCode.SERVICE_UNAVAILABLE`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_UNAVAILABLE()>): These are transient errors that should be handled with an appropriate retry policy. In the case of `SERVICE_DISCONNECTED`, re-establish a connection with Google Play before retrying.

## Test external payments links

License testers should be used to test your external payments integration. You won't be invoiced for transactions that have been initiated by license tester accounts. See [Test in-app billing with application licensing](<https://support.google.com/googleplay/android-developer/answer/6062777>) for more information on configuring license testers.

## Next steps

After you've finished in-app integration, you're ready to [integrate your backend](<https://developer.android.com/google/play/billing/outside-gpb-backend>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/externalpaymentlinks/integration).
