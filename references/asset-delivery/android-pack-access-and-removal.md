### Access asset packs

You can access an asset pack using file system calls after the download request reaches the [`COMPLETED`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/model/AssetPackStatus#completed>) state. Use the [`getPackLocation()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#getpacklocation>) method to get the root folder of the asset pack.

Assets are stored in the `assets` directory within the asset pack root directory. You can get the path to the `assets` directory by using the convenience method [`assetsPath()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackLocation#assetspath>). Use the following method to get the path to a specific asset:

**Kotlin**

```kotlin
private fun getAbsoluteAssetPath(assetPack: String, relativeAssetPath: String): String? {
    val assetPackPath: AssetPackLocation =
      assetPackManager.getPackLocation(assetPack)
      // asset pack is not ready
      ?: return null

    val assetsFolderPath = assetPackPath.assetsPath()
    // equivalent to: FilenameUtils.concat(assetPackPath.path(), "assets")
    return FilenameUtils.concat(assetsFolderPath, relativeAssetPath)
}
```

**Java**

```java
private String getAbsoluteAssetPath(String assetPack, String relativeAssetPath) {
    AssetPackLocation assetPackPath = assetPackManager.getPackLocation(assetPack);

    if (assetPackPath == null) {
        // asset pack is not ready
        return null;
    }

    String assetsFolderPath = assetPackPath.assetsPath();
    // equivalent to: FilenameUtils.concat(assetPackPath.path(), "assets");
    String assetPath = FilenameUtils.concat(assetsFolderPath, relativeAssetPath);
    return assetPath;
}
```

## Other Play Asset Delivery API methods

The following are some additional API methods you may want to use in your app.

### Cancel request

Use [`cancel()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#cancel>) to cancel an active asset pack request. Note that this request is a best-effort operation.

### Remove an asset pack

Use [`requestRemovePack()`](<https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#requestremovepack>) or [`removePack()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#removepack>) to schedule the removal of an asset pack.

### Get locations of multiple asset packs

Use [`getPackLocations()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#getpacklocations>) to query the status of multiple asset packs in bulk, which returns a map of asset packs and their locations. The map returned by `getPackLocations()` contains an entry for each pack that is currently downloaded and up-to-date.

## Next step

[Test Play Asset Delivery](<https://developer.android.com/guide/playcore/asset-delivery/test>) locally and from Google Play.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/integrate-java).
