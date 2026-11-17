The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

## Locally test module installs

The Play Feature Delivery Library allows you to locally test your app’s ability to do the following, without connecting to the Play Store:

- Request and monitor module installs.
- Handle install errors.
- Use [`SplitCompat`](<https://developer.android.com/reference/com/google/android/play/core/splitcompat/SplitCompat>) to [access modules](<https://developer.android.com/guide/playcore/dynamic-delivery#access_downloaded_modules>).

This page describes how to deploy your app's split APKs to your test device so that Play Feature Delivery automatically uses those APKs to simulate requesting, downloading, and installing modules from the Play Store.

Although you don't need to make any changes to your app's logic, you need to meet the following requirements:

- Download and install the [latest version of `bundletool`](<https://github.com/google/bundletool/releases>). You need `bundletool` to build a new set of installable APKs from your app's bundle.

> **Note:** Play Feature Delivery Library currently doesn’t support module uninstalls or deferred installs. To test this functionality, consider using [internal app sharing](<https://support.google.com/googleplay/android-developer/answer/9303479>).

### Build a set of APKs

If you haven't already done so, build your app’s split APKs, as follows:

1. Build an app bundle for your app using one of the following methods:

   - Use Android Studio and the Android plugin for Gradle to [build and sign an Android App Bundle](<https://developer.android.com/studio/publish/app-signing#sign-apk>).
   - [Build your app bundle from the command line](<https://developer.android.com/studio/build/building-cmdline#build_bundle>).
2. Use `bundletool` to [generate a set of APKs](<https://developer.android.com/studio/command-line/bundletool#generate_apks>) for all device configurations with the following command:

   ```text

   bundletool build-apks --local-testing
     --bundle my_app.aab
     --output my_app.apks
   ```

The `--local-testing` flag includes meta-data in your APKs' manifests that lets the Play Feature Delivery Library know to use the local split APKs to test installing feature modules, without connecting to the Play Store.

### Deploy your app to the device

After you [build a set of APKs](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#build-apks>) using the `--local-testing` flag, use `bundletool` to install the base version of your app and transfer additional APKs to your device's local storage. You can perform both actions with the following command:

```text

bundletool install-apks --apks my_app.apks
```

Now, when you start your app and complete the user flow to download and install a feature module, the Play Feature Delivery Library uses the APKs that `bundletool` transferred to the device's local storage.

### Simulate a network error

To simulate module installs from the Play Store, the Play Feature Delivery Library uses an alternative to the `SplitInstallManager`, called [`FakeSplitInstallManager`](<https://developer.android.com/reference/com/google/android/play/core/splitinstall/testing/FakeSplitInstallManager>), to request the module. When you use `bundletool` with the `--local-testing` flag to [build a set of APKs](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#build-apks>) and deploy them to your test device, it includes metadata that instructs the Play Feature Delivery Library to automatically switch your app's API calls to invoke `FakeSplitInstallManager`, instead of `SplitInstallManager`.

`FakeSplitInstallManager` includes a boolean flag that you can enable to simulate a network error the next time your app requests to install a module. To access `FakeSplitInstallManager` in your tests, you can get an instance of it using the [`FakeSplitInstallManagerFactory`](<https://developer.android.com/reference/com/google/android/play/core/splitinstall/testing/FakeSplitInstallManagerFactory>), as shown below:

**Kotlin**

```kotlin
// Creates an instance of FakeSplitInstallManager with the app's context.
val fakeSplitInstallManager = FakeSplitInstallManagerFactory.create(context)
// Tells Play Feature Delivery Library to force the next module request to
// result in a network error.
fakeSplitInstallManager.setShouldNetworkError(true)
```

**Java**

```java
// Creates an instance of FakeSplitInstallManager with the app's context.
FakeSplitInstallManager fakeSplitInstallManager =
    FakeSplitInstallManagerFactory.create(context);
// Tells Play Feature Delivery Library to force the next module request to
// result in a network error.
fakeSplitInstallManager.setShouldNetworkError(true);
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
