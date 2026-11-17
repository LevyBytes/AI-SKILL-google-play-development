Use the steps in this guide to access your app's asset packs from your C and C++ code.

Sample [integration code](<https://github.com/android/app-bundle-samples/tree/main/PlayAssetDelivery/NativeSample>) is available on GitHub.

## Build for Native

Use the following steps to build Play Asset Delivery into your project's Android App Bundle. You don't need to use Android Studio to perform these steps.

> **Note:** For a guided tutorial, see the [Using Play Asset Delivery in Native games Codelab](<https://codelabs.developers.google.com/codelabs/native-gamepad>).

1. Update the version of the Android Gradle plugin in your project's `build.gradle` file to `4.0.0` or later.
2. In the top-level directory of your project, create a directory for the asset pack. This directory name is used as the asset pack name. Asset pack names must start with a letter and can only contain letters, numbers, and underscores.
3. In the asset pack directory, create a `build.gradle` file and add the following code. Make sure to specify the name of the asset pack and only one delivery type:

   ```groovy
   // In the asset pack's build.gradle file:
   plugins {
       id 'com.android.asset-pack'
   }

   assetPack {
       packName = "asset-pack-name" // Directory name for the asset pack
       dynamicDelivery {
           deliveryType = "[ install-time | fast-follow | on-demand ]"
       }
   }
   ```
4. In the project's app `build.gradle` file, add the name of every asset pack in your project as shown below:

   ```groovy
   // In the app build.gradle file:
   android {
       ...
       assetPacks = [":asset-pack-name", ":asset-pack2-name"]
   }
   ```
5. In the project's `settings.gradle` file, include all asset packs in your project as shown below:

   ```groovy
   // In the settings.gradle file:
   include ':app'
   include ':asset-pack-name'
   include ':asset-pack2-name'
   ```
6. In the asset pack directory, create the following subdirectory: `src/main/assets`.
7. Place assets in the `src/main/assets` directory. You can create subdirectories in here as well. The directory structure for your app should now look like the following:

   - `build.gradle`
   - `settings.gradle`
   - `app/`
   - `asset-pack-name/build.gradle`
   - `asset-pack-name/src/main/assets/your-asset-directories`
8. [Build the Android App Bundle with Gradle](<https://developer.android.com/build/building-cmdline#build_bundle>). In the generated app bundle, the root-level directory now includes the following:

   - `asset-pack-name/manifest/AndroidManifest.xml`: Configures the asset pack's identifier and delivery mode
   - `asset-pack-name/assets/your-asset-directories`: Directory that contains all assets delivered as part of the asset pack

   Gradle generates the manifest for each asset pack and outputs the `assets/` directory for you.
9. (Optional) Configure your app bundle to support different [texture compression formats](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression>).

## Integrate with Play Asset Delivery Library

You implement this API according to the delivery type of the asset pack you want to access. These steps are shown in the following flowchart.

> **Note:** You use a different API to access `install-time` asset packs than `fast-follow` and `on-demand` asset packs.

![Asset pack flow diagram for native code](<https://developer.android.com/static/images/app-bundle/asset-pack-flow-native.png>)

**Figure 1.** Flow diagram for accessing asset packs.

The [Play Core Native SDK](<https://developer.android.com/reference/native/play/core>) provides the C header file `play/asset_pack.h` for requesting asset packs, managing downloads, and accessing the assets.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/integrate-native).
