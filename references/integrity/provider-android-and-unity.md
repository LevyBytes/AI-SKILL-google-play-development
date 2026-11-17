The [standard request workflow](standard-workflow.md) defines provider preparation, request-hash binding and backend verification. Reuse the prepared provider for token requests.

## Prepare the integrity token provider (one off)

Before you make a standard request for an integrity verdict from Google Play, you must prepare (or "warm up") the integrity token provider. This allows Google Play to smartly cache partial attestation information on the device in order to decrease the latency on the critical path when you make a request for an integrity verdict. Preparing the token provider again is a way to repeat less resource heavy integrity checks which will make the next integrity verdict that you request more up to date.

You might prepare the integrity token provider:

- When your app launches (i.e. on cold start up). Preparing the token provider is asynchronous and so will not impact the start up time. This option would work well if you plan to make an integrity verdict request shortly after the app is launched, for example when a user signs in or a player joins a game.
- When your app is opened (i.e. on warm start up). However, note that each app instance can only prepare the integrity token up to 5 times per minute.
- At any time in the background when you want to prepare the token in advance of an integrity verdict request.

To prepare the integrity token provider do the following:

1. Create a `StandardIntegrityManager`, as shown in the following examples.
2. Construct a `PrepareIntegrityTokenRequest`, supplying the Google Cloud project number through the `setCloudProjectNumber()` method.
3. Use the manager to call `prepareIntegrityToken()`, supplying the `PrepareIntegrityTokenRequest`.

> **Tip:** Typical warm up latency is a few seconds and the majority of all warm ups are under 10s. However, warming up invokes a server call so a timeout that accommodates a long tail of requests is recommended (e.g. of 1 minute).

**Java**

```java
import com.google.android.gms.tasks.Task;

// Create an instance of a manager.
StandardIntegrityManager standardIntegrityManager =
    IntegrityManagerFactory.createStandard(applicationContext);

StandardIntegrityTokenProvider integrityTokenProvider;
long cloudProjectNumber = ...;

// Prepare integrity token. Can be called once in a while to keep internal
// state fresh.
standardIntegrityManager.prepareIntegrityToken(
    PrepareIntegrityTokenRequest.builder()
        .setCloudProjectNumber(cloudProjectNumber)
        .build())
    .addOnSuccessListener(tokenProvider -> {
        integrityTokenProvider = tokenProvider;
    })
    .addOnFailureListener(exception -> handleError(exception));
```

**Unity**

```c#
IEnumerator PrepareIntegrityTokenCoroutine() {
    long cloudProjectNumber = ...;

    // Initialize the V2 manager. Requires Play Integrity Unity Plugin v2.0.0
    // or higher.
    var standardIntegrityManager = new StandardIntegrityManagerV2();

    // Request the token provider.
    var integrityTokenProviderOperation =
      standardIntegrityManager.PrepareIntegrityToken(
        new PrepareIntegrityTokenRequest(cloudProjectNumber));

    // Wait for PlayAsyncOperation to complete.
    yield return integrityTokenProviderOperation;

    // Check the resulting error code.
    if (integrityTokenProviderOperation.Error != null &&
        integrityTokenProviderOperation.Error.ErrorCode != StandardIntegrityErrorCode.NoError)
    {
        AppendStatusLog("StandardIntegrityAsyncOperation failed with error: " +
                integrityTokenProviderOperation.Error.ErrorCode);
        yield break;
    }

    // Get the response.
    var integrityTokenProvider = integrityTokenProviderOperation.GetResult();
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/standard).
