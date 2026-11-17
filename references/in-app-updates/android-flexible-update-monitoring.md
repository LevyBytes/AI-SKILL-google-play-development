Start a `FLEXIBLE` flow using [update launch](android-update-launch.md); [state monitoring](android-flexible-update-monitoring.md) precedes completion.

## Handle a flexible update

When you start a flexible update, a dialog first appears to the user to request consent. If the user consents, then the download starts in the background, and the user can continue to interact with your app. This section describes how to monitor and complete a flexible in-app update.

### Monitor the flexible update state

After the download begins for a flexible update, your app needs to monitor the update state to know when the update can be installed and to display the progress in your app's UI.

You can monitor the state of an update in progress by registering a listener for install status updates. You can also provide a progress bar in the app's UI to inform users of the download's progress.

**Kotlin**

```kotlin
// Create a listener to track request state updates.
val listener = InstallStateUpdatedListener { state ->
    // (Optional) Provide a download progress bar.
    if (state.installStatus() == InstallStatus.DOWNLOADING) {
      val bytesDownloaded = state.bytesDownloaded()
      val totalBytesToDownload = state.totalBytesToDownload()
      // Show update progress bar.
    }
    // Log state or install the update.
}

// Before starting an update, register a listener for updates.
appUpdateManager.registerListener(listener)

// Start an update.

// When status updates are no longer needed, unregister the listener.
appUpdateManager.unregisterListener(listener)
```

**Java**

```java
// Create a listener to track request state updates.
InstallStateUpdatedListener listener = state -> {
  // (Optional) Provide a download progress bar.
  if (state.installStatus() == InstallStatus.DOWNLOADING) {
      long bytesDownloaded = state.bytesDownloaded();
      long totalBytesToDownload = state.totalBytesToDownload();
      // Implement progress bar.
  }
  // Log state or install the update.
};

// Before starting an update, register a listener for updates.
appUpdateManager.registerListener(listener);

// Start an update.

// When status updates are no longer needed, unregister the listener.
appUpdateManager.unregisterListener(listener);
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java).
