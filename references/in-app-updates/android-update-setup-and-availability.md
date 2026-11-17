This guide describes how to support [in-app updates](<https://developer.android.com/guide/playcore/in-app-updates>) in your app using either Kotlin or Java. There are separate guides for cases where your implementation uses [native code (C/C++)](<https://developer.android.com/guide/playcore/in-app-updates/native>) and cases where your implementation uses [Unity](<https://developer.android.com/guide/playcore/in-app-updates/unity>) or [Unreal Engine](<https://developer.android.com/guide/playcore/in-app-updates/unreal-engine>).

## Set up your development environment

The Play In-App Update Library is a part of the [Google Play Core libraries](<https://developer.android.com/guide/playcore>). Include the following Gradle dependency to integrate the Play In-App Update Library.

**Groovy**

```groovy
// In your app's build.gradle file:
...
dependencies {
    // This dependency is downloaded from the Google's Maven repository.
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.play:app-update:2.1.0'

    // For Kotlin users also add the Kotlin extensions library for Play In-App Update:
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
    // So, make sure you also include that repository in your project's build.gradle file.
    implementation("com.google.android.play:app-update:2.1.0")

    // For Kotlin users also import the Kotlin extensions library for Play In-App Update:
    implementation("com.google.android.play:app-update-ktx:2.1.0")
    ...
}
```

## Check for update availability

Before requesting an update, check if there is an update available for your app. Use [`AppUpdateManager`](<https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager>) to check for an update:

**Kotlin**

```kotlin
val appUpdateManager = AppUpdateManagerFactory.create(context)

// Returns an intent object that you use to check for an update.
val appUpdateInfoTask = appUpdateManager.appUpdateInfo

// Checks that the platform will allow the specified type of update.
appUpdateInfoTask.addOnSuccessListener { appUpdateInfo ->
    if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
        // This example applies an immediate update. To apply a flexible update
        // instead, pass in AppUpdateType.FLEXIBLE
        && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.IMMEDIATE)
    ) {
        // Request the update.
    }
}
```

**Java**

```java
AppUpdateManager appUpdateManager = AppUpdateManagerFactory.create(context);

// Returns an intent object that you use to check for an update.
Task<AppUpdateInfo> appUpdateInfoTask = appUpdateManager.getAppUpdateInfo();

// Checks that the platform will allow the specified type of update.
appUpdateInfoTask.addOnSuccessListener(appUpdateInfo -> {
    if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
          // This example applies an immediate update. To apply a flexible update
          // instead, pass in AppUpdateType.FLEXIBLE
          && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.IMMEDIATE)) {
              // Request the update.
    }
});
```

The returned [`AppUpdateInfo`](<https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo>) instance contains the update availability status. Depending on the status of the update, the instance also contains the following:

- If an update is available and the update is allowed, the instance also contains an intent to start the update.
- If an in-app update is already in progress, the instance also reports the status of the in-progress update.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java).
