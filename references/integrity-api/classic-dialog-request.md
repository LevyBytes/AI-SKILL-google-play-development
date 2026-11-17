```text
public abstract class IntegrityDialogRequest
```

---

Request for `IntegrityManager#showDialog(IntegrityDialogRequest)`.

Since 1.5.0

## Summary

### Nested types

| Entry |
| --- |
| `public abstract class` [`IntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.Builder>)<br> Builder for [`IntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest>). |
| `public abstract class` [`IntegrityDialogRequest.IntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse>)<br> Encapsulates the result of an integrity check so it can be used to build an [`IntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest>). |
| `public final class` [`IntegrityDialogRequest.IntegrityResponse.ExceptionDetails`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse.ExceptionDetails>) `extends` [`IntegrityDialogRequest.IntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse>)<br> Represents a failed integrity check, containing the [`IntegrityServiceException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityServiceException>). |
| `public final class` [`IntegrityDialogRequest.IntegrityResponse.TokenResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse.TokenResponse>) `extends` [`IntegrityDialogRequest.IntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse>)<br> Represents a successful integrity check, containing the [`IntegrityTokenResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenResponse>). |

### Public constructors

| Entry |
| --- |
| [`IntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest#IntegrityDialogRequest()>)`()` |

### Public methods

| Declaration | Description |
| --- | --- |
| `abstract` [`Activity`](<https://developer.android.com/reference/android/app/Activity.html>) | [`activity`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest#activity()>)`()`<br> The activity to be used to show the dialog. |
| `static` [`IntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.Builder>) | [`builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest#builder()>)`()`<br> Creates [`IntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.Builder>). |
| `abstract` [`IntegrityDialogRequest.IntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse>) | [`integrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest#integrityResponse()>)`()`<br> The previous integrity check outcome for the dialog request. |
| `abstract int` | [`typeCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest#typeCode()>)`()`<br> The type of the integrity dialog to be shown. |

## Public constructors

### IntegrityDialogRequest

```text
public IntegrityDialogRequest()
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
public static IntegrityDialogRequest.Builder builder()
```

Creates `IntegrityDialogRequest.Builder`.

### integrityResponse

```text
public abstract IntegrityDialogRequest.IntegrityResponse integrityResponse()
```

The previous integrity check outcome for the dialog request.

See the details `Builder#setIntegrityResponse(IntegrityResponse)`.

### typeCode

```text
public abstract int typeCode()
```

The type of the integrity dialog to be shown.

See the details `Builder#setTypeCode(int)`.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest).
