The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

`SplitCompatApplication` simply overrides `ContextWrapper.attachBaseContext()` to include `SplitCompat.install(Context applicationContext)`. If you don’t want your `Application` class to extend `SplitCompatApplication`, you can override the `attachBaseContext()` method manually, as follows:

**Kotlin**

```kotlin
override fun attachBaseContext(base: Context) {
    super.attachBaseContext(base)
    // Emulates installation of future on demand modules using SplitCompat.
    SplitCompat.install(this)
}
```

**Java**

```java
@Override
protected void attachBaseContext(Context base) {
    super.attachBaseContext(base);
    // Emulates installation of future on demand modules using SplitCompat.
    SplitCompat.install(this);
}
```

If your on demand module is compatible with both instant apps and installed apps, you can invoke SplitCompat conditionally, as follows:

**Kotlin**

```kotlin
override fun attachBaseContext(base: Context) {
    super.attachBaseContext(base)
    if (!InstantApps.isInstantApp(this)) {
        SplitCompat.install(this)
    }
}
```

**Java**

```java
@Override
protected void attachBaseContext(Context base) {
    super.attachBaseContext(base);
    if (!InstantApps.isInstantApp(this)) {
        SplitCompat.install(this);
    }
}
```

### Enable SplitCompat for module activities

After you enable SplitCompat for your base app, you need to enable SplitCompat for each activity that your app downloads in a feature module. To do so, use the `SplitCompat.installActivity()` method, as follows:

**Kotlin**

```kotlin
override fun attachBaseContext(base: Context) {
    super.attachBaseContext(base)
    // Emulates installation of on demand modules using SplitCompat.
    SplitCompat.installActivity(this)
}
```

**Java**

```java
@Override
protected void attachBaseContext(Context base) {
    super.attachBaseContext(base);
    // Emulates installation of on demand modules using SplitCompat.
    SplitCompat.installActivity(this);
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
