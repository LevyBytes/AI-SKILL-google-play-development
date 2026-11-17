## Configure your app for release

After you gather all of your supporting materials, you can start configuring your app for release. This section provides a summary of the configuration changes we recommend that you make to your source code, resource files, and app manifest prior to releasing your app.

Although most of the configuration changes listed in this section are optional, they are considered good coding practices and we encourage you to implement them. In some cases, you might already have made these configuration changes as part of your development process.

### Choose a suitable application ID

Make sure you choose an application ID that is suitable over the life of your app. You can't change the application ID after you distribute your app to users. To set it, use the `applicationId` property in the module-level `build.gradle` or `build.gradle.kts` file. For more information, see [Set the application ID](<https://developer.android.com/studio/build/configure-app-module#set-application-id>).

### Turn off debugging

To configure whether the APK is debuggable, use the `debuggable` flag for Groovy or the `isDebuggable` flag for Kotlin script:

**Kotlin**

```kotlin
  android {
    ...
    buildTypes {
      release {
        isDebuggable = false
        ...
      }
      debug {
        isDebuggable = true
        ...
      }
    }
    ...
  }
  
```

**Groovy**

```groovy
  android {
    ...
    buildTypes {
      release {
        debuggable false
        ...
      }
      debug {
        debuggable true
        ...
      }
    }
    ...
  }
```

### Enable and configure app shrinking

Many of the following optimizations can be automated by enabling [shrinking](<https://developer.android.com/studio/build/shrink-code>) for your release build. For example, you can add ProGuard rules to remove log statements, and the shrinker will identify and remove unused code and resources. The shrinker can also replace class and variable names with shorter names to further reduce DEX size.

### Turn off logging

Deactivate logging before you build your app for release. You can deactivate logging by removing calls to `Log` methods in your source files. Also, remove any log files or static test files that were created in your project.

Also, remove all `Debug` tracing calls that you added to your code, such as [`startMethodTracing()`](<https://developer.android.com/reference/android/os/Debug#startMethodTracing()>) and [`stopMethodTracing()`](<https://developer.android.com/reference/android/os/Debug#stopMethodTracing()>) method calls.

**Important:** Ensure that you disable debugging for your app if using [`WebView`](<https://developer.android.com/reference/android/webkit/WebView>) to display paid content or if using JavaScript interfaces, because debugging lets users inject scripts and extract content using Chrome DevTools. To disable debugging, use the [`WebView.setWebContentsDebuggingEnabled()`](<https://developer.android.com/reference/android/webkit/WebView#setWebContentsDebuggingEnabled(boolean)>) method.

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/preparing).
