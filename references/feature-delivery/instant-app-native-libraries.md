The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

#### Load C/C++ libraries

If you want to load C/C++ libraries from a module that the device has already downloaded in an Instant App, use [`SplitInstallHelper.loadLibrary(Context context, String libName)`](<https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallHelper#loadLibrary(android.content.Context,%20java.lang.String)>), as shown below:

**Kotlin**

```kotlin
override fun onStateUpdate(state: SplitInstallSessionState) {
    if (state.sessionId() == mySessionId) {
        when (state.status()) {
            SplitInstallSessionStatus.INSTALLED -> {
                // Updates the app’s context as soon as a module is installed.
                val newContext = context.createPackageContext(context.packageName, 0)
                // To load C/C++ libraries from an installed module, use the following API
                // instead of System.load().
                SplitInstallHelper.loadLibrary(newContext, “my-cpp-lib”)
                ...
            }
        }
    }
}
```

**Java**

```java
public void onStateUpdate(SplitInstallSessionState state) {
    if (state.sessionId() == mySessionId) {
        switch (state.status()) {
            case SplitInstallSessionStatus.INSTALLED:
                // Updates the app’s context as soon as a module is installed.
                Context newContext = context.createPackageContext(context.getPackageName(), 0);
                // To load C/C++ libraries from an installed module, use the following API
                // instead of System.load().
                SplitInstallHelper.loadLibrary(newContext, “my-cpp-lib”);
                ...
        }
    }
}
```

### Known limitations

- It isn't possible to use Android WebView in an activity that accesses resources or assets from an optional module. This is due to an incompatibility between WebView and SplitCompat on Android API level 28 and lower.
- You can't cache Android `ApplicationInfo` objects, their contents, or objects that contain them within your app. You should always fetch these objects as needed from an app context. Caching such objects could cause the app to crash when installing a feature module.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
