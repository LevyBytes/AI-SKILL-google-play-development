```text
public final class IntegrityDialogRequest.IntegrityResponse.ExceptionDetails extends IntegrityDialogRequest.IntegrityResponse
```

| Entry | Details | Details |
| --- | --- | --- |
| [java.lang.Object](<https://developer.android.com/reference/java/lang/Object.html>) | [java.lang.Object](<https://developer.android.com/reference/java/lang/Object.html>) | [java.lang.Object](<https://developer.android.com/reference/java/lang/Object.html>) |
| ↳ | [com.google.android.play.core.integrity.IntegrityDialogRequest.IntegrityResponse](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse>) | [com.google.android.play.core.integrity.IntegrityDialogRequest.IntegrityResponse](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse>) |
|  | ↳ | [com.google.android.play.core.integrity.IntegrityDialogRequest.IntegrityResponse.ExceptionDetails](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse.ExceptionDetails>) |

---

Represents a failed integrity check, containing the `IntegrityServiceException`.

## Summary

### Public constructors

| Entry |
| --- |
| [`ExceptionDetails`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse.ExceptionDetails#ExceptionDetails(com.google.android.play.core.integrity.IntegrityServiceException)>)`(`[`IntegrityServiceException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityServiceException>) `exception)` |

### Public methods

| Declaration | Description |
| --- | --- |
| [`IntegrityServiceException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityServiceException>) | [`getException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse.ExceptionDetails#getException()>)`()`<br> Returns the associated [`IntegrityServiceException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityServiceException>). |

## Public constructors

### ExceptionDetails

```text
public ExceptionDetails(IntegrityServiceException exception)
```

## Public methods

### getException

```text
public IntegrityServiceException getException()
```

Returns the associated `IntegrityServiceException`.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityDialogRequest.IntegrityResponse.ExceptionDetails).
