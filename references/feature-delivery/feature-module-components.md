The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

## Access components defined in feature modules

### Start an activity defined in a feature module

You can launch activities defined in feature modules using [`startActivity()`](<https://developer.android.com/reference/android/app/Activity#startActivity(android.content.Intent)>) after enabling SplitCompat.

**Kotlin**

```kotlin
startActivity(Intent()
  .setClassName("com.package", "com.package.module.MyActivity")
  .setFlags(...))
```

**Java**

```java
startActivity(new Intent()
  .setClassName("com.package", "com.package.module.MyActivity")
  .setFlags(...));
```

The first parameter to `setClassName` is the package name of the app and the second parameter is the full class name of the activity.

When you have an activity in a feature module you downloaded on-demand, you must [enable SplitCompat in the activity](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#activity_splitcompat>).

### Start a service defined in a feature module

You can launch services defined in feature modules using [`startService()`](<https://developer.android.com/reference/android/content/Context#startService(android.content.Intent)>) after enabling SplitCompat.

**Kotlin**

```kotlin
startService(Intent()
  .setClassName("com.package", "com.package.module.MyService")
  .setFlags(...))
```

**Java**

```java
startService(new Intent()
  .setClassName("com.package", "com.package.module.MyService")
  .setFlags(...));
```

### Export a component defined in a feature module

You should not include exported Android components inside optional modules.

The build system merges manifest entries for all modules into the base module; if an optional module contained an exported component, it would be accessible even before the module is installed and can cause a crash due to missing code when invoked from another app.

This is not a problem for internal components; they are accessed only by the app, so the app can [check that the module is installed](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#manage_installed_modules>) before accessing the component.

If you need an exported component, and you want its content to be in an optional module, consider implementing a proxy pattern. You can do that by adding a proxy exported component in the base; when accessed, the proxy component can check for the presence of the module that contains the content. If the module is present, the proxy component can start the internal component from the module via an `Intent`, relaying the intent from the caller app. If the module is not present, the component can download the module or return an appropriate error message to the caller app.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
