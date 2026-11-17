## Release through a website

If you don't want to release your app on a marketplace like Google Play, you can make the app available for download on your own website or server, including on a private or enterprise server.

To release through a website:

1. [Prepare your app for release](<https://developer.android.com/tools/publishing/preparing>).
2. Host the release-ready APK file on your website.
3. Provide a download link to users.

When users browse to the download link from their Android-powered devices, the file is downloaded and the Android system automatically starts installing it on the device.

**Note:** The installation process will start automatically only if the user has configured their settings to allow the installation of apps from [unknown sources](<https://developer.android.com/studio/publish?hl=en#unknown-sources>).

Although it is relatively easy to release your app on your own website, it can be inefficient. For example, if you want to monetize your app, you need to process and track all financial transactions yourself, and you can't use Google Play's [in-app billing service](<https://developer.android.com/google/play/billing>) to sell in-app products. You also can't use [app licensing](<https://developer.android.com/google/play/licensing>) to help prevent unauthorized installation and use of your app.

## User opt-in for unknown apps and sources

Android protects users from inadvertent download and installation of apps from locations other than a trusted, first-party app store, such as Google Play. Android blocks such installs until the user opts into allowing the installation of apps from other sources. The opt-in process depends on the version of Android running on the user's device:

![Screenshot showing the settings screen for accepting install of unknown apps from different sources.](<https://developer.android.com/static/images/publishing/publishing_unknown_apps_sm.png>)

**Figure 1.** The **Install unknown apps** system settings screen, where users grant permission for a particular source to install unknown apps.

- On devices running Android 8.0 (API level 26) and higher, users must navigate to the **Install unknown apps** system settings screen to enable app installations from a particular source.
- On devices running Android 7.1.1 (API level 25) and lower, users must either enable the **Unknown sources** system setting or allow a single installation of an unknown app.

### Install unknown apps

On devices running Android 8.0 (API level 26) and higher, users must grant permission to install apps from a source that isn't a first-party app store. To do so, they must enable the **Allow app installs** setting for that source within the **Install unknown apps** system settings screen, shown in figure 1.

**Note:** Users can change this setting for a particular source at any time. Therefore, a source that installs unknown apps should always call ` canRequestPackageInstalls()` to check whether the user has granted that source permission to install unknown apps. If this method returns `false`, the source should prompt the user to re-enable the **Allow app installs** setting for that source.

### Unknown sources

![Screenshot showing the setting for accepting download and install of apps from unknown sources.](<https://developer.android.com/static/images/publishing/publishing_unknown_sources_sm.png>)

**Figure 2.** The **Unknown sources** setting determines whether users can install apps that aren't downloaded from Google Play.

To permit the installation of apps from non-first-party sources on devices running Android 7.1.1 (API level 25) and lower, users enable the **Unknown sources** setting in **Settings > Security**, as shown in Figure 2.

When users attempt to install an unknown app on a device running Android 7.1.1 (API level 25) or lower, the system sometimes shows a dialog that asks the user whether they want to allow only one particular unknown app to be installed. In most cases, it is recommended that users allow only one unknown app installation at a time, if the option is available.

In either case, users need to make this configuration change before they can download and install unknown apps onto their devices.

**Note:** Some network providers don't let users install apps from unknown sources.

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish).
