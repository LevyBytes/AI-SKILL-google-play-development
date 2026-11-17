The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

## Access modules

To access code and resources from a downloaded module after it is downloaded, your app needs to enable the [SplitCompat Library](<https://developer.android.com/reference/com/google/android/play/core/splitcompat/SplitCompat>) for both your app and each activity in the feature modules your app downloads.

You should note, however, the platform experiences the following restrictions to accessing contents of a module, for some time (days, in some cases) after downloading the module:

- The platform can not apply any new manifest entries introduced by the module.
- The platform can not access the module’s resources for system UI components, such as notifications. If you need to use such resources immediately, consider including those resource in the base module of your app.

### Enable SplitCompat

For your app to access code and resources from a downloaded module, you need to enable SplitCompat using one of the application setups below or [manual runtime setup](splitcompat-runtime-and-activities.md).

After you enable SplitCompat for your app, you need to also [enable SplitCompat for each activity](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#activity_splitcompat>) in the feature modules you want your app to have access to.

#### Declare SplitCompatApplication in the manifest

The simplest way to enable SplitCompat is to declare `SplitCompatApplication` as the [`Application`](<https://developer.android.com/reference/android/app/Application>) subclass in your app’s manifest, as shown below:

```xml
<application
    ...
    android:name="com.google.android.play.core.splitcompat.SplitCompatApplication">
</application>
```

After the app is installed on a device, you can access code and resources from downloaded feature modules automatically.

#### Invoke SplitCompat at runtime

You can also enable SplitCompat in specific activities or services at runtime. Enabling SplitCompat this way is required to launch activities included in feature modules. To do this, override `attachBaseContext` as seen below.

If you have a custom [Application](<https://developer.android.com/reference/android/app/Application>) class, have it instead extend [`SplitCompatApplication`](<https://developer.android.com/reference/com/google/android/play/core/splitcompat/SplitCompatApplication>) in order to enable SplitCompat for your app, as shown below:

**Kotlin**

```kotlin
class MyApplication : SplitCompatApplication() {
    ...
}
```

**Java**

```java
public class MyApplication extends SplitCompatApplication {
    ...
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
