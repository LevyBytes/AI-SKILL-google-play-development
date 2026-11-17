This page describes the Google Play Core libraries and how to add them to your project.

> **Important:** The Google Play Core Java and Kotlin library has been split into multiple separate libraries, one for each feature. Update to the new libraries to benefit from new product additions. For more information, see the [migration guide](<https://developer.android.com/guide/playcore?hl=en#playcore-migration>).

The Google Play Core libraries are your app's runtime interface with the Google Play Store. Some of the things you can do include the following:

- [Download additional language resources](<https://developer.android.com/guide/playcore/feature-delivery/on-demand#lang_resources>)
- [Manage delivery of feature modules](<https://developer.android.com/guide/playcore/feature-delivery>)
- [Manage delivery of asset packs](<https://developer.android.com/guide/playcore/asset-delivery>)
- [Trigger in-app updates](<https://developer.android.com/guide/playcore/in-app-updates>)
- [Request in-app reviews](<https://developer.android.com/guide/playcore/in-app-review>)

The Play Core libraries are available in [Java](<https://developer.android.com/reference/com/google/android/play/core/packages>), [native](<https://developer.android.com/reference/native/play/core>), and [Unity](<https://developer.android.com/reference/unity>). For more information about the latest releases, see the [Release notes](<https://developer.android.com/reference/com/google/android/play/core/release-notes>).

## Migration from the Play Core Java and Kotlin Library

The Play Core Java and Kotlin Library has been partitioned into multiple per-feature Android libraries. This reduces the size Play Core libraries add to your app and allows for faster release cycles of the individual features.

The behavior of each feature has stayed consistent in this migration. The only notable change is that the new versions have adopted the [Google Play services Task API](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task>).

Use the list below to migrate to the new libraries and benefit from new features and bug fixes. If you use multiple Play features, you can import multiple libraries in your `build.gradle` file at once.

### Common migration steps

1. Update any existing import statements of Task objects from `import com.google.android.play.core.tasks.*;` to `import com.google.android.gms.tasks.*;`. All class names are unchanged.
2. Remove any imports of the old Play Core libraries in your `build.gradle` file.

### Integrate the Play Asset Delivery Library

**Groovy**

```groovy
// In your app's build.gradle file:
...
dependencies {
    // This dependency is downloaded from the Google's Maven repository.
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.play:asset-delivery:2.3.0'

    // For Kotlin users also add the Kotlin extensions library for Play Asset Delivery:
    implementation 'com.google.android.play:asset-delivery-ktx:2.3.0'
    ...
}
```

**Kotlin**

```kotlin
// In your app's build.gradle.kts file:
...
dependencies {
    // This dependency is downloaded from the Google's Maven repository.
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation("com.google.android.play:asset-delivery:2.3.0")

    // For Kotlin users also import the Kotlin extensions library for Play Asset Delivery:
    implementation("com.google.android.play:asset-delivery-ktx:2.3.0")
    ...
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore).
