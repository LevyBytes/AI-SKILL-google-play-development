### Handle rejected or unfulfilled purchases

If a purchase fails your backend verification, user eligibility checks, fraud and abuse checks, or if your system can't fulfill the entitlement, don't grant the entitlement and don't acknowledge or consume the purchase.

While unacknowledged purchases are automatically refunded and revoked after the acknowledgment window expires as a consumer safety net, don't rely on this expiration window to reject purchases. Letting the acknowledgment window expire leaves the order in an unacknowledged state and is ambiguous to Google Play, which can't distinguish an intentional developer rejection from a backend processing timeout.

Instead, immediately revoke and refund rejected purchases from your backend using the Google Play Developer API:

- **Subscriptions**: Call [`purchases.subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) with `"fullRefund": {}` in [`revocationContext`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke#revocationcontext>). This immediately terminates the subscription, revokes access, and initiates a full refund.
- **One-time products**: Call [`orders.refund`](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund>) with the `revoke` parameter set to `true` to immediately refund an order and revoke its entitlement. When calling this method, you must pass the purchase's order ID, which you can retrieve using [`Purchase.getOrderId()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getorderid>) or [`purchases.productsv2.getproductpurchasev2`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.productsv2/getproductpurchasev2>). Never call [`consumeAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#consumeasync>), [`acknowledgePurchase()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#acknowledgepurchase>), [`Purchases.products:consume`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/consume>), or [`Purchases.products:acknowledge`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/acknowledge>) on rejected purchases.
- **RTDN and Voided Purchases behavior**: Developer-initiated revocations and refunds (`purchases.subscriptionsv2.revoke` and `orders.refund` with `revoke` set to `true`) trigger Real-time developer notifications and are recorded in the [Voided Purchases API](<https://developers.google.com/android-publisher/voided-purchases>) (`purchases.voidedpurchases.list` with the `voidedSource` response field set to `1` for developer):

  - **Subscriptions**: Sends both a `SUBSCRIPTION_REVOKED` notification and a `VoidedPurchaseNotification`.
  - **One-time products**: Sends a `VoidedPurchaseNotification` (and a `ONE_TIME_PRODUCT_CANCELED` notification if your app is configured in Play Console to receive all one-time product notifications).
  - Calling `orders.refund` without `revoke` set to `true` refunds the order without revoking entitlement and doesn't trigger a revocation or voided purchase notification. For more details, see [Manage subscriptions and one-time purchases](<https://developer.android.com/google/play/billing/manage-purchases#issue_refunds_and_revocations>).

### Recap

The following is a recap of these steps.

1. Send the purchase to your secure backend to [verify purchases before granting entitlements](<https://developer.android.com/google/play/billing/security#verify>).
2. Update your entitlement storage with the purchase. If purchase is in PENDING state then ensure the entitlement is marked as pending and the user does not receive benefits yet. It is recommended that this step is done on your secure backend and can combine in the API call to your backend in step 1.
3. Notify the user using appropriate messaging (delaying notification if needed as discussed previously).
4. Notify Google the purchase was processed using the steps discussed in the processing purchases section.

To verify your app has correctly implemented these steps you can follow the [testing guide](<https://developer.android.com/google/play/billing/test>).

## Handle pending transactions

Google Play supports *pending transactions*, or transactions that require one or more additional steps between when a user initiates a purchase and when the payment method for the purchase is processed. Your app shouldn't grant entitlement to these types of purchases until Google notifies you that the user's payment method was successfully charged.

For example, a user can initiate a transaction by choosing a physical store where they'll pay later with cash. The user receives a code through both notification and email. When the user arrives at the physical store, they can redeem the code with the cashier and pay with cash. Google then notifies both you and the user that payment has been received. Your app can then grant entitlement to the user.

Call [`enablePendingPurchases()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#enablependingpurchases(com.android.billingclient.api.PendingPurchasesParams)>) as part of initializing the `BillingClient` to enable pending transactions for your app. Your app must enable and support pending transactions for one-time products. Before adding support, be sure you understand the [purchase lifecycle](<https://developer.android.com/google/play/billing/lifecycle>) for pending transactions.

> **Note:** For apps using Google Play Billing Library version 7.0 and higher, you can enable pending transactions for subscription prepaid plan purchases. See [Handle subscription pending transactions](<https://developer.android.com/google/play/billing/subscriptions#pending>) for how to support in your app.

When your app receives a new purchase, either through your [`PurchasesUpdatedListener`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener>) or as a result of calling [`queryPurchasesAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>), use the [`getPurchaseState()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getpurchasestate>) method to determine whether the purchase state is `PURCHASED` or `PENDING`. You should grant entitlement **only** when the state is `PURCHASED`.

If your app is running and you have an active Play Billing Library connection when the user completes the purchase, your [`PurchasesUpdatedListener`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener>) is called again, and the `PurchaseState` is now `PURCHASED`. At this point, your app can process the purchase using the standard method for [Detecting and Processing Purchases](<https://developer.android.com/google/play/billing/integrate?hl=en#process>). Your app should also call `queryPurchasesAsync()` in your app's `onResume()` method to handle purchases that have transitioned to the `PURCHASED` state while your app was not running.

> **Note:** You should acknowledge a purchase only when the state is `PURCHASED`. That is, don't acknowledge it while a purchase is in `PENDING` state. The three-day acknowledgement window begins only when the purchase state transitions from 'PENDING' to 'PURCHASED'.

When the purchase transitions from `PENDING` to `PURCHASED`, your [real_time_developer_notifications](<https://developer.android.com/google/play/billing/getting-ready#configure-rtdn>) client receives a `ONE_TIME_PRODUCT_PURCHASED` or `SUBSCRIPTION_PURCHASED` notification. If the purchase is cancelled, you will receive a `ONE_TIME_PRODUCT_CANCELED` or `SUBSCRIPTION_PENDING_PURCHASE_CANCELED` notification. This can happen if your customer does not complete payment in the required timeframe. Note that you can always use the Google Play Developer API to check the current state of a purchase.

> **Note:** Pending transactions can be tested with application licensing. In addition to two test credit cards, license testers have access to two test instruments for delayed forms of payment where the payment automatically completes or cancels after a couple of minutes. You can find detailed steps on how to test this scenario at [Test pending transactions](<https://developer.android.com/google/play/billing/test#pending-purchases>).

## Handle multi-quantity purchases

Supported in versions 4.0 and higher of the Google Play Billing Library, Google Play allows customers to purchase more than one of the same one-time product in one transaction by specifying a quantity from the purchase cart. Your app is expected to handle multi-quantity purchases and grant entitlement based on the specified purchase quantity.

> **Note:** Multi-quantity is meant for consumable one-time products, products that can be purchased, consumed, and purchased again. Don't enable this feature for products that are not meant to be purchased repeatedly. And in the case of offers, multi-quantity purchases are only supported for [purchase options (buy or rent)](<https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers#options>) and not [offers](<https://developer.android.com/google/play/billing/one-time-product-multi-purchase-options-offers#options>).

To honor multi-quantity purchases, your app's provisioning logic needs to check for an item quantity. You can access a `quantity` field from one of the following APIs:

- [`getQuantity()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getquantity>) from the Google Play Billing Library.
- [`Purchases.products.quantity`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/get>) from the Google Play Developer API

After you've added logic to handle multi-quantity purchases, you then need to enable the multi-quantity feature for the corresponding product on the one-time product management page in the Google Play Developer Console.

> **Note:** Be sure your app honors multi-quantity purchases before enabling the feature in the console. You might need to force an update to a version of your app that provides support before you can enable the feature on a product.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/integrate).
