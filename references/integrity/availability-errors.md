## Error codes not to retry

Automatic retries are unlikely to help in these cases. However, a manual retry may help if the user addresses the condition that caused the issue. For example, if the user updates their Play Store version to a supported version, then a manual retry of the initial operation could work.

### [`API_NOT_AVAILABLE`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#API_NOT_AVAILABLE>) (Error Code -1)

The Play Store version installed on the device might be old and the Integrity API not available. Another possibility is that Integrity API is not enabled in Google Play Console.

#### Possible resolution

- Make sure that Integrity API is enabled in Google Play Console.
- Ask the user to update the Play Store.

#### See also

See [`API_NOT_AVAILABLE`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#API_NOT_AVAILABLE>) for classic request.

### [`PLAY_STORE_NOT_FOUND`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#PLAY_STORE_NOT_FOUND>) (Error Code -2)

No official Play Store app was found on the device.

#### Possible resolution

Ask the user to install or enable Google Play Store.

#### See also

See [`PLAY_STORE_NOT_FOUND`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#PLAY_STORE_NOT_FOUND>) for classic request.

### [`PLAY_STORE_ACCOUNT_NOT_FOUND`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#PLAY_STORE_ACCOUNT_NOT_FOUND>) (Error Code -4)

**Note:** This is only reported for classic request through `IntegrityErrorCode`.

No Play Store account is found on the device. Note that the Play Integrity API now supports unauthenticated requests. This error code is used only for older Play Store versions that lack support.

#### Possible resolution

Ask the user to update and sign in to the Google Play Store.

### [`APP_NOT_INSTALLED`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#APP_NOT_INSTALLED>) (Error Code -5)

The calling app is not installed. Something is wrong (possibly an attack).

#### Possible resolution

Non-actionable. Treat the outcome as if the client has failed all integrity checks.

#### See also

See [`APP_NOT_INSTALLED`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#APP_NOT_INSTALLED>) for classic request.

### [`PLAY_SERVICES_NOT_FOUND`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#PLAY_SERVICES_NOT_FOUND>) (Error Code -6)

Play services are unavailable or need to be updated.

#### Possible resolution

1. Use the [`GET_INTEGRITY`](<https://developer.android.com/google/play/integrity/remediation#get-integrity-dialog>) or [`GET_STRONG_INTEGRITY`](<https://developer.android.com/google/play/integrity/remediation#get-strong-integrity-dialog>) dialog to initiate a Play-guided experience that helps the user to install, update or enable Play services.
2. Ask the user to install, update, or enable Play services.

#### See also

See [`APP_NOT_INSTALLED`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#PLAY_SERVICES_NOT_FOUND>) for classic request.

### [`APP_UID_MISMATCH`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#APP_UID_MISMATCH>) (Error Code -7)

The calling app UID (user ID) does not match the one from Package Manager.

#### Possible resolution

Non-actionable. Treat the outcome as if the client has failed all integrity checks.

#### See also

See [`APP_UID_MISMATCH`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#APP_UID_MISMATCH>) for classic request.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/error-codes).
