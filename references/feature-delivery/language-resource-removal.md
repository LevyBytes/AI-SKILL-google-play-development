The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

### Uninstall additional language resources

Similar to feature modules, you can uninstall additional resources at any time. Before requesting an uninstall, you may want to first determine which languages are currently installed, as follows.

**Kotlin**

```kotlin
val installedLanguages: Set<String> = splitInstallManager.installedLanguages
```

**Java**

```java
Set<String> installedLanguages = splitInstallManager.getInstalledLanguages();
```

You can then decide which languages to uninstall using the `deferredLanguageUninstall()` method, as shown below.

**Kotlin**

```kotlin
splitInstallManager.deferredLanguageUninstall(
    Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)))
```

**Java**

```java
splitInstallManager.deferredLanguageUninstall(
    Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)));
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
