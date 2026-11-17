## Specify API level (SDK version) requirements

If your app requires a specific minimum version of the Android platform, you can specify that version requirement as API level settings in the app's `build.gradle` or `build.gradle.kts` file. During the build process, these settings are merged into your app's manifest file. Specifying API level requirements ensures that your app can only be installed on devices that are running a compatible version of the Android platform.

**Note:** If you specify API level requirements directly in your app's manifest file, the corresponding settings in the build files will override the settings in the manifest file. Additionally, defining these settings in the Gradle build files lets you specify different values for different versions of your app. For greater flexibility and to avoid potential overwriting when the manifest is merged, remove these attributes from the `<uses-sdk>` element and define your API level settings in the Gradle build files instead.

There are two API level settings available:

- `minSdk`: The minimum version of the Android platform on which the app will run, specified by the platform's API level identifier.
- `targetSdk`: The API level on which the app is designed to run. Possible numeric values are defined in [`Build.VERSION_CODES`](<https://developer.android.com/reference/android/os/Build.VERSION_CODES>). The running device's API level is reported by [`Build.VERSION.SDK_INT`](<https://developer.android.com/reference/android/os/Build.VERSION#SDK_INT>). In some cases, this allows the app to use manifest elements or behaviors defined in the target API level, rather than being restricted to using only those defined for the minimum API level.
It is not possible to specify that an app either targets or requires a minor SDK version. To call new APIs safely that require a higher major or minor SDK version than your `minSdkVersion`, you can guard a code block with a check for a minor or major release using the `SDK_INT_FULL` constant.
```kotlin
if (SDK_INT_FULL >= VERSION_CODES_FULL.[MAJOR or MINOR RELEASE]) {
  // Use APIs introduced in a major or minor SDK version
}
```

To specify default API level requirements in a `build.gradle` or `build.gradle.kts` file, add one or more of the API level settings to the `defaultConfig{}` block, nested inside the `android {}` block. You can also override these default values for different versions of your app by adding the settings to build types or product flavors.

The following file specifies default `minSdk` and `targetSdk` settings in the `defaultConfig {}` block and overrides `minSdk` for one product flavor:

**Groovy**

```groovy
android {
    ...
    defaultConfig {
        ...
        minSdk 21
        targetSdk 33
    }
    productFlavors {
        main {
            ...
        }
        afterNougat {
            ...
            minSdk 24
        }
    }
}
```

**Kotlin**

```kotlin
android {
    ...
    defaultConfig {
        ...
        minSdk = 21
        targetSdk = 33
    }
    productFlavors {
        create("main") {
            ...
        }
        create("afterNougat") {
            ...
            minSdk = 24
        }
    }
}
```

When preparing to install your app, the system checks the value of these settings and compares them to the system version. If the `minSdk` value is greater than the system version, the system prevents the installation of the app.

If you don't specify these settings, the system assumes that your app is compatible with all platform versions. This is equivalent to setting `minSdk` to `1`.

For more information, see [What is API Level?](<https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels>). For Gradle build settings, see [Configure build variants](<https://developer.android.com/studio/build/build-variants>).

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/versioning).
