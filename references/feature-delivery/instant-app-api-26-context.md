The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

#### Android Instant Apps on Android 8.0 and higher

When requesting an on demand module for an Android Instant App on Android 8.0 (API level 26) and higher, after an install request reports as `INSTALLED`, you need to update the app with the context of the new module through a call to [`SplitInstallHelper.updateAppInfo(Context context)`](<https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallHelper#updateAppInfo(android.content.Context)>). Otherwise, the app is not yet aware of the module’s code and resources. After updating the app’s metadata, you should load the module’s contents during the next main thread event by invoking a new [`Handler`](<https://developer.android.com/reference/android/os/Handler>), as shown below:

**Kotlin**

```kotlin
override fun onStateUpdate(state: SplitInstallSessionState ) {
    if (state.sessionId() == mySessionId) {
        when (state.status()) {
            ...
            SplitInstallSessionStatus.INSTALLED -> {
                // You need to perform the following only for Android Instant Apps
                // running on Android 8.0 (API level 26) and higher.
                if (BuildCompat.isAtLeastO()) {
                    // Updates the app’s context with the code and resources of the
                    // installed module.
                    SplitInstallHelper.updateAppInfo(context)
                    Handler().post {
                        // Loads contents from the module using AssetManager
                        val am = context.assets
                        ...
                    }
                }
            }
        }
    }
}
```

**Java**

```java
@Override
public void onStateUpdate(SplitInstallSessionState state) {
    if (state.sessionId() == mySessionId) {
        switch (state.status()) {
            ...
            case SplitInstallSessionStatus.INSTALLED:
            // You need to perform the following only for Android Instant Apps
            // running on Android 8.0 (API level 26) and higher.
            if (BuildCompat.isAtLeastO()) {
                // Updates the app’s context with the code and resources of the
                // installed module.
                SplitInstallHelper.updateAppInfo(context);
                new Handler().post(new Runnable() {
                    @Override public void run() {
                        // Loads contents from the module using AssetManager
                        AssetManager am = context.getAssets();
                        ...
                    }
                });
            }
        }
    }
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
