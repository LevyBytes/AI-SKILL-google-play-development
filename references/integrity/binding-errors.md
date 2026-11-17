### [`CANNOT_BIND_TO_SERVICE`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#CANNOT_BIND_TO_SERVICE>) (Error Code -9)

Binding to the service in the Play Store has failed. This can be due to having an old Play Store version installed on the device.

#### Possible resolution

Ask the user to update the Google Play Store.

#### See also

See [`CANNOT_BIND_TO_SERVICE`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#CANNOT_BIND_TO_SERVICE>) for classic request.

### [`NONCE_TOO_SHORT`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#NONCE_TOO_SHORT>) (Error Code -10)

**Note:** This is only reported for classic request through `IntegrityErrorCode`.

Nonce length is too short. The nonce must be a minimum of 16 bytes before base64 encoding.

#### Possible resolution

Retry with a longer nonce.

### [`NONCE_TOO_LONG`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#NONCE_TOO_LONG>) (Error Code -11)

**Note:** This is only reported for classic request through `IntegrityErrorCode`.

Nonce length is too long. The nonce must be less than 500 bytes before base64 encoding.

#### Possible resolution

Retry with a shorter nonce.

### [`NONCE_IS_NOT_BASE64`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#NONCE_IS_NOT_BASE64>) (Error Code -13)

**Note:** This is only reported for classic request through `IntegrityErrorCode`.

Nonce is not encoded as a base64 web-safe no-wrap string.

#### Possible resolution

Retry with a nonce in the correct format.

### [`PLAY_STORE_VERSION_OUTDATED`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#PLAY_STORE_VERSION_OUTDATED>) (Error Code -14)

Google Play Store app needs to be updated.

#### Possible resolution

Ask the user to update the Google Play Store.

#### See also

See [`PLAY_STORE_VERSION_OUTDATED`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#PLAY_STORE_VERSION_OUTDATED>) for classic request.

### [`PLAY_SERVICES_VERSION_OUTDATED`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#PLAY_SERVICES_VERSION_OUTDATED>) (Error Code -15)

Google Play services need to be updated.

#### Possible resolution

1. Use the [`GET_INTEGRITY`](<https://developer.android.com/google/play/integrity/remediation#get-integrity-dialog>) or [`GET_STRONG_INTEGRITY`](<https://developer.android.com/google/play/integrity/remediation#get-strong-integrity-dialog>) dialog to initiate a Play-guided experience that helps the user to update Google Play services.
2. Ask the user to update Google Play services.

#### See also

See [`PLAY_SERVICES_VERSION_OUTDATED`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#PLAY_SERVICES_VERSION_OUTDATED>) for classic request.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/error-codes).
