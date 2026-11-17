### Use the Google Play Unity plugin

[Get the Unity plugin (or package) for Play Asset Delivery](<https://developer.android.com/guide/playcore/asset-delivery/integrate-unity#prerequisites>) to create an app bundle with texture-targeted asset packs.

#### Prepare the assets

To prepare your texture assets for building an app bundle, do the following:

1. Package your scene and assets into multiple Unity [AssetBundles](<https://docs.unity3d.com/Manual/AssetBundlesIntro.html>).

   > **Note:** While the AssetBundle Manager is deprecated for Unity versions 2018.2 and higher, AssetBundles are still supported.
2. Determine the set of device types that you want to target for your game and the texture compression formats they support (for more information on formats, see [Background](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression?hl=en#background>)).
3. Modify your game's build script to generate the AssetBundles multiple times, once for each texture format that you want to support. See the following example script:

   [Complete c# example: Prepare the assets](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression#prepare_the_assets>).
4. Verify that each texture asset is output in a directory with the correct suffix in its name (for example, `#tcf_astc`).

   Verify that a directory with no suffix in its name is output (for example, `Assets/AssetBundles/`). This directory contains the default format of your texture assets. This default format should be supported by most devices (for example, ETC2). If a device does not support the other specified formats (for example, ASTC in the code from the previous step), then the Google Play Store installs this directory instead.

   ```text
   Assets/AssetBundles.meta
   Assets/AssetBundles/AssetBundles
   Assets/AssetBundles/AssetBundles.manifest
   Assets/AssetBundles/AssetBundles.manifest.meta
   Assets/AssetBundles/AssetBundles.meta
   Assets/AssetBundles/samplescene
   Assets/AssetBundles/samplescene.manifest
   Assets/AssetBundles/samplescene.manifest.meta
   Assets/AssetBundles/samplescene.meta
   Assets/AssetBundles/texturesbundle
   Assets/AssetBundles/texturesbundle.manifest
   Assets/AssetBundles/texturesbundle.manifest.meta
   Assets/AssetBundles/texturesbundle.meta
   Assets/AssetBundles#tcf_astc.meta
   Assets/AssetBundles#tcf_astc/AssetBundles
   Assets/AssetBundles#tcf_astc/AssetBundles.manifest
   Assets/AssetBundles#tcf_astc/AssetBundles.manifest.meta
   Assets/AssetBundles#tcf_astc/AssetBundles.meta
   Assets/AssetBundles#tcf_astc/samplescene
   Assets/AssetBundles#tcf_astc/samplescene.manifest
   Assets/AssetBundles#tcf_astc/samplescene.manifest.meta
   Assets/AssetBundles#tcf_astc/samplescene.meta
   Assets/AssetBundles#tcf_astc/texturesbundle
   Assets/AssetBundles#tcf_astc/texturesbundle.manifest
   Assets/AssetBundles#tcf_astc/texturesbundle.manifest.meta
   Assets/AssetBundles#tcf_astc/texturesbundle.meta
   ```
5. Select **Google > Android > Assets Delivery**.
6. Click **Add Folder** to add the folder containing your default asset bundles. These bundles are installed on devices that don't support the other formats you define.

   Make sure to set the **Delivery mode** for the AssetBundle.

   ![Unity AssetBundle Delivery default format](<https://developer.android.com/static/images/app-bundle/unity-asset-bundle-config.svg>)
7. Click **Add Folder** to add a folder containing AssetBundles built for another format (for example, ASTC). Repeat as needed.

   Make sure to set the **Delivery mode** for each AssetBundle.

   ![Unity AssetBundle Delivery ASTC format](<https://developer.android.com/static/images/app-bundle/unity-asset-bundle-config-2.svg>)

#### Build

Select **Google > Build Android App Bundle** to launch the Unity build of your game. It also packages the AssetBundles into multiple asset packs where each AssetBundle name is converted to a single asset pack.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/texture-compression).
