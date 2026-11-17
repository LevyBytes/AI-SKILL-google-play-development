### Check update priority

The Google Play Developer API lets you set the priority of each update. This allows your app to decide how strongly to recommend an update to the user. For example, consider the following strategy for setting update priority:

- Minor UI improvements: **Low-priority** update; request neither a flexible update nor an immediate update. Update only when the user isn't interacting with your app.
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

In your app's code, you can check the priority level for a given update using [`updatePriority()`](<https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo#updatePriority()>). The returned priority takes into account the `inAppUpdatePriority` for all app version codes between the installed version and latest available version, irrespective of the release track. For example, consider the following scenario:

- You release version 1 to a production track with no priority.
- You release version 2 to an internal test track with priority 5.
- You release version 3 to a production track with no priority.

When production users update from version 1 to version 3, they will get priority 5, even though version 2 was published on a different track.

**Kotlin**

```kotlin
val appUpdateManager = AppUpdateManagerFactory.create(context)

// Returns an intent object that you use to check for an update.
val appUpdateInfoTask = appUpdateManager.appUpdateInfo

// Checks whether the platform allows the specified type of update,
// and checks the update priority.
appUpdateInfoTask.addOnSuccessListener { appUpdateInfo ->
  if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
        && appUpdateInfo.updatePriority() >= 4 /* high priority */
        && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.IMMEDIATE)) {
            // Request an immediate update.
  }
}
```

**Java**

```java
AppUpdateManager appUpdateManager = AppUpdateManagerFactory.create(context);

// Returns an intent object that you use to check for an update.
Task<AppUpdateInfo> appUpdateInfoTask = appUpdateManager.getAppUpdateInfo();

// Checks whether the platform allows the specified type of update,
// and checks the update priority.
appUpdateInfoTask.addOnSuccessListener(appUpdateInfo -> {
  if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
        && appUpdateInfo.updatePriority() >= 4 /* high priority */
        && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.IMMEDIATE)) {
            // Request an immediate update.
  }
});
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java).
