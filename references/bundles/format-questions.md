## About Android App Bundles

### What is the Android App Bundle (AAB)?

The Android App Bundle (AAB) is a publishing format for Android that is supported by Google Play and other app stores, and by build tools such as Android Studio, Bazel, Buck, Cocos Creator, Gradle, Unity, and Unreal.

### What's the difference between AABs and APKs?

App bundles are only for publishing and cannot be installed on Android devices. The Android package (APK) is Android's installable, executable format for apps. App bundles must be processed by a distributor into APKs so that they can be installed on devices.

### Is the AAB a proprietary format that can only be used on Google Play?

No, the AAB is not proprietary. The app bundle is [open source](<https://github.com/google/bundletool>), so any app store can support it. Bundles are supported by Google Play and some other app stores.

### Does creating AABs prevent me from publishing to other app stores?

No, you are not prevented from publishing to other app stores. When you build your app, you can build AABs and APKs at the same time depending on what publishing format is required for each app store.

### How much work is required to use an AAB?

For most apps, building an AAB is equivalent effort to building an APK, since it simply involves choosing AAB instead of APK at build time. For some apps, there might be some changes needed to get the full benefits of AABs.

### Are any developers using AABs already?

Yes. Over 1 million apps and games are using app bundles to publish their production releases on Google Play including the majority of popular apps, representing billions of active installs. If you use Google Play to install apps, many of the apps on your device were published as app bundles.

### Does the AAB prevent users from "sideloading" apps?

No, AABs do not prevent users from installing APKs from any source. Since AAB is just a publishing format, they don't change how the Android platform works.

### If a developer uses AABs to deliver optimized APKs, does this mean that it's possible for users who share those APKs to run into issues?

There have always been rare cases on Android when APKs cannot directly transfer from one device to another, regardless of whether the app is published via APKs or AABs. Specifically, when APKs have been optimized for a device (for example, for a specific chip architecture) then transferring those APKs directly to another device may encounter issues if the target device doesn't match the properties of the original device. In these situations, an APK or set of APKs that are appropriate for the target device need to be installed.

### Can I publish to multiple app stores?

Yes, you can publish to multiple app stores whether or not you use AABs. You can publish AABs on Google Play and other app stores that support AABs at the same time as publishing APKs on other app stores or websites that don't support AABs.

### Does the AAB requirement apply to private apps published to managed Google Play?

Yes, private apps published to managed Google Play from Play Console are required to publish AABs.

Publishing APKs is still supported via [Managed Play iframe](<https://developers.google.com/android/work/play/emm-api/managed-play-iframe#private-apps>).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/app-bundle/faq).
