## Manage your own signing key

If your app qualifies for the [legacy Play App Signing exemption](<https://developer.android.com/studio/publish/app-signing#app-signing-google-play>) and you choose to manage your own app signing key and keystore, **you are responsible for securing the key and the keystore**. This distribution path cannot support Android App Bundles, Play Feature Delivery or Play Asset Delivery.

When you are ready to create your own key and keystore, make sure you first choose a strong password for your keystore and a separate strong password for each private key stored in the keystore. You must keep your keystore in a safe and secure place. If you lose access to your app signing key or your key is compromised, Google cannot retrieve the app signing key for you, and you will not be able to release new versions of your app to users as updates to the original app. For more information, see [Keep your key secure](<https://developer.android.com/studio/publish/app-signing?hl=en#secure_key>), below.

If you manage your own app signing key and keystore, when you sign your APK, you will sign it locally using your app signing key and upload the signed APK directly to the Google Play Store for distribution as shown in figure 12.

![Image](<https://developer.android.com/static/studio/images/publish/appsigning_selfmanagediagram_2x.png>)

**Figure 12**. Signing an app when you manage your own app signing key

When you use [Play App Signing](<https://developer.android.com/studio/publish/app-signing#google-play-app-signing>), Google keeps your signing key safe, and ensures your apps are correctly signed and able to receive updates throughout their lifespans. However, if you decide to manage your app signing key yourself, there are a few considerations you should keep in mind.

## Signing considerations

You should sign your app with the same certificate throughout its expected lifespan. There are several reasons why you should do so:

- **App upgrade:** When the system is installing an update to an app, it compares the certificate(s) in the new version with those in the existing version. The system allows the update if the certificates match. If you sign the new version with a different certificate, you must assign a different package name to the app. In this case, the user installs the new version as a completely new app.
- **App modularity:** Android allows APKs signed by the same certificate to run in the same process, if the apps so request, so that the system treats them as a single app. In this way you can deploy your app in modules, and users can update each of the modules independently.
- **Code/data sharing through permissions:** Android provides signature-based permissions enforcement, so that an app can expose functionality to another app that is signed with a specified certificate. By signing multiple APKs with the same certificate and using signature-based permissions checks, your apps can share code and data in a secure manner.

If you plan to support upgrades for an app, ensure that your app signing key has a validity period that exceeds the expected lifespan of that app. A validity period of 25 years or more is recommended. When your key's validity period expires, users will no longer be able to seamlessly upgrade to new versions of your app.

If you plan to publish on Google Play, the signing key must have a validity period that ends after the [minimum expiration required by Google Play](<https://developer.android.com/studio/publish/app-signing>). Check that exact requirement when creating the key. Google Play enforces it so users can seamlessly upgrade apps when new versions become available.

### Keep your key secure

If you choose to manage and secure your app signing key and keystore yourself (instead of opting in to [Play App Signing](<https://developer.android.com/studio/publish/app-signing?hl=en#app-signing-google-play>)), securing your app signing key is of critical importance, both to you and to the user. If you allow someone to use your key, or if you leave your keystore and passwords in an unsecured location such that a third-party could find and use them, your authoring identity and the trust of the user are compromised.

> **Note:** If you use Play App Signing, your app signing key is kept secure using Google's infrastructure. You should still keep your upload key secure as described below. If your upload key is compromised, you can [request an upload key reset](<https://developer.android.com/studio/publish/app-signing?hl=en#reset_upload_key>) in the Play Console.

If a third party should manage to take your app signing key without your knowledge or permission, that person could sign and distribute apps that maliciously replace your authentic apps or corrupt them. Such a person could also sign and distribute apps under your identity that attack other apps or the system itself, or corrupt or steal user data.

Your private key is required for signing all future versions of your app. If you lose or misplace your key, you will not be able to publish updates to your existing app. You cannot regenerate a previously generated key.

Your reputation as a developer entity depends on your securing your app signing key properly, at all times, until the key is expired. Here are some tips for keeping your key secure:

- Select strong passwords for the keystore and key.
- Do not give or lend anyone your private key, and do not let unauthorized persons know your keystore and key passwords.
- Keep the keystore file containing your private key in a safe, secure place.

In general, if you follow common-sense precautions when generating, using, and storing your key, it will remain secure.

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish/app-signing).
