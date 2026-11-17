## Request an integrity dialog to fix a client side exception

If an Integrity API request fails with a [`StandardIntegrityException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityException>) (Standard API) or [`IntegrityServiceException`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityServiceException>) (Classic API) and the exception is remediable, you can use either the [`GET_INTEGRITY`](<https://developer.android.com/google/play/integrity/remediation?hl=en#get-integrity-dialog>) or [`GET_STRONG_INTEGRITY`](<https://developer.android.com/google/play/integrity/remediation?hl=en#get-strong-integrity-dialog>) dialogs to fix the error.

> **Note:** Using the new `GET_INTEGRITY` or `GET_STRONG_INTEGRITY` dialogs requires the Integrity API Android library version 1.5.0 or higher. This update provides access to the new `showDialog` method in [`IntegrityManager`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityManager>) (Classic API) or [`StandardIntegrityManager`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager>) (Standard API) for resolving client-side exceptions.

The following steps outline how you can use the [`GET_INTEGRITY`](<https://developer.android.com/google/play/integrity/remediation?hl=en#get-integrity-dialog>) dialog to fix a remediable client side error reported by Integrity API.

1. Check that the exception returned from an Integrity API request is remediable.

   **Kotlin**

   ```kotlin
   private fun isExceptionRemediable(exception: ExecutionException): Boolean {
       val cause = exception.cause
       if (cause is StandardIntegrityException && cause.isRemediable) {
           return true
       }
       return false
   }
   ```

   **Java**

   ```java
   private boolean isExceptionRemediable(ExecutionException exception) {
       Throwable cause = exception.getCause();
       if (cause instanceof StandardIntegrityException integrityException
   && integrityException.isRemediable()) {
           return true;
       }
       return false;
   }
   ```

   **Unity**

   ```c#
   private bool IsExceptionRemediable(StandardIntegrityError error) {
       // Check if the operation resulted in a remediable error
       if (error != null && error.ErrorCode != StandardIntegrityErrorCode.NoError && error.IsRemediable) {
           return true;
       }
       return false;
   }
   ```

   **Native**

   ```c++
   bool IsErrorRemediable(StandardIntegrityToken* token) {
       /// Check if the error associated with the token is remediable
       bool isRemediable = false;
       if(StandardIntegrityToken_getIsRemediable(response, &isRemediable) == STANDARD_INTEGRITY_NO_ERROR){
         return isRemediable;
       }
       return false;
   }
   ```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/remediation).
