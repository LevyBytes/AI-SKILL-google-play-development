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
9. (Optional) If you plan to use fast-follow and on-demand delivery, include the [Play Asset Delivery Library](<https://developer.android.com/guide/playcore#java-kotlin-asset-delivery>):

   **Groovy**

   ```groovy
   implementation "com.google.android.play:asset-delivery:2.3.0"
   // For Kotlin use asset-delivery-ktx
   implementation "com.google.android.play:asset-delivery-ktx:2.3.0"
   ```

   **Kotlin**

   ```kotlin
   implementation("com.google.android.play:asset-delivery:2.3.0")
   // For Kotlin use core-ktx
   implementation("com.google.android.play:asset-delivery-ktx:2.3.0")
   ```
10. (Optional) Configure your app bundle to support different [texture compression formats](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression>).

> **Note:** You must run your app as an app bundle rather than as a standalone APK to access the bundled assets. Or, you can edit the default run or debug configuration to deliver the app as an APK rather than a bundle. See [Build and test your Android App Bundle](<https://developer.android.com/guide/app-bundle/test#deploy-using-studio>).

## Integrate with the Play Asset Delivery API

The [Play Asset Delivery Java API](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/package-summary>) provides the [`AssetPackManager`](<https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager>) class for requesting asset packs, managing downloads, and accessing the assets. Make sure to [Add the Play Asset Delivery Library](<https://developer.android.com/guide/playcore#java-kotlin-asset-delivery>) into your project first.

You implement this API according to the delivery type of the asset pack you want to access. These steps are shown in the following flowchart.

> **Note:** You use a different API to access `install-time` asset packs than `fast-follow` and `on-demand` asset packs.

![Asset pack flow diagram for the Java programming language](<https://developer.android.com/static/images/app-bundle/asset-pack-flow-java.png>)

**Figure 1.** Flow diagram for accessing asset packs.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/integrate-java).
