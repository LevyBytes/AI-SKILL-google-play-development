The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

## Monitor the request state

To be able to update a progress bar, fire an intent after installation, or gracefully handle a request error, you need to listen for state updates from the asynchronous `SplitInstallManager.startInstall()` task. Before you can start receiving updates for your install request, register a listener and get the session ID for the request, as shown below.

**Kotlin**

```kotlin
// Initializes a variable to later track the session ID for a given request.
var mySessionId = 0

// Creates a listener for request status updates.
val listener = SplitInstallStateUpdatedListener { state ->
    if (state.sessionId() == mySessionId) {
      // Read the status of the request to handle the state update.
    }
}

// Registers the listener.
splitInstallManager.registerListener(listener)

...

splitInstallManager
    .startInstall(request)
    // When the platform accepts your request to download
    // an on demand module, it binds it to the following session ID.
    // You use this ID to track further status updates for the request.
    .addOnSuccessListener { sessionId -> mySessionId = sessionId }
    // You should also add the following listener to handle any errors
    // processing the request.
    .addOnFailureListener { exception ->
        // Handle request errors.
    }

// When your app no longer requires further updates, unregister the listener.
splitInstallManager.unregisterListener(listener)
```

**Java**

```java
// Initializes a variable to later track the session ID for a given request.
int mySessionId = 0;

// Creates a listener for request status updates.
SplitInstallStateUpdatedListener listener = state -> {
    if (state.sessionId() == mySessionId) {
      // Read the status of the request to handle the state update.
    }
};

// Registers the listener.
splitInstallManager.registerListener(listener);

...

splitInstallManager
    .startInstall(request)
    // When the platform accepts your request to download
    // an on demand module, it binds it to the following session ID.
    // You use this ID to track further status updates for the request.
    .addOnSuccessListener(sessionId -> { mySessionId = sessionId; })
    // You should also add the following listener to handle any errors
    // processing the request.
    .addOnFailureListener(exception -> {
        // Handle request errors.
    });

// When your app no longer requires further updates, unregister the listener.
splitInstallManager.unregisterListener(listener);
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
