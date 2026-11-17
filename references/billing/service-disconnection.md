### [SERVICE_DISCONNECTED](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_DISCONNECTED>) (Error Code -1)

#### Problem

This fatal error indicates that the client app's connection to the Google Play Store service using the [`BillingClient`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient>) has been severed.

#### Possible resolution

##### Strongly Recommended: Enable Automatic Service Reconnection

The Play Billing Library version 8.0.0 introduced the `enableAutoServiceReconnection()` feature. **It is highly recommended that you enable this feature** when building your `BillingClient`. This allows the library to automatically attempt to re-establish the connection when a billing API call is made while the service is disconnected, significantly reducing the occurrences of this error.

**Kotlin**

```kotlin
val billingClient = BillingClient.newBuilder(context)
    .setListener(listener)
    .enablePendingPurchases(
        PendingPurchasesParams.newBuilder().enableOneTimeProducts().build()
    )
    .enableAutoServiceReconnection() // Enable automatic service reconnection
    .build()
```

**Java**

```java
BillingClient billingClient = BillingClient.newBuilder(context)
    .setListener(listener)
    .enablePendingPurchases()
    .enableAutoServiceReconnection() // Enable automatic service reconnection
    .build();
```

##### If you have enabled automatic service reconnection

The Play Billing Library will automatically attempt to reconnect. If you still receive a `SERVICE_DISCONNECTED` response code when making an API call, it indicates that the library was unable to reconnect after its automatic attempts. In this scenario, you should implement retry logic in your app:

- **For user-initiated actions (in-session):** Use simple retries of the API call. The underlying issue might be temporary.
- **For background requests:** Implement retries with exponential backoff to avoid overwhelming the system if the disconnection is prolonged.

##### If you have NOT enabled automatic service reconnection

To avoid this error as much as possible, always check the connection to Google Play services before making calls with the Play Billing Library by calling [`BillingClient.isReady`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#isReady()>).

To attempt recovery from [`SERVICE_DISCONNECTED`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_DISCONNECTED>), your client app should try to re-establish the connection using [`BillingClient.startConnection`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#startConnection(com.android.billingclient.api.BillingClientStateListener)>).

Just like with [`SERVICE_TIMEOUT`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#SERVICE_TIMEOUT>), use simple retries or exponential backoff, depending on which action triggered the error.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/errors).
