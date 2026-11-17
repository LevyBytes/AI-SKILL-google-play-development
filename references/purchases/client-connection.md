### Initialize a BillingClient

Once you've added a dependency on the Google Play Billing Library, you need to initialize a [`BillingClient`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient>) instance. `BillingClient` is the main interface for communication between the Google Play Billing Library and the rest of your app. `BillingClient` provides convenience methods, both synchronous and asynchronous, for many common billing operations. Make note of the following:

- It's recommended that you have one active [`BillingClient`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient>) connection open at one time to avoid multiple [`PurchasesUpdatedListener`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener>) callbacks for a single event.
- It's recommended to initiate a connection for the BillingClient when your app is launched or comes to the foreground to ensure your app processes purchases in a timely manner. This can be accomplished by using [`ActivityLifecycleCallbacks`](<https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks>) registered by [`registerActivityLifecycleCallbacks`](<https://developer.android.com/reference/android/app/Application#registerActivityLifecycleCallbacks(android.app.Application.ActivityLifecycleCallbacks)>) and listening for onActivityResumed to initialize a connection when you first detect an activity being resumed. Refer to the section on [processing purchases](<https://developer.android.com/google/play/billing/integrate?hl=en#process>) for more details on why this best practice should be followed. Also remember to end the connection when your app is closed.

To create a `BillingClient`, use [`newBuilder`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#newBuilder(android.content.Context)>). You can pass any context to `newBuilder()`, and `BillingClient` uses it to get an application context. That means you don't need to worry about memory leaks. To receive updates on purchases, you must also call [`setListener`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder#setListener(com.android.billingclient.api.PurchasesUpdatedListener)>), passing a reference to a [`PurchasesUpdatedListener`](<https://developer.android.com/reference/com/android/billingclient/api/PurchasesUpdatedListener>). This listener receives updates for all purchases in your app.

**Kotlin**

```kotlin
private val purchasesUpdatedListener =
    PurchasesUpdatedListener { billingResult, purchases ->
        // To be implemented in a later section.
    }

private var billingClient = BillingClient.newBuilder(context)
    .setListener(purchasesUpdatedListener)
    // Configure other settings.
    .build()
```

**Java**

```java
private PurchasesUpdatedListener purchasesUpdatedListener = new PurchasesUpdatedListener() {
  @Override
  public void onPurchasesUpdated(BillingResult billingResult, List<Purchase> purchases) {
      // To be implemented in a later section.
  }
};

private BillingClient billingClient = BillingClient.newBuilder(context)
  .setListener(purchasesUpdatedListener)
  // Configure other settings.
  .build();
```

> **Note:** The Google Play Billing Library returns errors in the form of [`BillingResult`](<https://developer.android.com/reference/com/android/billingclient/api/BillingResult>). A `BillingResult` contains a [`BillingResponseCode`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode>), which categorizes possible billing-related errors that your app can encounter. For example, if you receive a [`SERVICE_DISCONNECTED`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.BillingResponseCode#service_disconnected>) error code, your app should reinitialize the connection with Google Play. Additionally, a `BillingResult` contains a [debug message](<https://developer.android.com/reference/com/android/billingclient/api/BillingResult#getDebugMessage()>), which is useful during development to diagnose errors.

### Connect to Google Play

After you have created a `BillingClient`, you need to establish a connection to Google Play.

To connect to Google Play, call [`startConnection`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#startConnection(com.android.billingclient.api.BillingClientStateListener)>). The connection process is asynchronous, and you must implement a [`BillingClientStateListener`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClientStateListener>) to receive a callback once the setup of the client is complete and it's ready to make further requests.

If you haven't enabled [automatic service reconnection](<https://developer.android.com/google/play/billing/integrate?hl=en#automatic-service-reconnection>), you must also implement retry logic to handle lost connections to Google Play. To implement retry logic, override the [`onBillingServiceDisconnected()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClientStateListener#onBillingServiceDisconnected()>) callback method, and make sure that the `BillingClient` calls the [`startConnection()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#startConnection(com.android.billingclient.api.BillingClientStateListener)>) method to reconnect to Google Play before making further requests. If you have enabled [automatic service reconnection](<https://developer.android.com/google/play/billing/integrate?hl=en#automatic-service-reconnection>), you can implement this method as a no-op.

The following example demonstrates how to start a connection and test that it's ready to use:

**Kotlin**

```kotlin
billingClient.startConnection(object : BillingClientStateListener {
    override fun onBillingSetupFinished(billingResult: BillingResult) {
        if (billingResult.responseCode == BillingResponseCode.OK) {
            // The BillingClient is ready. You can query purchases here.
        }
    }
    override fun onBillingServiceDisconnected() {
        // If automatic service reconnection is enabled, this can be left empty (no-op)
        // because the library handles retries. You can still use this for non-retry
        // tasks like logging or updating the UI to reflect a disconnected state.
        // Otherwise, try to restart the connection on the next request to
        // Google Play by calling the startConnection() method.
    }
})
```

**Java**

```java
billingClient.startConnection(
        new BillingClientStateListener() {
            @Override
            public void onBillingSetupFinished(BillingResult billingResult) {
                if (billingResult.getResponseCode() == BillingResponseCode.OK) {
                    // The BillingClient is ready. You can query purchases here.
                    // It's a good practice to query products after the connection is established.
                    queryProductDetails();
                }
            }

            @Override
            public void onBillingServiceDisconnected() {
                // Try to restart the connection on the next request to
                // Google Play by calling the startConnection() method.
                // This is automatically handled by the library when you call a method that requires a connection.
            }
        });
```

> **Note:** Google Play strongly recommends that you use the [automatic service reconnection feature](client-reconnection.md). When this feature is enabled, the library handles service reconnections automatically when you make an API call. If you enable automatic service reconnection, you should **not** manually call `startConnection()` in `onBillingServiceDisconnected()`. You can implement the method as a **no-op** (leave it empty), or use it for state awareness tasks such as logging the disconnection or updating your app's UI. If you choose not to use the automatic service reconnection feature, it's strongly recommended that you implement your own connection retry logic and override the [`onBillingServiceDisconnected()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClientStateListener#onBillingServiceDisconnected()>) method. In either case, make sure you maintain the `BillingClient` connection when executing any methods.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/integrate).
