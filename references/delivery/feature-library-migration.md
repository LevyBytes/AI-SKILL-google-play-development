### Integrate the Play Feature Delivery Library

**Groovy**

```groovy
// In your app's build.gradle file:
...
dependencies {
    // This dependency is downloaded from the Google's Maven repository.
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.play:feature-delivery:2.1.0'

    // For Kotlin users, also add the Kotlin extensions library for Play Feature Delivery:
    implementation 'com.google.android.play:feature-delivery-ktx:2.1.0'
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
    implementation("com.google.android.play:feature-delivery:2.1.0")

    // For Kotlin users, also import the Kotlin extensions library for Play Feature Delivery:
    implementation("com.google.android.play:feature-delivery-ktx:2.1.0")
    ...
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore).
