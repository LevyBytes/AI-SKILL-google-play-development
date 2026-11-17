This step handles the exception captured by [exception remediation bootstrap](exception-remediation-bootstrap.md).

2. If the exception is remediable, request the `GET_INTEGRITY` dialog using the returned exception. The dialog will be displayed over the provided activity and the returned Task completes with a [response code](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogResponseCode>) after the user closes the dialog.

   **Kotlin**

   ```kotlin
     private fun showDialog(exception: StandardIntegrityException) {
         // Create a dialog request
         val standardIntegrityDialogRequest =
             StandardIntegrityDialogRequest.builder()
                 .setActivity(activity)
                 .setType(IntegrityDialogTypeCode.GET_INTEGRITY)
                 .setStandardIntegrityResponse(ExceptionDetails(exception))
                 .build()

         // Request dialog
         val responseCode: Task<Int> =
               standardIntegrityManager.showDialog(standardIntegrityDialogRequest)
   }
   ```

   **Java**

   ```java
     private void showDialog(StandardIntegrityException exception) {
         // Create a dialog request
         StandardIntegrityDialogRequest standardIntegrityDialogRequest =
             StandardIntegrityDialogRequest.builder()
                 .setActivity(this.activity)
                 .setType(IntegrityDialogTypeCode.GET_INTEGRITY)
                 .setStandardIntegrityResponse(new ExceptionDetails(exception))
                 .build();

         // Request dialog
         Task<Integer> responseCode =
               standardIntegrityManager.showDialog(standardIntegrityDialogRequest);
   }
   ```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/remediation).
