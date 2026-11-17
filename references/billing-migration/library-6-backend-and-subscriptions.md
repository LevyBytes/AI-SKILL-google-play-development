### Manage subscription purchase status with the new API in your backend

You should migrate the backend subscription purchase-status component to handle purchases of the new products created in the previous steps. Your existing component should continue handling automatically converted legacy subscription products and backward-compatible offers, but it does not support the new base-plan and offer functionality.

You need to implement the new [Subscription Purchases API](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) for your subscriptions purchase status management module, which checks the purchase status and manages Play Billing subscription entitlements in your backend. The [old version](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions>) of the API doesn't return all the necessary details to manage purchases in the new platform. For details on changes from previous versions, see the guide to the [base-plan and offer subscription features](<https://developer.android.com/google/play/billing/compatibility#managing_subscription_status>).

When migrating your purchase status management module:

- Call the [Subscription Purchases API](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) every time you receive a [`SubscriptionNotification` Real Time Developer Notification](<https://developer.android.com/google/play/billing/rtdn-reference#sub>) to pull the latest information about the subscription status.
- Replace your calls to [`purchases.subscriptions.get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/get>) with the new version of the Subscription Purchases API, [`purchases.subscriptionsv2.get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>).
- Use the new [`SubscriptionPurchaseV2`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#resource:-subscriptionpurchasev2>) resource, which provides enough information to manage purchase entitlement for subscriptions in the new model.

The new endpoint returns purchase status for every subscription product and purchase, regardless of the selling app's version or whether the product predates the base-plan and offer transition. After migration, only this version of your backend subscription purchase-status component is needed.

### Change a user's subscription purchases

In Play Billing Library 5 and earlier, [`ProrationMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.ProrationMode>) was used to apply changes to a user's subscription purchases, such as upgrades or downgrades. This has been deprecated and replaced with [`ReplacementMode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.SubscriptionUpdateParams.ReplacementMode>) in version 6.

### Handle subscription price changes

The previously deprecated `launchPriceConfirmationFlow` API has been removed in Play Billing Library 6. For alternatives, see the [price changes guide](<https://developer.android.com/google/play/billing/price-changes>).

### Handle Play Billing Library errors

In Play Billing Library 6, a new `NETWORK_ERROR` code has been added to indicate problems with the network connection between the user's device and the Google Play system. There were also changes to the codes `SERVICE_TIMEOUT` and `SERVICE_UNAVAILABLE`. For more information, see [Handle BillingResult response codes](<https://developer.android.com/google/play/billing/errors>).

### Handle pending transactions

Starting with version 6.0.0, the Play Billing Library does not create an order ID for pending purchases. For these purchases, the order ID is populated after the purchase is moved to the [`PURCHASED`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase.PurchaseState#PURCHASED>) state. Make sure that your integration only expects an order ID after a transaction is fully completed. You can still use the purchase token for your records. For more information about handling pending purchases, see the Play Billing Library [integration guide](<https://developer.android.com/google/play/billing/integrate>) and the [purchase lifecycle management guide](<https://developer.android.com/google/play/billing/lifecycle>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/migrate-gpblv6).
