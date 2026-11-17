These constants belong to `StandardIntegrityErrorCode`; [the class summary](standard-error-index.md) lists the full set.

### CLOUD_PROJECT_NUMBER_IS_INVALID

```text
public static final int CLOUD_PROJECT_NUMBER_IS_INVALID = -16
```

The provided cloud project number is invalid.

Use the cloud project number which can be found in Project info in your Google Cloud Console for the cloud project where Play Integrity API is enabled.

### INTEGRITY_TOKEN_PROVIDER_INVALID

```text
public static final int INTEGRITY_TOKEN_PROVIDER_INVALID = -19
```

The `StandardIntegrityTokenProvider` is invalid (e.g. it is outdated).

This error can be returned only for ` StandardIntegrityTokenProvider#request(StandardIntegrityTokenRequest)`.

Request a new integrity token provider by calling ` StandardIntegrityManager#prepareIntegrityToken(PrepareIntegrityTokenRequest)`.

### REQUEST_HASH_TOO_LONG

```text
public static final int REQUEST_HASH_TOO_LONG = -17
```

The provided request hash is too long. The request hash length must be less than 500 bytes.

Retry with a shorter request hash.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode).
