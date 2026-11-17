The [standard request workflow](standard-workflow.md) defines provider preparation, request-hash binding and backend verification. Reuse the prepared provider for token requests.

**Unreal Engine**

```c++
// .h
void MyClass::OnRequestIntegrityTokenCompleted(
  EStandardIntegrityErrorCode ErrorCode,
  UStandardIntegrityToken* Response)
{
  // Check the resulting error code.
  if (ErrorCode == EStandardIntegrityErrorCode::StandardIntegrity_NO_ERROR)
  {
    // Get the token.
    FString Token = Response->Token;
  }
}

// .cpp
void MyClass::RequestIntegrityToken()
{
  UStandardIntegrityTokenProvider* Provider = ...

  // Prepare the UStandardIntegrityTokenProvider.

  // Request integrity token by providing a user action request hash. Can be called
  // several times for different user actions.
  FString RequestHash = ...;
  FStandardIntegrityTokenRequest Request = { RequestHash };

  // Create a delegate to bind the callback function.
  FStandardIntegrityOperationCompletedDelegate Delegate;

  // Bind the completion handler (OnRequestIntegrityTokenCompleted) to the delegate.
  Delegate.BindDynamic(this, &MyClass::OnRequestIntegrityTokenCompleted);

  // Initiate the standard integrity token request, passing the delegate to handle the result.
  Provider->Request(Request, Delegate);
}
```

**Native**

```c++
/// Create a StandardIntegrityTokenRequest opaque object.
const char* requestHash = ...;
StandardIntegrityTokenRequest* tokenRequest;
StandardIntegrityTokenRequest_create(&tokenRequest);
StandardIntegrityTokenRequest_setRequestHash(tokenRequest, requestHash);

/// Prepare a StandardIntegrityToken opaque type pointer and call
/// StandardIntegrityTokenProvider_request(). Can be called several times for
/// different user actions. See above how to prepare token provider.
StandardIntegrityToken* token;
StandardIntegrityErrorCode error_code =
        StandardIntegrityTokenProvider_request(tokenProvider, tokenRequest, &token);

/// ...
/// Proceed to polling iff error_code == STANDARD_INTEGRITY_NO_ERROR
if (error_code != STANDARD_INTEGRITY_NO_ERROR)
{
    /// Remember to call the *_destroy() functions.
    return;
}
/// ...
/// Use polling to wait for the async operation to complete.

IntegrityResponseStatus token_status;

/// Check for error codes.
StandardIntegrityErrorCode error_code =
        StandardIntegrityToken_getStatus(token, &token_status);
if (error_code == STANDARD_INTEGRITY_NO_ERROR
    && token_status == INTEGRITY_RESPONSE_COMPLETED)
{
    const char* integrityToken = StandardIntegrityToken_getToken(token);
}
/// ...
/// Remember to free up resources.
StandardIntegrityTokenRequest_destroy(tokenRequest);
StandardIntegrityToken_destroy(token);
StandardIntegrityTokenProvider_destroy(tokenProvider);
StandardIntegrityManager_destroy();
```

If your app uses the same token provider for too long, the token provider can expire which results in the [INTEGRITY_TOKEN_PROVIDER_INVALID](<https://developer.android.com/google/play/integrity/error-codes#iErr_19>) error on the next token request. You should handle this error by requesting a new provider.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/standard).
