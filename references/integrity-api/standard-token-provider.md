```text
public interface StandardIntegrityManager.StandardIntegrityTokenProvider
```

---

Standard integrity token provider.

The instance is bound to `prepareIntegrityToken` call.

## Summary

### Public methods

| Declaration | Description |
| --- | --- |
| `abstract` [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>)`<`[`StandardIntegrityManager.StandardIntegrityToken`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityToken>)`>` | [`request`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenProvider#request(com.google.android.play.core.integrity.StandardIntegrityManager.StandardIntegrityTokenRequest)>)`(`<br> [`StandardIntegrityManager.StandardIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest>) `request`<br>`)`<br> Returns a token for integrity-related enquiries. |

## Public methods

### request

```text
abstract Task<StandardIntegrityManager.StandardIntegrityToken> request(    StandardIntegrityManager.StandardIntegrityTokenRequest request)
```

Returns a token for integrity-related enquiries.

This must be called only after `prepareIntegrityToken` completes.

| Parameters |  |
| --- | --- |
| [`StandardIntegrityManager.StandardIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest>) `request` | the object to request integrity token with. |

| Returns |  |
| --- | --- |
| [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>)`<`[`StandardIntegrityManager.StandardIntegrityToken`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityToken>)`>` | A [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>) that completes once the request flow succeeded or failed. In case of a failure, [`StandardIntegrityException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException>) wrapped with a [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>) will be thrown. |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenProvider).
