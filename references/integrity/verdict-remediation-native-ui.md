This step uses the token and backend decision from [request bootstrap](verdict-remediation-bootstrap.md) and [dialog-code selection](verdict-remediation-code-selection.md). Recheck the verdict after the dialog closes.

   **Unreal Engine**

   ```c++
   // .h
   void MyClass::OnShowDialogCompleted(
       EStandardIntegrityErrorCode Error,
       EIntegrityDialogResponseCode Response)
   {
       // Handle response code, call the Integrity API again to confirm that the
       // verdict issue has been resolved.
   }

   // .cpp
   void MyClass::RequestIntegrityToken()
   {
       UStandardIntegrityToken* Response = ...
       int TypeCode = YourServerResponse.integrityDialogTypeCode();

       // Create a delegate to bind the callback function.
       FShowDialogStandardOperationCompletedDelegate Delegate;

       // Bind the completion handler (OnShowDialogCompleted) to the delegate.
       Delegate.BindDynamic(this, &MyClass::OnShowDialogCompleted);

       // Call ShowDialog with TypeCode which completes when the dialog is closed.
       Response->ShowDialog(TypeCode, Delegate);
   }
   ```

   **Native**

   ```c++
   // Show dialog as indicated by the server
   int show_dialog_type = yourServerResponse.integrityDialogTypeCode();
   if(show_dialog_type == 0){
     return;
   }

   /// Create dialog request
   StandardIntegrityDialogRequest* dialog_request;
   StandardIntegrityDialogRequest_create(&dialog_request);
   StandardIntegrityDialogRequest_setTypeCode(dialog_request, show_dialog_type);
   StandardIntegrityDialogRequest_setActivity(dialog_request, activity);
   StandardIntegrityDialogRequest_setStandardIntegrityToken(dialog_request,
                                                   token_response);

   /// Call showDialog with the dialog request. The dialog will be shown on top
   /// of the provided activity and complete when the dialog is closed by the
   /// user.
   StandardIntegrityDialogResponse* dialog_response;
   StandardIntegrityErrorCode error_code =
       StandardIntegrityManager_showDialog(dialog_request, &dialog_response);

   /// Use polling to wait for the async operation to complete. Note, the polling
   /// shouldn't block the thread where the StandardIntegrityManager is running.
   IntegrityDialogResponseCode response_code = INTEGRITY_DIALOG_RESPONSE_UNKNOWN;
   while (error_code == STANDARD_INTEGRITY_NO_ERROR) {
       error_code = StandardIntegrityDialogResponse_getResponseCode(dialog_response, &response_code);
       if(response_code != INTEGRITY_DIALOG_RESPONSE_UNKNOWN){
         break;
       }
   }

   /// Free memory
   StandardIntegrityDialogRequest_destroy(dialog_request);
   StandardIntegrityDialogResponse_destroy(dialog_response);

   /// Handle response code, call the Integrity API again to confirm that the
   /// verdict issues have been resolved.
   ```
5. The dialog is displayed on top of the provided activity. When the user has closed the dialog, the Task completes with a [response code](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/model/IntegrityDialogResponseCode>).
6. (Optional) Request another token to display any further dialogs. If you make [standard requests](<https://developer.android.com/google/play/integrity/standard>), you need to warm up the token provider again to obtain a fresh verdict.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/remediation).
