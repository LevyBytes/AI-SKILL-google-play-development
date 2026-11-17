This guide shows you how to set up your native Android project to use the Play Integrity API from C or C++. Before you can make calls to the API, you must first integrate the Play Core Native SDK by configuring your development environment and updating your `build.gradle` and `CMakeLists.txt` files as shown in the following section. For more details see our [Native API Reference](<https://developer.android.com/reference/native/play/core/group/integrity>).

## Download Play Core Native SDK

Before downloading, you must agree to the following terms and conditions.

Review and accept the [SDK terms and conditions](<https://developer.android.com/guide/playcore/license>) before downloading or using the SDK.

[Download Play Core Native SDK](<https://dl.google.com/games/play/core/play-core-native-sdk-1.16.0.zip>)

*play-core-native-sdk-1.16.0.zip*

1. Do either of the following:

   - Install [Android Studio](<https://developer.android.com/studio>) version 4.0 or higher. Use the SDK Manager UI to install Android SDK Platform version 10.0 (API level 29).
   - Install the [Android SDK command-line tools](<https://developer.android.com/studio#command-tools>) and use [`sdkmanager`](<https://developer.android.com/studio/command-line/sdkmanager>) to install Android SDK Platform version 10.0 (API level 29).
2. Prepare Android Studio for native development by using the [SDK Manager](<https://developer.android.com/studio/intro/update#sdk-manager>) to install the latest CMake and Android Native Development Kit (NDK). For more information on creating or importing native projects, see [Getting Started with the NDK](<https://developer.android.com/ndk/guides>).
3. Download the zip file and extract it alongside your project.

   | Download Link | Size | SHA-256 Checksum |
   | --- | --- | --- |
   |  | 54.8 MiB | 008b8fedc6179a6dc6ccc21af75591afc7036f78f3d5559d844f1b923934fef0 |
4. Update your app’s `build.gradle` file as shown below:

   **Groovy**

   [Complete groovy example: Groovy](<https://developer.android.com/google/play/integrity/native-setup#groovy>).

   **Kotlin**

   [Complete kotlin example: Kotlin](<https://developer.android.com/google/play/integrity/native-setup#kts>).
5. Update your app’s `CMakeLists.txt` files as shown below:

   ```text

   cmake_minimum_required(VERSION 3.6)

   ...

   # Add a static library called “playcore” built with the c++_static STL.
   include(${PLAYCORE_LOCATION}/playcore.cmake)
   add_playcore_static_library()

   // In this example “main” is your native code library, i.e. libmain.so.
   add_library(main SHARED
           ...)

   target_include_directories(main PRIVATE
           ${PLAYCORE_LOCATION}/include
           ...)

   target_link_libraries(main
           android
           playcore
           ...)
   ```

## Data Collection

The Play Core Native SDK may collect version related data to allow Google to improve the product, including:

- App’s package name
- App’s package version
- Play Core Native SDK's version

This data will be collected when you upload [your app package](<https://developer.android.com/studio/publish/upload-bundle>) to the Play Console. To opt-out of this data collection process, remove the `$playcoreDir/playcore-native-metadata.jar` import in the build.gradle file.

Note, this data collection related to your use of the Play Core Native SDK and Google’s use of the collected data is separate and independent of Google’s collection of library dependencies declared in Gradle when you upload your app package to the Play Console.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/native-setup).
