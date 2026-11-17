## Initialize the in-app update API

Whenever you use the in-app update API, initialize it first by calling the [`AppUpdateManager_init()`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdatemanager_init>) function, as shown in the following example built with [`android_native_app_glue.h`](<https://developer.android.com/ndk/guides/concepts#naa>):

```c
void android_main(android_app* app) {
  app->onInputEvent = HandleInputEvent;

  AppUpdateErrorCode error_code =
    AppUpdateManager_init(app->activity->vm, app->activity->clazz);
  if (error_code == APP_UPDATE_NO_ERROR) {
    // You can use the API.
  }
}
```

## Check for update availability

Before you request an update, check if there is an update available for your app. [`AppUpdateManager_requestInfo()`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdatemanager_requestinfo>) starts an asynchronous request that gathers the required information to launch the in-app update flow later. The function returns `APP_UPDATE_NO_ERROR` if the request starts successfully.

```c
AppUpdateErrorCode error_code = AppUpdateManager_requestInfo()

if (error_code == APP_UPDATE_NO_ERROR) {
    // The request has successfully started, check the result using
    // AppUpdateManager_getInfo.
}
```

You can track the ongoing process and result of the request using [`AppUpdateManager_getInfo()`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdatemanager_getinfo>). In addition to the error code, this function returns an [`AppUpdateInfo`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdateinfo>) opaque struct, which you can use to retrieve information about the update request. For example, you might want to call this function in every game loop until it returns a non-null result for `info`:

```c
AppUpdateInfo* info;
GameUpdate() {

   // Keep calling this in every game loop until info != nullptr
   AppUpdateErrorCode error_code = AppUpdateManager_getInfo(&info);

   if (error_code == APP_UPDATE_NO_ERROR && info != nullptr) {
       // Successfully started, check the result in the following functions
   }
...
}
```

### Check update staleness

In addition to checking whether an update is available, you might also want to check how much time has passed since the user was last notified of an update through the Play Store. This can help you decide whether you should initiate a flexible update or an immediate update. For example, you might wait a few days before notifying the user with a flexible update, and a few days after that before requiring an immediate update.

Use [`AppUpdateInfo_getClientVersionStalenessDays()`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdateinfo_getclientversionstalenessdays>) to check the number of days since the update became available through the Play Store:

```c
int32_t staleness_days = AppUpdateInfo_getClientVersionStalenessDays(info);
```

### Check update priority

The Google Play Developer API lets you set the priority of each update. This allows your app to decide how strongly to recommend an update to the user. For example, consider the following strategy for setting update priority:

- Minor UI improvements: **Low-priority** update; request neither a flexible update nor an immediate update. Update only when the user isn't interacting with your app.
- Performance improvements: **Medium-priority** update; request a flexible update.
- Critical security update: **High-priority** update; request an immediate update.

To determine priority, Google Play uses an integer value between 0 and 5, with 0 being the default and 5 being the highest priority. To set the priority for an update, use the `inAppUpdatePriority` field under [`Edits.tracks.releases`](<https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks#release>) in the Google Play Developer API. All newly-added versions in the release are considered to be the same priority as the release. Priority can only be set when rolling out a new release and cannot be changed later.

Set the priority using the Google Play Developer API, as described in the [Play Developer API documentation](<https://developers.google.com/android-publisher/tracks#apk_workflow_example>). Specify in-app update priority in the [`Edit.tracks`](<https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks>) resource passed in the [`Edit.tracks: update`](<https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks/update>) method. The following example demonstrates releasing an app with version code 88 and `inAppUpdatePriority` 5:

```json
{
  "releases": [{
      "versionCodes": ["88"],
      "inAppUpdatePriority": 5,
      "status": "completed"
  }]
}
```

In your app's code, you can check the priority level for a given update using [`AppUpdateInfo_getPriority()`](<https://developer.android.com/reference/native/play/core/group/appupdate#appupdateinfo_getpriority>):

```c
int32_t priority = AppUpdateInfo_getPriority(info);
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/native).
