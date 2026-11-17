## Process purchases

Processing multi-product OTP purchases is the same as for existing single-item purchases as described in [Integrate the Google Play Billing Library into your app](<https://developer.android.com/google/play/billing/integrate#launch>). The only difference is that you need to grant entitlement for all products instead of only one for multi-product OTP purchases so that the user can receive multiple entitlements with a single purchase. A multi-product OTP purchase returns multiple items which can be retrieved by using [`Purchase.getProducts()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#getProducts()>) in the Google Play Billing Library, and then the `lineItems` list in [`purchases.products.get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) of the [Google Play Developer API](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>).

## Real-time developer notifications

The `sku` field isn't provided in [RTDN](<https://developer.android.com/google/play/billing/rtdn-reference>) for multi-product OTP purchases. The multi-product OTP purchases represent more than one product. Therefore, you can use the Play Developer APIs to get the purchase data, and see all the items in it.

## Refunds

In a multi-product OTP purchase, users can't request refunds for individual items, and you too can't issue refunds for individual items. However, request and issue of refunds for the entire multi-product OTP purchase is permitted. If you are cancelling a multi-product OTP purchase for a user, all the entitlements associated with the purchase are cancelled.

> **Note:** Refunded multi-product OTP orders will be available in the [Voided Purchases API](<https://developers.google.com/android-publisher/voided-purchases>) and RTDN.

## Financial reporting and reconciliation

Use the [Earnings report](<https://support.google.com/googleplay/android-developer/answer/6135870>) to reconcile your active multi-product OTP purchases with Google Payoffs and transactions on Play. Each transaction line item has an Order ID. For a multi-product OTP purchase, the [Earnings and Estimated sales reports](<https://support.google.com/googleplay/android-developer/answer/2482017>) will include separate rows (with the same Order ID) for each transaction such as charge, fee, tax, and refund, for each item involved.

For dashboards in the Play Console:

- The revenue statistics presented in the **Financial reporting** section of the console are broken down by individual products.
- Order management reflects multi-product OTP purchases, and show itemized lists of what was purchased. From order management, you may revoke, cancel or fully refund a user's purchase.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/multi-product-for-one-time-product).
