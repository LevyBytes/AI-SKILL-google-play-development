The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

## Manage installed modules

To check which feature modules are currently installed on the device, you can call [`SplitInstallManager.getInstalledModules()`](<https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#getInstalledModules()>), which returns a `Set<String>` of the names of the installed modules, as shown below.

> **Note:** If you're developing an Android Instant App, this section does not apply to you.

**Kotlin**

```kotlin
val installedModules: Set<String> = splitInstallManager.installedModules
```

**Java**

```java
Set<String> installedModules = splitInstallManager.getInstalledModules();
```

### Uninstall modules

You can request the device to uninstall modules by invoking [`SplitInstallManager.deferredUninstall(List<String> moduleNames)`](<https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#deferreduninstall>), as shown below.

**Kotlin**

```kotlin
// Specifies two feature modules for deferred uninstall.
splitInstallManager.deferredUninstall(listOf("pictureMessages", "promotionalFilters"))
```

**Java**

```java
// Specifies two feature modules for deferred uninstall.
splitInstallManager.deferredUninstall(Arrays.asList("pictureMessages", "promotionalFilters"));
```

Module uninstalls do not occur immediately. That is, the device uninstalls them in the background as needed to save storage space. You can confirm that the device has deleted a module by invoking [`SplitInstallManager.getInstalledModules()`](<https://developer.android.com/reference/com/google/android/play/core/splitinstall/SplitInstallManager#getinstalledmodules>) and inspecting the result, as described in the previous section.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
