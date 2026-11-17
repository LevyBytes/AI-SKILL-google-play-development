## Handle an immediate update

After you have an up-to-date `UAppUpdateInfo` object and a properly-configured `UAppUpdateOptions` object, you can call `InAppUpdatesManager::StartUpdate` to request an update flow.

MyClass.h

```c
void MyClass::OnStartUpdateOperationCompleted(EAppUpdateErrorCode ErrorCode)
{
  // ...
}
```

MyClass.cpp

```c
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

For an immediate update flow, Google Play displays a user confirmation dialog. When the user accepts the request, Google Play automatically downloads and installs the update, then restarts the app to the updated version if installation is successful.

## Error handling

This section describes solutions for common errors.

- If `UInAppUpdatesManager::StartUpdate` returns an `AppUpdate_INVALID_REQUEST` error, it means that `UAppUpdateInfo` is invalid. Make sure the `UAppUpdateInfo` object returned from `UInAppUpdatesManager::RequestInfo` is not null before starting the update flow.
- If `UInAppUpdatesManager::StartUpdate` returns the `AppUpdate_NOT_ALLOWED` error, it means that the `UAppUpdateOptions` object indicates an update type that is not allowed for the available update. Check whether the `UAppUpdateInfo` object indicates that the selected update type is allowed before starting the update flow.

## Next steps

[Test your app's in-app updates](<https://developer.android.com/guide/playcore/in-app-updates/test>) to verify that your integration is working correctly.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/unreal-engine).
