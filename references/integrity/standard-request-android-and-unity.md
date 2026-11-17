The [standard request workflow](standard-workflow.md) defines provider preparation, request-hash binding and backend verification. Reuse the prepared provider for token requests.

## Request an integrity verdict (on demand)

After you have prepared the integrity token provider, you can start requesting integrity verdicts from Google Play. To do so, complete the following steps:

1. [Obtain a `StandardIntegrityTokenProvider`](<https://developer.android.com/google/play/integrity/standard?hl=en#prepare-integrity>).
2. Construct an `StandardIntegrityTokenRequest`, supplying the request hash of the user action you want to protect through the `setRequestHash` method.
3. Use the integrity token provider to call `request()`, supplying the `StandardIntegrityTokenRequest`.

**Java**

```java
import com.google.android.gms.tasks.Task;

StandardIntegrityTokenProvider integrityTokenProvider;

// See above how to prepare integrityTokenProvider.

// Request integrity token by providing a user action request hash. Can be called
// several times for different user actions.
String requestHash = "2cp24z...";
Task<StandardIntegrityToken> integrityTokenResponse =
    integrityTokenProvider.request(
        StandardIntegrityTokenRequest.builder()
            .setRequestHash(requestHash)
            .build());
integrityTokenResponse
    .addOnSuccessListener(response -> sendToServer(response.token()))
    .addOnFailureListener(exception -> handleError(exception));
```

**Unity**

```c#
IEnumerator RequestIntegrityTokenCoroutine() {
    StandardIntegrityManagerV2.StandardIntegrityTokenProvider integrityTokenProvider;

    // See above how to prepare integrityTokenProvider.

    // Request integrity token by providing a user action request hash. Can be called
    // several times for different user actions.
    String requestHash = "2cp24z...";
    var integrityTokenOperation = integrityTokenProvider.Request(
      new StandardIntegrityTokenRequest(requestHash)
    );

    // Wait for PlayAsyncOperation to complete.
    yield return integrityTokenOperation;

    // Check the resulting error code.
    if (integrityTokenOperation.Error != null &&
        integrityTokenOperation.Error.ErrorCode != StandardIntegrityErrorCode.NoError)
    {
        AppendStatusLog("StandardIntegrityAsyncOperation failed with error: " +
                integrityTokenOperation.Error.ErrorCode);
        yield break;
    }

    // Get the response.
    var integrityToken = integrityTokenOperation.GetResult();
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/standard).
