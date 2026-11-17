The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

## Access code and resources from installed modules

If you [enable SplitCompat](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#access_downloaded_modules>) for your base application context and the activities in your feature module, you can use the code and resources from a feature module as if it were a part of the base APK, once the optional module is installed.

### Access code from a different module

#### Access base code from a module

Code that is inside your base module can be used directly by other modules. You don't need to do anything special; just import and use the classes you need.

#### Access module code from another module

An object or class inside a module cannot be statically accessed from another module directly, but it can be accessed indirectly, using reflection.

You should be wary of how often this happens, due to the performance costs of reflection. For complex use cases, use dependency injection frameworks like [Dagger 2](<https://dagger.dev/>) to guarantee a single reflection call per application lifetime.

To simplify the interactions with the object after instantiation, it is recommended to define an interface in the base module and its implementation in the feature module. For instance:

**Kotlin**

```kotlin
// In the base module
interface MyInterface {
  fun hello(): String
}

// In the feature module
object MyInterfaceImpl : MyInterface {
  override fun hello() = "Hello"
}

// In the base module, where we want to access the feature module code
val stringFromModule = (Class.forName("com.package.module.MyInterfaceImpl")
    .kotlin.objectInstance as MyInterface).hello();
```

**Java**

```java
// In the base module
public interface MyInterface {
  String hello();
}

// In the feature module
public class MyInterfaceImpl implements MyInterface {
  @Override
  public String hello() {
    return "Hello";
  }
}

// In the base module, where we want to access the feature module code
String stringFromModule =
   ((MyInterface) Class.forName("com.package.module.MyInterfaceImpl").getConstructor().newInstance()).hello();
```

### Access resources and assets from a different module

Once a module is installed, you can access resources and assets within the module in the standard way, with two caveats:

- If you are accessing a resource from a different module, the module will not have access to the resource identifier, though the resource can still be accessed by name. Note that the package to use to reference the resource is the package of the module where the resource is defined.
- If you want to access assets or resources that exist in a newly installed module from a different installed module of your app, you must do so [using the application context](<https://developer.android.com/guide/topics/resources/providing-resources#Accessing>). The context of the component that's trying to access the resources will not yet be updated. Alternatively, you can recreate that component (for instance calling [Activity.recreate()](<https://developer.android.com/reference/android/app/Activity#recreate()>)) or [reinstall SplitCompat](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#activity_splitcompat>) on it after the feature module installation.

### Load native code in an app using on-demand delivery

We recommend using [ReLinker](<https://github.com/KeepSafe/ReLinker>) to load all your native libraries when using on-demand delivery of feature modules. ReLinker fixes an issue in loading native libraries after the installation of a feature module. You can learn more about ReLinker in the [Android JNI Tips](<https://developer.android.com/training/articles/perf-jni#native-libraries>).

### Load native code from an optional module

Once a split is installed, we recommend loading its native code through [ReLinker](<https://github.com/KeepSafe/ReLinker>). For instant apps you should use [this special method](<https://developer.android.com/guide/playcore/feature-delivery/on-demand?hl=en#load_native_libs>).

If you are using `System.loadLibrary()` to load your native code and your native library has a dependency on another library in the module, you must manually load that other library first. If you are using ReLinker, the equivalent operation is `Relinker.recursively().loadLibrary()`.

If you are using `dlopen()` in native code to load a library defined in an optional module, it will not work with relative library paths. The best solution is to retrieve the absolute path of the library from Java code via `ClassLoader.findLibrary()` and then use it in your `dlopen()` call. Do this before entering the native code or use a JNI call from your native code into Java.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
