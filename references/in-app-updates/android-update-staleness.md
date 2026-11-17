### Check update staleness

In addition to checking whether an update is available, you might also want to check how much time has passed since the user was last notified of an update through the Play Store. This can help you decide whether you should initiate a flexible update or an immediate update. For example, you might wait a few days before notifying the user with a flexible update, and a few days after that before requiring an immediate update.

Use [`clientVersionStalenessDays()`](<https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateInfo#clientVersionStalenessDays()>) to check the number of days since the update became available on the Play Store:

**Kotlin**

```kotlin
val appUpdateManager = AppUpdateManagerFactory.create(context)

// Returns an intent object that you use to check for an update.
val appUpdateInfoTask = appUpdateManager.appUpdateInfo

// Checks whether the platform allows the specified type of update,
// and current version staleness.
appUpdateInfoTask.addOnSuccessListener { appUpdateInfo ->
  if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
        && (appUpdateInfo.clientVersionStalenessDays() ?: -1) >= DAYS_FOR_FLEXIBLE_UPDATE
        && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.FLEXIBLE)) {
            // Request the update.
  }
}
```

**Java**

```java
AppUpdateManager appUpdateManager = AppUpdateManagerFactory.create(context);

// Returns an intent object that you use to check for an update.
Task<AppUpdateInfo> appUpdateInfoTask = appUpdateManager.getAppUpdateInfo();

// Checks whether the platform allows the specified type of update,
// and current version staleness.
appUpdateInfoTask.addOnSuccessListener(appUpdateInfo -> {
  if (appUpdateInfo.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE
        && appUpdateInfo.clientVersionStalenessDays() != null
        && appUpdateInfo.clientVersionStalenessDays() >= DAYS_FOR_FLEXIBLE_UPDATE
        && appUpdateInfo.isUpdateTypeAllowed(AppUpdateType.FLEXIBLE)) {
            // Request the update.
  }
});
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java).
