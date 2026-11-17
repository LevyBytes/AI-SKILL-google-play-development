The Google Play Billing plugin extends Unity's built-in services and assets for in-app purchases, called [Unity IAP](<https://docs.unity3d.com/Manual/UnityIAP.html>), to provide your game with all the latest features of the Google Play Billing Library. This guide explains how to set up your project to use the plugin. This guide also describes how to implement Google Play Billing Library features in your game in Unity.

### Set up the Google Play Billing plugin

To set up the plugin, complete the steps in each of these linked sections:

1. [Enable the Unity IAP abstraction layer](<https://developer.android.com/google/play/billing/unity?hl=en#abstraction-layer>).
2. [Download and import the plugin](<https://developer.android.com/google/play/billing/unity?hl=en#import-plugin>).
3. [Configure the plugin's build settings](<https://developer.android.com/google/play/billing/unity?hl=en#plugin-build-settings>).
4. [Enable the plugin](<https://developer.android.com/google/play/billing/unity?hl=en#enable-plugin>).

#### Enable the Unity IAP abstraction layer

The Google Play Billing plugin is built on an abstraction layer included with Unity IAP, so you need to enable this abstraction layer before you download and import the plugin. To enable the Unity IAP abstraction layer, do the following:

1. Complete all the steps in the following Unity tutorial: [Set up your project for Unity Services](<https://docs.unity3d.com/Manual/SettingUpProjectServices.html>).
2. Complete all the steps in the following Unity tutorial: [Enable the Unity IAP service](<https://docs.unity3d.com/Manual/UnityIAPSettingUp.html>).

#### Download and import the plugin

The plugin is shipped as a Unity package in the `.unitypackage` format. To download and import the plugin, follow these steps:

1. Download the latest release of the Google Play Plugins for Unity from the repository's [releases page on GitHub](<https://github.com/google/play-unity-plugins/releases>).
2. From the Unity menu bar, click **Assets > Import Package > Custom Package**.

   ![Image](<https://developer.android.com/static/images/google/play/billing/unity-import-custom-package.png>)
3. Locate where you downloaded the `.unitypackage` file and select it.
4. In the **Import Unity Package** dialog, leave all assets selected and click **Import**.

   ![Image](<https://developer.android.com/static/images/google/play/billing/import-unity-package.png>)

After the package imports, a new folder called **GooglePlayPlugins** (at the root of the Assets folder) is added to your project's assets. This folder contains all of the Google Play Billing Library assets for the plugin.

#### Configure build settings

Because the plugin extends Unity IAP, Unity will encounter conflicts and fail to build an Android APK unless some older, overlapping dependencies in Unity IAP are removed from the build. The plugin provides an automatic way to remove the conflicting libraries from your project. To resolve these conflicts, follow these steps:

1. From the Unity menu bar, select **Google > Play Billing > Build Settings**.

   ![Image](<https://developer.android.com/static/images/google/play/billing/unity-plugin-build-settings.png>)
2. In the Play Billing Build Settings window, click **Fix**. This resolves the conflict and moves the conflicting Unity IAP files to a backup directory. After you click **Fix**, the button changes to **Restore**, which you can click to restore the original, conflicting files.

   ![Image](<https://developer.android.com/static/images/google/play/billing/unity-resolve-plugin-conflicts.png>)

#### Enable the plugin

To enable the plugin, replace Unity IAP’s implementation of Google Play with the Google Play Billing plugin. For example, when using the [Unity IAP Purchaser Script](<https://learn.unity.com/tutorial/unity-iap#5c7f8528edbc2a002053b46e>), you would change the `StandardPurchaseModule` that's passed into the IAP builder to use the `Google.Play.Billing.GooglePlayStoreModule`:

```c#
// Create a builder using the GooglePlayStoreModule.
var configurationBuilder =
    ConfigurationBuilder.Instance(Google.Play.Billing.GooglePlayStoreModule.Instance());
```

> **Note:** To avoid any potential conflicts with Unity's standard IAP implementation, you should fully specify the namespace by including `Google.Play.Billing` whenever your code refers to the public classes in Google Play Billing plugin. All of the code examples in this guide use this approach.

If your game uses the same Purchaser Script for multiple platforms, then you should add a platform check to make sure that Unity will continue to use its own IAP solution for other platforms:

```c#
ConfigurationBuilder builder;
if (Application.platform == RuntimePlatform.Android)
{
  builder = ConfigurationBuilder.Instance(
      Google.Play.Billing.GooglePlayStoreModule.Instance());
}
else
{
  builder = ConfigurationBuilder.Instance(StandardPurchasingModule.Instance());
}
```

If you publish your game on other Android app stores besides the Google Play Store, then you should replace the default Unity IAP implementation only when you’re selecting the Google Play Store:

```c#
ConfigurationBuilder builder;
if (Application.platform == RuntimePlatform.Android
       && SelectedAndoidAppStore == AppStore.GooglePlay)
{
  builder = ConfigurationBuilder.Instance(
      Google.Play.Billing.GooglePlayStoreModule.Instance());
}
else
{
  builder = ConfigurationBuilder.Instance(StandardPurchasingModule.Instance());
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/unity).
