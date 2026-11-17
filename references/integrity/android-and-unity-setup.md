## Integrate Play Integrity API into your app

To integrate the Play Integrity API into your app or SDK, do one of the following depending on your development environment:

### Kotlin or Java

The latest Android library for the Play Integrity API is available from [Google's Maven Repository](<https://maven.google.com/web/index.html#com.google.android.play:integrity>). Add the following dependency to your app's `build.gradle` file:

```groovy
implementation 'com.google.android.play:integrity:1.6.0'
```

### Unity

The following sections describe how to integrate and set up the Google Play Integrity API for Unity projects, covering supported Unity versions, installation methods, and environment setup.

#### Supported Unity versions

- All versions of 2019.x, 2020.x, and newer are supported.
- If you use Unity 2018.x, version 2018.4 or newer are supported.
- Unity 2017.x and older aren't supported.

#### Set up your development environment

##### OpenUPM-CLI

If you have the [OpenUPM CLI](<https://github.com/openupm/openupm-cli#installation>) installed you can install the OpenUPM registry with the following command:

```bash
openupm add com.google.play.integrity
```

##### OpenUPM

1. Open the [package manager settings](<https://docs.unity3d.com/Manual/class-PackageManager.html>) by selecting the Unity menu option **Edit > Project Settings > Package Manager**.
2. Add OpenUPM as a scoped registry to the Package Manager window:

   ```text
   Name: package.openupm.com
   URL: https://package.openupm.com
   Scopes: com.google.external-dependency-manager
     com.google.play.common
     com.google.play.core
     com.google.play.integrity
   ```
3. Open the [package manager menu](<https://docs.unity3d.com/Manual/upm-ui-install.html>) by selecting the Unity menu option **Window > Package Manager**.
4. Set the manager scope drop-down to select **My Registries**.
5. Select the **Google Play Integrity plugin for Unity** package from the package list and press **Install**.

##### Import from GitHub

1. Download the latest [`.unitypackage`](<https://github.com/google/play-integrity-unity/releases/latest>) release from GitHub.
2. Import the `.unitypackage` file by selecting the Unity menu option **Assets > Import package > Custom Package** and importing all items.

> **Note:** By downloading and using Google Play Unity Plugins, you agree to the [Play Core Software Development Kit Terms of Service](<https://developer.android.com/guide/playcore#license>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/setup).
