#### New proration mode

When upgrading or downgrading a user's subscription, you can use a new proration mode, `DEFERRED`. This mode updates the user's subscription when it next renews. To learn more about how to set this proration mode, see [Set proration mode](<https://developer.android.com/google/play/billing/subscriptions#replacement-modes>).

#### New method for setting SKU details

In the `BillingFlowParams` class, the `setSku()` method has been deprecated. This change serves to optimize the Google Play Billing flow.

When constructing a new instance of `BillingFlowParams` in your in-app billing client, we recommend that you instead work with the JSON object directly using `setSkuDetails()`, as shown in the following code snippet:

In the `BillingFlowParams` Builder class, the `setSku()` method has been deprecated. Instead, use the `setSkuDetails()` method, as shown in the following code snippet. The object passed into `setSkuDetails()` object comes from the [`querySkuDetailsAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#querySkuDetailsAsync(com.android.billingclient.api.SkuDetailsParams,%20com.android.billingclient.api.SkuDetailsResponseListener)>) method.

**Kotlin**

```kotlin
private lateinit var mBillingClient: BillingClient
private val mSkuDetailsMap = HashMap<String, SkuDetails>()

private fun querySkuDetails() {
    val skuDetailsParamsBuilder = SkuDetailsParams.newBuilder()
    mBillingClient.querySkuDetailsAsync(skuDetailsParamsBuilder.build()
    ) { responseCode, skuDetailsList ->
        if (responseCode == 0) {
            for (skuDetails in skuDetailsList) {
                mSkuDetailsMap[skuDetails.sku] = skuDetails
            }
        }
    }
}

private fun startPurchase(skuId: String) {
    val billingFlowParams = BillingFlowParams.newBuilder()
    .setSkuDetails(mSkuDetailsMap[skuId])
    .build()
}
```

**Java**

```java
private BillingClient mBillingClient;
private Map<String, SkuDetails> mSkuDetailsMap = new HashMap<>();

private void querySkuDetails() {
    SkuDetailsParams.Builder skuDetailsParamsBuilder
            = SkuDetailsParams.newBuilder();
    mBillingClient.querySkuDetailsAsync(skuDetailsParamsBuilder.build(),
            new SkuDetailsResponseListener() {
                @Override
                public void onSkuDetailsResponse(int responseCode,
                        List<SkuDetails> skuDetailsList) {
                    if (responseCode == 0) {
                        for (SkuDetails skuDetails : skuDetailsList) {
                            mSkuDetailsMap.put(skuDetails.getSku(), skuDetails);
                        }
                    }
                }
            });
}

private void startPurchase(String skuId) {
    BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
            .setSkuDetails(mSkuDetailsMap.get(skuId))
            .build();
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/release-notes).
