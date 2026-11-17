You should be testing your integration throughout development. To test during the development phase, we recommend leveraging *license testers* and [*Play Billing Lab*](<https://play.google.com/store/apps/details?id=com.google.android.apps.play.billingtestcompanion>) to run through the scenarios described in this section.

## License Testers

To configure license testers, see [Test in-app billing with application licensing](<https://support.google.com/googleplay/android-developer/answer/6062777>).

Using license testers provide the following benefits:

- Ordinarily, the Google Play Billing Library is blocked for apps that aren't signed and uploaded to Google Play. License testers can bypass this check, meaning you can sideload apps for testing, even for apps using debug builds with debug signatures without the need to upload to the new version of your app. Note that the package name must match that of the app that is configured for Google Play, and the Google Account must be a license tester for the Google Play Console account.
- License testers have access to test payment methods that avoid charging the testers real money for purchases. You can also use test payment methods to simulate certain situations, such as when a payment is declined. Figure 1 shows these test forms of payment as they appear within the purchase flow.
- License testers can [rapidly test subscription features](<https://developer.android.com/google/play/billing/test?hl=en#subs>).

![license testers have access to test payment methods](<https://developer.android.com/static/images/google/play/billing/test-payment-methods.png>)

**Figure 1.** License testers have access to test payment methods.

Here are some additional details about the test purchase process:

- Test purchases use the same app purchase flow used by actual purchases.
- Taxes are not computed for test purchases.
- Google Play indicates a test purchase by displaying a notice across the center of the purchase dialog.

You can confirm the account that is making a purchase by expanding the purchase dialog. Note the following:

- Test accounts must be on the tester's Android-powered device.
- If the device has more than one account, the purchase is made with the account that downloaded the app.
- If none of the accounts have downloaded the app, the purchase is made with the first account.

Use Google Play [test tracks](<https://support.google.com/googleplay/android-developer/answer/3131213>) for pre-distribution validation, such as allowing your QA team to qualify new releases. With test tracks, license testers can install and evaluate unreleased versions of your app from Google Play. Regular users can make real purchases using standard payment methods.

> **Note:** Users incur actual charges for their test track purchases unless the user is a license tester. Draft apps and internal test track releases are subject to [spend limits](<https://developer.android.com/google/play/billing/test?hl=en#spend-limits>).

To test your Google Play Billing Library integration using test tracks, do the following:

1. Publish your app to a [test track](<https://support.google.com/googleplay/android-developer/answer/3131213>). Note that after you publish an app to a testing track, it can take a few hours for the app to be available for testers.
2. Ensure each tester [opts-in to your app's test](<https://support.google.com/googleplay/android-developer/answer/3131213>). On your test's opt-in URL, your testers see an explanation of what it means to be a tester along with a link to opt-in.

You can test your integration on any Android-powered hardware device running Android 1.6 or higher. The most current version of the Google Play application must be installed on the device. For general information about how to set up a device for use in developing Android applications, see [Using Hardware Devices](<https://developer.android.com/tools/device>).

> **Note:**
>
> - While license testers are recommended for development and testing, ensure you also test your app using non-license tester accounts, either occasionally or when making large changes. Non-license testing helps to ensure that your app does not rely on testing specific logic such as renewal durations.
> - Users in the testing tracks can also be license testers for your app.

## Play Billing Lab

Play Billing Lab is an Android app that helps developers test their integration with Google Play's billing system. It provides a convenient way for developers to test billing features, integrate faster, and launch with higher confidence. You can download and install Play Billing Lab from the [Play Store](<https://play.google.com/store/apps/details?id=com.google.android.apps.play.billingtestcompanion>).

Play Billing Lab lets you to do the following in your testing:

- Change [Play Country](<https://support.google.com/googleplay/answer/7431675>) from within Play Billing Lab and apply the settings to your test. This enables [testing custom user-experiences in different countries/regions](<https://developer.android.com/google/play/billing/test?hl=en#regions>) regardless of where the tester is physically testing
- [Test trial or introductory offers](<https://developer.android.com/google/play/billing/test?hl=en#trial-offers>) repeatedly with the same account
- [Test subscription price changes](<https://developer.android.com/google/play/billing/test?hl=en#price-changes>) without affecting other active subscribers
- [Accelerate subscription state transition](<https://developer.android.com/google/play/billing/test?hl=en#subscription-state-transition>) to accelerate subscription renewals, or move your test subscription into grace period or account hold state with one click to speed up your testing
- [Test with real payment methods](<https://developer.android.com/google/play/billing/test?hl=en#real-fop-testing>) to bypass certain purchase flow risk signals
- [Test out-of-app purchases](<https://developer.android.com/google/play/billing/test?hl=en#out-of-app>) to make sure that your backend can handle them

![Play Billing Lab Dashboard](<https://developer.android.com/static/images/google/play/billing/play-billing-lab-dashboard.png>)

**Figure 2.** Play Billing Lab Dashboard.

> **Note:**
>
> - Be sure to log into Play Billing Lab using the same account as the billing account. Be sure that the account is registered as a license tester for the app under test. Play country, testing trial or introductory offers, and testing with real payment methods configurations expire in 2 hours.
> - If you get errors when applying changes in Play Billing Lab, log into Play Billing Lab again and retry. If you notice long delay for the configuration to be applied or you are using another Android-powered device to perform the testing, clear the Play Store cache manually on the device on which the test was performed after you have made configuration changes in the Play Billing Lab.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/test).
