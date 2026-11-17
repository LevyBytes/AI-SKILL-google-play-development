## Error codes you can retry

The cause of these errors is sometimes due to transient conditions, and thus you should retry the call.

### [`NETWORK_ERROR`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#NETWORK_ERROR>) (Error Code -3)

This error indicates that there was a problem with the network connection between the device and Play systems.

#### Possible resolution

1. Use the [`GET_INTEGRITY`](<https://developer.android.com/google/play/integrity/remediation#get-integrity-dialog>) or [`GET_STRONG_INTEGRITY`](<https://developer.android.com/google/play/integrity/remediation#get-strong-integrity-dialog>) dialog to initiate a Play-guided experience that helps the user establish and confirm network connectivity.
2. Ask the user to check for network connectivity, and use basic retries or exponential backoff, depending on which action triggered the error.

#### See also

[`NETWORK_ERROR`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#NETWORK_ERROR>) for classic requests.

### [`TOO_MANY_REQUESTS`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#TOO_MANY_REQUESTS>) (Error Code -8)

The calling app is making too many requests to the API and has been throttled, or your app has exceeded its daily request quota.

#### Possible resolution

1. Retry with an exponential backoff.
2. Request to [increase your daily maximum](<https://developer.android.com/google/play/integrity/setup#increase-daily>) number of requests

#### See also

[`TOO_MANY_REQUESTS`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#TOO_MANY_REQUESTS>) for classic requests.

### [`GOOGLE_SERVER_UNAVAILABLE`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#GOOGLE_SERVER_UNAVAILABLE>) (Error Code -12)

Unknown internal Google server error.

#### Possible resolution

Retry with an exponential backoff. Consider [filing a bug](<https://issuetracker.google.com/issues/new?component=1152695&template=1655477>) if it fails consistently.

#### See also

[`GOOGLE_SERVER_UNAVAILABLE`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#GOOGLE_SERVER_UNAVAILABLE>) for classic requests.

### [`CLIENT_TRANSIENT_ERROR`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#CLIENT_TRANSIENT_ERROR>) (Error Code -18)

Transient error has occurred on the client device.

For Standard API requests, this is supported as of version 1.3.0 of the [Play Integrity API library for Kotlin and Java](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/release-notes#1-3-0>), [Google Play Integrity Plugin for Unity](<https://developers.google.com/unity/packages#play_integrity_api>) 1.3.0 or higher and [Play Core Native SDK](<https://developer.android.com/guide/playcore/native#play_core_native_sdk>) 1.13.0 or higher.

#### Possible resolution

Retry with an exponential backoff.

#### See also

[`CLIENT_TRANSIENT_ERROR`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#CLIENT_TRANSIENT_ERROR>) for classic requests.

**Note:** When reported while using a Classic API request, the value returned is -17.

### [`INTERNAL_ERROR`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/StandardIntegrityErrorCode#INTERNAL_ERROR>) (Error Code -100)

Unknown internal error.

#### Possible resolution

Retry with an exponential backoff. Consider filing a bug if it fails consistently.

#### See also

[`INTERNAL_ERROR`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityErrorCode#INTERNAL_ERROR>) for classic requests.

### [`STANDARD_INTEGRITY_INTERNAL_ERROR`](<https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggade0d369f226c3a93cb70dbeba6b89601a7430edd4361bdca9585a38971c32174f>) (Error Code -100)

Unknown internal error.

#### Possible resolution

Retry with an exponential backoff. Consider filing a bug if it fails consistently.

#### See also

See [`INTEGRITY_INTERNAL_ERROR`](<https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggaf9eae9c6d1e03ee0d21395087c0bfac1a5e97a5a309ee2448717440633b9fab87>) for classic requests.

### [`STANDARD_INTEGRITY_INITIALIZATION_FAILED`](<https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggade0d369f226c3a93cb70dbeba6b89601ac3439c555b8c3b4996f518e255e5a45a>) (Error Code -102)

There was an error initializing the Standard Integrity API.

#### Possible resolution

Retry with an exponential backoff. Consider filing a bug if it fails consistently.

#### See also

See [`INTEGRITY_INITIALIZATION_FAILED`](<https://developer.android.com/reference/native/play/core/group/integrity#group__integrity_1ggaf9eae9c6d1e03ee0d21395087c0bfac1a5e97a5a309ee2448717440633b9fab87>) for classic requests.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/error-codes).
