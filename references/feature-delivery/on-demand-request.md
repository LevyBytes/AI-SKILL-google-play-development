## Request an on demand module

When your app needs to use a feature module, it can request one while it's in the foreground through the [`SplitInstallManager`](<https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager>) class. When making a request, your app needs to specify the name of the module as defined by the `split` element in the target module’s manifest. When you [create a feature module](<https://developer.android.com/guide/app-bundle/play-feature-delivery>) using Android Studio, the build system uses the **Module name** you provide to inject this property into the module's manifest at compile time. For more information, read about the [feature module manifests](<https://developer.android.com/guide/playcore/feature-delivery#feature-module-manifest>).

For example, consider an app that has an on demand module to capture and send picture messages using the device’s camera, and this on demand module specifies `split="pictureMessages"` in its manifest. The following sample uses `SplitInstallManager` to request the `pictureMessages` module (along with an additional module for some promotional filters):

**Kotlin**

```kotlin
// Creates an instance of SplitInstallManager.
val splitInstallManager = SplitInstallManagerFactory.create(context)

// Creates a request to install a module.
val request =
    SplitInstallRequest
        .newBuilder()
        // You can download multiple on demand modules per
        // request by invoking the following method for each
        // module you want to install.
        .addModule("pictureMessages")
        .addModule("promotionalFilters")
        .build()

splitInstallManager
    // Submits the request to install the module through the
    // asynchronous startInstall() task. Your app needs to be
    // in the foreground to submit the request.
    .startInstall(request)
    // You should also be able to gracefully handle
    // request state changes and errors. To learn more, go to
    // the section about how to Monitor the request state.
    .addOnSuccessListener { sessionId -> ... }
    .addOnFailureListener { exception ->  ... }
```

**Java**

```java
// Creates an instance of SplitInstallManager.
SplitInstallManager splitInstallManager =
    SplitInstallManagerFactory.create(context);

// Creates a request to install a module.
SplitInstallRequest request =
    SplitInstallRequest
        .newBuilder()
        // You can download multiple on demand modules per
        // request by invoking the following method for each
        // module you want to install.
        .addModule("pictureMessages")
        .addModule("promotionalFilters")
        .build();

splitInstallManager
    // Submits the request to install the module through the
    // asynchronous startInstall() task. Your app needs to be
    // in the foreground to submit the request.
    .startInstall(request)
    // You should also be able to gracefully handle
    // request state changes and errors. To learn more, go to
    // the section about how to Monitor the request state.
    .addOnSuccessListener(sessionId -> { ... })
    .addOnFailureListener(exception -> { ... });
```

When your app requests an on demand module, the Play Feature Delivery Library employs a “fire-and-forget” strategy. That is, it sends the request to download the module to the platform, but it does not monitor whether the installation succeeded. To move the user journey forward after installation or gracefully handle errors, make sure you [monitor the request state](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#monitor_requests>).

**Note:** It's okay to request a feature module that’s already installed on the device. The API instantly considers the request as completed if it detects the module is already installed. Additionally, after a module is installed, Google Play keeps it updated automatically. That is, when you upload a new version of your app bundle, the platform updates all installed APKs that belong to your app. For more information, read [Manage app updates](<https://developer.android.com/guide/app-bundle/configure-base#manage_app_updates>).

To have access to the module's code and resources, your app needs to [enable SplitCompat](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#access_downloaded_modules>). Note that SplitCompat is not required for Android Instant Apps.

### Defer installation of on demand modules

If you do not need your app to immediately download and install an on demand module, you can defer installation for when the app is in the background. For example, if you want to preload some promotional material for a later launch of your app.

You can specify a module to be download later using the [`deferredInstall()`](<https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#deferredinstall>) method, as shown below. And, unlike [`SplitInstallManager.startInstall()`](<https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#startinstall>), your app does not need to be in the foreground to initiate a request for a deferred installation.

**Kotlin**

```kotlin
// Requests an on demand module to be downloaded when the app enters
// the background. You can specify more than one module at a time.
splitInstallManager.deferredInstall(listOf("promotionalFilters"))
```

**Java**

```java
// Requests an on demand module to be downloaded when the app enters
// the background. You can specify more than one module at a time.
splitInstallManager.deferredInstall(Arrays.asList("promotionalFilters"));
```

Requests for deferred installs are best-effort and you cannot track their progress. So, before trying to access a module you have specified for deferred installation, you should [check that the module has been installed](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#manage_installed_modules>). If you need the module to be available immediately, instead use `SplitInstallManager.startInstall()` to request it, as shown in the previous section.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
