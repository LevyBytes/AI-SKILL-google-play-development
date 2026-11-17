## Handle a flexible update

After you have an up-to-date `AppUpdateInfo` object and a properly-configured `AppUpdateOptions` object, you can call `AppUpdateManager.StartUpdate()` to asynchronously request an update flow.

```c#
IEnumerator StartFlexibleUpdate()
{
  // Creates an AppUpdateRequest that can be used to monitor the
  // requested in-app update flow.
  var startUpdateRequest = appUpdateManager.StartUpdate(
    // The result returned by PlayAsyncOperation.GetResult().
    appUpdateInfoResult,
    // The AppUpdateOptions created defining the requested in-app update
    // and its parameters.
    appUpdateOptions);

  while (!startUpdateRequest.IsDone)
  {
  // For flexible flow,the user can continue to use the app while
  // the update downloads in the background. You can implement a
  // progress bar showing the download status during this time.
  yield return null;
  }

}
```

For a flexible update flow, you must trigger the installation of the app update after the download finishes successfully. To do this, call [`AppUpdateManager.CompleteUpdate()`](<https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateManager#completeupdate>), as shown in the following example:

```c#
IEnumerator CompleteFlexibleUpdate()
{
  var result = appUpdateManager.CompleteUpdate();
  yield return result;

  // If the update completes successfully, then the app restarts and this line
  // is never reached. If this line is reached, then handle the failure (e.g. by
  // logging result.Error or by displaying a message to the user).
}
```

## Handle an immediate update

After you have an up-to-date `AppUpdateInfo` object and a properly-configured `AppUpdateOptions` object, you can call `AppUpdateManager.StartUpdate()` to asynchronously request an update flow.

```c#
IEnumerator StartImmediateUpdate()
{
  // Creates an AppUpdateRequest that can be used to monitor the
  // requested in-app update flow.
  var startUpdateRequest = appUpdateManager.StartUpdate(
    // The result returned by PlayAsyncOperation.GetResult().
    appUpdateInfoResult,
    // The AppUpdateOptions created defining the requested in-app update
    // and its parameters.
    appUpdateOptions);
  yield return startUpdateRequest;

  // If the update completes successfully, then the app restarts and this line
  // is never reached. If this line is reached, then handle the failure (for
  // example, by logging result.Error or by displaying a message to the user).
}
```

For an immediate update flow, Google Play displays a user confirmation dialog. When the user accepts the request, Google Play automatically downloads and installs the update, then restarts the app to the updated version if installation is successful.

## Error handling

This section describes solutions for common errors.

- If `StartUpdate()` throws an `ArgumentNullException`, it means that `AppUpdateInfo` is null. Make sure the `AppUpdateInfo` object returned from `GetAppUpdateInfo()` is not null before starting the update flow.
- If `PlayAsyncOperation` returns the `ErrorUpdateUnavailable` error code, make sure there is an updated app version available that has the same application ID and signing key.
- If `PlayAsyncOperation` returns the `ErrorUpdateNotAllowed` error code, it means that the `AppUpdateOptions` object indicates an update type that is not allowed for the available update. Check whether the `AppUpdateInfo` object indicates that the selected update type is allowed before starting the update flow.

## Next steps

[Test your app's in-app updates](<https://developer.android.com/guide/playcore/in-app-updates/test>) to verify that your integration is working correctly.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/unity).
