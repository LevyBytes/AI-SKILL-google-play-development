This page describes how to interpret and work with the returned integrity verdict. Whether you make a standard or classic API request, the integrity verdict is returned in the same format with similar content. The integrity verdict communicates information about the validity of devices, apps, and accounts. Your app's server can use the resulting payload in a decrypted, verified verdict to determine how best to proceed with a particular action or request in your app.

## Returned integrity verdict format

The payload is plain-text JSON and contains integrity signals alongside developer-provided information.

The general payload structure is as follows:

```json
{
  "requestDetails": { ... },
  "accountDetails": { ... },
  "appIntegrity": { ... },
  "deviceIntegrity": { ... },
  "environmentDetails": { ... }
}
```

The order of the fields in the JSON payload is not guaranteed. You must first check that the values in the `requestDetails` field match those of the original request before checking each integrity verdict. Field contracts continue in [account verdicts](account-verdict.md), [application verdicts](application-verdict.md), [device verdicts](device-verdict.md) and [environment details](app-access-risk-verdict.md).

### Request details field

The `requestDetails` field contains information about the request, including developer-provided information in the `requestHash` for standard requests and the `nonce` for classic requests.

For **standard** API requests:

```json
"requestDetails": {
  // Application package name this attestation was requested for.
  // Note that this field might be spoofed in the middle of the request.
  "requestPackageName": "com.package.name",
  // Request hash provided by the developer.
  "requestHash": "aGVsbG8gd29scmQgdGhlcmU",
  // The timestamp in milliseconds when the integrity token
  // was requested.
  "timestampMillis": "1675655009345"
}
```

These values should match those of the original request. Therefore, verify the `requestDetails` part of the JSON payload by making sure that the `requestPackageName` and `requestHash` match what was sent in the original request, as shown in the following code snippet:

**Kotlin**

```kotlin
val requestDetails = JSONObject(payload).getJSONObject("requestDetails")
val requestPackageName = requestDetails.getString("requestPackageName")
val requestHash = requestDetails.getString("requestHash")
val timestampMillis = requestDetails.getLong("timestampMillis")
val currentTimestampMillis = ...

// Ensure the token is from your app.
if (!requestPackageName.equals(expectedPackageName)
        // Ensure the token is for this specific request
    || !requestHash.equals(expectedRequestHash)
        // Ensure the freshness of the token.
    || currentTimestampMillis - timestampMillis > ALLOWED_WINDOW_MILLIS) {
        // The token is invalid! See below for further checks.
        ...
}
```

**Java**

```java
RequestDetails requestDetails =
    decodeIntegrityTokenResponse
    .getTokenPayloadExternal()
    .getRequestDetails();
String requestPackageName = requestDetails.getRequestPackageName();
String requestHash = requestDetails.getRequestHash();
long timestampMillis = requestDetails.getTimestampMillis();
long currentTimestampMillis = ...;

// Ensure the token is from your app.
if (!requestPackageName.equals(expectedPackageName)
        // Ensure the token is for this specific request.
    || !requestHash.equals(expectedRequestHash)
        // Ensure the freshness of the token.
    || currentTimestampMillis - timestampMillis > ALLOWED_WINDOW_MILLIS) {
        // The token is invalid! See below for further checks.
        ...
}
```

For **classic** API requests:

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/verdicts).
