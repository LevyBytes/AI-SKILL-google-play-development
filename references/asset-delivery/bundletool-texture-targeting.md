### (Advanced) Use bundletool

For more information on `bundletool`, see [Build an app bundle using bundletool](<https://developer.android.com/build/building-cmdline#bundletool-build>).

To create the app bundle, do the following:

1. Download [`bundletool`](<https://github.com/google/bundletool/releases>) from its GitHub repository.
2. Determine the set of device types that you want to target for your game and the texture compression formats they support (for more information on formats, see [Background](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression?hl=en#background>)).
3. Build versions of your assets for each texture compression format from the previous step. This could involve generating sprite sheets using software like [TexturePacker](<https://www.codeandweb.com/texturepacker>), or running a script that converts raw assets into those with a specific format (for example, [astc-encoder](<https://github.com/ARM-software/astc-encoder>)).
4. Create [asset packs](<https://developer.android.com/guide/playcore/asset-delivery>) (see [Build for C++ or Java](<https://developer.android.com/guide/playcore/asset-delivery/integrate-java>)), which contain your game assets and are used by Play Asset Delivery. For example, you can create one asset pack per level or asset packs for different parts of your game.

   > **Note:** You don't need to use Play Asset Delivery APIs inside your game if you select the `install-time` delivery type for your asset packs. These asset packs are installed at the same time as the main application APK.
5. In your different asset packs, add [supported suffixes](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression?hl=en#supported-suffixes>) to the texture directory names that correspond to the texture compression format used for the contained files.

   Create a directory with no suffix in its name (for example, `common/src/main/assets/textures/`). In this directory, place the default format of your texture assets. This default format should be supported by most devices (for example, ETC1 or ETC2). If a device does not support the other specified formats (for example, PVRTC and ASTC in the table below), the Google Play Store installs this directory instead.

   > **Note:** You decide what content goes into this directory. In most cases, the files in this directory should be the same as in the other directories, differing only by the texture format. However, some formats may require additional support files. For example, textures in the ETC1 format may have an extra file to support alpha channel. Verify how your game or game engine loads textures to determine the optimal file organization.

   | Directory before | Directory after |
   | --- | --- |
   | `common` **asset pack**: <br> common/build.gradle <br> common/src/main/assets/textures/... | `common` **asset pack**: <br> common/build.gradle <br> common/src/main/assets/textures/... <br> common/src/main/assets/textures#tcf_astc/... <br> common/src/main/assets/textures#tcf_pvrtc/... <br> |
   | `level1` **asset pack**: <br> level1/build.gradle <br> level1/src/main/assets/textures/... | `level1` **asset pack**: <br> level1/build.gradle <br> level1/src/main/assets/textures/... <br> level1/src/main/assets/textures#tcf_astc/... <br> level1/src/main/assets/textures#tcf_pvrtc/... <br> |
   | `level2` **asset pack**: <br> level2/build.gradle <br> level2/src/main/assets/textures/... | `level2` **asset pack**: <br> level2/build.gradle <br> level2/src/main/assets/textures/... <br> level2/src/main/assets/textures#tcf_astc/... <br> level2/src/main/assets/textures#tcf_pvrtc/... <br> |
6. Add the TCF dimension to the [app bundle metadata file](<https://developer.android.com/build/building-cmdline#bundleconfig>) (`BundleConfig.json`). Use `TEXTURE_COMPRESSION_FORMAT` for the `value` field:

   ```json
   {
     ...
     "optimizations": {
       "splitsConfig": {
         "splitDimension": [
         ...
         {
            "value": "TEXTURE_COMPRESSION_FORMAT",
            "negate": false,
            "suffixStripping": {
              "enabled": true,
              "defaultSuffix": ""
             }
         }],
       }
     }
   }
   ```

   Set `suffixStripping.enabled` to `true` to remove the suffix (for example, `#tcf_astc`) from the directory names when generating the asset packs. This enables your game to read files from a well-known directory name (such as `level1/assets/textures`). Some game engines can detect the format of a file, so your game can be indifferent about the format of texture assets that it was installed with.

   `suffixStripping.defaultSuffix` specifies the default directory suffix when `bundletool` generates a standalone APK for devices running Android 5.0 (API level 21) and lower. In the example table earlier, the default version of the texture assets is installed on these devices; this is the intended behavior in most cases.
7. Build the app bundle:

   ```text
   bundletool build-bundle --config=BUILD_CONFIG.json \
     --modules=level1.zip,level2.zip,common.zip,base.zip --output=MY_BUNDLE.aab
   ```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/texture-compression).
