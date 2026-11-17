```text
public class StandardIntegrityException extends ApiException
```

Inheritance: [`java.lang.Object`](<https://developer.android.com/reference/java/lang/Object.html>) → [`kotlin.Throwable`](<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-throwable/index.html>) → [`java.lang.Exception`](<https://developer.android.com/reference/java/lang/Exception.html>) → [`com.google.android.gms.common.api.ApiException`](<https://developers.google.com/android/reference/com/google/android/gms/common/api/ApiException.html>) → [`com.google.android.play.core.integrity.StandardIntegrityException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException>).

---

An exception indicating something went wrong with the Standard Integrity API.

See `getErrorCode` for the specific problem.

## Summary

### Public constructors

| Entry |
| --- |
| [`StandardIntegrityException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException#StandardIntegrityException(int)>)`(int errorCode)`<br> Constructs an `StandardIntegrityException` with the specified error code. |

### Public methods

| Declaration | Description |
| --- | --- |
| `synchronized` [`Throwable`](<https://developer.android.com/reference/java/lang/Throwable.html>) | [`getCause`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException#getCause()>)`()` |
| `int` | [`getErrorCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException#getErrorCode()>)`()`<br> Returns the error code resulting from the operation. |
| `int` | [`getStatusCode`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException#getStatusCode()>)`()`<br> Returns the error code resulting from the operation. |
| `boolean` | [`isRemediable`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException#isRemediable()>)`()`<br> Returns whether the exception is remediable by the device integrity dialogs. |

### Inherited fields

From [com.google.android.gms.common.api.ApiException](<https://developers.google.com/android/reference/com/google/android/gms/common/api/ApiException.html>)

| Declaration | Description |
| --- | --- |
| `final` [`Status`](<https://developers.google.com/android/reference/com/google/android/gms/common/api/Status.html>) | [`mStatus`](<https://developers.google.com/android/reference/com/google/android/gms/common/api/ApiException.html#mStatus-->)<br> **This field is deprecated.** |

### Inherited methods

From [com.google.android.gms.common.api.ApiException](<https://developers.google.com/android/reference/com/google/android/gms/common/api/ApiException.html>)

| Declaration | Description |
| --- | --- |
| [`Status`](<https://developers.google.com/android/reference/com/google/android/gms/common/api/Status.html>) | [`getStatus`](<https://developers.google.com/android/reference/com/google/android/gms/common/api/ApiException.html#getStatus-->)`()` |
| [`String`](<https://developer.android.com/reference/java/lang/String.html>) | [`getStatusMessage`](<https://developers.google.com/android/reference/com/google/android/gms/common/api/ApiException.html#getStatusMessage-->)`()`<br> **This method is deprecated.** |

From [java.lang.Throwable](<https://developer.android.com/reference/java/lang/Throwable.html>)

| Declaration | Description |
| --- | --- |
| `synchronized final void` | [`addSuppressed`](<https://developer.android.com/reference/java/lang/Throwable.html#addSuppressed(java.lang.Throwable)>)`(`[`Throwable`](<https://developer.android.com/reference/java/lang/Throwable.html>) `p)` |
| `synchronized` [`Throwable`](<https://developer.android.com/reference/java/lang/Throwable.html>) | [`fillInStackTrace`](<https://developer.android.com/reference/java/lang/Throwable.html#fillInStackTrace()>)`()` |
| [`String`](<https://developer.android.com/reference/java/lang/String.html>) | [`getLocalizedMessage`](<https://developer.android.com/reference/java/lang/Throwable.html#getLocalizedMessage()>)`()` |
| [`String`](<https://developer.android.com/reference/java/lang/String.html>) | [`getMessage`](<https://developer.android.com/reference/java/lang/Throwable.html#getMessage()>)`()` |
| `StackTraceElement[]` | [`getStackTrace`](<https://developer.android.com/reference/java/lang/Throwable.html#getStackTrace()>)`()` |
| `synchronized final Throwable[]` | [`getSuppressed`](<https://developer.android.com/reference/java/lang/Throwable.html#getSuppressed()>)`()` |
| `synchronized` [`Throwable`](<https://developer.android.com/reference/java/lang/Throwable.html>) | [`initCause`](<https://developer.android.com/reference/java/lang/Throwable.html#initCause(java.lang.Throwable)>)`(`[`Throwable`](<https://developer.android.com/reference/java/lang/Throwable.html>) `p)` |
| `void` | [`printStackTrace`](<https://developer.android.com/reference/java/lang/Throwable.html#printStackTrace()>)`()` |
| `void` | [`setStackTrace`](<https://developer.android.com/reference/java/lang/Throwable.html#setStackTrace(java.lang.StackTraceElement[])>)`(StackTraceElement[] p)` |
| [`String`](<https://developer.android.com/reference/java/lang/String.html>) | [`toString`](<https://developer.android.com/reference/java/lang/Throwable.html#toString()>)`()` |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException).
