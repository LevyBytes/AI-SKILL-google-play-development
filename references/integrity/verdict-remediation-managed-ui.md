This step uses the token and backend decision from [request bootstrap](verdict-remediation-bootstrap.md) and [dialog-code selection](verdict-remediation-code-selection.md). Recheck the verdict after the dialog closes.

4. On your app, call `showDialog` with the requested code retrieved from your server:

   **Kotlin**

   ```kotlin
   // Show dialog as indicated by the server
   val showDialogType: Int? = yourServerResponse.integrityDialogTypeCode()
   if (showDialogType == null) {
        return
   }

   // Create dialog request
   val dialogRequest = StandardIntegrityDialogRequest.builder()
             .setActivity(activity)
             .setTypeCode(showDialogType)
             .setStandardIntegrityResponse(StandardIntegrityResponse.TokenResponse(token))
             .build()

   // Call showDialog, the dialog will be shown on top of the provided activity
   // and the task will complete when the dialog is closed.
   val result: Task<Int> = standardIntegrityManager.showDialog(dialogRequest)

   // Handle response code, call the Integrity API again to confirm that the
   // verdict issue has been resolved.
   ```

   **Java**

   ```java
   // Show dialog as indicated by the server
   @Nullable Integer showDialogType = yourServerResponse.integrityDialogTypeCode();
   if (showDialogType == null) {
        return;
   }

   // Create dialog request
   StandardIntegrityDialogRequest dialogRequest =
         StandardIntegrityDialogRequest.builder()
             .setActivity(getActivity())
             .setTypeCode(showDialogTypeCode)
             .setStandardIntegrityResponse(new StandardIntegrityResponse.TokenResponse(token))
             .build();

   // Call showDialog, the dialog will be shown on top of the provided activity
   // and the task will complete when the dialog is closed.
   Task<Integer> result = standardIntegrityManager.showDialog(dialogRequest);

   // Handle response code, call the Integrity API again to confirm that the
   // verdict issue has been resolved.
   ```

   **Unity**

   ```c#
   // Initialize the V2 manager. Requires Play Integrity Unity Plugin v2.0.0 or
   // higher.
   var standardIntegrityManager = new StandardIntegrityManagerV2();
   IEnumerator ShowDialogCoroutine() {
       int showDialogType = yourServerResponse.IntegrityDialogTypeCode();

       PlayAsyncOperation<IntegrityDialogResponseCode, StandardIntegrityError> showDialogTask;

       using (var activity = UnityPlayerHelper.GetCurrentActivity())
       {
           // Create a dialog request
           var dialogRequest = new StandardIntegrityDialogRequest(tokenResponse, activity, showDialogType);

           // Call showDialog with the request, the dialog will be shown on top of the
           // provided activity and complete when the dialog is closed.
           showDialogTask = standardIntegrityManager.ShowDialog(dialogRequest);
       }

       // Wait for PlayAsyncOperation to complete.
       yield return showDialogTask;

       // Handle response code, call the Integrity API again to confirm that the
       // verdict issue been resolved.
   }
   ```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/remediation).
