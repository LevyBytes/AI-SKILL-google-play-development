Google Play's app serving model uses [Android App Bundles](<https://developer.android.com/guide/app-bundle>) to generate and serve optimized APKs for each user's device configuration, so users download only the code and resources they need to run your app.

Play Feature Delivery uses advanced capabilities of app bundles, allowing certain features of your app to be delivered conditionally or downloaded on demand. To do that, first you need to separate these features from your base app into feature modules.

## Feature module build configuration

When you create a new feature module using Android Studio, the IDE applies the following Gradle plugin to the module's `build.gradle` file.

```groovy
// The following applies the dynamic-feature plugin to your feature module.
// The plugin includes the Gradle tasks and properties required to configure and build
// an app bundle that includes your feature module.

plugins {
  id 'com.android.dynamic-feature'
}

```

Many of the properties available to [the standard application plugin](<https://developer.android.com/studio/build#module-level>) are also available to your feature module. The following sections describe the properties you should and shouldn't include in your feature module's build configuration.

### What not to include in the feature module build configuration

Because each feature module depends on the base module, it also inherits certain configurations. So, you should omit the following in the feature module's `build.gradle` file:

- **Signing configurations:** App bundles are signed using signing configurations that you specify in the base module.
- **The `minifyEnabled` property:** You can [enable code shrinking](<https://developer.android.com/studio/build/shrink-code#shrink-code>) for your entire app project from only the base module's build configuration. So, you should omit this property from feature modules. You can, however, [specify additional ProGuard rules](<https://developer.android.com/guide/playcore/feature-delivery?hl=en#dynamic_feature_proguard>) for each feature module.
- **`versionCode` and `versionName`**: When building your app bundle, Gradle uses app version information that the base module provides. You should omit these properties from your feature module's `build.gradle` file.

### Establish a relationship to the base module

When Android Studio creates your feature module, it makes it visible to the base module by adding the `android.dynamicFeatures` property to the base module's `build.gradle` file, as shown below:

```groovy
// In the base module's build.gradle file.
android {
    ...
    // Specifies feature modules that have a dependency on
    // this base module.
    dynamicFeatures = [":dynamic_feature", ":dynamic_feature2"]
}
```

Additionally, Android Studio includes the base module as a dependency of the feature module, as shown below:

```groovy
// In the feature module's build.gradle file:
...
dependencies {
    ...
    // Declares a dependency on the base module, ':app'.
    implementation project(':app')
}
```

### Specify additional ProGuard rules

Although only the base module's build configuration may enable code shrinking for your app project, you can provide custom ProGuard rules with each feature module using the [`proguardFiles`](<https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.BuildType.html#com.android.build.gradle.internal.dsl.BuildType:proguardFiles>) property, as shown below.

```groovy
android.buildTypes {
     release {
         // You must use the following property to specify additional ProGuard
         // rules for feature modules.
         proguardFiles 'proguard-rules-dynamic-features.pro'
     }
}
```

Note that these ProGuard rules are merged with those from other modules (including the base module) at build time. So, while each feature module may specify a new set of rules, those rules apply to all modules in the app project.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery).
