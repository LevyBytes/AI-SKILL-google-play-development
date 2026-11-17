## Offering alternative billing only

This section describes how to offer your users alternative billing. Before using these APIs, finish the following prerequisites:

- Review the requirements and enroll in one of the [alternative billing programs](<https://support.google.com/googleplay/android-developer/topic/16471103>).
- Integrate [Play Billing Library 6.2.1](<https://developer.android.com/google/play/billing/release-notes>) or higher.

We recommend having a [Google Play Developer API integration setup](<https://developers.google.com/android-publisher/getting_started>) ready because the backend integration will be built on it.

### Configuring in Play Console

> **Note:** If you are not yet ready to integrate with the alternative billing APIs, continue to make changes to your enrollment status through the [enrollment form](<https://support.google.com/googleplay/android-developer/contact/alternative_billing_edit_package>) instead of the Play Console.

Developers that have completed enrollment and are integrated with alternative billing APIs can manage their alternative billing settings through [Play Console](<https://play.google.com/console/developers>):

- For each of your eligible apps, opt in or out of offering an alternative billing only (without user choice) in each available country

![Image](<https://developer.android.com/static/images/google/play/billing/alternative/alt-bill-settings.png>)

Mock UI, intended for illustrative purposes, subject to change.

### Information screen for users

> **Note:** If you are offering alternative billing only through alternative billing APIs, the user experience requirements will be met by integrating with the client-side APIs. You will not need to separately follow the [interim user experience guidelines](<https://developer.android.com/google/play/billing/alt-billing>).

The information screen helps users understand that only an alternative billing system is being offered within the eligible app. The information screen will be shown to users at the start of their first purchase in your app after alternative billing has been enabled. This message will not be displayed on subsequent purchases made by the same user in your app on the same device. Note that there may be times when the dialog is shown again to a user in situations such as if the user clears caches on their device.

| ![Image](<https://developer.android.com/static/images/google/play/billing/alternative/alt-billing-info-screen-us.png>) Information screen for users |
| --- |

Example for illustrative purposes only.

### Next steps

To begin integrating the alternative billing APIs, follow the in-depth guides for both [in-app integration](<https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app>) and [backend integration](<https://developer.android.com/google/play/billing/alternative/backend>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/alternative).
