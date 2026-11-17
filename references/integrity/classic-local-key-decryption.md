### Decrypt and verify locally

> **Note:** To protect your app's security, it's recommended that you [allow Google Play to manage your response encryption](<https://developer.android.com/google/play/integrity/classic?hl=en#decrypt-verify-google-servers>) for your app.

If you choose to manage and download your response encryption keys, you can decrypt and verify the returned token within your own secure server environment. You can obtain the returned token by using the `IntegrityTokenResponse#token()` method.

The following example shows how to decode the AES key and the DER-encoded public EC key for signature verification from the Play Console to language-specific (the Java programming language, in our case) keys in the app's backend. Note that the keys are base64-encoded using default flags.

**Kotlin**

```kotlin
// base64OfEncodedDecryptionKey is provided through Play Console.
var decryptionKeyBytes: ByteArray =
    Base64.decode(base64OfEncodedDecryptionKey, Base64.DEFAULT)

// Deserialized encryption (symmetric) key.
var decryptionKey: SecretKey = SecretKeySpec(
    decryptionKeyBytes,
    /* offset= */ 0,
    AES_KEY_SIZE_BYTES,
    AES_KEY_TYPE
)

// base64OfEncodedVerificationKey is provided through Play Console.
var encodedVerificationKey: ByteArray =
    Base64.decode(base64OfEncodedVerificationKey, Base64.DEFAULT)

// Deserialized verification (public) key.
var verificationKey: PublicKey = KeyFactory.getInstance(EC_KEY_TYPE)
    .generatePublic(X509EncodedKeySpec(encodedVerificationKey))
```

**Java**

```java
// base64OfEncodedDecryptionKey is provided through Play Console.
byte[] decryptionKeyBytes =
    Base64.decode(base64OfEncodedDecryptionKey, Base64.DEFAULT);

// Deserialized encryption (symmetric) key.
SecretKey decryptionKey =
    new SecretKeySpec(
        decryptionKeyBytes,
        /* offset= */ 0,
        AES_KEY_SIZE_BYTES,
        AES_KEY_TYPE);

// base64OfEncodedVerificationKey is provided through Play Console.
byte[] encodedVerificationKey =
    Base64.decode(base64OfEncodedVerificationKey, Base64.DEFAULT);
// Deserialized verification (public) key.
PublicKey verificationKey =
    KeyFactory.getInstance(EC_KEY_TYPE)
        .generatePublic(new X509EncodedKeySpec(encodedVerificationKey));
```

Next, use these keys to first decrypt the integrity token (JWE part) and then verify and extract the nested JWS part.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/classic).
