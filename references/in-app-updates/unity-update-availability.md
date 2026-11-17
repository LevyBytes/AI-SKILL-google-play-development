## Check for update availability

Before you request an update, check if there is an update available for your app. Use `AppUpdateManager` to check for an update in a [coroutine](<https://docs.unity3d.com/Manual/Coroutines>):

```c#
IEnumerator CheckForUpdate()
{
  PlayAsyncOperation<AppUpdateInfo, AppUpdateErrorCode> appUpdateInfoOperation =
    appUpdateManager.GetAppUpdateInfo();

  // Wait until the asynchronous operation completes.
  yield return appUpdateInfoOperation;

  if (appUpdateInfoOperation.IsSuccessful)
  {
    var appUpdateInfoResult = appUpdateInfoOperation.GetResult();
    // Check AppUpdateInfo's UpdateAvailability, UpdatePriority,
    // IsUpdateTypeAllowed(), ... and decide whether to ask the user
    // to start an in-app update.
  }
  else
  {
    // Log appUpdateInfoOperation.Error.
  }
}
```

The returned [`AppUpdateInfo`](<https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateInfo>) instance contains the update availability status. If an in-app update is already in progress, the instance also reports the status of the in-progress update.

### Check update staleness

In addition to checking whether an update is available, you might also want to check how much time has passed since the user was last notified of an update through the Play Store. This can help you decide whether you should initiate a flexible update or an immediate update. For example, you might wait a few days before notifying the user with a flexible update, and a few days after that before requiring an immediate update.

Use [`ClientVersionStalenessDays`](<https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateInfo#clientversionstalenessdays>) to check the number of days since the update became available through the Play Store:

```c#
var stalenessDays = appUpdateInfoOperation.ClientVersionStalenessDays;
```

### Check update priority

The Google Play Developer API lets you set the priority of each update. This allows your app to decide how strongly to recommend an update to the user. For example, consider the following strategy for setting update priority:

- Minor UI improvements: **Low-priority** update; request neither a flexible update nor an immediate update.
- Performance improvements: **Medium-priority** update; request a flexible update.
- Critical security update: **High-priority** update; request an immediate update.

To determine priority, Google Play uses an integer value between 0 and 5, with 0 being the default and 5 being the highest priority. To set the priority for an update, use the `inAppUpdatePriority` field under `Edits.tracks.releases` in the Google Play Developer API. All newly-added versions in the release are considered to be the same priority as the release. Priority can only be set when rolling out a new release and cannot be changed later.

Set the priority using the Google Play Developer API as described in the [Play Developer API documentation](<https://developers.google.com/android-publisher/tracks#apk_workflow_example>). In-app update priority should be specified in the [`Edit.tracks`](<https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks>) resource passed in the [`Edit.tracks: update`](<https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks/update>) method. The following example demonstrates releasing an app with version code 88 and `inAppUpdatePriority` 5:

```json
{
  "releases": [{
      "versionCodes": ["88"],
      "inAppUpdatePriority": 5,
      "status": "completed"
  }]
}
```

In your app's code, you can check the priority level for a given update using [`UpdatePriority`](<https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateInfo#updatepriority>):

```c#
var priority = appUpdateInfoOperation.UpdatePriority;
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/unity).
