The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

### Access installed Android Instant Apps

After an Android Instant App module reports as `INSTALLED`, you can access its code and resources using a refreshed app [Context](<https://developer.android.com/reference/android/content/Context>). A context that your app creates *before* installing a module (for example, one that's already stored in a variable) does not contain the content of the new module. But a fresh context does; this can be obtained, for example, using [`createPackageContext`](<https://developer.android.com/reference/android/content/Context#createPackageContext(java.lang.String,%20int)>).

**Kotlin**

```kotlin
// Generate a new context as soon as a request for a new module
// reports as INSTALLED.
override fun onStateUpdate(state: SplitInstallSessionState ) {
    if (state.sessionId() == mySessionId) {
        when (state.status()) {
            ...
            SplitInstallSessionStatus.INSTALLED -> {
                val newContext = context.createPackageContext(context.packageName, 0)
                // If you use AssetManager to access your app’s raw asset files, you’ll need
                // to generate a new AssetManager instance from the updated context.
                val am = newContext.assets
            }
        }
    }
}
```

**Java**

```java
// Generate a new context as soon as a request for a new module
// reports as INSTALLED.
@Override
public void onStateUpdate(SplitInstallSessionState state) {
    if (state.sessionId() == mySessionId) {
        switch (state.status()) {
            ...
            case SplitInstallSessionStatus.INSTALLED:
                Context newContext = context.createPackageContext(context.getPackageName(), 0);
                // If you use AssetManager to access your app’s raw asset files, you’ll need
                // to generate a new AssetManager instance from the updated context.
                AssetManager am = newContext.getAssets();
        }
    }
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
