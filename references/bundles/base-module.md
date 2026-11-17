An app bundle is different from an APK in that you can't deploy one to a device. Rather, it's a publishing format that includes all your app's compiled code and resources in a single build artifact. So, after you upload your signed app bundle, Google Play has everything it needs to build and sign your app's APKs, and serve them to users.

## Get started

Most app projects won't require much effort to support Android App Bundles. That's because the module that includes code and resources for your app's base APK is the standard app module, which you get by default when you [create a new app project in Android Studio](<https://developer.android.com/studio/projects/create-project>). That is, the module that applies the `application` plugin, as shown in the following snippet, to its `build.gradle` file provides the code and resources for the base functionality of your app.

**Groovy**

```groovy
// The standard application plugin creates your app's base module.
plugins {
 id 'com.android.application'
}
```

**Kotlin**

```kotlin
plugins {
    // The standard application plugin creates your app's base module.
    id("com.android.application")
}
```

In addition to providing the core functionality for your app, the base module also provides many of the build configurations and manifest entries that affect your entire app project.

## The base module build configuration

For most existing app projects, you don't need to change anything in your base module's build configuration. However, if you are considering adding feature modules to your app project or if you previously released your app using multiple APKs, there are some aspects to the base module's build configuration that you should keep in mind.

### Version code and app updates

With Android App Bundles, you no longer have to manage version codes for multiple APKs that you upload to Google Play. Instead, you manage only one version code in the base module of your app, as shown below:

```groovy
// In your base module build.gradle file
android {
    defaultConfig {
        …
        // You specify your app's version code only in the base module.
        versionCode 5
        versionName "1.0"
    }
}
```

After you upload your app bundle, Google Play uses the version code in your base module to assign the same version code to all the APKs it generates from that bundle. That is, when a device downloads and installs your app, all split APKs for that app share the same version code.

When you want to update your app with new code or resources, you must update the version code in your app's base module, and build a new, full app bundle. When you upload that app bundle to Google Play, it generates a new set of APKs based on the version code the base module specifies. Subsequently, when users update your app, Google Play serves them updated versions of all APKs currently installed on the device. That is, all installed APKs are updated to the new version code.

### Other considerations

- **App signing**: If you include signing information in your build files, you should only include it in the base module's build configuration file. For more information, see [Configure Gradle to sign your app](<https://developer.android.com/studio/publish/app-signing#gradle-sign>).
- **Code shrinking**: If you want to [enable code shrinking](<https://developer.android.com/studio/build/shrink-code#shrink-code>) for your entire app project (including its feature modules), you must do so from the base module's `build.gradle` file. That is, you can include custom ProGuard rules in a feature module, but the `minifyEnabled` property in feature module build configurations is ignored.
- **The `splits` block is ignored**: When building an app bundle, Gradle ignores properties in the `android.splits` block. If you want to control which types of configuration APKs your app bundle supports, instead use `android.bundle` to [disable types of configuration APKs](<https://developer.android.com/guide/app-bundle/configure-base?hl=en#disable_config_apks>).
- **App versioning**: The base module determines the version code and version name for your entire app project. For more information, see [Version code and app updates](<https://developer.android.com/guide/app-bundle/configure-base?hl=en#version_and_updates>).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/app-bundle/configure-base).
