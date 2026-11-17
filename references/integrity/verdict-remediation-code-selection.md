The server verifies the token obtained by [request bootstrap](verdict-remediation-bootstrap.md); its reply selects the dialog type for the client.

3. If the token contains `appLicensingVerdict: "UNLICENSED"`, reply to your app client, requesting it show the licensing dialog:

   **Kotlin**

   ```kotlin
   private fun getDialogTypeCode(integrityToken: String): Int{
       // Get licensing verdict from decrypted and verified integritytoken
       val licensingVerdict: String = getLicensingVerdictFromDecryptedToken(integrityToken)

       return if (licensingVerdict == "UNLICENSED") {
               1 // GET_LICENSED
           } else 0
   }
   ```

   **Java**

   ```java
   private int getDialogTypeCode(String integrityToken) {
       // Get licensing verdict from decrypted and verified integrityToken
       String licensingVerdict = getLicensingVerdictFromDecryptedToken(integrityToken);

       if (licensingVerdict.equals("UNLICENSED")) {
         return 1; // GET_LICENSED
       }
       return 0;
   }
   ```

   **Unity**

   ```c#
   private int GetDialogTypeCode(string IntegrityToken) {
       // Get licensing verdict from decrypted and verified integrityToken
       string licensingVerdict = GetLicensingVerdictFromDecryptedToken(IntegrityToken);

       if (licensingVerdict == "UNLICENSED") {
         return 1; // GET_LICENSED
       }
       return 0;
   }
   ```

   **Unreal Engine**

   ```c++
   private int GetDialogTypeCode(FString IntegrityToken) {
       // Get licensing verdict from decrypted and verified integrityToken
       FString LicensingVerdict = GetLicensingVerdictFromDecryptedToken(IntegrityToken);

       if (LicensingVerdict == "UNLICENSED") {
         return 1; // GET_LICENSED
       }
       return 0;
   }
   ```

   **Native**

   ```c++
   private int getDialogTypeCode(string integrity_token) {
       /// Get licensing verdict from decrypted and verified integrityToken
       string licensing_verdict = getLicensingVerdictFromDecryptedToken(integrity_token);

       if (licensing_verdict == "UNLICENSED") {
         return 1; // GET_LICENSED
       }
       return 0;
   }
   ```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/remediation).
