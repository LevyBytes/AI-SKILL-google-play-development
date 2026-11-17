### Integrate the Play In-App Review Library

**Groovy**

```groovy
// In your app's build.gradle file:
...
dependencies {
    // This dependency is downloaded from the Google's Maven repository.
    // Make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.play:review:2.0.2'

    // For Kotlin users, also add the Kotlin extensions library for Play In-App Review:
    implementation 'com.google.android.play:review-ktx:2.0.2'
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
    implementation("com.google.android.play:review:2.0.2")

    // For Kotlin users, also import the Kotlin extensions library for Play In-App Review:
    implementation("com.google.android.play:review-ktx:2.0.2")
    ...
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore).
