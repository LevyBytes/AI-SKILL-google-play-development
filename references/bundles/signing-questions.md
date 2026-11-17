## About Play App Signing

### What is Play App Signing?

Every APK on Android must be cryptographically signed with an app signing key in order to be installable. The Android platform uses the key to ensure that any app updates match the installed app on a device so that, after an initial install happens, each app update comes from the same key holder. This reduces the risk of malicious app updates. [Play App Signing](<https://support.google.com/googleplay/android-developer/answer/9842756>) is Google Play's key management service that protects and manages Play developers' app signing keys for their Play-distributed apps. In addition, Play App Signing performs the signing operation on the APKs that Play generates from uploaded AABs. Play App Signing is required for new apps so that they can use AABs.

### Why did Google launch Play App Signing?

For years, app signing keys were a challenge for Play developers. Losing the key would mean no longer being able to deliver app updates to users and a key becoming compromised puts users at risk of malicious updates. It's common in software distribution for distribution channels to store and manage the keys for the software they distribute because it mitigates these risks. [Play App Signing](<https://support.google.com/googleplay/android-developer/answer/9842756>) was introduced to eliminate the risk of losing Play distribution keys, to make it possible to protect Play users following a key compromise, and to give developers' the benefit of Google's ongoing security investment.

### How does Google ensure the security of Play App Signing?

Google protects developers keys in the same industry-leading, secure infrastructure used to protect Google's own keys. Keys are stored encrypted on locked-down, dedicated key management servers with strict ACLs and tamper-evident audit trails covering all operations. Google's cloud security operations and best practices are [detailed online](<https://cloud.google.com/security/overview/whitepaper>).

### Can I choose the app signing key that Play uses for my app?

Yes, when you create a new app you can either choose to have Google generate and store an app signing key on your behalf or you can choose your own app signing key and upload a copy of it.

### I want to use the same app signing key for Play and other app stores. Is this still possible?

If you've decided to use the same signing key on multiple app stores after considering [how app updates work](<https://developer.android.com/google/play/app-updates>), then it's still possible to do so. Remember, this will allow each app store to perform cross-store app updates for your app. You have two options:

- You can generate a key locally and upload a copy of it to Play. That way, you can use the same key used by Google Play when you build your app for other app stores.
- You can use a Google-generated key for Play App Signing, then download distribution APKs from Play Console that are signed with the Google-generated key and use those APKs for distribution on other app stores or websites.

### Can an eligible legacy app use Play App Signing without supplying its existing app signing key?

Yes, Play App Signing supports a 'key upgrade' option for eligible legacy apps under the [documented signing exemption](<https://developer.android.com/studio/publish/app-signing#app-signing-google-play>). This allows the app to start using Play App Signing with a new app signing key. However, in order to use this option, after you perform the upgrade you will be required to upload two things in each release: an app bundle and a legacy APK signed with your old app signing key. Play will use your AABs to generate APKs signed with the upgraded key for new installs and their updates; at the same time Play will use your legacy APKs for app updates to users who already have your app installed. Over time, the legacy installs will migrate to the upgraded key (e.g. when users move to a new mobile device).

### Can eligible legacy apps and new apps use the same app signing key?

It's generally not recommended to use the same app signing key for multiple apps, it's more secure to use a unique key for each app. However, if you need to use the same app signing key for multiple apps this is possible. Either, you can upload a copy of the existing app signing key when configuring Play App Signing. Or, if you don't want to share the existing app signing key, you can use the documented 'key upgrade' option for an eligible legacy app to start using Play App Signing. That way both the eligible legacy app and the new app can use the same new key.

### Can I ever change the app signing key used by Play App Signing?

Yes, apps can change their key by requesting a [key upgrade](<https://support.google.com/googleplay/android-developer/answer/9842756#upgrade>) in Play Console.

### How can I check that Google Play hasn't made unexpected changes to my code?

At any time, you can download and inspect artifacts from Google Play and from [Latest releases and bundles](<https://play.google.com/console/u/0/developers/app/releases/overview>) in Play Console. In addition, the Play Developer API will soon offer the ability to verify APKs before you commit them to a release track. You can also use an optional feature called [code transparency for app bundles](<https://developer.android.com/guide/app-bundle/code-transparency>). With code transparency, you and your end-users can hold an app store like Google Play to account for the code it delivers.

### How does code transparency for app bundles work?

Code transparency is an optional feature that makes it possible to hold an app store distributing your app to account for the code it delivers. To use code transparency, at build time you generate a code transparency file in your app that represents your code (specifically it's a file that contains hashes of your app's code). You sign it with your own private code transparency key that only you hold. You never have to provide your code transparency key to Google. Then, on a device, you can inspect an installed APK and verify that the code transparency file you signed still matches the APK's code. This gives you assurance that, even if the APK itself was re-signed during distribution, the code verified by code transparency hasn't been modified. If there is a mismatch, then that's evidence that the code was changed during distribution. Code transparency doesn't replace APK signatures and is not part of the Android platform.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/app-bundle/faq).
