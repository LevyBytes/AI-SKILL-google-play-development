### Access asset packs

You can access an asset pack using file system calls after the download request reaches the `COMPLETED` state. Each asset pack is stored in a separate directory in the app's internal storage. Use [`AssetPackManager_getAssetPackLocation()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_getassetpacklocation>) to get an [`AssetPackLocation`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpacklocation>) for the specified asset pack. Use [`AssetPackLocation_getStorageMethod()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpacklocation_getstoragemethod>) on that location to determine the storage method:

- `ASSET_PACK_STORAGE_APK`: The asset pack is installed as an APK. See [Install-time delivery](<https://developer.android.com/guide/playcore/asset-delivery/integrate-native?hl=en#install-time-delivery>) to access these assets.
- `ASSET_PACK_STORAGE_FILES`: Use [`AssetPackLocation_getAssetsPath()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpacklocation_getassetspath>) to get a path to the directory containing the assets, or null if the assets have not been downloaded. Don't modify downloaded files in this path.

```c
AssetPackLocation* location;

AssetPackErrorCode error_code = AssetPackManager_getAssetPackLocation(asset-pack-name, &location);

if (error_code == ASSET_PACK_NO_ERROR) {
    AssetPackStorageMethod storage_method = AssetPackLocation_getStorageMethod(location);
    const char* assets_path = AssetPackLocation_getAssetsPath(location);
    AssetPackLocation_destroy(location);
}
```

Once you locate the assets, use functions like `fopen` or `ifstream` to access the files.

> **Note:** Don't rely on cached asset pack locations between app launches. The app should check for the existence of asset packs at every launch. Asset packs may become invalid due to app updates or if the user clears the app data.

## Other Play Core API methods

The following are some additional API methods you may want to use in your app.

### Cancel request

Use [`AssetPackManager_cancelDownload()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_canceldownload>) to cancel an active asset pack request. Note that this request is a best-effort operation.

### Request removal

Use [`AssetPackManager_requestRemoval()`](<https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_requestremoval>) to schedule the removal of an asset pack.

## Next steps

[Test Play Asset Delivery](<https://developer.android.com/guide/playcore/asset-delivery/test>) locally and from Google Play.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/integrate-native).
