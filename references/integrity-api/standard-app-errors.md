These constants belong to `StandardIntegrityErrorCode`; [the class summary](standard-error-index.md) lists the full set.

### API_NOT_AVAILABLE

```text
public static final int API_NOT_AVAILABLE = -1
```

Standard Integrity API is not available.

Standard Integrity API is not enabled, or the Play Store version might be old.

Recommended actions:

- Make sure to be allowlisted to use Standard Integrity API.
- Make sure that Integrity API is enabled in Google Play Console.
- Ask the user to update Play Store.

### APP_NOT_INSTALLED

```text
public static final int APP_NOT_INSTALLED = -5
```

The calling app is not installed.

Something is wrong (possibly an attack). Non-actionable.

### APP_UID_MISMATCH

```text
public static final int APP_UID_MISMATCH = -7
```

The calling app UID (user id) does not match the one from Package Manager.

Something is wrong (possibly an attack). Non-actionable.

### CANNOT_BIND_TO_SERVICE

```text
public static final int CANNOT_BIND_TO_SERVICE = -9
```

Binding to the service in the Play Store has failed. This can be due to having an old Play Store version installed on the device or device memory is overloaded.

Ask the user to update Play Store.

Retry with an exponential backoff.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode).
