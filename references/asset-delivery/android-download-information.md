### Get download information about asset packs

Apps are required to disclose the size of the download before fetching the asset pack. Use the [`requestPackStates()`](<https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#requestpackstates>) or the [`getPackStates()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#getpackstates>) method to determine the size of the download and whether the pack is already downloading.

**Kotlin**

```kotlin
suspend fun requestPackStates(packNames: List<String>): AssetPackStates
```

**Java**

```java
Task<AssetPackStates> getPackStates(List<String> packNames)
```

`requestPackStates()` is a suspend function returning an [`AssetPackStates`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackStates>) object, whereas `getPackStates()` is an asynchronous method that returns a `Task<AssetPackStates>`. The [`packStates()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackStates#packstates>) method of an `AssetPackStates` object returns a `Map<String, AssetPackState>`. This map contains the state of each requested asset pack, keyed by its name:

**Kotlin**

```kotlin
AssetPackStates#packStates(): Map<String, AssetPackState>
```

**Java**

```java
Map<String, AssetPackState> AssetPackStates#packStates()
```

The final request is shown by the following:

**Kotlin**

```kotlin
const val assetPackName = "assetPackName"
coroutineScope.launch {
  try {
    val assetPackStates: AssetPackStates =
      manager.requestPackStates(listOf(assetPackName))
    val assetPackState: AssetPackState =
      assetPackStates.packStates()[assetPackName]
  } catch (e: RuntimeExecutionException) {
    Log.d("MainActivity", e.message)
  }
}
```

**Java**

```java
final String assetPackName = "myasset";

assetPackManager
  .getPackStates(Collections.singletonList(assetPackName))
  .addOnCompleteListener(new OnCompleteListener<AssetPackStates>() {
      @Override
      public void onComplete(Task<AssetPackStates> task) {
          AssetPackStates assetPackStates;
          try {
              assetPackStates = task.getResult();
              AssetPackState assetPackState =
                  assetPackStates.packStates().get(assetPackName);
          } catch (RuntimeExecutionException e) {
              Log.d("MainActivity", e.getMessage());
              return;
          })
```

The following [`AssetPackState`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState>) methods provide the size of the asset pack, the downloaded amount so far (if requested), and the amount already transferred to the app:

- [`totalBytesToDownload()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState#totalbytestodownload>)
- [`bytesDownloaded()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState#bytesdownloaded>)
- [`transferProgressPercentage()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState#transferprogresspercentage>)

To get the status of an asset pack, use the [`status()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState#status>) method, which returns the status as an integer that corresponds to a constant field in the [`AssetPackStatus`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/model/AssetPackStatus>) class. An asset pack that's not installed yet has the status `AssetPackStatus.NOT_INSTALLED`.

If a request fails, use the [`errorCode()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState#errorcode>) method, whose return value corresponds to a constant field in the [`AssetPackErrorCode`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/model/AssetPackErrorCode>) class.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/integrate-java).
