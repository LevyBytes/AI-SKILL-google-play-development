Start a `FLEXIBLE` flow using [update launch](android-update-launch.md); [state monitoring](android-flexible-update-monitoring.md) precedes completion.

### Install a flexible update

When you detect the `InstallStatus.DOWNLOADED` state, you need to restart the app to install the update.

Unlike with immediate updates, Google Play does not automatically trigger an app restart for a flexible update. This is because during a flexible update, the user has an expectation to continue interacting with the app until they decide that they want to install the update.

It is recommended that you provide a notification (or some other UI indication) to inform the user that the update is ready to install and request confirmation before restarting the app.

The following example demonstrates implementing a [Material Design snackbar](<https://material.io/design/components/snackbars.html>) that requests confirmation from the user to restart the app:

**Kotlin**

```kotlin
val listener = InstallStateUpdatedListener { state ->
    if (state.installStatus() == InstallStatus.DOWNLOADED) {
        // After the update is downloaded, show a notification
        // and request user confirmation to restart the app.
        popupSnackbarForCompleteUpdate()
    }
    ...
}

// Displays the snackbar notification and call to action.
fun popupSnackbarForCompleteUpdate() {
    Snackbar.make(
        findViewById(R.id.activity_main_layout),
        "An update has just been downloaded.",
        Snackbar.LENGTH_INDEFINITE
    ).apply {
        setAction("RESTART") { appUpdateManager.completeUpdate() }
        setActionTextColor(resources.getColor(R.color.snackbar_action_text_color))
        show()
    }
}
```

**Java**

```java
InstallStateUpdatedListener listener = state -> {
    if (state.installStatus() == InstallStatus.DOWNLOADED) {
        // After the update is downloaded, show a notification
        // and request user confirmation to restart the app.
        popupSnackbarForCompleteUpdate();
    }
    ...
};

// Displays the snackbar notification and call to action.
private void popupSnackbarForCompleteUpdate() {
  Snackbar snackbar =
      Snackbar.make(
          findViewById(R.id.activity_main_layout),
          "An update has just been downloaded.",
          Snackbar.LENGTH_INDEFINITE);
  snackbar.setAction("RESTART", view -> appUpdateManager.completeUpdate());
  snackbar.setActionTextColor(
      getResources().getColor(R.color.snackbar_action_text_color));
  snackbar.show();
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java).
