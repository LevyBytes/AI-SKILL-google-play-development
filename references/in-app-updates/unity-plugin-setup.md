This guide describes how to support [in-app updates](<https://developer.android.com/guide/playcore/in-app-updates>) in your app using Unity. There are separate guides for cases where your implementation uses [the Kotlin programming language or the Java programming language](<https://developer.android.com/guide/playcore/in-app-updates/kotlin-java>), and cases where your implementation uses [native code (C/C++)](<https://developer.android.com/guide/playcore/in-app-updates/native>).

## Unity SDK overview

The Play in-app update API is part of the [Play Core SDK](<https://developer.android.com/reference/com/google/android/play/core/release-notes>) family. The Unity Plugin offers an [`AppUpdateManager`](<https://developer.android.com/reference/unity/class/Google/Play/AppUpdate/AppUpdateManager>) class to handle communication between your app and the Google Play API. You must instantiate this class before you can use it to manage in-app updates:

```c#
AppUpdateManager appUpdateManager = new AppUpdateManager();
```

## Set up your development environment

### OpenUPM-CLI

If you have the [OpenUPM CLI](<https://github.com/openupm/openupm-cli#installation>) installed you can install the OpenUPM registry with the following command:

```bash
openupm add com.google.play.appupdate
```

### OpenUPM

1. Open the [package manager settings](<https://docs.unity3d.com/Manual/class-PackageManager.html>) by selecting the Unity menu option **Edit > Project Settings > Package Manager**.
2. Add OpenUPM as a scoped registry to the Package Manager window:

   ```text
   Name: package.openupm.com
   URL: https://package.openupm.com
   Scopes: com.google.external-dependency-manager
     com.google.play.common
     com.google.play.core
     com.google.play.appupdate
   ```
3. Open the [package manager menu](<https://docs.unity3d.com/Manual/upm-ui-install.html>) by selecting the Unity menu option **Window > Package Manager**.
4. Set the manager scope drop-down to select **My Registries**.
5. Select the **Google Play Integrity plugin for Unity** package from the package list and press **Install**.

### Import from GitHub

1. Download the latest [`.unitypackage`](<https://github.com/google/play-in-app-updates-unity/releases/latest>) release from GitHub.
2. Import the `.unitypackage` file by selecting the Unity menu option **Assets > Import package > Custom Package** and importing all items.

> **Note:** By downloading and using Google Play Unity Plugins, you agree to the [Play Core Software Development Kit Terms of Service](<https://developer.android.com/guide/playcore#license>).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/unity).
