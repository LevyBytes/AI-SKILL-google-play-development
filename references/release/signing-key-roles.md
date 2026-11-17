Android requires that all APKs be digitally signed with a certificate before they are installed on a device or updated. When releasing using [Android App Bundles](<https://developer.android.com/guide/app-bundle>), you need to sign your app bundle with an upload key before uploading it to the Play Console, and Play App Signing takes care of the rest. For apps distributing using APKs on the Play Store or on other stores, you must manually sign your APKs for upload.

This page guides you through some important concepts related to app signing and security, how to sign your app for release to Google Play using Android Studio, and how to configure Play App Signing.

The following is a high-level overview of the steps you might need to take to sign and publish a new app to Google Play:

1. [Generate an upload key and keystore](<https://developer.android.com/studio/publish/app-signing?hl=en#generate-key>)
2. [Sign your app with your upload key](<https://developer.android.com/studio/publish/app-signing?hl=en#sign_release>)
3. [Configure Play App Signing](<https://developer.android.com/studio/publish/app-signing?hl=en#enroll>)
4. [Upload your app to Google Play](<https://developer.android.com/studio/publish/upload-bundle>)
5. [Prepare & roll out release of your app](<https://support.google.com/googleplay/android-developer/answer/7159011>)

If instead your app is already published to the Google Play Store with an existing app signing key, or you would like to choose the app signing key for a new app instead of having Google generate it, follow these steps:

1. [Sign your app](<https://developer.android.com/studio/publish/app-signing?hl=en#sign_release>) with your app’s *signing key*.
2. [Upload your app’s signing key](<https://developer.android.com/studio/publish/app-signing?hl=en#enroll_existing>) to Play App Signing.
3. (Recommended) [Generate and register an upload certificate](<https://developer.android.com/studio/publish/app-signing?hl=en#generate-key>) for future updates to your app
4. [Upload your app to Google Play](<https://developer.android.com/studio/publish/upload-bundle>)
5. [Prepare & roll out release of your app](<https://support.google.com/googleplay/android-developer/answer/7159011>)

This page also explores how to manage your own keys for when uploading your app to other app stores. If you do not use Android Studio or would rather sign your app from the command line, learn about how to use [`apksigner`](<https://developer.android.com/studio/command-line/apksigner>).

> **Note:** If you are building a Wear OS app, the process for signing the app can differ from the process described in this Android app signing guide. See the information about [packaging and publishing Wear OS apps](<https://developer.android.com/training/wearables/apps/packaging>).

## Play App Signing

With Play App Signing, Google manages and protects your app's signing key for you and uses it to sign your APKs for distribution. And, because app bundles defer building and signing APKs to the Google Play Store, you need to configure Play App Signing before you upload your app bundle. Doing so lets you benefit from the following:

- Use the Android App Bundle and support Google Play’s advanced delivery modes. The Android App Bundle makes your app much smaller, your releases simpler, and makes it possible to use feature modules and offer instant experiences.
- Increase the security of your signing key, and make it possible to use a separate upload key to sign the app bundle you upload to Google Play.
- Key upgrade lets you change your app signing key in case your existing one is compromised or if you need to migrate to a cryptographically stronger key

  > **Note:** In order to ensure security, after you configure Play App Signing with either an auto-generated key, or a key that you supply, you cannot retrieve a copy of your app's signing key and Google may retain a backup copy of the key for disaster recovery purposes.

Play App Signing uses two keys: the *app signing key* and the *upload key*, which are described in further detail in the section about [Keys and keystores](<https://developer.android.com/studio/publish/app-signing?hl=en#certificates-keystores>). You keep the upload key and use it to sign your app for upload to the Google Play Store. Google uses the upload certificate to verify your identity, and signs your APK(s) with your app signing key for distribution as shown in figure 1. By using a separate upload key you can [request an upload key reset](<https://support.google.com/googleplay/android-developer/answer/7384423#reset>) if your key is ever lost or compromised.

By comparison, for apps that have not opted in to Play App Signing, if you lose your app’s signing key, you lose the ability to update your app.

> **Important:** If you want to use the same signing key across multiple stores, make sure to provide your own signing key when you [configure Play App Signing](<https://developer.android.com/studio/publish/app-signing?hl=en#enroll>), instead of having Google generate one for you.

![Image](<https://developer.android.com/static/studio/images/publish/appsigning_googleplayappsigningdiagram_2x.png>)

**Figure 1**. Signing an app with Play App Signing

Your keys are stored on the same infrastructure that Google uses to store its own keys, where they are protected by Google’s Key Management Service. You can learn more about Google’s technical infrastructure by reading the [Google Cloud Security Whitepapers](<https://services.google.com/fh/files/misc/security_whitepapers_march2018.pdf>).

When you use Play App Signing, if you lose your upload key, or if it is compromised, you can request an upload key reset in the Play Console. Because your app signing key is secured by Google, you can continue to upload new versions of your app as updates to the original app, even if you change upload keys. To learn more, read [Reset a lost or compromised private upload key](<https://developer.android.com/studio/publish/app-signing?hl=en#reset_upload_key>).

The next section describes some important terms and concepts related to app signing and security. If you’d rather skip ahead and learn how to prepare your app for upload to the Google Play Store, go to [Sign your app for release](<https://developer.android.com/studio/publish/app-signing?hl=en#sign-apk>).

### Keystores, keys, and certificates

Java Keystores (.jks or .keystore) are binary files that serve as repositories of certificates and private keys.

A **public key certificate** (`.der` or `.pem` files), also known as a digital certificate or an identity certificate, contains the public key of a public/private key pair, as well as some other metadata identifying the owner (for example, name and location) who holds the corresponding private key.

The following are the different types of keys you should understand:

- **App signing key:** The key that is used to sign APKs that are installed on a user's device. As part of Android’s secure update model, the signing key never changes during the lifetime of your app. The app signing key is private and must be kept secret. You can, however, share the certificate that is generated using your app signing key.
- **Upload key:** The key you use to sign the app bundle or APK before you upload it for [app signing with Google Play](<https://developer.android.com/studio/publish/app-signing?hl=en#app-signing-google-play>). You must keep the upload key secret. However, you can share the certificate that is generated using your upload key. You may generate an upload key in one of the following ways:

  - If you choose for Google to generate the app signing key for you when you opt in, then the key you use to [sign your app for release](<https://developer.android.com/studio/publish/app-signing?hl=en#sign-apk>) is designated as your upload key.
  - If you provide the app signing key to Google when opting in your new or existing app, then you have the option to generate a new upload key during or after opting in for increased security.
  - If you do not generate a new upload key, you continue to use your app signing key as your upload key to sign each release.

  **Tip:** To keep your keys secure, it’s a good idea to make sure your app signing key and upload key are different.

### Working with API providers

You can download the certificate for the app signing key and your upload key from the **Release > Setup > App signing** page in the [Play Console](<https://play.google.com/console/>). This is used to register public key(s) with API providers; it's intended to be shared, as it does not contain your private key.

A **certificate fingerprint** is a short and unique representation of a certificate that is often requested by API providers alongside the package name to register an app to use their service. The MD5, SHA-1 and SHA-256 fingerprints of the upload and app signing certificates can be found on the app signing page of the Play Console. Other fingerprints can also be computed by downloading the original certificate (`.der`) from the same page.

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/app-signing).
