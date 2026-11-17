The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

### Handle request errors

Keep in mind that on demand installation of feature modules can sometime fail, just like app installation doesn't always succeed. Failure to install can be due to issues like low device storage, no network connectivity, or the user not being signed in to the Google Play Store. For suggestions on how to handle these situations gracefully from the user's perspective, check out our [UX guidelines for on demand delivery](<https://developer.android.com/guide/playcore/feature-delivery/ux-guidelines>).

Code-wise, you should handle failures downloading or installing a module using `addOnFailureListener()`, as shown below:

**Kotlin**

```kotlin
splitInstallManager
    .startInstall(request)
    .addOnFailureListener { exception ->
        when ((exception as SplitInstallException).errorCode) {
            SplitInstallErrorCode.NETWORK_ERROR -> {
                // Display a message that requests the user to establish a
                // network connection.
            }
            SplitInstallErrorCode.ACTIVE_SESSIONS_LIMIT_EXCEEDED -> checkForActiveDownloads()
            ...
        }
    }

fun checkForActiveDownloads() {
    splitInstallManager
        // Returns a SplitInstallSessionState object for each active session as a List.
        .sessionStates
        .addOnCompleteListener { task ->
            if (task.isSuccessful) {
                // Check for active sessions.
                for (state in task.result) {
                    if (state.status() == SplitInstallSessionStatus.DOWNLOADING) {
                        // Cancel the request, or request a deferred installation.
                    }
                }
            }
        }
}
```

**Java**

```java
splitInstallManager
    .startInstall(request)
    .addOnFailureListener(exception -> {
        switch (((SplitInstallException) exception).getErrorCode()) {
            case SplitInstallErrorCode.NETWORK_ERROR:
                // Display a message that requests the user to establish a
                // network connection.
                break;
            case SplitInstallErrorCode.ACTIVE_SESSIONS_LIMIT_EXCEEDED:
                checkForActiveDownloads();
            ...
    });

void checkForActiveDownloads() {
    splitInstallManager
        // Returns a SplitInstallSessionState object for each active session as a List.
        .getSessionStates()
        .addOnCompleteListener( task -> {
            if (task.isSuccessful()) {
                // Check for active sessions.
                for (SplitInstallSessionState state : task.getResult()) {
                    if (state.status() == SplitInstallSessionStatus.DOWNLOADING) {
                        // Cancel the request, or request a deferred installation.
                    }
                }
            }
        });
}
```

The table below describes the error states your app may need to handle:

| Error code | Description | Suggested action |
| --- | --- | --- |
| ACTIVE_SESSIONS_LIMIT_EXCEEDED | The request is rejected because there is at least one existing request that is currently downloading. | Check if there are any requests that are still downloading, as shown in the sample above. |
| MODULE_UNAVAILABLE | Google Play is unable to find the requested module based on the current installed version of the app, device, and user’s Google Play account. | If the user does not have access to the module, notify them. |
| INVALID_REQUEST | Google Play received the request, but the request is not valid. | Verify that the information included in the request is complete and accurate. |
| SESSION_NOT_FOUND | A session for a given session ID was not found. | If you’re trying to monitor the state of a request by its session ID, make sure that the session ID is correct. |
| API_NOT_AVAILABLE | The Play Feature Delivery Library is not supported on the current device. That is, the device is not able to download and install features on demand. | For devices running Android 4.4 (API level 20) or lower, you should include feature modules at install time using the `dist:fusing` manifest property. To learn more, read about the [feature module manifest](<https://developer.android.com/guide/playcore/feature-delivery#feature-module-manifest>). |
| NETWORK_ERROR | The request failed because of a network error. | Prompt the user to either establish a network connection or change to a different network. |
| ACCESS_DENIED | The app is unable to register the request because of insufficient permissions. | This typically occurs when the app is in the background. Attempt the request when the app returns to the foreground. |
| INCOMPATIBLE_WITH_EXISTING_SESSION | The request contains one or more modules that have already been requested but have not yet been installed. | Either create a new request that does not include modules that your app has already requested, or wait for all currently requested modules to finish installing before retrying the request. Keep in mind, requesting a module that has already been installed does not resolve in an error. |
| SERVICE_DIED | The service responsible for handling the request has died. | Retry the request. Your `SplitInstallStateUpdatedListener` receives a `SplitInstallSessionState` with this error code, status `FAILED` and session ID `-1`. |
| INSUFFICIENT_STORAGE | The device does not have enough free storage to install the feature module. | Notify the user that they do not have enough storage to install this feature. |
| SPLITCOMPAT_VERIFICATION_ERROR, SPLITCOMPAT_EMULATION_ERROR, SPLITCOMPAT_COPY_ERROR | SplitCompat could not load the feature module. | These errors should automatically resolve themselves after the next app restart. |
| PLAY_STORE_NOT_FOUND | The Play Store app is not installed on the device. | Let the user know that the Play Store app is required to download this feature. |
| APP_NOT_OWNED | The app has not been installed by Google Play and the feature cannot be downloaded. This error can only occur for deferred installs. | If you want the user to acquire the app on Google Play, use `startInstall()` which can obtain the necessary [user confirmation](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#obtain_confirmation>). |
| INTERNAL_ERROR | An internal error occurred within the Play Store. | Retry the request. |

If a user requests downloading an on demand module and an error occurs, consider displaying a dialog that provides two options for the user: **Try again** (which attempts the request again) and **Cancel** (which abandons the request). For additional support, you should also provide **Help** link that directs users to the [Google Play Help center](<https://support.google.com/googleplay/answer/7513003>).

> **Note:** When testing your app, if you see `onError(-2)`, it might be because you have not yet uploaded your app to Google Play. To test on demand functionality of your app, you must either [share your app with a URL](<https://support.google.com/googleplay/android-developer/answer/9303479>) or [set up an open, closed, or internal test](<https://support.google.com/googleplay/android-developer/answer/3131213>).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
