The [client connection](client-connection.md) supplies the `BillingClient` and listener. [Product queries](product-query.md) supply the product details used by the purchase flow.

### Notify Google the purchase was processed

After your app has granted entitlement to the user and notified them about the successful transaction, your app needs to notify Google that the purchase was successfully processed. This is done by acknowledging the purchase and must be done **within three days so that the purchase isn't automatically refunded and entitlement revoked**. The process for acknowledging different types of purchases is described in the following sections.

#### Consumable products

For consumables, if your app has a secure backend, we recommend that you use [`Purchases.products:consume`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/consume>) to reliably consume purchases. Make sure the purchase wasn't already consumed by checking the `consumptionState` from the result of calling [`Purchases.products:get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/get>). If your app is client-only without a backend, use [`consumeAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#consumeasync>) from the Google Play Billing Library. Both methods fulfill the acknowledgement requirement and indicate that your app has granted entitlement to the user. These methods also enable your app to make the one-time product corresponding to the input purchase token available for repurchase. With `consumeAsync()` you must also pass an object that implements the [`ConsumeResponseListener`](<https://developer.android.com/reference/com/android/billingclient/api/ConsumeResponseListener>) interface. This object handles the result of the consumption operation. You can override the [`onConsumeResponse()`](<https://developer.android.com/reference/com/android/billingclient/api/ConsumeResponseListener#onConsumeResponse(com.android.billingclient.api.BillingResult,java.lang.String)>) method, which the Google Play Billing Library calls when the operation is complete.

The following example illustrates consuming a product with the Google Play Billing Library using the associated purchase token:

**Kotlin**

```kotlin
val consumeParams =
    ConsumeParams.newBuilder()
        .setPurchaseToken(purchase.getPurchaseToken())
        .build()
val consumeResult = withContext(Dispatchers.IO) {
    client.consumePurchase(consumeParams)
}
```

**Java**

```java
ConsumeParams consumeParams =
        ConsumeParams.newBuilder().setPurchaseToken(purchase.getPurchaseToken()).build();

ConsumeResponseListener listener =
        (billingResult, purchaseToken) -> {
            if (billingResult.getResponseCode() == BillingResponseCode.OK) {
                // Handle the success of the consume operation.
            }
        };

billingClient.consumeAsync(consumeParams, listener);
```

> **Note:** As consumption requests can occasionally fail, you must check your secure backend server to verify that each purchase token hasn't been used so your app doesn't grant entitlement multiple times for the same purchase. Alternatively, your app can wait until you receive a successful consumption response from Google Play before granting entitlement. If you choose to withhold purchases from the user until Google Play sends a successful consumption response, you must be very careful not to lose track of the purchases for which you have sent a consumption request.

#### Non-consumable products

To acknowledge non-consumable purchases, if your app has a secure backend, we recommend using [`Purchases.products:acknowledge`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/acknowledge>) to reliably acknowledge purchases. Make sure the purchase hasn't been previously acknowledged by checking the [`acknowledgementState`](<https://developers.google.com/android-publisher/api-ref/purchases/products>) from the result of calling [`Purchases.products:get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.products/get>).

If your app is client-only, use [`BillingClient.acknowledgePurchase()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#acknowledgepurchase>) from the Google Play Billing Library in your app. Before acknowledging a purchase, your app should check whether it was already acknowledged by using the [`isAcknowledged()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#isacknowledged>) method in the Google Play Billing Library.

The following example shows how to acknowledge a purchase using the Google Play Billing Library:

**Kotlin**

```kotlin
val client: BillingClient = billingClient
val acknowledgePurchaseParams = AcknowledgePurchaseParams.newBuilder()
    .setPurchaseToken(purchase.purchaseToken)
val ackPurchaseResult = withContext(Dispatchers.IO) {
    client.acknowledgePurchase(acknowledgePurchaseParams.build())
}
```

**Java**

```java
if (purchase.getPurchaseState() == Purchase.PurchaseState.PURCHASED) {
    if (!purchase.isAcknowledged()) {
        AcknowledgePurchaseParams acknowledgePurchaseParams =
                AcknowledgePurchaseParams.newBuilder()
                        .setPurchaseToken(purchase.getPurchaseToken())
                        .build();
        billingClient.acknowledgePurchase(acknowledgePurchaseParams, (billingResult) -> {
            // Acknowledgment handled.
        });
    }
}
```

#### Subscriptions

Subscriptions are handled similarly to non-consumables. If possible, use [`Purchases.subscriptions.acknowledge`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/acknowledge>) from the Google Play Developer API to reliably acknowledge the purchase from your secure backend. Verify that the purchase hasn't been previously acknowledged by checking the `acknowledgementState` in the purchase resource from [`Purchases.subscriptions:get`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>). Otherwise, you can acknowledge a subscription using [`BillingClient.acknowledgePurchase()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#acknowledgePurchase>) from the Google Play Billing Library after checking [`isAcknowledged()`](<https://developer.android.com/reference/com/android/billingclient/api/Purchase#isAcknowledged()>). All initial subscription purchases need to be acknowledged. Subscription renewals don't need to be acknowledged. For more information about when subscriptions need to be acknowledged, see the [Sell subscriptions](<https://developer.android.com/google/play/billing/subs>) topic.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/integrate).
