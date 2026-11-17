## Start an update

After ensuring that an update is available, you can request an update using [`AppUpdateManager.StartUpdate()`](<https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateManager#startupdate>). Before you request an update, make sure that you have an up-to-date `AppUpdateInfo` object. You must also create an [`AppUpdateOptions`](<https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateOptions>) object to configure the update flow.

The following example creates an `AppUpdateOptions` object for an immediate update flow:

```c#
// Creates an AppUpdateOptions defining an immediate in-app
// update flow and its parameters.
var appUpdateOptions = AppUpdateOptions.ImmediateAppUpdateOptions();
```

The following example creates an `AppUpdateOptions` object for a flexible update flow:

```c#
// Creates an AppUpdateOptions defining a flexible in-app
// update flow and its parameters.
var appUpdateOptions = AppUpdateOptions.FlexibleAppUpdateOptions();
```

The `AppUpdateOptions` object also contains an `AllowAssetPackDeletion` field that defines whether the update is allowed to clear [asset packs](<https://developer.android.com/guide/app-bundle/asset-delivery>) in case of limited device storage. This field is set to `false` by default, but you can pass the `allowAssetPackDeletion` optional argument to `ImmediateAppUpdateOptions()` or `FlexibleAppUpdateOptions()` to set it to `true` instead:

```c#
// Creates an AppUpdateOptions for an immediate flow that allows
// asset pack deletion.
var appUpdateOptions =
  AppUpdateOptions.ImmediateAppUpdateOptions(allowAssetPackDeletion: true);

// Creates an AppUpdateOptions for a flexible flow that allows asset
// pack deletion.
var appUpdateOptions =
  AppUpdateOptions.FlexibleAppUpdateOptions(allowAssetPackDeletion: true);
```

> **Note:** Use the `AllowAssetPackDeletion` API option with care to avoid accidentally deleting assets. Before setting this option to `true`, you should check `AppUpdateManager.IsUpdateTypeAllowed()` with the `AllowAssetPackDeletion` option set to `false`.

The next steps depend on whether you are requesting a [flexible update](<https://developer.android.com/guide/playcore/in-app-updates/unity?hl=en#flexible>) or an [immediate update](<https://developer.android.com/guide/playcore/in-app-updates/unity?hl=en#immediate>).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/unity).
