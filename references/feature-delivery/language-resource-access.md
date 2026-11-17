The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

### Access downloaded language resources

To gain access to downloaded language resources, your app needs to run the `SplitCompat.installActivity()` method within the `attachBaseContext()` method of each activity that requires access to those resources, as shown below.

**Kotlin**

```kotlin
override fun attachBaseContext(base: Context) {
  super.attachBaseContext(base)
  SplitCompat.installActivity(this)
}
```

**Java**

```java
@Override
protected void attachBaseContext(Context base) {
  super.attachBaseContext(base);
  SplitCompat.installActivity(this);
}
```

For each activity you want to use language resources your app has downloaded, update the base context and set a new locale through its [`Configuration`](<https://developer.android.com/reference/android/content/res/Configuration>):

**Kotlin**

```kotlin
override fun attachBaseContext(base: Context) {
  val configuration = Configuration()
  configuration.setLocale(Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)))
  val context = base.createConfigurationContext(configuration)
  super.attachBaseContext(context)
  SplitCompat.install(this)
}
```

**Java**

```java
@Override
protected void attachBaseContext(Context base) {
  Configuration configuration = new Configuration();
  configuration.setLocale(Locale.forLanguageTag(sharedPrefs.getString(LANGUAGE_SELECTION)));
  Context context = base.createConfigurationContext(configuration);
  super.attachBaseContext(context);
  SplitCompat.install(this);
}
```

In order for these changes to take effect, you have to recreate your activity after the new language is installed and ready to use. You can use the `Activity#recreate()` method.

**Kotlin**

```kotlin
when (state.status()) {
  SplitInstallSessionStatus.INSTALLED -> {
      // Recreates the activity to load resources for the new language
      // preference.
      activity.recreate()
  }
  ...
}
```

**Java**

```java
switch (state.status()) {
  case SplitInstallSessionStatus.INSTALLED:
      // Recreates the activity to load resources for the new language
      // preference.
      activity.recreate();
  ...
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
