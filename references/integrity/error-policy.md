If your app makes a Play Integrity API request and the call fails, your app receives an error code. These errors can happen for various reasons, such as environmental issues like a poor network connection, problems with your API integration, or malicious activity and active attacks. The type of error code returned depends on the type of request:

- Standard requests: The API returns a [StandardIntegrityErrorCode](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode>).
- Classic requests: The API returns a [IntegrityErrorCode](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode>).

> **Note:** If the error is due to transient conditions, you should retry the call. If the conditions are not transient, you shouldn't retry the call.

## Retry strategies

Use exponential backoff for Play Integrity operations that happen in the background and don't affect the user experience while the user is in session.

For example, it is appropriate to implement this when acknowledging new purchases because this operation can happen in the background, and acknowledgment doesn't need to happen in real time if an error occurs.

After the first failure, start with an initial delay of 5 seconds before retrying.

Implement a retry strategy with a maximum number of attempts as an exit condition using an exponentially increased delay each time (10s, 20s).

While performing these retry attempts, check for a network connection and don't overload the device.

If you continue to see errors after three retry attempts, treat the outcome as if the client has failed all integrity checks. The error can be for several reasons, including (but not limited to): an overloaded device, network connection issues, or an attempt by an attacker.

## Error code values for the Java library

|  | [`IntegrityErrorCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode>) | [`StandardIntegrityErrorCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode>) |
| --- | --- | --- |
| -1 | [`API_NOT_AVAILABLE`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_1>) | [`API_NOT_AVAILABLE`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_1>) |
| -2 | [`PLAY_STORE_NOT_FOUND`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_2>) | [`PLAY_STORE_NOT_FOUND`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_2>) |
| -3 | [`NETWORK_ERROR`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_3>) | [`NETWORK_ERROR`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_3>) |
| -4 | [`PLAY_STORE_ACCOUNT_NOT_FOUND`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_4>) |  |
| -5 | [`APP_NOT_INSTALLED`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_5>) | [`APP_NOT_INSTALLED`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_5>) |
| -6 | [`PLAY_SERVICES_NOT_FOUND`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_6>) | [`PLAY_SERVICES_NOT_FOUND`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_6>) |
| -7 | [`APP_UID_MISMATCH`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_7>) | [`APP_UID_MISMATCH`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_7>) |
| -8 | [`TOO_MANY_REQUESTS`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_8>) | [`TOO_MANY_REQUESTS`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_8>) |
| -9 | [`CANNOT_BIND_TO_SERVICE`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_9>) | [`CANNOT_BIND_TO_SERVICE`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_9>) |
| -10 | [`NONCE_TOO_SHORT`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_10>) |  |
| -11 | [`NONCE_TOO_LONG`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_11>) |  |
| -12 | [`GOOGLE_SERVER_UNAVAILABLE`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_12>) | [`GOOGLE_SERVER_UNAVAILABLE`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_12>) |
| -13 | [`NONCE_IS_NOT_BASE64`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_13>) |  |
| -14 | [`PLAY_STORE_VERSION_OUTDATED`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_14>) | [`PLAY_STORE_VERSION_OUTDATED`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_14>) |
| -15 | [`PLAY_SERVICES_VERSION_OUTDATED`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_15>) | [`PLAY_SERVICES_VERSION_OUTDATED`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_15>) |
| -16 | [`CLOUD_PROJECT_NUMBER_IS_INVALID`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_16>) | [`CLOUD_PROJECT_NUMBER_IS_INVALID`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_16>) |
| -17 | [`CLIENT_TRANSIENT_ERROR`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_18>) | [`REQUEST_HASH_TOO_LONG`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_17>) |
| -18 |  | [`CLIENT_TRANSIENT_ERROR`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_18>) |
| -19 |  | [`INTEGRITY_TOKEN_PROVIDER_INVALID`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_19>) |
| -100 | [`INTERNAL_ERROR`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_100>) | [`INTERNAL_ERROR`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErr_100>) |

## Additional error code values for the native library

|  | [`IntegrityErrorCode`](<https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1gaf9eae9c6d1e03ee0d21395087c0bfac1>) | [`StandardIntegrityErrorCode`](<https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1gade0d369f226c3a93cb70dbeba6b89601>) |
| --- | --- | --- |
| -100 | [`INTEGRITY_INTERNAL_ERROR`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErrC100>) | [`STANDARD_INTEGRITY_INTERNAL_ERROR`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErrC100>) |
| -101 | [`INTEGRITY_INITIALIZATION_NEEDED`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErrC101>) | [`STANDARD_INTEGRITY_INITIALIZATION_NEEDED`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErrC101>) |
| -102 | [`INTEGRITY_INITIALIZATION_FAILED`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErrC102>) | [`STANDARD_INTEGRITY_INITIALIZATION_FAILED`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErrC102>) |
| -103 | [`INTEGRITY_INVALID_ARGUMENT`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErrC103>) | [`STANDARD_INTEGRITY_INVALID_ARGUMENT`](<https://developer.android.com/google/play/integrity/error-codes?hl=en#iErrC103>) |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/error-codes).
