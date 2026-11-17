The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

## Download additional language resources

With app bundles, devices download only the code and resources they require to run your app. So, for language resources, a user’s device downloads only your app’s language resources that match the one or more languages currently selected in the device’s settings.

If you want your app to have access to additional language resources, for example, to implement an in-app language picker, you can use the Play Feature Delivery Library to download them on demand. The process is similar to that of downloading a feature module, as shown below.

**Kotlin**

```kotlin
// Captures the user’s preferred language and persists it
// through the app’s SharedPreferences.
sharedPrefs.edit().putString(LANGUAGE_SELECTION, "fr").apply()
...

// Creates a request to download and install additional language resources.
val request = SplitInstallRequest.newBuilder()
        // Uses the addLanguage() method to include French language resources in the request.
        // Note that country codes are ignored. That is, if your app
        // includes resources for “fr-FR” and “fr-CA”, resources for both
        // country codes are downloaded when requesting resources for "fr".
        .addLanguage(Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)))
        .build()

// Submits the request to install the additional language resources.
splitInstallManager.startInstall(request)
```

**Java**

```java
// Captures the user’s preferred language and persists it
// through the app’s SharedPreferences.
sharedPrefs.edit().putString(LANGUAGE_SELECTION, "fr").apply();
...

// Creates a request to download and install additional language resources.
SplitInstallRequest request =
    SplitInstallRequest.newBuilder()
        // Uses the addLanguage() method to include French language resources in the request.
        // Note that country codes are ignored. That is, if your app
        // includes resources for “fr-FR” and “fr-CA”, resources for both
        // country codes are downloaded when requesting resources for "fr".
        .addLanguage(Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)))
        .build();

// Submits the request to install the additional language resources.
splitInstallManager.startInstall(request);
```

The request is handled as if it were a request for a feature module. That is, you can [monitor the request state](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#monitor_requests>) like you normally would.

If your app doesn't require the additional language resources immediately, you can defer the installation for when the app is in the background, as shown below.

**Kotlin**

```kotlin
splitInstallManager.deferredLanguageInstall(
    Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)))
```

**Java**

```java
splitInstallManager.deferredLanguageInstall(
    Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)));
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
