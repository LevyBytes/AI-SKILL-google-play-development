Start a `FLEXIBLE` flow using [update launch](android-update-launch.md); [state monitoring](android-flexible-update-monitoring.md) precedes completion.

When you call [`appUpdateManager.completeUpdate()`](<https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager#completeUpdate()>) in the foreground, the platform displays a full-screen UI that restarts the app in the background. After the platform installs the update, your app restarts into its main activity.

If you instead call `completeUpdate()` when your app is [in the background](<https://developer.android.com/guide/background#definition>), the update is installed silently without obscuring the device UI.

Whenever the user brings your app to the foreground, check whether your app has an update waiting to be installed. If your app has an update in the `DOWNLOADED` state, prompt the user to install the update. Otherwise, the update data continues to occupy the user's device storage.

**Kotlin**

```kotlin
// Checks that the update is not stalled during 'onResume()'.
// However, you should execute this check at all app entry points.
override fun onResume() {
    super.onResume()

    appUpdateManager
        .appUpdateInfo
        .addOnSuccessListener { appUpdateInfo ->
            ...
            // If the update is downloaded but not installed,
            // notify the user to complete the update.
            if (appUpdateInfo.installStatus() == InstallStatus.DOWNLOADED) {
                popupSnackbarForCompleteUpdate()
            }
        }
}
```

**Java**

```java
// Checks that the update is not stalled during 'onResume()'.
// However, you should execute this check at all app entry points.
@Override
protected void onResume() {
  super.onResume();

  appUpdateManager
      .getAppUpdateInfo()
      .addOnSuccessListener(appUpdateInfo -> {
              ...
              // If the update is downloaded but not installed,
              // notify the user to complete the update.
              if (appUpdateInfo.installStatus() == InstallStatus.DOWNLOADED) {
                  popupSnackbarForCompleteUpdate();
              }
          });
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java).
