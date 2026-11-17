The [standard request workflow](standard-workflow.md) defines provider preparation, request-hash binding and backend verification. Reuse the prepared provider for token requests.

**Unreal Engine**

```c++
// .h
void MyClass::OnPrepareIntegrityTokenCompleted(
  EStandardIntegrityErrorCode ErrorCode,
  UStandardIntegrityTokenProvider* Provider)
{
  // Check the resulting error code.
  if (ErrorCode == EStandardIntegrityErrorCode::StandardIntegrity_NO_ERROR)
  {
    // ...
  }
}

// .cpp
void MyClass::PrepareIntegrityToken()
{
  int64 CloudProjectNumber = ...

  // Create the Integrity Token Request.
  FPrepareIntegrityTokenRequest Request = { CloudProjectNumber };

  // Create a delegate to bind the callback function.
  FPrepareIntegrityOperationCompletedDelegate Delegate;

  // Bind the completion handler (OnPrepareIntegrityTokenCompleted) to the delegate.
  Delegate.BindDynamic(this, &MyClass::OnPrepareIntegrityTokenCompleted);

  // Initiate the prepare integrity token operation, passing the delegate to handle the result.
  GetGameInstance()
    ->GetSubsystem<UStandardIntegrityManager>()
    ->PrepareIntegrityToken(Request, Delegate);
}
```

**Native**

```c++
/// Initialize StandardIntegrityManager
StandardIntegrityManager_init(/* app's java vm */, /* an android context */);
/// Create a PrepareIntegrityTokenRequest opaque object.
int64_t cloudProjectNumber = ...;
PrepareIntegrityTokenRequest* tokenProviderRequest;
PrepareIntegrityTokenRequest_create(&tokenProviderRequest);
PrepareIntegrityTokenRequest_setCloudProjectNumber(tokenProviderRequest, cloudProjectNumber);

/// Prepare a StandardIntegrityTokenProvider opaque type pointer and call
/// StandardIntegrityManager_prepareIntegrityToken().
StandardIntegrityTokenProvider* tokenProvider;
StandardIntegrityErrorCode error_code =
        StandardIntegrityManager_prepareIntegrityToken(tokenProviderRequest, &tokenProvider);

/// ...
/// Proceed to polling iff error_code == STANDARD_INTEGRITY_NO_ERROR
if (error_code != STANDARD_INTEGRITY_NO_ERROR)
{
    /// Remember to call the *_destroy() functions.
    return;
}
/// ...
/// Use polling to wait for the async operation to complete.

IntegrityResponseStatus token_provider_status;

/// Check for error codes.
StandardIntegrityErrorCode error_code =
        StandardIntegrityTokenProvider_getStatus(tokenProvider, &token_provider_status);
if (error_code == STANDARD_INTEGRITY_NO_ERROR
    && token_provider_status == INTEGRITY_RESPONSE_COMPLETED)
{
    /// continue to request token from the token provider
}
/// ...
/// Remember to free up resources.
PrepareIntegrityTokenRequest_destroy(tokenProviderRequest);
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/standard).
