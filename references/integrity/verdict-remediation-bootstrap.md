This page describes how to handle issues with integrity verdicts.

After an integrity token is requested, you have the option to display a Google Play dialog to the user. You can display the dialog when there are one or more issues with the integrity verdict or if an exception occurred during an Integrity API request. Once the dialog is closed, you can verify that the issue is fixed with another integrity token request. If you make [standard requests](<https://developer.android.com/google/play/integrity/standard>), you need to warm up the token provider again to obtain a fresh verdict.

> **Note:** All integrity dialog types can be shown to users, regardless of the contents of the integrity token. You should check the contents of the integrity token on your server to determine which dialog should be shown.

## Request an integrity dialog to fix a verdict issue

When the client requests an integrity token, you can use the method offered in the [`StandardIntegrityToken`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/StandardIntegrityManager.StandardIntegrityToken#showDialog(android.app.Activity,%20int)>) (Standard API) and [`IntegrityTokenResponse`](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityTokenResponse#showDialog(android.app.Activity,%20int)>) (Classic API): `showDialog(Activity activity, int integrityDialogTypeCode)`.

> **Note:** To use integrity dialogs, you must be using Integrity API Android library version 1.3.0 or higher.

The following steps outline how you can use the Play Integrity API to show a remediation dialog using the [`GET_LICENSED`](<https://developer.android.com/google/play/integrity/remediation?hl=en#get-licensed-dialog>) dialog code. Other dialog codes that your app can request are listed after this section.

1. Request an integrity token from your app, and send the token to your server. You can use the Standard or Classic request.

   **Kotlin**

   ```kotlin
   // Request an integrity token
   val tokenResponse: StandardIntegrityToken = requestIntegrityToken()
   // Send token to app server and get response on what to do next
   val yourServerResponse: YourServerResponse = sendToServer(tokenResponse.token())
   ```

   **Java**

   ```java
   // Request an integrity token
   StandardIntegrityToken tokenResponse = requestIntegrityToken();
   // Send token to app server and get response on what to do next
   YourServerResponse yourServerResponse = sendToServer(tokenResponse.token());
   ```

   **Unity**

   ```c#
   // Request an integrity token
   StandardIntegrityToken tokenResponse = RequestIntegrityToken();
   // Send token to app server and get response on what to do next
   YourServerResponse yourServerResponse = sendToServer(tokenResponse.Token);
   ```

   **Unreal Engine**

   ```c++
   // Request an integrity token
   StandardIntegrityToken* Response = RequestIntegrityToken();
   // Send token to app server and get response on what to do next
   YourServerResponse YourServerResponse = SendToServer(Response->Token);
   ```

   **Native**

   ```c++
   /// Request an integrity token
   StandardIntegrityToken* response = requestIntegrityToken();
   /// Send token to app server and get response on what to do next
   YourServerResponse yourServerResponse = sendToServer(StandardIntegrityToken_getToken(response));
   ```
2. On your server, decrypt the integrity token and check the `appLicensingVerdict` field. It could look something like this:

   ```json
   // Licensing issue
   {
       ...
       "accountDetails": {
           "appLicensingVerdict": "UNLICENSED"
       }
   }
   ```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/remediation).
