### Integrate the Play In-App Update Library

**Groovy**

```groovy
// In your app's build.gradle file:
...
dependencies {
    // This dependency is downloaded from the Google's Maven repository.
    // Make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.play:app-update:2.1.0'

    // For Kotlin users, also add the Kotlin extensions library for Play In-App Update:
    implementation 'com.google.android.play:app-update-ktx:2.1.0'
    ...
}
```

**Kotlin**

```kotlin
// In your app's build.gradle.kts file:
...
dependencies {
    // This dependency is downloaded from the Google's Maven repository.
    // Make sure you also include that repository in your project's build.gradle file.
    implementation("com.google.android.play:app-update:2.1.0")

    // For Kotlin users, also import the Kotlin extensions library for Play In-App Update:
    implementation("com.google.android.play:app-update-ktx:2.1.0")
    ...
}
```

Review and accept the [SDK terms and conditions](<https://developer.android.com/guide/playcore/license>) before downloading or using the SDK.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore).
