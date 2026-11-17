## Verify the contents of the app bundle

If you haven't already, [download `bundletool`](<https://github.com/google/bundletool/releases>) from the GitHub repository.

Verify the contents of the output app bundle by building APKs from it and inspecting them:

```text
bundletool build-apks --output=APKS.apks --bundle=MY_BUNDLE.aab
zipinfo APKS.apks
```

The output should be similar to the following:

```text
toc.pb
splits/base-master.apk
splits/base-armeabi_v7a.apk
splits/…
asset-slices/level1-astc.apk
asset-slices/level1-other_tcf.apk
asset-slices/level1-pvrtc.apk
```

These names indicate that the TCF targeting is properly applied. If you extract the contents of a level APK (for example, `asset-slices/level1-astc.apk`), you can verify that *only one* directory named `textures` is present.

## Test the app bundle

Connect a device and install the applicable asset packs:

```text
bundletool install-apks --apks=APKS.apks
```

This command installs only the asset packs that meet the device's specification. These specifications include ABI, screen density, language, and the most applicable texture compression format. This operation simulates what is done by the Google Play Store for your published game.

To verify that the correct asset packs were installed, do any of the following:

- Use the `bundletool extract-apks` command to output the apks installed for your device into a directory and then inspect this directory.

  1. Extract the specification of your device:

     ```text
     bundletool get-device-spec --output=MY_DEVICE_SPEC.json
     ```
  2. Run `bundletool extract-apks` with this device specification:

     ```text
     bundletool extract-apks --apks=APKS.apks --device-spec=MY_DEVICE_SPEC.json \
         --output-dir out
     ```
  3. List the files in the `out` directory and verify that the proper asset packs are installed. Asset pack names are suffixed by the texture format name (for example, `level1-astc.apk`).
- Add log statements in your game that output the texture format when loading a texture.
- Generate a test set of textures (for example, replace a texture with a single bright color for a given format). Run the game and verify that it is present.

If your app contains `on-demand` or `fast-follow` asset packs, use the [local testing solution for asset delivery](<https://developer.android.com/guide/playcore/asset-delivery/test>).

## Supported suffixes for texture directory names

Google Play understands the following suffixes used in texture directory names:

- `#tcf_astc` for Adaptive Scalable Texture Compression (ASTC)
- `#tcf_atc` for ATI texture compression (ATC)
- `#tcf_dxt1` for S3 DXT1 texture compression (DXT1)
- `#tcf_latc` for Luminance-Alpha texture compression (LATC)
- `#tcf_paletted` for generic paletted texture compression
- `#tcf_pvrtc` for PowerVR texture compression (PVRTC)
- `#tcf_etc1` for Ericsson texture compression (ETC1)
- `#tcf_etc2` for Ericsson texture compression 2 (ETC2)
- `#tcf_s3tc` for S3 texture compression (S3TC)
- `#tcf_3dc` for ATI 3Dc texture compression (3Dc)

## Google Play serving rules

Google Play inspects the OpenGL extension strings used by the device and the OpenGL version supported by the device. Google Play uses this information to determine the correct texture format to deliver to the device from the Android App Bundle.

Google Play delivers the **first format**, in the order listed in the following table, that is supported by the device.

If none of the texture formats in the App Bundle are supported by the device, Google Play delivers the texture formats packaged in the **default format**. (Unless you are targeting specific device hardware, ETC1 or ETC2 are good choices for a default format.) For information on how to package assets in the default format, see [Use bundletool](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression?hl=en#use-bundletool>) or [Use the Google Play Unity plugin](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression?hl=en#unity-plugin>).

If assets have not been packaged in a default format, Google Play marks the app as not available for the device. In this case, users cannot download the app.

| Format (designated in `tcf_xxxx`) | Supported on devices with OpenGL extension string |
| --- | --- |
| astc | `GL_KHR_texture_compression_astc_ldr` |
| pvrtc | `GL_IMG_texture_compression_pvrtc` |
| s3tc | `GL_EXT_texture_compression_s3tc` |
| dxt1 | `GL_EXT_texture_compression_dxt1` |
| latc | `GL_EXT_texture_compression_latc` |
| atc | `GL_AMD_compressed_ATC_texture` |
| 3dc | `GL_AMD_compressed_3DC_texture` |
| etc2 | Not applicable. The device must support OpenGL ES version 3.0 or later. |
| etc1 | `GL_OES_compressed_ETC1_RGB8_texture` |
| paletted | `GL_OES_compressed_paletted_texture` |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/texture-compression).
