All Google Play Billing Library versions have a two-year deprecation cycle. Check the [official version-support schedule](<https://developer.android.com/google/play/billing/deprecation-faq>) for the exact new-app, update and extension cutoffs before submitting a release.

This page answers common questions about the Google Play Billing Library version deprecation and migrating to higher versions.

## Support timeline for different versions

Use the live schedule to resolve deprecation and extension deadlines for each library version:

| Version | New app and update deadline | Extension deadline |
| --- | --- | --- |
| 5 | [Current published cutoff](<https://developer.android.com/google/play/billing/deprecation-faq>) | [Extension rules](<https://developer.android.com/google/play/billing/deprecation-faq>) |
| 6 | [Current published cutoff](<https://developer.android.com/google/play/billing/deprecation-faq>) | [Extension rules](<https://developer.android.com/google/play/billing/deprecation-faq>) |
| 7 | [Current published cutoff](<https://developer.android.com/google/play/billing/deprecation-faq>) | [Extension rules](<https://developer.android.com/google/play/billing/deprecation-faq>) |
| 8 | [Current published cutoff](<https://developer.android.com/google/play/billing/deprecation-faq>) | [Extension rules](<https://developer.android.com/google/play/billing/deprecation-faq>) |
| 9 | [Current published cutoff](<https://developer.android.com/google/play/billing/deprecation-faq>) | [Extension rules](<https://developer.android.com/google/play/billing/deprecation-faq>) |

****How do you find which APKs use a deprecated Play Billing Library version?****

Check your `build.gradle` file. Apps must use a supported version from the table. These dependencies only appear in APKs that require the `com.android.vending.BILLING` permission.

****Do you need to update unmaintained APKs?****

We recommend updating maintained APKs. Unmaintained APKs don't need updates; existing apps still work, but new apps and updates must use supported versions.

****How do you fix a deprecation warning if you've already updated your app to a supported version?****

Make sure your `AndroidManifest.xml` file contains `com.google.android.play.billingclient.version`. If it's missing, check whether [manifest merging](<https://developer.android.com/studio/build/manage-manifests#merge-manifests>) removes this attribute.

****How do you upgrade from a lower version of the Google Play Billing Library?****

Update the dependency in your release to use a supported version from the table. To learn what changed between releases, see the [release notes](<https://developer.android.com/google/play/billing/release-notes>).

To migrate, see the [migration guide for version 9](<https://developer.android.com/google/play/billing/migrate-gpblv9>).

****Where do you find the extension form to continue distributing to users until the extension deadline?****

If your app uses an unsupported Google Play Billing Library version, you'll receive a warning in the Google Play Console. On the warning's details page on the [**Policy status**](<https://play.google.com/console/developers/app/policy-center>) page, open the extension form.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/deprecation-faq).
