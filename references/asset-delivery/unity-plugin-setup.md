When integrating asset delivery, Unity games can access asset packs using Addressables or AssetBundles. Addressables are the more recent and recommended asset delivery solution for games built with Unity 2019.4 or higher, while AssetBundles provide support of asset packs in Unity 2017.4 and 2018.4.

## Unity Addressables

Games built with Unity 2019.4 or higher should use [Addressables](<https://unity.com/how-to/simplify-your-content-management-addressables#where-can-i-learn-more-about-addressables>) for asset delivery on Android. Unity provides a Play Asset Delivery (PAD) API for handling Android asset packs using Addressables. For information about using Addressables, see the following:

- [Addressables for Android package](<https://docs.unity3d.com/Packages/com.unity.addressables.android@1.0/manual/index.html>)
- [PAD guide for Unity](<https://docs.unity3d.com/Manual/play-asset-delivery.html>)
- PAD API for Unity [reference documentation](<https://docs.unity3d.com/ScriptReference/Android.AndroidAssetPacks.html>)

## Use AssetBundle files

Games built with Unity 2017.4 and 2018.4 can use AssetBundle files for asset delivery on Android. Unity [AssetBundle](<https://docs.unity3d.com/Manual/AssetBundlesIntro.html>) files contain serialized assets that can be loaded by the Unity engine while the app is running. These files are platform-specific (for example, built for Android) and can be used in combination with asset packs. Most commonly, one AssetBundle file is packaged into a single asset pack, with the pack using the same name as the AssetBundle. If you want more flexibility in creating an asset pack, configure the asset pack [using the API](<https://developer.android.com/guide/playcore/asset-delivery/integrate-unity?hl=en#configure-asset-packs-api>).

At runtime, use the [Play Asset Delivery for Unity](<https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetDelivery>) class to retrieve an AssetBundle packaged in an asset pack.

### Prerequisites

1. Set up your development environment:

### OpenUPM-CLI

If you have the [OpenUPM CLI](<https://github.com/openupm/openupm-cli#installation>) installed you can install the OpenUPM registry with the following command:

```bash
openupm add com.google.play.assetdelivery
```

### OpenUPM

1. Open the [package manager settings](<https://docs.unity3d.com/Manual/class-PackageManager.html>) by selecting the Unity menu option **Edit > Project Settings > Package Manager**.
2. Add OpenUPM as a scoped registry to the Package Manager window:

   ```text
   Name: package.openupm.com
   URL: https://package.openupm.com
   Scopes: com.google.external-dependency-manager
     com.google.play.common
     com.google.play.core
     com.google.play.assetdelivery
     com.google.android.appbundle
   ```
3. Open the [package manager menu](<https://docs.unity3d.com/Manual/upm-ui-install.html>) by selecting the Unity menu option **Window > Package Manager**.
4. Set the manager scope drop-down to select **My Registries**.
5. Select the **Google Play Integrity plugin for Unity** package from the package list and press **Install**.

### Import from GitHub

1. Download the latest [`.unitypackage`](<https://github.com/google/play-asset-delivery-unity/releases/latest>) release from GitHub.
2. Import the `.unitypackage` file by selecting the Unity menu option **Assets > Import package > Custom Package** and importing all items.

> **Note:** By downloading and using Google Play Unity Plugins, you agree to the [Play Core Software Development Kit Terms of Service](<https://developer.android.com/guide/playcore#license>).

1. [Create AssetBundles in Unity](<https://docs.unity3d.com/Manual/AssetBundles-Workflow.html>).

   > **Note:** You can use the [Unity AssetBundle Browser](<https://docs.unity3d.com/Packages/com.unity.assetbundlebrowser@1.7/manual/index.html>) to create and manage AssetBundles in your Unity project.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity).
