```text
public abstract class StandardIntegrityManager.StandardIntegrityDialogRequest.Builder
```

---

Builder for `StandardIntegrityDialogRequest`.

## Summary

### Public constructors

| Entry |
| --- |
| [`Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder#Builder()>)`()` |

### Public methods

| Declaration | Description |
| --- | --- |
| `abstract` [`StandardIntegrityManager.StandardIntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest>) | [`build`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder#build()>)`()`<br> Builds a [`StandardIntegrityDialogRequest`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest>). |
| `abstract` [`StandardIntegrityManager.StandardIntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder>) | [`setActivity`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder#setActivity(android.app.Activity)>)`(`[`Activity`](<https://developer.android.com/reference/android/app/Activity.html>) `activity)`<br> Sets the activity to be used to show the dialog. |
| `abstract` [`StandardIntegrityManager.StandardIntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder>) | [`setStandardIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder#setStandardIntegrityResponse(com.google.android.play.core.integrity.StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse)>)`(`<br> [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse>) `standardIntegrityResponse`<br>`)`<br> Sets the integrity check outcome for the dialog request. |
| `abstract` [`StandardIntegrityManager.StandardIntegrityDialogRequest.Builder`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder>) | [`setTypeCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder#setTypeCode(int)>)`(int typeCode)`<br> Sets the dialog type. |

## Public constructors

### Builder

```text
public Builder()
```

## Public methods

### build

```text
public abstract StandardIntegrityManager.StandardIntegrityDialogRequest build()
```

Builds a `StandardIntegrityDialogRequest`.

### setActivity

```text
public abstract StandardIntegrityManager.StandardIntegrityDialogRequest.Builder setActivity(Activity activity)
```

Sets the activity to be used to show the dialog.

| Parameters |  |
| --- | --- |
| [`Activity`](<https://developer.android.com/reference/android/app/Activity.html>) `activity` | the android activity to be used to show the dialog. |

### setStandardIntegrityResponse

```text
public abstract StandardIntegrityManager.StandardIntegrityDialogRequest.Builder setStandardIntegrityResponse(    StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse standardIntegrityResponse)
```

Sets the integrity check outcome for the dialog request.

| Parameters |  |
| --- | --- |
| [`StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse>) `standardIntegrityResponse` | The [`StandardIntegrityResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse>) representing either a successful [`StandardIntegrityResponse.TokenResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.TokenResponse>) or a failed [`StandardIntegrityResponse.ExceptionDetails`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.ExceptionDetails>). |

### setTypeCode

```text
public abstract StandardIntegrityManager.StandardIntegrityDialogRequest.Builder setTypeCode(int typeCode)
```

Sets the dialog type.

| Parameters |  |
| --- | --- |
| `int typeCode` | determines which [`IntegrityDialogTypeCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogTypeCode>) should be shown. |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.Builder).
