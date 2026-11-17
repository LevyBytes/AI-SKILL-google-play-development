## Configure classic request settings (optional)

Skip this section if you only plan to make [standard API requests](<https://developer.android.com/google/play/integrity/standard>).

By default, Google Play manages response encryption, meaning your backend calls Google's server to decrypt verdicts. Alternatively, you can manage keys yourself to decrypt locally within your secure server environment.

### Let Google manage your response encryption (recommended)

We recommend allowing Google to generate and manage keys to protect your app's security. Your backend will call Google Play's server to decrypt and verify responses.

### Manage your own encryption keys

To decrypt locally within your own secure server environment, you can download encryption keys from the Play Console or the Play SDK Console. Your app must be available on Google Play to use this feature.

Before you change your response encryption management strategy in the Play Console, make sure your server is correctly configured to decrypt and verify integrity tokens on Google Play's servers to avoid disruption.

> **Caution:** Never decrypt tokens or expose keys within your client app.

> **Tip:** Even when self-managing keys, your app can still fall back to Google Play's server for decryption.

### Switch between Google-managed and self-managed encryption keys

1. Open the **Play Console** and select your app .
2. Go to **Protected with Play**.
3. Next to **Play Integrity API**, click **[Manage](<https://play.google.com/console/developers/app/app-integrity/integrity-api-settings>)**.
4. Under **Classic requests**, next to **Response encryption**, click **Edit**.

To switch to self-managed keys:

1. Select **Manage and download my response encryption keys** and upload your public key.
2. Click **Save** to automatically download your encrypted keys.
3. Update your secure backend server to decrypt locally using these keys.

To switch to Google-managed keys:

1. Select **Let Google manage my response encryption (recommended)**.
2. Click **Save changes**.

> **Caution:** Switching to Google-managed encryption immediately invalidates previously downloaded keys, even in production. Before switching, make sure your server is configured to handle the change to avoid disruption.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/setup).
