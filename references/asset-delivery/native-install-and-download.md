## Install-time delivery

Asset packs configured as `install-time` are immediately available at app launch. Use the [NDK AAssetManager API](<https://developer.android.com/ndk/reference/group/asset#aassetmanager>) to access assets served in this mode:

```c
#include <android/asset_manager.h>
#include <android_native_app_glue.h>
...
AAssetManager* assetManager = app->activity->assetManager;
AAsset* asset = AAssetManager_open(assetManager, "asset-name", AASSET_MODE_BUFFER);
size_t assetLength = AAsset_getLength(asset);
char* buffer = (char*) malloc(assetLength + 1);
AAsset_read(asset, buffer, assetLength);
```

## Fast-follow and on-demand delivery

For `fast-follow` and `on-demand` asset packs, initialize the API, query download information and start the download as described here, then [access downloaded packs](native-pack-access-and-removal.md).

### App launch

Always call [`AssetPackManager_init()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_init>) to initialize the asset pack API before calling any other function. Check for any [asset pack error codes](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackerrorcode>).

```c
#include "play/asset_pack.h"
...
AssetPackErrorCode AssetPackManager_init(JavaVM* jvm, jobject android_context);
```

Also be sure to call the following functions in the `onPause()` and `onResume()` of [`ANativeActivityCallbacks`](<https://developer.android.com/ndk/reference/struct/a-native-activity-callbacks>):

- [`AssetPackErrorCode AssetPackManager_onPause()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_onpause>)
- [`AssetPackErrorCode AssetPackManager_onResume()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_onresume>)

### Get download information about asset packs

Apps are required to disclose the size of the download before fetching the asset pack. Use the [`AssetPackManager_requestInfo()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_requestinfo>) function to start an asynchronous request for the size of the download and whether the pack is already downloading. Then use [`AssetPackManager_getDownloadState()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_getdownloadstate>) to poll for the download state (for example, call this function once per frame in your game loop). If a request fails, check the [asset pack error codes](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackerrorcode>).

```c
AssetPackErrorCode AssetPackManager_requestInfo();      // Call once
AssetPackErrorCode AssetPackManager_getDownloadState(); // Call once per frame in your game loop
```

The `AssetPackManager_getDownloadState()` function returns the opaque type [`AssetPackDownloadState`](<https://developer.android.com/reference/native/play/core/group/assetpack#group__assetpack_1gaa635665bad061c34cbee483ada331afc>) as an output pointer. Use this pointer to call the following functions:

```c
AssetPackDownloadState* state;
AssetPackErrorCode error_code = AssetPackManager_getDownloadState(asset-pack-name, &state);
AssetPackDownloadStatus status = AssetPackDownloadState_getStatus(state);
uint64_t downloadedBytes = AssetPackDownloadState_getBytesDownloaded(state);
uint64_t totalBytes = AssetPackDownloadState_getTotalBytesToDownload(state));
AssetPackDownloadState_destroy(state);
```

### Install

Use [`AssetPackManager_requestDownload()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_requestdownload>) to start downloading an asset pack for the first time or to request for an asset pack update to complete:

```c
AssetPackErrorCode AssetPackManager_requestDownload();  // Call once
AssetPackErrorCode AssetPackManager_getDownloadState(); // Call once per frame in your game loop
```

The `AssetPackManager_getDownloadState()` function returns the opaque type [`AssetPackDownloadState`](<https://developer.android.com/reference/native/play/core/group/assetpack#group__assetpack_1gaa635665bad061c34cbee483ada331afc>). For information on how to use this type, see [Get download information](<https://developer.android.com/guide/playcore/asset-delivery/integrate-native?hl=en#get-download-information>).

> **Note:** The Android system notification bar shows download progress for `fast-follow` and `on-demand` asset packs. The user can cancel the download from this bar at any time.

#### Large downloads

If the download is larger than 200MB and the user is not on Wi-Fi, the download does not start until the user explicitly gives their consent to proceed with the download using a mobile data connection. Similarly, if the download is large and the user loses Wi-Fi, the download pauses and explicit consent is required to proceed using a mobile data connection. A paused pack has state `WAITING_FOR_WIFI`. To trigger the UI flow to prompt the user for consent, use the following:

- [`AssetPackManager_showConfirmationDialog()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_showconfirmationdialog>)
- [`AssetPackManager_getShowConfirmationDialogStatus()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_getshowconfirmationdialogstatus>)

#### Required user confirmation

If a pack has the `REQUIRES_USER_CONFIRMATION` status, the download doesn't proceed until the user accepts the dialog that is shown with `AssetPackManager_showConfirmationDialog()`. This status can arise if the app is not recognized by Play. Note that calling `AssetPackManager_showConfirmationDialog()` in this case causes the app to be updated. After the update, request the assets again.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/integrate-native).
