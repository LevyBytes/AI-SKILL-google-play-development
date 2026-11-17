## Launch the in-app review flow

Once the `RequestReviewFlow` operation is complete, you can launch the in-app review flow. This is done by binding a delegate to handle the completion event, ensuring the app reacts to the outcome (success or failure) of the review request.

MyClass.h

```c
void MyClass::OnReviewOperationCompleted(EInAppReviewErrorCode ErrorCode)
{
  // ...
}
```

MyClass.cpp

```c
void MyClass::LaunchReviewFlow()
{
  // Create a delegate to bind the callback function.
  FReviewOperationCompletedDelegate Delegate;

  // Bind the completion handler (OnReviewOperationCompleted) to the delegate.
  Delegate.BindDynamic(this, &MyClass::OnReviewOperationCompleted);

  // Launch the review flow, passing the delegate to handle the result.
  GetGameInstance()
    ->GetSubsystem<UInAppReviewsManager>()
    ->LaunchReviewFlow(Delegate);
}
```

## Next steps

[Test your app's in-app review flow](<https://developer.android.com/guide/playcore/in-app-review/test>) to verify that your integration is working correctly.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-review/unreal-engine).
