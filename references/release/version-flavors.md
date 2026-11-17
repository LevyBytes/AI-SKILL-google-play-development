### Define version values

You can define default values for these settings by including them in the `defaultConfig {}` block, nested inside the `android {}` block of your module's `build.gradle` or `build.gradle.kts` file. You can then override these default values for different versions of your app by defining separate values for individual build types or product flavors. The following file shows the `versionCode` and `versionName` settings in the `defaultConfig {}` block, as well as the `productFlavors {}` block.

These values are then merged into your app's manifest file during the build process.

**Groovy**

```groovy
    android {
        ...
        defaultConfig {
            ...
            versionCode 2
            versionName "1.1"
        }
        productFlavors {
            demo {
                ...
                versionName "1.1-demo"
            }
            full {
                ...
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
            versionCode = 2
            versionName = "1.1"
        }
        productFlavors {
            create("demo") {
                ...
                versionName = "1.1-demo"
            }
            create("full") {
                ...
            }
        }
    }
    
```

In the `defaultConfig {}` block of this example, the `versionCode` value indicates that the current APK contains the second release of the app, and the `versionName` string specifies that it will appear to users as version 1.1. This file also defines two product flavors, "demo" and "full." Since the "demo" product flavor defines `versionName` as "1.1-demo", the "demo" build uses this `versionName` instead of the default value. The "full" product flavor block doesn't define `versionName`, so it uses the default value of "1.1".

**Note:** If your app defines the app version directly in the `<manifest>` element, the version values in the Gradle build file override the settings in the manifest. Additionally, defining these settings in the Gradle build files lets you specify different values for different versions of your app. For greater flexibility and to avoid potential overwriting when the manifest is merged, remove these attributes from the `<manifest>` element and define your version settings in the Gradle build files instead.

The Android framework provides an API to let you query the system for version information about your app. To obtain version information, use the ` PackageManager.getPackageInfo(java.lang.String, int)` method.

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/versioning).
