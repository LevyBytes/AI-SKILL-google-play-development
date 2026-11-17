## Using Play App Signing

Configure [Play App Signing](<https://developer.android.com/studio/publish/app-signing?hl=en#app-signing-google-play>) for distribution through Google Play unless the app qualifies for the documented legacy exemption permitting self-signed APKs. Choose the procedure for a new unpublished app or an existing app that already has an app signing key; verify exemption eligibility in the official signing guide.

### Configure a new app

To configure signing for an app that has not yet been published to Google Play, proceed as follows:

1. If you haven’t already done so, [generate an upload key](<https://developer.android.com/studio/publish/app-signing?hl=en#generate-key>) and [sign your app](<https://developer.android.com/studio/publish/app-signing?hl=en#sign_release>) with that upload key.
2. Sign in to your [Play Console](<https://play.google.com/console/>).
3. Follow the steps to [prepare & roll out your release](<https://support.google.com/googleplay/android-developer/answer/7159011>) to create a new release.
4. After you choose a release track, configure app signing under the **App signing** section as follows:

   - To have Google Play generate an app signing key for you and use it to sign your app, you don't have to do anything. The key you use to sign your first release becomes your upload key, and you should use it to sign future releases.
   - To use the same key as another app on your developer account, select **Change app signing key > Use the same key as another app in this account**, select an app, and then click **Continue**.
   - To provide your own signing key for Google to use when signing your app, select **Change app signing key** and select one of the **Export and upload** options that lets you securely upload a private key and its public certificate.

> **Note:** If you haven't already accepted the [Terms of Service](<https://play.google.com/about/play-app-signing-terms.html>), you are required to review the terms and select **Accept** to continue.

In the section called **App Bundles**, click **Browse files** to locate and upload the app you signed using your upload key. For more information about releasing your app, refer to [prepare & roll out your release](<https://support.google.com/googleplay/android-developer/answer/7159011>). When you release your app after configuring Play App Signing, Google Play generates (unless you upload an existing key) and manages your app’s signing key for you. Simply sign subsequent updates to your app using your app’s upload key before uploading it to Google Play.

If you need to create a new upload key for you app, go to the section about how to [Reset a lost or compromised private upload key](<https://developer.android.com/studio/publish/app-signing?hl=en#reset_upload_key>).

### Opt in an existing app

If you’re updating an app that’s already published to Google Play using an existing app signing key, you can opt in to Play App Signing as follows:

1. Sign in to your [Play Console](<https://play.google.com/console/>) and navigate to your app.
2. On the left menu, click **Release > Setup > App signing**.
3. If applicable, review the Terms of Service and select **Accept**.
4. Select one of the options that best describes the signing key you want to upload to Google Play and follow the instructions that are shown. For example, if you are using a Java Keystore for your signing key, select **Upload a new app signing key from Java Keystore** and follow the instructions to download and run the PEPK tool, and upload the generated file with your encrypted key.
5. Click **Enroll**.

You should now see a page with the details of your app’s signing and upload certificates. Google Play now signs your app with your existing key when deploying it to users. However, one of the most important benefits to Play App Signing is the ability to separate the key you use to sign the artifact you upload to Google Play from the key that Google Play uses to sign your app for distribution to users. So, consider following the steps in the next section to generate and register a separate upload key.

#### Generate and register an upload certificate

When you're publishing an app that is not signed by an upload key, the Google Play Console provides the option to register one for future updates to the app. Although this is an optional step, it’s recommended that you publish your app with a key that’s separate from the one Google Play uses to distribute your app to users. That way, Google keeps your signing key secure, and you have the option to [reset a lost or compromised private upload key](<https://developer.android.com/studio/publish/app-signing?hl=en#reset_upload_key>). This section describes how to create an upload key, generate an upload certificate from it, and register that certificate with Google Play for future updates of your app.

The following describes the situations in which you see the option to register an upload certificate in the Play Console:

- When you publish a new app that’s signed with a signing key and opt it in to Play App Signing.
- When you are about to publish an existing app that’s already opted in to Play App Signing, but it is signed using its signing key.

If you are not publishing an update to an existing app that’s already opted in to Play App Signing, and you’d like to register an upload certificate, complete the steps below and continue on to the section about how to [reset a lost or compromised private upload key](<https://developer.android.com/studio/publish/app-signing?hl=en#reset_upload_key>).

If you haven’t already done so, [generate an upload key and keystore](<https://developer.android.com/studio/publish/app-signing?hl=en#generate-key>).

After you create your upload key and keystore, you need to generate a public certificate from your upload key using [`keytool`](<https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html>), with the following command:

```text

$ keytool -export -rfc
  -keystore your-upload-keystore.jks
  -alias upload-alias
  -file output_upload_certificate.pem
```

Now that you have your upload certificate, register it with Google when prompted in the Play Console or [when resetting your upload key](<https://developer.android.com/studio/publish/app-signing?hl=en#reset_upload_key>).

#### Upgrade your app signing key

In some circumstances, you might want to change your app's signing key. For example, because you want a cryptographically stronger key or your signing key has been compromised. However, because users can only update your app if the update is signed with the same signing key, it's difficult to change the signing key for an app that's already published.

If you publish your app to Google Play, you can upgrade the signing key for your published app through the Play Console; your new key is used to sign installs and app updates on Android 13 and higher, while your older app signing key is used to sign updates for users on earlier versions of Android.

To learn more, read [Upgrade your app signing key](<https://support.google.com/googleplay/android-developer/answer/7384423#Upgrade>).

### Reset a lost or compromised private upload key

If you lost your private upload key or your private key has been compromised, you can create a new one and [request an upload key reset](<https://support.google.com/googleplay/android-developer/answer/7384423#reset>) in the Play console.

> **Note:** Resetting your upload key will not affect the app signing key that Google Play uses to re-sign APKs before delivering to users.

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/app-signing).
