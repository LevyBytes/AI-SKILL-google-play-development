Generate and bind [the nonce](classic-request-nonce.md) before requesting this token, then perform [server verification](classic-server-verification.md).

**Unreal Engine**

```c++
// .h
void MyClass::OnRequestIntegrityTokenCompleted(
  EIntegrityErrorCode ErrorCode,
  UIntegrityTokenResponse* Response)
{
  // Check the resulting error code.
  if (ErrorCode == EIntegrityErrorCode::Integrity_NO_ERROR)
  {
    // Get the token.
    FString Token = Response->Token;
  }
}

// .cpp
void MyClass::RequestIntegrityToken()
{
  // Receive the nonce from the secure server.
  FString Nonce = ...

  // Create the Integrity Token Request.
  FIntegrityTokenRequest Request = { Nonce };

  // Create a delegate to bind the callback function.
  FIntegrityOperationCompletedDelegate Delegate;

  // Bind the completion handler (OnRequestIntegrityTokenCompleted) to the delegate.
  Delegate.BindDynamic(this, &MyClass::OnRequestIntegrityTokenCompleted);

  // Initiate the integrity token request, passing the delegate to handle the result.
  GetGameInstance()
    ->GetSubsystem<UIntegrityManager>()
    ->RequestIntegrityToken(Request, Delegate);
}
```

**Native**

```c++
/// Create an IntegrityTokenRequest opaque object.
const char* nonce = RequestNonceFromServer();
IntegrityTokenRequest* request;
IntegrityTokenRequest_create(&request);
IntegrityTokenRequest_setNonce(request, nonce);

/// Prepare an IntegrityTokenResponse opaque type pointer and call
/// IntegerityManager_requestIntegrityToken().
IntegrityTokenResponse* response;
IntegrityErrorCode error_code =
      IntegrityManager_requestIntegrityToken(request, &response);

/// ...
/// Proceed to polling iff error_code == INTEGRITY_NO_ERROR
if (error_code != INTEGRITY_NO_ERROR)
{
  /// Remember to call the *_destroy() functions.
  return;
}
/// ...
/// Use polling to wait for the async operation to complete.
/// Note, the polling shouldn't block the thread where the IntegrityManager
/// is running.

IntegrityResponseStatus response_status;

/// Check for error codes.
IntegrityErrorCode error_code =
      IntegrityTokenResponse_getStatus(response, &response_status);
if (error_code == INTEGRITY_NO_ERROR
  && response_status == INTEGRITY_RESPONSE_COMPLETED)
{
  const char* integrity_token = IntegrityTokenResponse_getToken(response);
  SendTokenToServer(integrity_token);
}
/// ...
/// Remember to free up resources.
IntegrityTokenRequest_destroy(request);
IntegrityTokenResponse_destroy(response);
IntegrityManager_destroy();
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/classic).
