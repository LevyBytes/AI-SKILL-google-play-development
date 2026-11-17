## Install-time delivery

Asset packs configured as `install-time` are immediately available at app launch. Use the Java [AssetManager API](<https://developer.android.com/reference/android/content/res/AssetManager>) to access assets served in this mode:

**Kotlin**

```kotlin
import android.content.res.AssetManager
...
val context: Context = createPackageContext("com.example.app", 0)
val assetManager: AssetManager = context.assets
val stream: InputStream = assetManager.open("asset-name")
```

**Java**

```java
import android.content.res.AssetManager;
...
Context context = createPackageContext("com.example.app", 0);
AssetManager assetManager = context.getAssets();
InputStream is = assetManager.open("asset-name");
```

## Fast-follow and on-demand delivery

For `fast-follow` and `on-demand` asset packs, [get download information](android-download-information.md), [install and monitor](android-install-and-monitor.md), then [access downloaded packs](android-pack-access-and-removal.md).

### Check status

Each asset pack is stored in a separate folder in the app's internal storage. Use the [`getPackLocation()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#getpacklocation>) method to determine the root folder of an asset pack. This method returns the following values:

| Return value | Status |
| --- | --- |
| A valid [`AssetPackLocation`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackLocation>) object | Asset pack root folder is ready for immediate access at [`assetsPath()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackLocation#assetspath>) |
| `null` | Unknown asset pack or assets are not available |

> **Note:** Don't rely on cached asset pack locations between app launches. The app should always check for the existence of asset packs at every launch. Asset packs may become invalid due to app updates or if the user clears the app data.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/integrate-java).
