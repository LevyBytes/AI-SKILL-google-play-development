## Handle a flexible update

After you have an up-to-date `UAppUpdateInfo` object and a properly-configured `UAppUpdateOptions` object, you can call `UInAppUpdatesManager::StartUpdate` to request an update flow.

MyClass.h

```c
void MyClass::OnStartUpdateOperationCompleted(EAppUpdateErrorCode ErrorCode)
{
  // ...
}
```

MyClass.cpp

```c
// .cpp
void MyClass::StartUpdate()
{
  // Create a delegate to bind the callback function.
  FUpdateOperationCompletedDelegate Delegate;

  // Bind the completion handler (OnStartUpdateOperationCompleted) to the delegate.
  Delegate.BindDynamic(this, &MyClass::OnStartUpdateOperationCompleted);

  // Initiate the start update operation, passing the delegate to handle the result.
  GetGameInstance()
    ->GetSubsystem<UInAppUpdatesManager>()
    ->StartUpdate(UpdateInfo, UpdateOptions, Delegate);
}
```

For a flexible update flow, you must trigger the installation of the app update after the download finishes successfully. To do this, call `InAppUpdatesManager::CompleteUpdate`, as shown in the following example:

MyClass.h

```c
void MyClass::OnCompleteUpdateOperationCompleted(EAppUpdateErrorCode ErrorCode)
{
  // ...
}
```

MyClass.cpp

```c
void MyClass::CompleteFlexibleUpdate()
{
  // Create a delegate to bind the callback function.
  FUpdateOperationCompletedDelegate Delegate;

  // Bind the completion handler (OnCompleteUpdateOperationCompleted) to the delegate.
  Delegate.BindDynamic(this, &MyClass::OnCompleteUpdateOperationCompleted);

  // Initiate the complete update operation, passing the delegate to handle the result.
  GetGameInstance()
    ->GetSubsystem<UInAppUpdatesManager>()
    ->CompleteUpdate(UpdateInfo, UpdateOptions, Delegate);
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/unreal-engine).
