```text
public final class StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.ExceptionDetails extends StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse
```

| Entry | Details | Details |
| --- | --- | --- |
| [java.lang.Object](<https://developer.android.com/reference/java/lang/Object.html>) | [java.lang.Object](<https://developer.android.com/reference/java/lang/Object.html>) | [java.lang.Object](<https://developer.android.com/reference/java/lang/Object.html>) |
| ↳ | [com.google.android.play.core.integrity.StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse>) | [com.google.android.play.core.integrity.StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse>) |
|  | ↳ | [com.google.android.play.core.integrity.StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.ExceptionDetails](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.ExceptionDetails>) |

---

Represents a failed integrity check, containing the `StandardIntegrityException`.

## Summary

### Public constructors

| Entry |
| --- |
| [`ExceptionDetails`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.ExceptionDetails#ExceptionDetails(com.google.android.play.core.integrity.StandardIntegrityException)>)`(`[`StandardIntegrityException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException>) `exception)` |

### Public methods

| Declaration | Description |
| --- | --- |
| [`StandardIntegrityException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException>) | [`getException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.ExceptionDetails#getException()>)`()`<br> Returns the associated [`StandardIntegrityException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException>). |

## Public constructors

### ExceptionDetails

```text
public ExceptionDetails(StandardIntegrityException exception)
```

## Public methods

### getException

```text
public StandardIntegrityException getException()
```

Returns the associated `StandardIntegrityException`.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityDialogRequest.StandardIntegrityResponse.ExceptionDetails).
