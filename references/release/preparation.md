> Android developer verification links individuals and organizations to their Android apps. Check the applicable registration requirements and rollout in the [Android developer verification guides](<https://developer.android.com/developer-verification/guides>) before preparing distribution to certified Android devices.

To prepare your app for release, you need to configure, build, and test a release version of your app. The configuration tasks involve basic code cleanup and code modification tasks that help optimize your app. The build process is similar to the debug build process and can be done using JDK and Android SDK tools.

Testing tasks serve as a final check, helping ensure that your app performs as expected under real-world conditions. Firebase offers a large set of both physical and virtual test devices through [Firebase Test Lab](<https://firebase.google.com/products/test-lab>) that you can use to improve your app quality.

When you are finished preparing your app for release, you have a signed APK file, which you can distribute directly to users or distribute through an app marketplace such as [Google Play](<https://play.google.com>).

This document summarizes the main tasks you need to perform to prepare your app for release. The tasks include [build settings](build-settings.md) and [release readiness](readiness.md) and apply to all Android apps, regardless of how they are released or distributed to users. If you are releasing your app through Google Play, read [Release with confidence](<https://developer.android.com/distribute/best-practices/launch/launch-checklist>).

**Note:** As a best practice, make sure your app meets all of your release criteria for functionality, performance, and stability before you perform the tasks in this release preparation guide.

![Shows how the preparation process fits into the development process](<https://developer.android.com/static/images/publishing/publishing_overview_prep.png>)

**Figure 1.** Preparing for release is a required development task and is the first step in the publishing process.

## Tasks to prepare for release

To release your app to users, you need to create a release-ready package that users can install and run on their Android-powered devices. The release-ready package contains the same components as the debug APK file (compiled source code, resources, manifest file, and so on) and is built using the same build tools. However, unlike the debug APK file, the release-ready APK file is signed with your own certificate and is optimized with the `zipalign` tool.

![Shows the five tasks you perform to prepare your app for release](<https://developer.android.com/static/images/publishing/publishing_preparing.png>)

**Figure 2.** There are five main tasks to prepare your app for release.

The signing and optimization tasks are usually seamless if you are building your app with Android Studio. For example, you can use Android Studio with the Gradle build files to compile, sign, and optimize your app all at once. You can also configure the Gradle build files to do the same when you build from the command line. For more details about using the Gradle build files, see [Configure your build](<https://developer.android.com/studio/build>).

To prepare your app for release, you typically perform five main tasks, as shown in figure 2. Each main task may include one or more smaller tasks, depending on how you are releasing your app. For example, if you are releasing your app through Google Play, you may want to add special filtering rules to your manifest while you are configuring your app for release. Similarly, to meet Google Play publishing guidelines you may have to prepare screenshots and create promotional text while you are gathering materials for release.

You usually perform the tasks listed in figure 2 after you have thoroughly debugged and tested your app. The Android SDK contains several tools to help you test and debug your Android apps. For more information, see [Debug your app](<https://developer.android.com/tools/debugging>) and [Test your app](<https://developer.android.com/tools/testing>).

## Gather materials and resources

To prepare your app for release, you need to gather several supporting items. At a minimum, this includes cryptographic keys for signing your app and an app icon. You might also want to include an end-user license agreement.

### Cryptographic keys

Android requires every APK to be digitally signed with a certificate before installation or update. New [Google Play Store](<https://play.google.com>) apps must use [Play App Signing](<https://developer.android.com/studio/publish/app-signing#app-signing-google-play>); legacy self-signing is available only to apps that meet the documented exemption. Uploading an AAB to Play Console still requires signing it with your developer certificate. Whether using Play App Signing or an eligible self-signing path, sign the app before uploading it.

To learn about certificate requirements, see [Sign your app](<https://developer.android.com/tools/publishing/app-signing>).

**Important:** Your cryptographic key must satisfy [Google Play's required minimum signing-key expiration](<https://developer.android.com/studio/publish/app-signing>). Verify the exact requirement before creating the release key.

You might also have to obtain other release keys if your app accesses a service or uses a third-party library that requires you to use a key that is based on your private key.

### App icon

Your app's icon helps users identify your app on a device's Home screen and in the Launcher window. It also appears in Manage Applications, My Downloads, and elsewhere. In addition, publishing services such as Google Play display your icon to users. Be sure you have an app icon and that it meets the recommended [icon guidelines](<https://material.io/design/iconography/product-icons.html#design-principles>).

**Note:** If you are releasing your app on Google Play, you need to create a high-resolution version of your icon. See [Add preview assets to showcase your app](<https://www.google.com/support/androidmarket/developer/bin/answer.py?answer=1078870>) for more information.

### End-user license agreement

Consider preparing an end-user license agreement (EULA) for your app. A EULA can help protect your person, organization, and intellectual property, and we recommend that you provide one with your app.

### Miscellaneous materials

You might also have to prepare promotional and marketing materials to publicize your app. For example, if you are releasing your app on Google Play, you will need to prepare some promotional text and you will need to create screenshots of your app. For more information, see [Add preview assets to showcase your app](<https://www.google.com/support/androidmarket/developer/bin/answer.py?answer=1078870>).

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/preparing).
