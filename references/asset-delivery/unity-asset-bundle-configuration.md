### Configure AssetBundles using the UI

1. Configure each AssetBundle in an asset pack:

   1. Select **Google > Android App Bundle > Asset Delivery Settings**.
   2. To select folders that directly contain AssetBundle files, click **Add Folder**.

   ![Asset Delivery Settings Add Folder button in Unity](<https://developer.android.com/static/images/app-bundle/unity-add-assetbundle-folder.png>)
2. For each bundle, change the **Delivery Mode** to **Install Time**, **Fast Follow**, or **On Demand**. Resolve any errors or dependencies and close the window.

   ![Asset Delivery delivery mode selector per bundle in Unity](<https://developer.android.com/static/images/app-bundle/unity-asset-delivery-method-per-bundle.png>)
3. Select **Google > Build Android App Bundle** to build the app bundle.
4. (Optional) Configure your app bundle to support different [texture compression formats](<https://developer.android.com/guide/playcore/asset-delivery/texture-compression>).

### Configure asset packs using the API

You can configure asset delivery through editor scripts which can be run as part of an automated build system.

Use the [`AssetPackConfig`](<https://developer.android.com/reference/unity/class/Google/Android/AppBundle/Editor/AssetPackConfig>) class to define which assets to include in an Android App Bundle build, as well as the delivery mode of the assets. These asset packs don't need to contain an AssetBundle.

```c#
public void ConfigureAssetPacks {
   // Creates an AssetPackConfig with a single asset pack, named
   // examplePackName, containing all the files in path/to/exampleFolder.
   var assetPackConfig = new AssetPackConfig();
   assetPackConfig.AddAssetsFolder("examplePackName",
                                   "path/to/exampleFolder",
                                   AssetPackDeliveryMode.OnDemand);

   // Configures the build system to use the newly created assetPackConfig when
   // calling Google > Build and Run or Google > Build Android App Bundle.
   AssetPackConfigSerializer.SaveConfig(assetPackConfig);

   // Alternatively, use BundleTool.BuildBundle to build an App Bundle from script.
   BuildBundle(new buildPlayerOptions(), assetPackConfig);
}
```

You can also use the static [`BuildBundle`](<https://developer.android.com/reference/unity/class/Google/Android/AppBundle/Editor/Bundletool#classGoogle_1_1Android_1_1AppBundle_1_1Editor_1_1Bundletool_1a419f1884fceff86fad1175c0546b85e8>) method in the `Bundletool` class to generate an Android App Bundle with asset packs, given [BuildPlayerOptions](<https://docs.unity3d.com/ScriptReference/BuildPlayerOptions.html>) and [`AssetPackConfig`](<https://developer.android.com/reference/unity/class/Google/Android/AppBundle/Editor/AssetPackConfig>).

For a guided tutorial, see the [Using Play Asset Delivery in Unity games Codelab](<https://codelabs.developers.google.com/codelabs/unity-gamepad>).

### Integrate with Play Asset Delivery Unity API

The [Play Asset Delivery Unity API](<https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetDelivery>) provides the functionality for requesting asset packs, managing downloads, and accessing the assets. Make sure to [Add the Unity plugin](<https://developer.android.com/guide/playcore/asset-delivery/integrate-unity?hl=en#prerequisites>) into your project first.

The functions you use in the API depend on how you created the asset packs.

If you [created asset packs using the plugin UI](<https://developer.android.com/guide/playcore/asset-delivery/integrate-unity#configure-assetbundles-ui>), select **Plugin-configured asset packs**.

If you [created asset packs using the API (or plugin UI)](<https://developer.android.com/guide/playcore/asset-delivery/integrate-unity#configure-asset-packs-api>), select **API-configured asset packs**.

## Next steps

[Test asset delivery](<https://developer.android.com/guide/playcore/asset-delivery/test>) locally and from Google Play.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity).
