These constants belong to `IntegrityErrorCode`; [the class summary](classic-error-index.md) lists the full set.

### CLIENT_TRANSIENT_ERROR

```text
public static final int CLIENT_TRANSIENT_ERROR = -17
```

There was a transient error in the client device.

Retry with an exponential backoff.

Introduced in Integrity Play Core version 1.1.0 (prior versions returned a token with empty Device Integrity Verdict). If the error persists after a few retries, you should assume that the device has failed integrity checks and act accordingly.

### GOOGLE_SERVER_UNAVAILABLE

```text
public static final int GOOGLE_SERVER_UNAVAILABLE = -12
```

Unknown internal Google server error.

Retry with an exponential backoff. Consider filing a bug if fails consistently.

### INTERNAL_ERROR

```text
public static final int INTERNAL_ERROR = -100
```

Unknown internal error.

Retry with an exponential backoff. Consider filing a bug if fails consistently.

### NETWORK_ERROR

```text
public static final int NETWORK_ERROR = -3
```

No available network is found.

Recommended actions:

- Ask the user to check and enable their network connection.
- For a guided user experience that helps the user to establish a network connection, you can show either `GET_INTEGRITY` or `GET_STRONG_INTEGRITY` dialog.

### TOO_MANY_REQUESTS

```text
public static final int TOO_MANY_REQUESTS = -8
```

The calling app has made too many requests to the API and has been throttled, or your app has exceeded its daily request quota.

Retry with an exponential backoff. Request an increase to your daily request quota if you're at your daily request limit.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode).
