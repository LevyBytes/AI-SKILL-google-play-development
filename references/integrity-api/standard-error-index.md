```text
public annotation StandardIntegrityErrorCode
```

---

Error codes for Standard Integrity API.

## Summary

### Constants

| Declaration | Description |
| --- | --- |
| `static final int` | [`API_NOT_AVAILABLE`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#API_NOT_AVAILABLE>) `= -1`<br> Standard Integrity API is not available. |
| `static final int` | [`APP_NOT_INSTALLED`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#APP_NOT_INSTALLED>) `= -5`<br> The calling app is not installed. |
| `static final int` | [`APP_UID_MISMATCH`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#APP_UID_MISMATCH>) `= -7`<br> The calling app UID (user id) does not match the one from Package Manager. |
| `static final int` | [`CANNOT_BIND_TO_SERVICE`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#CANNOT_BIND_TO_SERVICE>) `= -9`<br> Binding to the service in the Play Store has failed. |
| `static final int` | [`CLIENT_TRANSIENT_ERROR`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#CLIENT_TRANSIENT_ERROR>) `= -18`<br> There was a transient error in the client device. |
| `static final int` | [`CLOUD_PROJECT_NUMBER_IS_INVALID`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#CLOUD_PROJECT_NUMBER_IS_INVALID>) `= -16`<br> The provided cloud project number is invalid. |
| `static final int` | [`GOOGLE_SERVER_UNAVAILABLE`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#GOOGLE_SERVER_UNAVAILABLE>) `= -12`<br> Unknown internal Google server error. |
| `static final int` | [`INTEGRITY_TOKEN_PROVIDER_INVALID`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#INTEGRITY_TOKEN_PROVIDER_INVALID>) `= -19`<br> The `StandardIntegrityTokenProvider` is invalid (e.g. it is outdated). |
| `static final int` | [`INTERNAL_ERROR`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#INTERNAL_ERROR>) `= -100`<br> Unknown internal error. |
| `static final int` | [`NETWORK_ERROR`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#NETWORK_ERROR>) `= -3`<br> No available network is found. |
| `static final int` | [`NO_ERROR`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#NO_ERROR>) `= 0` |
| `static final int` | [`PLAY_SERVICES_NOT_FOUND`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#PLAY_SERVICES_NOT_FOUND>) `= -6`<br> Play Services is not available or version is too old. |
| `static final int` | [`PLAY_SERVICES_VERSION_OUTDATED`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#PLAY_SERVICES_VERSION_OUTDATED>) `= -15`<br> Play Services needs to be updated. |
| `static final int` | [`PLAY_STORE_NOT_FOUND`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#PLAY_STORE_NOT_FOUND>) `= -2`<br> No Play Store app is found on device or not official version is installed. |
| `static final int` | [`PLAY_STORE_VERSION_OUTDATED`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#PLAY_STORE_VERSION_OUTDATED>) `= -14`<br> The Play Store needs to be updated. |
| `static final int` | [`REQUEST_HASH_TOO_LONG`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#REQUEST_HASH_TOO_LONG>) `= -17`<br> The provided request hash is too long. |
| `static final int` | [`TOO_MANY_REQUESTS`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#TOO_MANY_REQUESTS>) `= -8`<br> The calling app has made too many requests to the API and has been throttled, or your app has exceeded its daily request quota. |

## Constants

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode).
