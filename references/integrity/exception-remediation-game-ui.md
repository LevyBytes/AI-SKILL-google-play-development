This step handles the exception captured by [exception remediation bootstrap](exception-remediation-bootstrap.md).

   **Unity**

   ```c#
   // Initialize the V2 manager. Requires Play Integrity Unity Plugin v2.0.0 or
   // higher.
   var standardIntegrityManager = new StandardIntegrityManagerV2();
   IEnumerator ShowDialogToFixError(StandardIntegrityError error) {
       PlayAsyncOperation<IntegrityDialogResponseCode, StandardIntegrityError> showDialogTask;

       using (var activity = UnityPlayerHelper.GetCurrentActivity())
       {
           // Create a dialog request using the error
           var dialogRequest = new StandardIntegrityDialogRequest(error, activity, GET_INTEGRITY_DIALOG);

           // Request dialog
           showDialogTask = standardIntegrityManager.ShowDialog(dialogRequest);
       }

       // Wait for PlayAsyncOperation to complete.
       yield return showDialogTask;
   }
   ```

   **Native**

   ```c++
   private void showDialogToFixError(StandardIntegrityToken* token) {
       /// If the token request failed, and the underlying error is not fixable
       /// then return early
       if(isErrorRemediable(token)) {
         return;
       }

       /// Create dialog request
       StandardIntegrityDialogRequest* dialog_request;
       StandardIntegrityDialogRequest_create(&dialog_request);
       StandardIntegrityDialogRequest_setTypeCode(dialog_request,
                                          kGetIntegrityDialogTypeCode);
       StandardIntegrityDialogRequest_setActivity(dialog_request, activity);
       StandardIntegrityDialogRequest_setStandardIntegrityToken(dialog_request,
                                                       token_response);

       /// Call showDialog with the dialog request. The dialog will be shown on
       /// top of the provided activity and complete when the dialog is closed by
       /// the user.
       StandardIntegrityDialogResponse* dialog_response;
       StandardIntegrityErrorCode error_code =
           StandardIntegrityManager_showDialog(dialog_request, &dialog_response);

       /// Use polling to wait for the async operation to complete.
       /// Note, the polling shouldn't block the thread where the
       /// StandardIntegrityManager is running.
       IntegrityDialogResponseCode response_code = INTEGRITY_DIALOG_RESPONSE_UNKNOWN;
       while (error_code == STANDARD_INTEGRITY_NO_ERROR) {
           error_code = StandardIntegrityDialogResponse_getResponseCode(response, &response_code);
           if(response_code != INTEGRITY_DIALOG_RESPONSE_UNKNOWN){
             break;
           }
       }

       /// Free memory
       StandardIntegrityDialogRequest_destroy(dialog_request);
       StandardIntegrityDialogResponse_destroy(dialog_response);

   }
   ```
3. If the returned response code indicates a success, the next request for an integrity token should succeed without any exceptions. If you make standard requests, you need to warm up the token provider again to obtain a fresh verdict.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/remediation).
