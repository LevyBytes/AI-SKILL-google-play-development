This guide describes how to support [in-app updates](<https://developer.android.com/guide/playcore/in-app-updates>) in your app using Unreal Engine. There are separate guides for cases where your implementation uses [the Kotlin programming language or the Java programming language](<https://developer.android.com/guide/playcore/in-app-updates/kotlin-java>), and cases where your implementation uses [native code (C/C++)](<https://developer.android.com/guide/playcore/in-app-updates/native>) or [Unity](<https://developer.android.com/guide/playcore/in-app-updates/unity>).

## Unreal Engine SDK overview

The Play In-App Updates API is part of Play Core SDK family. The API for Unreal Engine offers a `UInAppUpdatesManager` class to handle communication between your app and the Play API. After a request is made, your app can check the status of the request using `EAppUpdateErrorCode`.

## Supported Unreal Engine versions

The plugin supports **Unreal Engine 5.0** and all subsequent versions.

## Set up your development environment

> **Note:** If you have already used the In-app Reviews or In-app Updates plugins in Unreal Engine, you can skip to the final step.

1. Download the [Play Unreal Engine Plugin](<https://github.com/google/play-unreal-engine-plugin>) from the GitHub repository.
2. Copy the `GooglePlay` folder inside your `Plugins` folder in your Unreal Engine project.
3. Open your Unreal Engine project and click **Edit → Plugins**.
4. Search for **Google Play** and check the **Enabled** checkbox.
5. Restart the game project and trigger a build.
6. Open your project's `Build.cs` file and add the `PlayInAppUpdates` module to `PublicDependencyModuleNames`:

   ```c#
   using UnrealBuildTool;

   public class MyGame : ModuleRules
   {
     public MyGame(ReadOnlyTargetRules Target) : base(Target)
     {
       // ...

       PublicDependencyModuleNames.Add("PlayInAppUpdates");

       // ...
     }
   }
   ```

## Check for update availability

Before you request an update, check if there is an update available for your app. Use `UInAppUpdatesManager::RequestInfo` to check for an update:

MyClass.h

```c
void MyClass::OnRequestInfoOperationCompleted(
  EAppUpdateErrorCode ErrorCode,
  UAppUpdateInfo* UpdateInfo)
{
  // Check the resulting error code.
  if (ErrorCode == EAppUpdateErrorCode::AppUpdate_NO_ERROR)
  {
    // Check AppUpdateInfo's UpdateAvailability, UpdatePriority,
    // IsUpdateTypeAllowed(), ... and decide whether to ask the user
    // to start an in-app update.
  }
}
```

MyClass.cpp

```c
void MyClass::CheckForUpdateAvailability()
{
  // Create a delegate to bind the callback function.
  FRequestInfoOperationCompletedDelegate Delegate;

  // Bind the completion handler (OnRequestInfoOperationCompleted) to the delegate.
  Delegate.BindDynamic(this, &MyClass::OnRequestInfoOperationCompleted);

  // Initiate the request info operation, passing the delegate to handle the result.
  GetGameInstance()
    ->GetSubsystem<UInAppUpdatesManager>()
    ->RequestInfo(Delegate);
}
```

The returned `UAppUpdateInfo` instance contains the update availability status. If an in-app update is already in progress, the instance also reports the status of the in-progress update.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/unreal-engine).
