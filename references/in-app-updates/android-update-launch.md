## Start an update

After you confirm that an update is available, you can request an update using [`AppUpdateManager.startUpdateFlowForResult()`](<https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager#startupdateflowforresult>):

**Kotlin**

```kotlin
appUpdateManager.startUpdateFlowForResult(
    // Pass the intent that is returned by 'getAppUpdateInfo()'.
    appUpdateInfo,
    // An activity result launcher registered using registerForActivityResult.
    activityResultLauncher,
    // Or pass 'AppUpdateType.FLEXIBLE' to newBuilder() for
    // flexible updates.
    AppUpdateOptions.newBuilder(AppUpdateType.IMMEDIATE).build())
```

**Java**

```java
appUpdateManager.startUpdateFlowForResult(
    // Pass the intent that is returned by 'getAppUpdateInfo()'.
    appUpdateInfo,
    // An activity result launcher registered using registerForActivityResult.
    activityResultLauncher,
    // Or pass 'AppUpdateType.FLEXIBLE' to newBuilder() for
    // flexible updates.
    AppUpdateOptions.newBuilder(AppUpdateType.IMMEDIATE).build());
```

> **Note:** Be mindful of how often you request updates to avoid annoying or tiring your users. You should only request in-app updates for changes that are important to the core functionality of your app.

Each `AppUpdateInfo` instance can be used to start an update only once. To retry the update in case of failure, request a new `AppUpdateInfo` and check again that the update is available and allowed.

You can register an activity result launcher using the built-in [`ActivityResultContracts.StartIntentSenderForResult`](<https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.StartIntentSenderForResult>) contract. Check the section on [getting callback for update status](<https://developer.android.com/guide/playcore/in-app-updates/kotlin-java?hl=en#status-callback>).

The next steps depend on whether you are requesting a [flexible update](<https://developer.android.com/guide/playcore/in-app-updates/kotlin-java?hl=en#flexible>) or an [immediate update](<https://developer.android.com/guide/playcore/in-app-updates/kotlin-java?hl=en#immediate>).

### Configure an update with AppUpdateOptions

[`AppUpdateOptions`](<https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateOptions>) contains an `AllowAssetPackDeletion` field that defines whether the update is allowed to clear [asset packs](<https://developer.android.com/guide/app-bundle/asset-delivery>) in case of limited device storage. This field is set to `false` by default, but you can use the [`setAllowAssetPackDeletion()`](<https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateOptions.Builder#setallowassetpackdeletion>) method to set it to `true` instead:

**Kotlin**

```kotlin
appUpdateManager.startUpdateFlowForResult(
    // Pass the intent that is returned by 'getAppUpdateInfo()'.
    appUpdateInfo,
    // An activity result launcher registered using registerForActivityResult.
    activityResultLauncher,
    // Or pass 'AppUpdateType.FLEXIBLE' to newBuilder() for
    // flexible updates.
    AppUpdateOptions.newBuilder(AppUpdateType.IMMEDIATE)
        .setAllowAssetPackDeletion(true)
        .build())
```

**Java**

```java
appUpdateManager.startUpdateFlowForResult(
    // Pass the intent that is returned by 'getAppUpdateInfo()'.
    appUpdateInfo,
    // An activity result launcher registered using registerForActivityResult.
    activityResultLauncher,
    // Or pass 'AppUpdateType.FLEXIBLE' to newBuilder() for
    // flexible updates.
    AppUpdateOptions.newBuilder(AppUpdateType.IMMEDIATE)
        .setAllowAssetPackDeletion(true)
        .build());
```

> **Caution:** Use the `AllowAssetPackDeletion` API option with care to avoid accidentally deleting assets. Before setting this option to `true`, check whether the update is allowed with this option set to `false`.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java).
