Generate and bind [the nonce](classic-request-nonce.md) before requesting this token, then perform [server verification](classic-server-verification.md).

**Unity**

```c#
IEnumerator RequestIntegrityTokenCoroutine() {
  // Receive the nonce from the secure server.
  var nonce = ...

// Initialize the V2 manager. Requires Play Integrity Unity Plugin v2.0.0
  // or higher.
  var integrityManager = new IntegrityManagerV2();

// Request the integrity token by providing a nonce.
  var tokenRequest = new IntegrityTokenRequest(nonce);
  var requestIntegrityTokenOperation =
      integrityManager.RequestIntegrityToken(tokenRequest);

// Wait for PlayAsyncOperation to complete.
  yield return requestIntegrityTokenOperation;

// Check the resulting error code.
  if (requestIntegrityTokenOperation.Error != null &&
      requestIntegrityTokenOperation.Error.ErrorCode != IntegrityErrorCode.NoError)
  {
      AppendStatusLog("IntegrityAsyncOperation failed with error: " +
              requestIntegrityTokenOperation.Error.ErrorCode);
      yield break;
  }

// Get the response.
  var tokenResponse = requestIntegrityTokenOperation.GetResult();
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/classic).
