This guide describes how to integrate in-app reviews in your app using either Kotlin or Java. There are separate integration guides if you are using [native code](<https://developer.android.com/guide/playcore/in-app-review/native>), [Unity](<https://developer.android.com/guide/playcore/in-app-review/unity>) or [Unreal Engine](<https://developer.android.com/guide/playcore/in-app-review/unreal-engine>).

## Set up your development environment

The Play In-App Review Library is a part of the [Google Play Core libraries](<https://developer.android.com/guide/playcore>). Include the following Gradle dependency to integrate the Play In-App Review Library.

**Groovy**

```groovy
// In your app's build.gradle file:
...
dependencies {
    // This dependency is downloaded from the Google's Maven repository.
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.play:review:2.0.2'

    // For Kotlin users also add the Kotlin extensions library for Play In-App Review:
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
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation("com.google.android.play:review:2.0.2")

    // For Kotlin users also import the Kotlin extensions library for Play In-App Review:
    implementation("com.google.android.play:review-ktx:2.0.2")
    ...
}
```

## Create the ReviewManager

The [`ReviewManager`](<https://developer.android.com/reference/com/google/android/play/core/review/ReviewManager>) is the interface that lets your app start an in-app review flow. Obtain it by creating an instance using the [`ReviewManagerFactory`](<https://developer.android.com/reference/com/google/android/play/core/review/ReviewManagerFactory>).

**Kotlin**

```kotlin
val manager = ReviewManagerFactory.create(context)
```

**Java**

```java
ReviewManager manager = ReviewManagerFactory.create(context)
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-review/kotlin-java).
