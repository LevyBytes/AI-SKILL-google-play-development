## Start an update

After you confirm that an update is available, you can request an update using [`AppUpdateManager_requestStartUpdate()`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdatemanager_requeststartupdate>). Before you request an update, get an up-to-date `AppUpdateInfo` object and create an [`AppUpdateOptions`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdateoptions>) object to configure the update flow. An `AppUpdateOptions` object defines options for an in-app update flow, including whether the update should be flexible or immediate.

The following example creates an `AppUpdateOptions` object for a flexible update flow:

```c
// Creates an AppUpdateOptions configuring a flexible in-app update flow.
AppUpdateOptions* options;
AppUpdateErrorCode error_code = AppUpdateOptions_createOptions(APP_UPDATE_TYPE_FLEXIBLE, &options);
```

The following example creates an `AppUpdateOptions` object for an immediate update flow:

```c
// Creates an AppUpdateOptions configuring an immediate in-app update flow.
AppUpdateOptions* options;
AppUpdateErrorCode error_code = AppUpdateOptions_createOptions(APP_UPDATE_TYPE_IMMEDIATE, &options);
```

The `AppUpdateOptions` object also contains an `AllowAssetPackDeletion` field that defines whether the update is allowed to clear [asset packs](<https://developer.android.com/guide/app-bundle/asset-delivery>) in case of limited device storage. This field is set to `false` by default, but you can use the [`AppUpdateOptions_setAssetPackDeletionAllowed()`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdateoptions_setassetpackdeletionallowed>) method to set it to `true` instead:

```c
bool allow = true;
AppUpdateErrorCode error_code = AppUpdateOptions_setAssetPackDeletionAllowed(options, allow);
```

> **Caution:** Use the `AllowAssetPackDeletion` API option with care to avoid accidentally deleting assets. Before setting this option to `true`, you should check whether the update is allowed with this option set to `false`.

After you have an up-to-date `AppUpdateInfo` object and a properly-configured `AppUpdateOptions` object, call `AppUpdateManager_requestStartUpdate()` to asynchronously request an update flow, passing in an Android Activity `jobject` for the final parameter.

```c
AppUpdateErrorCode request_error_code =
AppUpdateManager_requestStartUpdate(info, options, app->activity->clazz);
```

To free up resources, release instances of `AppUpdateInfo` and `AppUpdateOptions` that you no longer need by calling [`AppUpdateInfo_destroy()`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdateinfo_destroy>) and [`AppUpdateOptions_destroy()`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdateoptions_destroy>), respectively.

```c
AppUpdateInfo_destroy(info);
AppUpdateOptions_destroy(options);
```

For an immediate update flow, Google Play displays a user confirmation page. When the user accepts the request, Google Play automatically downloads and installs the update in the foreground, then restarts the app to the updated version if installation is successful.

For a flexible update flow, you can keep requesting up-to-date `AppUpdateInfo` objects to keep track of the current update status while the user continues to interact with the app. After the download finishes successfully, you must trigger the completion of the update by calling [`AppUpdateManager_requestCompleteUpdate()`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdatemanager_requestcompleteupdate>), as shown in the following example:

```c
AppUpdateStatus status = AppUpdateInfo_getStatus(info);
if (status == APP_UPDATE_DOWNLOADED) {
    AppUpdateErrorCode error_code = AppUpdateManager_requestCompleteUpdate();
    if (error_code != APP_UPDATE_NO_ERROR)
    {
      // There was an error while completing the update flow.
    }
}
```

Free up resources by calling the [`AppUpdateManager_destroy()`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdatemanager_destroy>) function after your app has finished using the API.

## Error handling

This section describes solutions for common errors indicated by specific [`AppUpdateErrorCode`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdateerrorcode>) values:

- An error code of `-110, APP_UPDATE_INITIALIZATION_NEEDED` indicates that the API has not been initialized successfully. Call `AppUpdateManager_init()` to initialize the API.
- An error code of `-4, APP_UPDATE_INVALID_REQUEST` indicates that some parameters of the update flow request are malformed. Check to make sure that the `AppUpdateInfo` and `AppUpdateOptions` objects are not null and are correctly formatted.
- An error code of `-5, APP_UPDATE_UNAVAILABLE` indicates that there is no applicable update available. Make sure that the target version has the same [package name](<https://developer.android.com/studio/build/configure-app-module#change_the_package_name>), [application ID](<https://developer.android.com/studio/build/configure-app-module#set_the_application_id>), and [signing key](<https://developer.android.com/studio/publish/app-signing>). If there is an update available, clear the app's cache and call `AppUpdateManager_requestAppUpdateInfo()` again to refresh `AppUpdateInfo`.
- An error code of `-6, APP_UPDATE_NOT_ALLOWED` indicates that the update type indicated by the `AppUpdateOption` object is not allowed. Check whether the `AppUpdateInfo` object indicates that the update type is allowed before starting the update flow.

## Next steps

[Test your app's in-app updates](<https://developer.android.com/guide/playcore/in-app-updates/test>) to verify that your integration is working correctly.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/native).
