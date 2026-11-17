*Textures* are images that can be applied to the surface of a 3D model. Textures are also used by 2D renderers to draw elements such as sprites or backgrounds. This page describes popular texture compression formats used in games and how to target them in Android App Bundles. Read [About Android App Bundles](<https://developer.android.com/guide/app-bundle>) and [Play Asset Delivery](<https://developer.android.com/guide/playcore/asset-delivery>) before starting this guide.

## Background

GPUs typically support a set of texture compression formats. A texture compression format (or TCF) is a file format that is optimized for GPUs. The GPU loads and renders a texture quicker, and with less memory, than if it were using an array of RGBA values in memory. This support is done at the hardware level: the GPU manufacturer embeds components into the graphic cards chip that read, decompress, and render the supported formats.

The following are common texture compression formats on modern mobile hardware:

- ASTC: Recent format designed to supersede prior formats. More flexible than previous formats due to support for various block sizes. Using this format is a good way to optimize the size of your game.
- ETC2: Supported by all devices that support OpenGL ES 3.0 and higher. This includes nearly all active Android mobile devices.

These formats are supported by the following approximate percentages of Android devices:

| Texture compression format | Percentage of Google Play devices with support |
| --- | --- |
| ASTC | >80% |
| ETC2 | >95% |

Desktop computer GPUs running Google Play Games for PC also support this format:

- DDS or S3TC: Sometimes called BCn, DXTC or DXT*n*.

Older, no longer recommended texture compression formats include:

- ETC1: Supported on most devices. This format has no transparency support, but games can use a second texture file for the alpha component.
- PVRTC: Popular with iOS games, and also supported on some Android devices.

ETC1 support is only a requirement for games supporting very old legacy devices or select Android TV devices which don't support OpenGL ES 3.0 and higher.

### A default format

With so many available formats (with varying levels of device support), you may not know which formats to use when building your game textures. As a safeguard, the app bundle format lets you select a default texture compression format for each asset pack. If a device does not support the other specified formats, assets using this default format are installed.

Unless you are targeting very old device hardware, ETC2 is a good choice for a default format. Use the ETC2 formats [supported in OpenGL ES 3.0](<https://en.wikipedia.org/wiki/Ericsson_Texture_Compression>). These formats are also available in the Vulkan graphics API.

> **Note:** Some game engines transcode the textures in memory if the format is not supported on the device. For example, consider a game bundled with ETC2 as the default format and no ETC1 support. Devices that support only ETC1 are still be able to run the game, but with slower loading times and performance. Refer to your game engine's documentation to verify if this transcoding is done and if it is acceptable for your use case. As an example, Unity decompresses the texture at runtime to a fallback format for older devices that don't support it. For more information, see the [Unity documentation](<https://docs.unity3d.com/2020.2/Documentation/Manual/class-TextureImporterOverride.html#notes-on-android>).

### Recommended formats

The ASTC format defines a variety of compression block sizes, which allow you to selectively trade reduced image quality for greater compression. Depending on the nature of the source art material, for a given texture you may choose a smaller or larger block size to maintain acceptable visual quality.

If your game supports Google Play Games for PC and uses Vulkan, you should include S3TC textures. The S3TC formats are supported by all desktop GPUs.

## Build an app bundle

Google Play uses Android App Bundles to generate and serve optimized APKs for each user's device configuration, so users download only the code and resources they need to run your game. These optimized APKs include a single set of texture assets, formatted with the optimal compression format for the device.

If your game is not in Unity, [use Gradle](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression?hl=en#use-gradle>) to build an app bundle. Advanced users may want to [use `bundletool`](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression?hl=en#use-bundletool>).

If your game is in Unity, support for app bundles with Play Asset Delivery is available in Unity 2021.3 and higher. For more information, see the [Unity documentation](<https://docs.unity3d.com/2022.3/Documentation/Manual/play-asset-delivery.html>). You can [use a Unity plugin](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression?hl=en#unity-plugin>) to build an app bundle with lower versions of Unity.

### Use Gradle

1. Update the version of the Android Gradle plugin in your project's `build.gradle` file to 4.1 or higher (for example, `com.android.tools.build:gradle:4.1.0`).
2. Determine the set of device types that you want to target for your game and the texture compression formats they support (for more information on formats, see [Background](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression?hl=en#background>)).
3. Build versions of your assets for each texture compression format from the previous step. This could involve generating sprite sheets using software like [TexturePacker](<https://www.codeandweb.com/texturepacker>), or running a script that converts raw assets into those with a specific format (for example, [astc-encoder](<https://github.com/ARM-software/astc-encoder>)).
4. Create [asset packs](<https://developer.android.com/guide/playcore/asset-delivery>) (see [Build for C++ or Java](<https://developer.android.com/guide/playcore/asset-delivery/integrate-java>)), which contain your game assets and are used by Play Asset Delivery. For example, you can create one asset pack per level or asset packs for different parts of your game.

   > **Note:** You don't need to use Play Asset Delivery APIs inside your game if you select the `install-time` delivery type for your asset packs. These asset packs are installed at the same time as the main application APK.
5. Inside your asset packs, add directories for each texture compression format that you want to support. Add [supported suffixes](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression?hl=en#supported-suffixes>) to the texture directory names that correspond to the texture compression format used for the contained files.

   Create a directory with no suffix in its name (for example, `common/src/main/assets/textures/`). In this directory, place the default format of your texture assets. This default format should be supported by most devices (for example, ETC1 or ETC2). If a device does not support the other specified formats (for example, PVRTC and ASTC in the table below), the Google Play Store installs this directory instead.

   > **Note:** You decide what content goes into this directory. In most cases, the files in this directory should be the same as in the other directories, differing only by the texture format. However, some formats may require additional support files. For example, textures in the ETC1 format may have an extra file to support alpha channel. Verify how your game or game engine loads textures to determine the optimal file organization.

   | Directory before | Directory after |
   | --- | --- |
   | `common` **asset pack**: <br> common/build.gradle <br> common/src/main/assets/textures/... | `common` **asset pack**: <br> common/build.gradle <br> common/src/main/assets/textures/... <br> common/src/main/assets/textures#tcf_astc/... <br> common/src/main/assets/textures#tcf_pvrtc/... <br> |
   | `level1` **asset pack**: <br> level1/build.gradle <br> level1/src/main/assets/textures/... | `level1` **asset pack**: <br> level1/build.gradle <br> level1/src/main/assets/textures/... <br> level1/src/main/assets/textures#tcf_astc/... <br> level1/src/main/assets/textures#tcf_pvrtc/... <br> |
   | `level2` **asset pack**: <br> level2/build.gradle <br> level2/src/main/assets/textures/... | `level2` **asset pack**: <br> level2/build.gradle <br> level2/src/main/assets/textures/... <br> level2/src/main/assets/textures#tcf_astc/... <br> level2/src/main/assets/textures#tcf_pvrtc/... <br> |
6. Update your app's `build.gradle` file to **enable the splitting of your asset packs per textures**.

   ```groovy
   // In the app build.gradle file:
   android {
       ...
       bundle {
           texture {
               enableSplit true
           }
       }
   }
   ```
7. In Android Studio, select **Build > Generate Signed Bundle / APK**, or launch the [Gradle task from the command line](<https://developer.android.com/build/building-cmdline>) to generate your bundle.

   > **Note:** When APKs (to be installed on a device) are generated from the app bundle, the suffixes (for example, `#tcf_xxx`) are removed from the directory names. Your game only has to read files from a well-known directory name (for example, `level1/assets/textures`). Some game engines can detect the format of a file, so your game can be indifferent about which format of game assets are installed.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/texture-compression).
