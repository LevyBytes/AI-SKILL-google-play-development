### Check update staleness

In addition to checking whether an update is available, you might also want to check how much time has passed since the user was last notified of an update through the Play Store. This can help you decide whether you should initiate a flexible update or an immediate update. For example, you might wait a few days before notifying the user with a flexible update, and a few days after that before requiring an immediate update.

Use `UAppUpdateInfo:GetClientVersionStalenessDays` to check the number of days since the update became available through the Play Store:

```c
int32 ClientVersionStalenessDays = UpdateInfo->GetClientVersionStalenessDays();
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

In your app's code, you can check the priority level for a given update using `UAppUpdateInfo::UpdatePriority`:

```c
int32 Priority = UpdateInfo->GetPriority();
```

## Start an update

After you confirm that an update is available, you can request an update using `UInAppUpdatesManager::StartUpdate`. Before you request an update, make sure that you have an up-to-date `UAppUpdateInfo` object. You must also create an `UAppUpdateOptions` object to configure the update flow.

The following example creates an `UAppUpdateOptions` object for an immediate update flow:

```c
// Creates an UAppUpdateOptions defining an immediate in-app
// update flow and its parameters.
UAppUpdateOptions* Options = NewObject<UAppUpdateOptions>();
Options->CreateOptions(EAppUpdateType::AppUpdate_TYPE_IMMEDIATE);
```

The following example creates an `UAppUpdateOptions` object for a flexible update flow:

```c
// Creates an UAppUpdateOptions defining a flexible in-app
// update flow and its parameters.
UAppUpdateOptions* Options = NewObject<UAppUpdateOptions>();
Options->CreateOptions(EAppUpdateType::AppUpdate_TYPE_FLEXIBLE);
```

The `UAppUpdateOptions` object also contains an `IsAssetPackDeletionAllowed` function that returns whether the update is allowed to clear [asset packs](<https://developer.android.com/guide/app-bundle/asset-delivery>) in case of limited device storage. This field is set to `false` by default, but you can set the field using `UAppUpdateOptions::SetAssetPackDeletionAllowed` to set it to `true` instead:

```c
// Sets the AssetPackDeletionAllowed field to true.
Options->SetAssetPackDeletionAllowed(true);
```

> **Note:** Use the `AllowAssetPackDeletion` API option with care to avoid accidentally deleting assets. Before setting this option to `true`, you should check `UAppUpdateInfo::IsUpdateTypeAllowed` with the `AllowAssetPackDeletion` option set to `false`.

The next steps depend on whether you are requesting a [flexible update](<https://developer.android.com/guide/playcore/in-app-updates/unreal-engine?hl=en#flexible>) or an [immediate update](<https://developer.android.com/guide/playcore/in-app-updates/unreal-engine?hl=en#immediate>).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/unreal-engine).
