```text
public interface StandardIntegrityManager
```

---

Manages requests for integrity information.

## Summary

### Nested types

| Entry |
| --- |
| `public abstract class` [`StandardIntegrityManager.PrepareIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest>)<br> Request for [`prepareIntegrityToken`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager#prepareIntegrityToken(com.google.android.play.core.integrity.StandardIntegrityManager.PrepareIntegrityTokenRequest)>). |
| `public abstract class` [`StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest.Builder>)<br> Builder for [`PrepareIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest>). |
| `public abstract class` [`StandardIntegrityManager.StandardIntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest>)<br> Request for [`StandardIntegrityManager#showDialog(StandardIntegrityDialogRequest)`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager#showDialog(com.google.android.play.core.integrity.StandardIntegrityManager.StandardIntegrityDialogRequest)>). |
| `public abstract class` [`StandardIntegrityManager.StandardIntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder>)<br> Builder for [`StandardIntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest>). |
| `public abstract class` [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse>)<br> Encapsulates the result of a standard integrity check so it can be used to build a [`StandardIntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest>). |
| `public final class` [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.ExceptionDetails`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.ExceptionDetails>) `extends` [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse>)<br> Represents a failed integrity check, containing the [`StandardIntegrityException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException>). |
| `public final class` [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.TokenResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.TokenResponse>) `extends` [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse>)<br> Represents a successful integrity check, containing the [`StandardIntegrityToken`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityToken>). |
| `public abstract class` [`StandardIntegrityManager.StandardIntegrityToken`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityToken>)<br> Response of [`StandardIntegrityTokenProvider#request(StandardIntegrityTokenRequest)`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenProvider#request(com.google.android.play.core.integrity.StandardIntegrityManager.StandardIntegrityTokenRequest)>). |
| `public interface` [`StandardIntegrityManager.StandardIntegrityTokenProvider`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenProvider>)<br> Standard integrity token provider. |
| `public abstract class` [`StandardIntegrityManager.StandardIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest>)<br> Request for [`StandardIntegrityTokenProvider#request(StandardIntegrityTokenRequest)`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenProvider#request(com.google.android.play.core.integrity.StandardIntegrityManager.StandardIntegrityTokenRequest)>). |
| `public abstract class` [`StandardIntegrityManager.StandardIntegrityTokenRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest.Builder>)<br> Builder for [`StandardIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenRequest>). |

### Public methods

| Declaration | Description |
| --- | --- |
| `abstract` [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>)`<`[`StandardIntegrityManager.StandardIntegrityTokenProvider`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenProvider>)`>` | [`prepareIntegrityToken`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager#prepareIntegrityToken(com.google.android.play.core.integrity.StandardIntegrityManager.PrepareIntegrityTokenRequest)>)`(`<br> [`StandardIntegrityManager.PrepareIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest>) `request`<br>`)`<br> Prepares the integrity token and makes it available for requesting via [`StandardIntegrityTokenProvider`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenProvider>). |
| `abstract` [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>)`<`[`Integer`](<https://developer.android.com/reference/java/lang/Integer.html>)`>` | [`showDialog`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager#showDialog(com.google.android.play.core.integrity.StandardIntegrityManager.StandardIntegrityDialogRequest)>)`(`<br> [`StandardIntegrityManager.StandardIntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest>) `request`<br>`)`<br> Displays a dialog to the user. |

## Public methods

### prepareIntegrityToken

```text
abstract Task<StandardIntegrityManager.StandardIntegrityTokenProvider> prepareIntegrityToken(    StandardIntegrityManager.PrepareIntegrityTokenRequest request)
```

Prepares the integrity token and makes it available for requesting via `StandardIntegrityTokenProvider`.

You can call this method from time to time in order to refresh the resulting `StandardIntegrityTokenProvider`.

Note that this API makes a call to Google servers and hence requires a network connection.

| Parameters |  |
| --- | --- |
| [`StandardIntegrityManager.PrepareIntegrityTokenRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.PrepareIntegrityTokenRequest>) `request` | the object to prepare the integrity token with. |

| Returns |  |
| --- | --- |
| [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>)`<`[`StandardIntegrityManager.StandardIntegrityTokenProvider`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityTokenProvider>)`>` | A [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>) that completes once the prepareIntegrityToken flow succeeded or failed. In case of a failure, [`StandardIntegrityException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException>) wrapped with a [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>) will be thrown. |

### showDialog

```text
abstract Task<Integer> showDialog(    StandardIntegrityManager.StandardIntegrityDialogRequest request)
```

Displays a dialog to the user.

This method can only be called once per `StandardIntegrityDialogRequest.StandardIntegrityResponse`.

**Note:** Added in library version 1.5.0.

Since 1.5.0

| Parameters |  |
| --- | --- |
| [`StandardIntegrityManager.StandardIntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest>) `request` | contains the configuration for the dialog to be shown. |

| Returns |  |
| --- | --- |
| [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>)`<`[`Integer`](<https://developer.android.com/reference/java/lang/Integer.html>)`>` | A [`Task`](<https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html>) that completes with a [`IntegrityDialogResponseCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogResponseCode>) once the showDialog flow succeeded or failed. |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager).
