```text
public abstract class IntegrityDialogRequest.Builder
```

---

Builder for `IntegrityDialogRequest`.

## Summary

### Public constructors

| Entry |
| --- |
| [`Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.Builder#Builder()>)`()` |

### Public methods

| Declaration | Description |
| --- | --- |
| `abstract` [`IntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest>) | [`build`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.Builder#build()>)`()`<br> Builds an [`IntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest>). |
| `abstract` [`IntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.Builder>) | [`setActivity`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.Builder#setActivity(android.app.Activity)>)`(`[`Activity`](<https://developer.android.com/reference/android/app/Activity.html>) `activity)`<br> Sets the activity to be used to show the dialog. |
| `abstract` [`IntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.Builder>) | [`setIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.Builder#setIntegrityResponse(com.google.android.play.core.integrity.IntegrityDialogRequest.IntegrityResponse)>)`(`<br> [`IntegrityDialogRequest.IntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse>) `integrityResponse`<br>`)`<br> Sets the previous integrity check outcome for the dialog request. |
| `abstract` [`IntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.Builder>) | [`setTypeCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.Builder#setTypeCode(int)>)`(int typeCode)`<br> Sets the dialog type. |

## Public constructors

### Builder

```text
public Builder()
```

## Public methods

### build

```text
public abstract IntegrityDialogRequest build()
```

Builds an `IntegrityDialogRequest`.

### setActivity

```text
public abstract IntegrityDialogRequest.Builder setActivity(Activity activity)
```

Sets the activity to be used to show the dialog.

| Parameters |  |
| --- | --- |
| [`Activity`](<https://developer.android.com/reference/android/app/Activity.html>) `activity` | the android activity to be used to show the dialog. |

### setIntegrityResponse

```text
public abstract IntegrityDialogRequest.Builder setIntegrityResponse(    IntegrityDialogRequest.IntegrityResponse integrityResponse)
```

Sets the previous integrity check outcome for the dialog request.

| Parameters |  |
| --- | --- |
| [`IntegrityDialogRequest.IntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse>) `integrityResponse` | The [`IntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse>) representing either a successful [`IntegrityResponse.TokenResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse.TokenResponse>) or a failed [`IntegrityResponse.ExceptionDetails`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse.ExceptionDetails>). |

### setTypeCode

```text
public abstract IntegrityDialogRequest.Builder setTypeCode(int typeCode)
```

Sets the dialog type.

| Parameters |  |
| --- | --- |
| `int typeCode` | determines which [`IntegrityDialogTypeCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode>) should be shown. |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.Builder).
