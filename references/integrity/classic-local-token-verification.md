This example requires the response decryption and signature verification keys from [local key decryption](classic-local-key-decryption.md). [Server-managed verification](classic-server-verification.md) is the recommended alternative.

**Kotlin**

```kotlin
val jwe: JsonWebEncryption =
    JsonWebStructure.fromCompactSerialization(integrityToken) as JsonWebEncryption
jwe.setKey(decryptionKey)

// This also decrypts the JWE token.
val compactJws: String = jwe.getPayload()

val jws: JsonWebSignature =
    JsonWebStructure.fromCompactSerialization(compactJws) as JsonWebSignature
jws.setKey(verificationKey)

// This also verifies the signature.
val payload: String = jws.getPayload()
```

**Java**

```java
JsonWebEncryption jwe =
    (JsonWebEncryption)JsonWebStructure
        .fromCompactSerialization(integrityToken);
jwe.setKey(decryptionKey);

// This also decrypts the JWE token.
String compactJws = jwe.getPayload();

JsonWebSignature jws =
    (JsonWebSignature) JsonWebStructure.fromCompactSerialization(compactJws);
jws.setKey(verificationKey);

// This also verifies the signature.
String payload = jws.getPayload();
```

The resulting payload is a plain-text token that contains [integrity verdicts](<https://developer.android.com/google/play/integrity/verdicts>).

## Remediate verdict issues with a Google Play prompt (optional)

After your server receives an integrity verdict, the server can determine how to proceed. If the verdict indicates there's an issue, such as the app being unlicensed, tampered with, or the device being compromised, you can give users a chance to fix the issue themselves.

The Play Integrity API provides an option to show a Google Play dialog that prompts the user to take action, for example, to get the official version of your app from Google Play.

To learn how to trigger these dialogs from your app based on the server's response, see [Remediation dialogs](<https://developer.android.com/google/play/integrity/remediation>).

> **Tip:** At any time, users can [check their device's Play Protect certification status and troubleshoot issues](<https://support.google.com/googleplay/answer/7165974>) in the Play Store app. You can point your users to this support page if they need help troubleshooting a device integrity issue.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/classic).
