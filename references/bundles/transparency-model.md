Code transparency is an optional code signing and verification mechanism for apps published with the Android App Bundle. It uses a code transparency signing key, which is solely held by the app developer.

Code transparency is independent of the signing scheme used for app bundles and APKs. The code transparency key is separate and different from the app signing key that is stored on Google's secure infrastructure when using [Play App Signing](<https://developer.android.com/studio/publish/app-signing#app-signing-google-play>).

## How code transparency works

The process works by including a code transparency file in the bundle after it has been built, but before it is uploaded to Play Console for distribution.

The code transparency file is a JSON Web Token (JWT) that contains a list of DEX files and native libraries included in the bundle, and their hashes. It is then signed using the code transparency key that is held only by the developer.

![Code transparency diagram](<https://developer.android.com/static/images/app-bundle/code_transparency_diagram.png>)

This code transparency file is propagated to the base APK built from the app bundle (specifically to the main split of the base module). It can then be verified that:

- All DEX and native code files present in the APKs have matching hashes in the code transparency file.
- The public key component of the code transparency signing key in the app matches the public key of the developer (which must be provided by the developer over a separate, secure channel).

Together, this information verifies that the code contained in the APKs matches what the developer had intended, and that it has not been modified.

The code transparency file does not verify resources, assets, the Android Manifest, or any other files that are not DEX files or native libraries contained in the `lib/` folder.

> **Important:** The Android OS does not verify code transparency files at install time, and continues to rely on the [APK signing schemes](<https://source.android.com/security/apksigning>) for verification of any installed APKs.

Code transparency verification is used solely for the purpose of inspection by developers and end users, who want to ensure that code they're running matches the code that was originally built and signed by the app developer.

## Known limitations

There are certain situations when code transparency cannot be used:

- Apps that specify the [`sharedUserId`](<https://developer.android.com/guide/topics/manifest/manifest-element#uid>) attribute in the manifest. Such applications may share their process with other applications, which makes it difficult to make assurances about the code they're executing.
- Apps using anti-tamper protection or any other service that makes code changes after the code transparency file is generated will cause the code transparency verification to fail.
- Apps that use legacy Multidex on API levels below 21 (Android 5.0) and use feature modules. Code transparency will continue to work when the app is installed by Google Play on Android 5.0+ devices. Code transparency will be disabled on older OS versions.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/app-bundle/code-transparency).
