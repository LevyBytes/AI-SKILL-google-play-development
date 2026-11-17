These constants belong to `IntegrityErrorCode`; [the class summary](classic-error-index.md) lists the full set.

### CLOUD_PROJECT_NUMBER_IS_INVALID

```text
public static final int CLOUD_PROJECT_NUMBER_IS_INVALID = -16
```

The provided cloud project number is invalid.

Use the cloud project number which can be found in Project info in your Google Cloud Console for the cloud project where Play Integrity API is enabled.

### NONCE_IS_NOT_BASE64

```text
public static final int NONCE_IS_NOT_BASE64 = -13
```

Nonce is not encoded as a base64 web-safe no-wrap string.

Retry with correct nonce format.

### NONCE_TOO_LONG

```text
public static final int NONCE_TOO_LONG = -11
```

Nonce length is too long. The nonce must be less than 500 bytes before base64 encoding.

Retry with a shorter nonce.

### NONCE_TOO_SHORT

```text
public static final int NONCE_TOO_SHORT = -10
```

Nonce length is too short. The nonce must be a minimum of 16 bytes (before base64 encoding) to allow for a better security.

Retry with a longer nonce.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode).
