Versioning is a critical component of your app upgrade and maintenance strategy. Versioning is important because:

- Users need to have specific information about the app version that is installed on their devices and the upgrade versions available for installation.
- Other apps, including other apps that you publish as a suite, need to query the system for your app's version to determine compatibility and identify dependencies.
- Services where you publish your app(s) may also need to query your app for its version so that they can display the version to users. A publishing service may also need to check the app version to determine compatibility and establish upgrade/downgrade relationships.

The Android system uses your app's version information to protect against downgrades. The system doesn't use app version information to enforce restrictions on upgrades or compatibility of third-party apps. Your app must enforce any version restrictions and tell users about them.

The Android system enforces system version compatibility, as expressed by the `minSdk` setting in the build files. This setting lets an app specify the minimum system API that it is compatible with. For more information about API requirements, see [Specify API level (SDK version) requirements](<https://developer.android.com/studio/publish/versioning?hl=en#minsdk>).

Versioning requirements vary between different projects. However, many developers consider [Semantic Versioning](<https://semver.org>) a good basis for a versioning strategy.

## Set app version information

To define the version information for your app, set values for the version settings in the Gradle build files:

**Groovy**

```groovy
    android {
      namespace 'com.example.testapp'
      compileSdk 33

      defaultConfig {
          applicationId "com.example.testapp"
          minSdk 24
          targetSdk 33
          versionCode 1
          versionName "1.0"
          ...
      }
      ...
    }
    ...
    
```

**Kotlin**

```kotlin
    android {
      namespace = "com.example.testapp"
      compileSdk = 33

      defaultConfig {
          applicationId = "com.example.testapp"
          minSdk = 24
          targetSdk = 33
          versionCode = 1
          versionName = "1.0"
          ...
      }
      ...
    }
    ...
      
```

### Version settings

Define values for both of the version settings available: `versionCode` and `versionName`.

**`versionCode`**

A positive integer used as an internal version number. This number helps determine whether one version is more recent than another, with higher numbers indicating more recent versions. This is not the version number shown to users; that number is set by the `versionName` setting. The Android system uses the `versionCode` value to protect against downgrades by preventing users from installing an APK with a lower `versionCode` than the version currently installed on their device.

The value is a positive integer so that other apps can programmatically evaluate it to check an upgrade or downgrade relationship, for instance. You can set the value to any positive integer. However, make sure that each successive release of your app uses a greater value.

**Note:** The greatest value Google Play allows for `versionCode` is 2100000000.

You can't upload an APK to the Play Store with a `versionCode` you have already used for a previous version.

**Note:** In some situations, you might want to upload a version of your app with a lower `versionCode` than the most recent version. For example, if you are publishing multiple APKs, you might have pre-set `versionCode` ranges for specific APKs. For more about assigning `versionCode` values for multiple APKs, see [Assigning version codes](<https://developer.android.com/google/play/publishing/multiple-apks#VersionCodes>).

Typically, you release the first version of your app with `versionCode` set to 1, then monotonically increase the value with each release, regardless of whether the release constitutes a major or minor release. This means that the `versionCode` value doesn't necessarily resemble the app release version that is visible to the user. Apps and publishing services shouldn't display this version value to users.

**`versionName`**

A string used as the version number shown to users. This setting can be specified as a raw string or as a reference to a string resource.

The value is a string so that you can describe the app version as a `<major>.<minor>.<point>` string or as any other type of absolute or relative version identifier. The `versionName` is the only value displayed to users.

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/versioning).
