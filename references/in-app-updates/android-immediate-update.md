## Handle an immediate update

When you start an immediate update and the user consents to begin the update, Google Play displays the update progress on top of your app's UI throughout the entire duration of the update. If the user closes or terminates your app during the update, the update should continue to download and install in the background without additional user confirmation.

However, when your app returns to the foreground, you should confirm that the update is not stalled in the [`UpdateAvailability.DEVELOPER_TRIGGERED_UPDATE_IN_PROGRESS`](<https://developer.android.com/reference/com/google/android/play/core/install/model/UpdateAvailability#DEVELOPER_TRIGGERED_UPDATE_IN_PROGRESS>) state. If the update is stalled in this state, resume the update:

**Kotlin**

```kotlin
// Checks that the update is not stalled during 'onResume()'.
// However, you should execute this check at all entry points into the app.
override fun onResume() {
    super.onResume()

    appUpdateManager
        .appUpdateInfo
        .addOnSuccessListener { appUpdateInfo ->
            ...
            if (appUpdateInfo.updateAvailability()
                == UpdateAvailability.DEVELOPER_TRIGGERED_UPDATE_IN_PROGRESS
            ) {
                // If an in-app update is already running, resume the update.
                appUpdateManager.startUpdateFlowForResult(
                  appUpdateInfo,
                  activityResultLauncher,
                  AppUpdateOptions.newBuilder(AppUpdateType.IMMEDIATE).build())
            }
        }
}
```

**Java**

```java
// Checks that the update is not stalled during 'onResume()'.
// However, you should execute this check at all entry points into the app.
@Override
protected void onResume() {
  super.onResume();

  appUpdateManager
      .getAppUpdateInfo()
      .addOnSuccessListener(
          appUpdateInfo -> {
            ...
            if (appUpdateInfo.updateAvailability()
                == UpdateAvailability.DEVELOPER_TRIGGERED_UPDATE_IN_PROGRESS) {
                // If an in-app update is already running, resume the update.
                appUpdateManager.startUpdateFlowForResult(
                  appUpdateInfo,
                  activityResultLauncher,
                  AppUpdateOptions.newBuilder(AppUpdateType.IMMEDIATE).build());
            }
          });
}
```

The update flow returns a result as described in the reference documentation for [`startUpdateFlowForResult()`](<https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager#startUpdateFlowForResult(com.google.android.play.core.appupdate.AppUpdateInfo,%20android.app.Activity,%20com.google.android.play.core.appupdate.AppUpdateOptions,%20int)>). In particular, your app should be able to handle cases where a user declines the update or cancels the download. When the user performs either of these actions, the Google Play UI closes. Your app should determine the best way to proceed.

If possible, let the user continue without the update and prompt them again later. If your app can't function without the update, consider displaying an informative message before restarting the update flow or prompting the user to close the app. That way, the user understands that they can relaunch your app when they're ready to install the required update.

## Next steps

[Test your app's in-app updates](<https://developer.android.com/guide/playcore/in-app-updates/test>) to verify that your integration is working correctly.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java).
