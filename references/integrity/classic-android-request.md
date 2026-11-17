Generate and bind [the nonce](classic-request-nonce.md) before requesting this token, then perform [server verification](classic-server-verification.md).

## Request an integrity verdict

After generating a `nonce`, you can request an integrity verdict from Google Play. To do so, complete the following steps:

1. Create an `IntegrityManager`, as shown in the following examples.
2. Construct an `IntegrityTokenRequest`, supplying the `nonce` through the `setNonce()` method in the associated builder. Apps exclusively distributed outside of Google Play and SDKs also have to specify their Google Cloud project number through the `setCloudProjectNumber()` method. Apps on Google Play are linked to a Cloud project in the Play Console and don't need to set the Cloud project number in the request.
3. Use the manager to call `requestIntegrityToken()`, supplying the `IntegrityTokenRequest`. Caution: `nonce` values are passed as-is to Google's systems, so you shouldn't include personally identifiable information or other sensitive data directly or indirectly in the `nonce`.

**Kotlin**

```kotlin
// Receive the nonce from the secure server.
val nonce: String = ...

// Create an instance of a manager.
val integrityManager =
    IntegrityManagerFactory.create(applicationContext)

// Request the integrity token by providing a nonce.
val integrityTokenResponse: Task<IntegrityTokenResponse> =
    integrityManager.requestIntegrityToken(
        IntegrityTokenRequest.builder()
             .setNonce(nonce)
             .build())
```

**Java**

```java
import com.google.android.gms.tasks.Task; ...

// Receive the nonce from the secure server.
String nonce = ...

// Create an instance of a manager.
IntegrityManager integrityManager =
    IntegrityManagerFactory.create(getApplicationContext());

// Request the integrity token by providing a nonce.
Task<IntegrityTokenResponse> integrityTokenResponse =
    integrityManager
        .requestIntegrityToken(
            IntegrityTokenRequest.builder().setNonce(nonce).build());
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/classic).
