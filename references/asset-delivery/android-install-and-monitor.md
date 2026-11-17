### Install

Use the [`requestFetch()`](<https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary#requestfetch>) or [`fetch()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#fetch>) method to download an asset pack for the first time or call for the update of an asset pack to complete:

**Kotlin**

```kotlin
suspend fun AssetPackManager.requestFetch(packs: List<String>): AssetPackStates
```

**Java**

```java
Task<AssetPackStates> fetch(List<String> packNames)
```

This method returns an [`AssetPackStates`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackStates>) object containing a list of packs and their initial download states and sizes. If an asset pack requested using `requestFetch()` or `fetch()` is already downloading, the download status is returned and no additional download is started.

> **Note:** In most cases, you implement a `listener` to track the download and installation process as covered in the next section.

### Monitor download states

You should implement an [`AssetPackStateUpdatedListener`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackStateUpdateListener>) to track the installation progress of asset packs. The status updates are broken down per pack to support tracking the status of individual asset packs. You can start using available asset packs before all other downloads for your request have completed.

**Kotlin**

```kotlin
fun registerListener(listener: AssetPackStateUpdatedListener)
fun unregisterListener(listener: AssetPackStateUpdatedListener)
```

**Java**

```java
void registerListener(AssetPackStateUpdatedListener listener)
void unregisterListener(AssetPackStateUpdatedListener listener)
```

> **Note:** The Play Store automatically triggers the download of any `fast-follow` packs after the user installs or updates the app. However, these packs may not be ready to use immediately. You must check the status of the `fast-follow` packs at every app launch. If the download is in progress, monitor it with a listener. If the download is canceled or paused, you can resume it by using the `fetch()` method, as covered in the [Install](<https://developer.android.com/guide/playcore/asset-delivery/integrate-java?hl=en#install>) section.

#### Large downloads

If the download is larger than 200 MB and the user is not on Wi-Fi, the download does not start until the user explicitly gives their consent to proceed with the download using a mobile data connection. Similarly, if the download is large and the user loses Wi-Fi, the download is paused and explicit consent is required to proceed using a mobile data connection. A paused pack has state `WAITING_FOR_WIFI`. To trigger the UI flow to prompt the user for consent, use the [`showConfirmationDialog()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#showConfirmationDialog(androidx.activity.result.ActivityResultLauncher%3Candroidx.activity.result.IntentSenderRequest%3E)>) method.

Note that if the app does not call this method, the download is paused and will resume automatically only when the user is back on a Wi-Fi connection.

#### Required user confirmation

If a pack has the `REQUIRES_USER_CONFIRMATION` status, the download won't proceed until the user accepts the dialog that is shown with [`showConfirmationDialog()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#showConfirmationDialog(androidx.activity.result.ActivityResultLauncher%3Candroidx.activity.result.IntentSenderRequest%3E)>). This status can occur when the app is not recognized by Play, for example, if the app was side-loaded. Note that calling [`showConfirmationDialog()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#showConfirmationDialog(androidx.activity.result.ActivityResultLauncher%3Candroidx.activity.result.IntentSenderRequest%3E)>) in this case will cause the app to be updated. After the update, you will need to request the assets again.

The following is an example implementation of a listener:

**Kotlin**

[Complete kotlin example: Required user confirmation](<https://developer.android.com/guide/playcore/asset-delivery/integrate-java#required-confirmations>).

**Java**

[Complete java example: Kotlin](<https://developer.android.com/guide/playcore/asset-delivery/integrate-java#kotlin_6>).

Alternatively, you can use the [`getPackStates()`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager#getpackstates>) method to get the status of current downloads. [`AssetPackStates`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackStates>) contains the download progress, download status, and any failure error codes.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/integrate-java).
