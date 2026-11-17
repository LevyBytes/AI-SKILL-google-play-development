```json
"requestDetails": {
  // Application package name this attestation was requested for.
  // Note that this field might be spoofed in the middle of the
  // request.
  "requestPackageName": "com.package.name",
  // base64-encoded URL-safe no-wrap nonce provided by the developer.
  "nonce": "aGVsbG8gd29scmQgdGhlcmU",
  // The timestamp in milliseconds when the request was made
  // (computed on the server).
  "timestampMillis": "1617893780"
}
```

These values should match those of the original request. Therefore, verify the `requestDetails` part of the JSON payload by making sure that the `requestPackageName` and `nonce` match what was sent in the original request, as shown in the following code snippet:

**Kotlin**

```kotlin
val requestDetails = JSONObject(payload).getJSONObject("requestDetails")
val requestPackageName = requestDetails.getString("requestPackageName")
val nonce = requestDetails.getString("nonce")
val timestampMillis = requestDetails.getLong("timestampMillis")
val currentTimestampMillis = ...

// Ensure the token is from your app.
if (!requestPackageName.equals(expectedPackageName)
        // Ensure the token is for this specific request. See 'Generate a nonce'
        // section of the doc on how to store/compute the expected nonce.
    || !nonce.equals(expectedNonce)
        // Ensure the freshness of the token.
    || currentTimestampMillis - timestampMillis > ALLOWED_WINDOW_MILLIS) {
        // The token is invalid! See below for further checks.
        ...
}
```

**Java**

```java
JSONObject requestDetails =
    new JSONObject(payload).getJSONObject("requestDetails");
String requestPackageName = requestDetails.getString("requestPackageName");
String nonce = requestDetails.getString("nonce");
long timestampMillis = requestDetails.getLong("timestampMillis");
long currentTimestampMillis = ...;

// Ensure the token is from your app.
if (!requestPackageName.equals(expectedPackageName)
        // Ensure the token is for this specific request. See 'Generate a nonce'
        // section of the doc on how to store/compute the expected nonce.
    || !nonce.equals(expectedNonce)
        // Ensure the freshness of the token.
    || currentTimestampMillis - timestampMillis > ALLOWED_WINDOW_MILLIS) {
        // The token is invalid! See below for further checks.
        ...
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/verdicts).
