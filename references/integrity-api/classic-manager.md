```text
public interface IntegrityManager
```

---

Manages requests for integrity information.

## Summary

### Public methods

| Declaration | Description |
| --- | --- |
| `abstract` [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>)`<`[`IntegrityTokenResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenResponse>)`>` | [`requestIntegrityToken`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityManager#requestIntegrityToken(com.google.android.play.core.integrity.IntegrityTokenRequest)>)`(`[`IntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest>) `request)`<br> Generates and returns a token for integrity-related enquiries. |
| `abstract` [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>)`<`[`Integer`](<https://developer.android.com/reference/java/lang/Integer.html>)`>` | [`showDialog`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityManager#showDialog(com.google.android.play.core.integrity.IntegrityDialogRequest)>)`(`[`IntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest>) `request)`<br> Displays a dialog to the user. |

## Public methods

### requestIntegrityToken

```text
abstract Task<IntegrityTokenResponse> requestIntegrityToken(IntegrityTokenRequest request)
```

Generates and returns a token for integrity-related enquiries.

The JSON payload is signed and encrypted as a nested JWT, that is [JWE](<https://tools.ietf.org/html/rfc7516>) of [JWS](<https://tools.ietf.org/html/rfc7515>).

JWE uses [A256KW](<https://tools.ietf.org/html/rfc7518#section-4.4>) as a key wrapping algorithm and [A256GCM](<https://tools.ietf.org/html/rfc7518#section-5.3>) as a content encryption algorithm. JWS uses [ES256](<https://tools.ietf.org/html/rfc7518#section-3.4>) as a signing algorithm.

All decryption and verification should be done within a secure server environment. Do not decrypt or verify the received token from within the client app. In particular, never expose any decryption keys to the client app.

See https://developer.android.com/google/play/integrity/verdict#token-format.

| Parameters |  |
| --- | --- |
| [`IntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenRequest>) `request` | the object to request integrity token with. |

| Returns |  |
| --- | --- |
| [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>)`<`[`IntegrityTokenResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenResponse>)`>` | A [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>) that completes once the requestIntegrityToken flow succeeded or failed. |

### showDialog

```text
abstract Task<Integer> showDialog(IntegrityDialogRequest request)
```

Displays a dialog to the user.

This method can only be called once per `IntegrityDialogRequest.IntegrityResponse`.

**Note:** Added in library version 1.5.0.

Since 1.5.0

| Parameters |  |
| --- | --- |
| [`IntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest>) `request` | contains the configuration for the dialog to be shown. |

| Returns |  |
| --- | --- |
| [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>)`<`[`Integer`](<https://developer.android.com/reference/java/lang/Integer.html>)`>` | A [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>) that completes with a [`IntegrityDialogResponseCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogResponseCode>) once the showDialog flow succeeded or failed. |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityManager).
