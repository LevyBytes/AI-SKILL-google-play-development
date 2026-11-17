```text
public abstract class IntegrityTokenRequest.Builder
```

---

Builder for `IntegrityTokenRequest`.

## Summary

### Public constructors

| Entry |
| --- |
| [`Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest.Builder#Builder()>)`()` |

### Public methods

| Declaration | Description |
| --- | --- |
| `abstract` [`IntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest>) | [`build`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest.Builder#build()>)`()`<br> Builds a [`IntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest>). |
| `abstract` [`IntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest.Builder>) | [`setCloudProjectNumber`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest.Builder#setCloudProjectNumber(long)>)`(long cloudProjectNumber)`<br> A cloud project number to link to the integrity token. |
| `abstract` [`IntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest.Builder>) | [`setNonce`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest.Builder#setNonce(java.lang.String)>)`(`[`String`](<https://developer.android.com/reference/java/lang/String.html>) `nonce)`<br> A nonce to bind the integrity token to. |

## Public constructors

### Builder

```text
public Builder()
```

## Public methods

### build

```text
public abstract IntegrityTokenRequest build()
```

Builds a `IntegrityTokenRequest`.

### setCloudProjectNumber

```text
public abstract IntegrityTokenRequest.Builder setCloudProjectNumber(long cloudProjectNumber)
```

A cloud project number to link to the integrity token.

This field is required for apps exclusively distributed outside of Google Play and SDKs. For apps distributed on Google Play, the cloud project number is configured in the Play Console and need not be set on the request.

Cloud project number can be found in Project info in your Google Cloud Console for the cloud project where Play Integrity API is enabled.

Calls to [decrypt the token on Google's server](<https://developer.android.com/google/play/integrity/classic#decrypt-verify-google-servers>) must be authenticated using the cloud account that was linked to the token in this request.

### setNonce

```text
public abstract IntegrityTokenRequest.Builder setNonce(String nonce)
```

A nonce to bind the integrity token to.

It must be base64 encoded in web-safe no-wrap form.

See [details](<https://developer.android.com/google/play/integrity/classic#nonce>) about the nonce requirements and recommendations.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest.Builder).
