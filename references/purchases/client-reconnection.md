### Automatically Re-establish a Connection

With the introduction of the `enableAutoServiceReconnection()` method in [`BillingClient.Builder`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder>) in version 8.0.0, the Play Billing Library can now automatically re-establish the service connection if an API call is made while the service is disconnected. This can lead to a reduction in [`SERVICE_DISCONNECTED`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_DISCONNECTED>) responses since the reconnection is handled internally before the API call is made.

#### How to enable automatic reconnection

When building a [`BillingClient`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient>) instance, use the `enableAutoServiceReconnection()` method in the [`BillingClient.Builder`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder>) to enable automatic reconnection.

**Kotlin**

```kotlin
val billingClient = BillingClient.newBuilder(context)
    .setListener(listener)
    .enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())
    .enableAutoServiceReconnection() // Add this line to enable reconnection
    .build()
```

**Java**

```java
BillingClient billingClient = BillingClient.newBuilder(context)
    .setListener(listener)
    .enablePendingPurchases()
    .enableAutoServiceReconnection() // Add this line to enable reconnection
    .build();
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/integrate).
