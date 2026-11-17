### Re-enable or disable types of configuration APKs

By default, when you build an app bundle, it supports generating configuration APKs for each set of language resources, screen density resources, and ABI libraries. Using the `android.bundle` block in your base module's `build.gradle` file, as shown below, you can disable support for one or more types of configuration APKs:

**Groovy**

```groovy
android {
    // When building Android App Bundles, the splits block is ignored.
    // You can remove it, unless you're going to continue to build multiple
    // APKs in parallel with the app bundle
    splits {...}

    // Instead, use the bundle block to control which types of configuration APKs
    // you want your app bundle to support.
    bundle {
        language {
            // This property is set to true by default.
            // You can specify `false` to turn off
            // generating configuration APKs for language resources.
            // These resources are instead packaged with each base and
            // feature APK.
            // Continue reading below to learn about situations when an app
            // might change setting to `false`, otherwise consider leaving
            // the default on for more optimized downloads.
            enableSplit = false
        }
        density {
            // This property is set to true by default.
            enableSplit = true
        }
        abi {
            // This property is set to true by default.
            enableSplit = true
        }
    }
}
```

**Kotlin**

```kotlin
android {
    // When building Android App Bundles, the splits block is ignored.
    // You can remove it, unless you're going to continue to build multiple
    // APKs in parallel with the app bundle
    splits {...}

    // Instead, use the bundle block to control which types of configuration APKs
    // you want your app bundle to support.
    bundle {
        language {
            // This property is set to true by default.
            // You can specify `false` to turn off
            // generating configuration APKs for language resources.
            // These resources are instead packaged with each base and
            // feature APK.
            // Continue reading below to learn about situations when an app
            // might change setting to `false`, otherwise consider leaving
            // the default on for more optimized downloads.
            enableSplit = false
        }
        density {
            // This property is set to true by default.
            enableSplit = true
        }
        abi {
            // This property is set to true by default.
            enableSplit = true
        }
    }
}
```

### Handling language changes

Google Play determines which language resources to install with the app based on the language selection in the user's device settings. Consider a user who changes their default system language after already downloading your app. If your app supports that language, the device requests and downloads additional configuration APKs for those language resources from Google Play.

For apps that offer a language picker inside the application and dynamically change the app's language, independent of the system level language setting, you must make some changes to prevent crashes due to missing resources. Either set the `android.bundle.language.enableSplit` property to `false`, or consider implementing on-demand language downloads using the Play Core library as described in [Download additional language resources](<https://developer.android.com/guide/playcore/feature-delivery/on-demand#lang_resources>).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/app-bundle/configure-base).
