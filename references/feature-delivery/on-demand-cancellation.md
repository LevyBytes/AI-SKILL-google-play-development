The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

### Cancel an install request

If your app needs to cancel a request before it is installed, it can invoke the `cancelInstall()` method using the request’s session ID, as shown below.

**Kotlin**

```kotlin
splitInstallManager
    // Cancels the request for the given session ID.
    .cancelInstall(mySessionId)
```

**Java**

```java
splitInstallManager
    // Cancels the request for the given session ID.
    .cancelInstall(mySessionId);
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
