The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

### Handle state updates

After you register a listener and record the session ID for your request, use [`StateUpdatedListener.onStateUpdate()`](<https://developer.android.com/reference/com/google/android/play/core/listener/StateUpdatedListener#onStateUpdate(StateT)>) to handle state changes, as shown below.

**Kotlin**

```kotlin
override fun onStateUpdate(state : SplitInstallSessionState) {
    if (state.status() == SplitInstallSessionStatus.FAILED
        && state.errorCode() == SplitInstallErrorCode.SERVICE_DIED) {
       // Retry the request.
       return
    }
    if (state.sessionId() == mySessionId) {
        when (state.status()) {
            SplitInstallSessionStatus.DOWNLOADING -> {
              val totalBytes = state.totalBytesToDownload()
              val progress = state.bytesDownloaded()
              // Update progress bar.
            }
            SplitInstallSessionStatus.INSTALLED -> {

              // After a module is installed, you can start accessing its content or
              // fire an intent to start an activity in the installed module.
              // For other use cases, see access code and resources from installed modules.

              // If the request is an on demand module for an Android Instant App
              // running on Android 8.0 (API level 26) or higher, you need to
              // update the app context using the SplitInstallHelper API.
            }
        }
    }
}
```

**Java**

```java
@Override
public void onStateUpdate(SplitInstallSessionState state) {
    if (state.status() == SplitInstallSessionStatus.FAILED
        && state.errorCode() == SplitInstallErrorCode.SERVICE_DIES) {
       // Retry the request.
       return;
    }
    if (state.sessionId() == mySessionId) {
        switch (state.status()) {
            case SplitInstallSessionStatus.DOWNLOADING:
              int totalBytes = state.totalBytesToDownload();
              int progress = state.bytesDownloaded();
              // Update progress bar.
              break;

            case SplitInstallSessionStatus.INSTALLED:

              // After a module is installed, you can start accessing its content or
              // fire an intent to start an activity in the installed module.
              // For other use cases, see access code and resources from installed modules.

              // If the request is an on demand module for an Android Instant App
              // running on Android 8.0 (API level 26) or higher, you need to
              // update the app context using the SplitInstallHelper API.
        }
    }
}
```

The possible states for your install request are described in the table below.

| Request state | Description | Suggested action |
| --- | --- | --- |
| PENDING | The request has been accepted and the download should start soon. | Initialize UI components, such as a progress bar, to provide the user feedback on the download. |
| REQUIRES_USER_CONFIRMATION | The download requires user confirmation. Most commonly this status occurs if the app has not been installed through Google Play. | Prompt the user to confirm the feature download through Google Play. To learn more, go to the section about how to [obtain user confirmation](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#obtain_confirmation>). |
| DOWNLOADING | Download is in progress. | If you provide a progress bar for the download, use the `SplitInstallSessionState.bytesDownloaded()` and `SplitInstallSessionState.totalBytesToDownload()` methods to update the UI (see the code sample above this table). |
| DOWNLOADED | The device has downloaded the module but installation has not yet begun. | Apps should [enable SplitCompat](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#access_downloaded_modules>) to have access to downloaded modules and avoid seeing this state. This is required in order to access the feature module's code and resources. |
| INSTALLING | The device is currently installing the module. | Update the progress bar. This state is typically short. |
| INSTALLED | The module is installed on the device. | [Access code and resource in the module](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#access_installed_modules>) to continue the user journey. If the module is for an Android Instant App running on Android 8.0 (API level 26) or higher, you need to use `splitInstallHelper` to [update app components with the new module](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#aia_update_context>). |
| FAILED | The request failed before the module was installed on the device. | Prompt the user to either retry the request or cancel it. |
| CANCELING | The device is in the process of cancelling the request. | To learn more, go to the section about how to [cancel an install request](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#cancel_request>). |
| CANCELED | The request has been cancelled. |  |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
