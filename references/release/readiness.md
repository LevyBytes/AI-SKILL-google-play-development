### Clean up your project directories

Clean up your project and make sure it conforms to the directory structure described in [Projects overview](<https://developer.android.com/tools/projects#ApplicationProjects>). Leaving stray or orphaned files in your project can prevent your app from compiling and cause your app to behave unpredictably. At a minimum, perform the following cleanup tasks:

- Review the contents of your `cpp/`, `lib/`, and `src/` directories. The `cpp/` directory should contain only source files associated with the [Android NDK](<https://developer.android.com/tools/sdk/ndk>), such as C or C++ source files, header files, or makefiles. The `lib/` directory should contain only third-party library files or private library files, including prebuilt shared and static libraries. The `src/` directory should contain only the source files for your app (Java, Kotlin, and AIDL files). The `src/` directory shouldn't contain any JAR files.
- Check your project for private or proprietary data files that your app doesn't use and remove them. For example, look in your project's `res/` directory for old drawable files, layout files, and values files that you are no longer using and delete them.
- Check your `lib/` directory for test libraries and remove them if they are no longer being used by your app.
- Review the contents of your `assets/` directory and your `res/raw/` directory for raw asset files and static files that you need to update or remove prior to release.

### Review and update your manifest and Gradle build settings

Verify that the following manifest and build files items are set correctly:

- `<uses-permission>` element

  Specify only those permissions that are relevant and required for your app.
- `android:icon` and `android:label` attributes

  You must specify values for these attributes, which are located in the `<application>` element.
- `versionCode` and `versionName` properties

  We recommend that you specify values for these properties, which are located in the app module-level `build.gradle` or `build.gradle.kts` file. For more information, see [Version your app](<https://developer.android.com/tools/publishing/versioning>).

There are several additional build file elements that you can set if you are releasing your app on Google Play. For example, the `minSdk` and `targetSdk` attributes, which are located in the app module-level `build.gradle` or `build.gradle.kts` file. For more information about these and other Google Play settings, see [Filters on Google Play](<https://developer.android.com/google/play/filters>).

### Address compatibility issues

Android provides several tools and techniques to make your app compatible with a wide range of devices. To make your app available to the largest number of users, consider doing the following:

**Add support for multiple screen configurations.**

Make sure you meet the best practices for [supporting multiple screens](<https://developer.android.com/guide/practices/screens_support#screen-independence>). By supporting multiple screen configurations, you can create an app that functions properly and looks good on any of the screen sizes supported by Android.

**Optimize your app for larger displays.**

You can optimize your app to work well on devices with large displays such as tablets and foldables. For example, [list-detail layouts](<https://developer.android.com/guide/topics/large-screens/large-screen-canonical-layouts#list-detail>) can improve usability on larger screens.

**Consider using Jetpack libraries.**

Jetpack is a suite of libraries to help developers follow best practices, reduce boilerplate code, and write code that works consistently across Android versions and devices.

### Update URLs for servers and services

If your app accesses remote servers or services, make sure you are using the production URL or path for the server or service and not a test URL or path.

### Implement licensing for Google Play

If you are releasing a paid app through Google Play, consider adding support for Google Play Licensing. Licensing lets you control access to your app based on whether the current user has purchased it. Using Google Play Licensing is optional, even if you are releasing your app through Google Play.

For more information about the Google Play Licensing Service and how to use it in your app, see [App Licensing](<https://developer.android.com/google/play/licensing>).

## Build your app for release

After you finish configuring your app, you can build it into a release-ready APK file that is signed and optimized. The JDK includes the tools for signing the APK file (Keytool and Jarsigner); the Android SDK includes the tools for compiling and optimizing the APK file. If you are using Android Studio or you are using the Gradle build system from the command line, you can automate the entire build process. For more information about configuring Gradle builds, see [Configure build variants](<https://developer.android.com/tools/building/configuring-gradle>).

If you are using a [continuous integration system](<https://developer.android.com/studio/projects/continuous-integration>), you can configure a task to automate your release process. This is not limited to building your release APK or AAB. You can also configure it to automatically upload the build artifact(s) to Play Console.

### Build with Android Studio

You can use the Gradle build system, integrated with Android Studio, to build a release-ready APK file that is signed with your private key and optimized. To learn how to set up and run builds from Android Studio, see [Build and run your app](<https://developer.android.com/tools/building/building-studio>).

The build process assumes that you have a certificate and private key suitable for signing your app. If you don't have a suitable certificate and private key, Android Studio can help you generate one. For more information about the signing process, see [Sign your app](<https://developer.android.com/tools/publishing/app-signing>).

## Prepare external servers and resources

If your app relies on a remote server, make sure the server is secure and that it is configured for production use. This is particularly important if you are implementing [in-app billing](<https://developer.android.com/google/play/billing>) in your app and you are performing the signature verification step on a remote server.

Also, if your app fetches content from a remote server or a real-time service (such as a content feed), be sure the content you are providing is up to date and production ready.

## Test your app for release

Testing the release version of your app helps ensure that your app runs properly under realistic device and network conditions. Ideally, test your app on at least one handset-sized device and one tablet-sized device to verify that your user interface elements are sized correctly and that your app's performance and battery efficiency are acceptable. [Firebase Test Lab](<https://firebase.google.com/docs/test-lab>) can also be useful for testing across a variety of different devices and Android OS versions.

As a starting point for testing, see [Core app quality](<https://developer.android.com/tools/testing/what_to_test>). When you are done testing and satisfied that the release version of your app behaves correctly, you can release your app to users. For more information, see [Release your app to users](<https://developer.android.com/tools/publishing/publishing_overview#publishing-release>).

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/preparing).
