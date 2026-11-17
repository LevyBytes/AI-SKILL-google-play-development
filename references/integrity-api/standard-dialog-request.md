```text
public abstract class StandardIntegrityManager.StandardIntegrityDialogRequest
```

---

Request for `StandardIntegrityManager#showDialog(StandardIntegrityDialogRequest)`.

Since 1.5.0

## Summary

### Nested types

| Entry |
| --- |
| `public abstract class` [`StandardIntegrityManager.StandardIntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder>)<br> Builder for [`StandardIntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest>). |
| `public abstract class` [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse>)<br> Encapsulates the result of a standard integrity check so it can be used to build a [`StandardIntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest>). |
| `public final class` [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.ExceptionDetails`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.ExceptionDetails>) `extends` [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse>)<br> Represents a failed integrity check, containing the [`StandardIntegrityException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException>). |
| `public final class` [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.TokenResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.TokenResponse>) `extends` [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse>)<br> Represents a successful integrity check, containing the [`StandardIntegrityToken`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityToken>). |

### Public constructors

| Entry |
| --- |
| [`StandardIntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest#StandardIntegrityDialogRequest()>)`()` |

### Public methods

| Declaration | Description |
| --- | --- |
| `abstract` [`Activity`](<https://developer.android.com/reference/android/app/Activity.html>) | [`activity`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest#activity()>)`()`<br> The activity to be used to show the dialog. |
| `static` [`StandardIntegrityManager.StandardIntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder>) | [`builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest#builder()>)`()`<br> Creates [`StandardIntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder>). |
| `abstract` [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse>) | [`standardIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest#standardIntegrityResponse()>)`()`<br> The integrity check outcome for the dialog request. |
| `abstract int` | [`typeCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest#typeCode()>)`()`<br> The type of the integrity dialog to be shown. |

## Public constructors

### StandardIntegrityDialogRequest

```text
public StandardIntegrityDialogRequest()
```

## Public methods

### activity

```text
public abstract Activity activity()
```

The activity to be used to show the dialog.

See the details `Builder#setActivity(Activity)`.

### builder

```text
public static StandardIntegrityManager.StandardIntegrityDialogRequest.Builder builder()
```

Creates `StandardIntegrityDialogRequest.Builder`.

### standardIntegrityResponse

```text
public abstract StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse standardIntegrityResponse()
```

The integrity check outcome for the dialog request.

See the details `Builder#setStandardIntegrityResponse(StandardIntegrityResponse)`.

### typeCode

```text
public abstract int typeCode()
```

The type of the integrity dialog to be shown.

See the details `Builder#setTypeCode(int)`.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest).
