## Feature module manifest reference

When creating a new feature module using Android Studio, the IDE includes most of the manifest attributes that the module requires to behave like a feature module. Additionally, some attributes are injected by the build system at compile time, so you needn't specify or modify them yourself. The following table describes the manifest attributes that are important to feature modules.

| Attribute | Description |
| --- | --- |
| &lt;manifest | This is a typical [`<manifest>`](<https://developer.android.com/guide/topics/manifest/manifest-element>) block. |
| xmlns:dist="http://schemas.android.com/apk/distribution" | Specifies a new `dist:` XML namespace that's described further below. |
| split="split_name" | When Android Studio builds your app bundle, it includes this attribute for you. So, **you should not include or modify this attribute yourself**. Defines the name of the module, which your app specifies when requesting an on demand module using the Play Feature Delivery Library. <br> **How Gradle determines the value for this attribute:**<br> By default, when you create a feature module using Android Studio, The IDE uses what you specify as its **Module name** to identify the module as a Gradle subproject in your [Gradle settings file](<https://developer.android.com/studio/build#settings-file>). <br> When you build your app bundle, Gradle uses the last element of the subproject path to inject this manifest attribute in the module's manifest. For example, if you create a new feature module in the `MyAppProject/features/` directory and specified "dynamic_feature1" as its **Module name**, the IDE adds `':features:dynamic_feature1'` as a subproject in your `settings.gradle` file. When building your app bundle, Gradle then injects `<manifest split="dynamic_feature1">` in the module's manifest. |
| android:isFeatureSplit="true \| false"&gt; | When Android Studio builds your app bundle, it includes this attribute for you. So, **you should not include or modify this attribute manually**. Specifies that this module is a feature module. Manifests in the base module and configuration APKs either omit this attribute or set it to `false`.  |
| &lt;dist:module | Defines attributes that determine how the module is packaged and distributed as APKs. |
| dist:instant="true \| false" | Specifies whether the module should be available through [Google Play Instant](<https://developer.android.com/topic/google-play-instant/overview>) as an instant experience. If your app includes one or more instant-enabled feature modules, you must also instant-enable the base module. When using Android Studio 3.5 or higher, the IDE does this for you when you [create an instant-enabled feature module](<https://developer.android.com/guide/app-bundle/instant-delivery>).<br> You can't set this XML element to `true` while also setting `<dist:on-demand/>`. However, you can still request on demand downloads of your instant-enabled feature modules *as instant experiences* [using the Play Feature Delivery Library](<https://developer.android.com/guide/playcore#java-kotlin-feature-delivery>). When a user downloads and *installs* your app, the device downloads and installs your app's instant-enabled feature modules, along with the base APK, by default.  |
| dist:title="@string/feature_name"&gt; | Specifies a user-facing title for the module. For example, the device may display this title when it requests download confirmation. You need to include the string resource for this title in the base module's `module_root``/src/``source_set``/res/values/strings.xml` file.  |
| &lt;dist:fusing dist:include="true \| false" /&gt; | Specifies whether to include the module in multi-APKs that target devices running Android 4.4 (API level 20) and lower. Additionally, when you [use `bundletool` to generate APKs from an app bundle](<https://developer.android.com/studio/command-line/bundletool#generate_apks>), only feature modules that set this property to `true` are included in the universal APK, which is a monolithic APK that includes code and resources for all device configurations your app supports.  |
| &lt;dist:delivery&gt; | Encapsulates options that customizes module delivery, as shown below. Keep in mind, each feature module must configure only one type of these custom delivery options. |
| &lt;dist:install-time&gt; | Specifies that the module should be available at install time. This is the default behavior for feature modules that don't specify another type of custom delivery option. To learn more about install-time downloads, read [Configure install-time delivery](<https://developer.android.com/guide/playcore/feature-delivery/install-time>). <br> This node is can also specify conditions that limit the module to devices that meet certain requirements, such as device features, user country, or minimum API level. To learn more, read [Configure conditional delivery](<https://developer.android.com/guide/playcore/feature-delivery/conditional>).  |
| &lt;dist:removable dist:value="true \| false" /&gt; | When unset or set to `false`, bundletool will fuse install-time modules into the base module when generating split APKs from the bundle. Because there will be fewer split APKs as a result of fusing, this setting may improve your app's performance. <br> When `removable` is set to `true`: install-time modules won't be fused into the base module. Set to `true` if you want to uninstall modules in the future. However, configuring too many modules to be removable might increase the install time for your app. <br> Defaults to `false`. It's only necessary to set this value in the manifest if you want to disable fusing for a feature module. <br> **Note:** This feature is only available when using Android Gradle plugin 4.2 or when using bundletool v1.0 from the command line.  |
| &lt;/dist:install-time&gt; |  |
| &lt;dist:on-demand /&gt; | Specifies that the module should be available as an on demand download. That is, the module is not available at install time, but your app may request to download it later. To learn more about on demand downloads, read [Configure on demand delivery](<https://developer.android.com/guide/app-bundle/on-demand-delivery>).  |
| &lt;/dist:delivery&gt; |  |
| &lt;/dist:module&gt; |  |
| &lt;application <br> [android:hasCode](<https://developer.android.com/guide/topics/manifest/application-element#code>)="true \| false"&gt; <br>... <br>&lt;/application&gt; | If the feature module generates no DEX files (that is, it contains no code that is later compiled into the DEX file format), you must do the following (otherwise, you may get runtime errors): Set `android:hasCode` to `"false"` in the feature module's manifest.<br> Add the following to your **base** module's manifest: <br>Complete code example follows this table. <br>  |
| ...<br>&lt;/manifest&gt; |  |

```xml
<application
  android:hasCode="true"
  tools:replace="android:hasCode">
  ...
</application>
```

> **Note:** Feature modules shouldn't specify activities in their manifest with [`android:exported`](<https://developer.android.com/guide/topics/manifest/activity-element#exported>) set to `true`. That's because there's no guarantee that the device has downloaded the feature module when another app tries to launch the activity. Additionally, your app should confirm that a feature is downloaded before trying to access its code and resources. To learn more, read [Manage installed modules](<https://developer.android.com/guide/playcore/feature-delivery/on-demand#manage_installed_modules>).

## Additional resources

To learn more about using feature modules, try the following resources.

### Blog posts

- [Patchwork Plaid: A modularization story](<https://medium.com/androiddevelopers/a-patchwork-plaid-monolith-to-modularized-app-60235d9f212e>)

### Videos

- [Customizable Delivery with the App Bundle and Easy Sharing of Test Builds](<https://www.youtube.com/watch?v=flhib2krW7U>)
- [New Tools to Optimize Your App's Size and Boost Installs on Google Play](<https://www.youtube.com/watch?v=rEuwVWpYBOY>)

## Terms of service and data safety

By accessing or using the Play Feature Delivery Library, you agree to the [Play Core Software Development Kit Terms of Service](<https://developer.android.com/guide/playcore#license>). Read and understand all applicable terms and policies before accessing the library.

## Data Safety

The Play Core libraries are your app's runtime interface with the Google Play Store. As such, when you use Play Core in your app, the Play Store runs its own processes, which include handling data as governed by the [Google Play Terms of Service](<https://play.google.com/about/play-terms/index.html>). The information below describes how the Play Core libraries handle data to process specific requests from your app.

### Additional languages API

| Data collected on usage | List of languages installed |
| --- | --- |
| Purpose of data collection | The data collected is used to deliver different language versions of the app and to preserve installed languages after an app update. |
| Data encryption | Data is encrypted. |
| Data sharing | Data is not transferred to any third parties. |
| Data deletion | Data is deleted following a fixed retention period. |

### Play Feature Delivery

| Data collected on usage | Device metadata<br> Application version |
| --- | --- |
| Purpose of data collection | The data collected is used to serve the right module to the device and to preserve installed modules after an update and backup and restore. |
| Data encryption | Data is encrypted. |
| Data sharing | Data is not transferred to any third parties. |
| Data deletion | Data is deleted following a fixed retention period. |

While we aim to be as transparent as possible, you are solely responsible for deciding how to respond to Google Play's data safety section form regarding your app's user data collection, sharing, and security practices.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery).
