## Building a URI for a resource

If you want to access a resource stored in a feature module using a URI, here's how to generate a feature module resource URI using [`Uri.Builder()`](<https://developer.android.com/reference/kotlin/android/net/Uri.Builder>):

**Kotlin**

```kotlin
val uri = Uri.Builder()
                .scheme(ContentResolver.SCHEME_ANDROID_RESOURCE)
                .authority(context.getPackageName()) // Look up the resources in the application with its splits loaded
                .appendPath(resources.getResourceTypeName(resId))
                .appendPath(String.format("%s:%s",
                  resources.getResourcePackageName(resId), // Look up the dynamic resource in the split namespace.
                  resources.getResourceEntryName(resId)
                  ))
                .build()
```

**Java**

```java
String uri = Uri.Builder()
                .scheme(ContentResolver.SCHEME_ANDROID_RESOURCE)
                .authority(context.getPackageName()) // Look up the resources in the application with its splits loaded
                .appendPath(resources.getResourceTypeName(resId))
                .appendPath(String.format("%s:%s",
                  resources.getResourcePackageName(resId), // Look up the dynamic resource in the split namespace.
                  resources.getResourceEntryName(resId)
                  ))
                .build().toString();
```

Each part of the path to the resource is constructed at run time, ensuring that the correct namespace is generated after the split APKs have been loaded.

As an example of how the URI is generated, suppose you have an app and feature modules with these names:

- App package name: `com.example.my_app_package`
- Feature's resources package name: `com.example.my_app_package.my_dynamic_feature`

If the `resId` in the code snippet above refers to a raw file resource named "my_video" in your feature module, then the `Uri.Builder()` code above would output the following:

```text
android.resource://com.example.my_app_package/raw/com.example.my_app_package.my_dynamic_feature:my_video
```

This URI can then be used by your app to access the feature module's resource.

To validate the paths in your URI, you can use the [APK Analyzer](<https://developer.android.com/studio/debug/apk-analyzer>) to inspect your feature module APK and determine the package name:

![The APK Analyzer inspecting the contents of a compiled resource file.](<https://developer.android.com/static/images/app-bundle/apk-analyzer-package-name.png>)

**Figure 1.** Use the APK Analyzer to inspect the package name in a compiled resource file.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery).
