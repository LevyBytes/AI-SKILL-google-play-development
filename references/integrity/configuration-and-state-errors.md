### [`CLOUD_PROJECT_NUMBER_IS_INVALID`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#CLOUD_PROJECT_NUMBER_IS_INVALID>) (Error Code -16)

The provided cloud project number is invalid.

#### Possible resolution

Use the Cloud project number for the Cloud project for which you enabled Play Integrity API.

#### See also

See [`CLOUD_PROJECT_NUMBER_IS_INVALID`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#CLOUD_PROJECT_NUMBER_IS_INVALID>) for classic request.

### [`REQUEST_HASH_TOO_LONG`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#REQUEST_HASH_TOO_LONG>) (Error Code -17)

**Note:** This is only reported when using standard request through `StandardIntegrityErrorCode`.

The provided `requestHash` is too long. The `requestHash` length must be less than 500 characters.

#### Possible resolution

Retry with a shorter `requestHash`.

### [`INTEGRITY_TOKEN_PROVIDER_INVALID`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#INTEGRITY_TOKEN_PROVIDER_INVALID>) (Error Code -19)

**Note:** This is only reported for standard request through `StandardIntegrityErrorCode`.

The `StandardIntegrityTokenProvider` is no longer valid. This can happen because the token provider expired or the user cleared the Play Store app's data, which removed the token provider.

This error code is available only for Standard API requests, where it is supported as of library version 1.3.0 for the Kotlin and Java programming languages, Google Play Integrity Plugin for Unity 1.3.0 or higher and Play Core Native SDK 1.13.0 or higher.

#### Possible resolution

Request a new integrity token provider.

### [`STANDARD_INTEGRITY_INITIALIZATION_NEEDED`](<https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggade0d369f226c3a93cb70dbeba6b89601aa8faf582b855a79456116940366c1b63>) (Error Code -101)

`StandardIntegrityManager` is not initialized.

#### Possible resolution

Call [`StandardIntegrityManager_init()`](<https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1gaaf0091c762d6849a6906a3f21ea22671>) first.

#### See also

See [`INTEGRITY_INITIALIZATION_NEEDED`](<https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggaf9eae9c6d1e03ee0d21395087c0bfac1ad76b1d459925665e0ab487ec30e6fb4c>) for Classic Requests

### [`STANDARD_INTEGRITY_INVALID_ARGUMENT`](<https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggade0d369f226c3a93cb70dbeba6b89601a78857bcc3411049517d5eac4af9115c8>) (Error Code -103)

Invalid argument passed to the Standard Integrity API.

#### Possible resolution

Retry with the correct argument.

#### See also

See [`INTEGRITY_INVALID_ARGUMENT`](<https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggaf9eae9c6d1e03ee0d21395087c0bfac1a996161e5beb0d9669bebe448e0f1e468>) for Classic Requests.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/error-codes).
