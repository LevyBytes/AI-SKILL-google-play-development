```text
public abstract class StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder
```

---

Builder for `PrepareIntegrityTokenRequest`.

## Summary

### Public constructors

| Entry |
| --- |
| [`Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder#Builder()>)`()` |

### Public methods

| Declaration | Description |
| --- | --- |
| `abstract` [`StandardIntegrityManager.PrepareIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest>) | [`build`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder#build()>)`()`<br> Builds a [`PrepareIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest>). |
| `abstract` [`StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder>) | [`setCloudProjectNumber`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder#setCloudProjectNumber(long)>)`(long value)`<br> A cloud project number to link to the integrity token. |
| `abstract` [`StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder>) | [`setWebViewRequestMode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder#setWebViewRequestMode(int)>)`(int value)`<br> The WebView request mode to apply during token preparation. |

## Public constructors

### Builder

```text
public Builder()
```

## Public methods

### build

```text
public abstract StandardIntegrityManager.PrepareIntegrityTokenRequest build()
```

Builds a `PrepareIntegrityTokenRequest`.

### setCloudProjectNumber

```text
public abstract StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder setCloudProjectNumber(long value)
```

A cloud project number to link to the integrity token.

This field is required.

Cloud project number can be found in Project info in your Google Cloud Console for the cloud project where Play Integrity API is enabled.

Calls to [decrypt the token on Google's server](<https://developer.android.com/google/play/integrity/verdict#decrypt-verify-google-servers>) must be authenticated using the cloud account that was linked to the token in this request.

### setWebViewRequestMode

```text
public abstract StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder setWebViewRequestMode(int value)
```

The WebView request mode to apply during token preparation.

This parameter is only used for advanced system use cases and must be left unspecified by app, game, or SDK developers.

A standard integrity WebView request mode that allows WebView to specify a subset of integrity verdicts to be received. The available values can be found in the `StandardIntegrityWebViewRequestMode`.

Caller must be allowlisted to be able to call the standard integrity API using this mode.

Unspecified by default.

Since 1.6.0

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder).
