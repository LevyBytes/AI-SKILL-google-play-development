This page explains how to set up your app, game or SDK to use the Play Integrity API. To integrate the API, you must have a Google Cloud project, which is necessary to begin making requests. You can then link your Google Cloud project in the Google Play Console (for apps) or the Google Play SDK Console (for SDKs). **Linking your project is required to access additional configuration options, testing features, API reporting, and to request an increase to your daily request quota.**

## Enable Play Integrity API

Every app or SDK calling the Play Integrity API must have a Google Cloud project to use the API and monitor usage. This is the mandatory first step for all integrations. You can enable the Play Integrity API in the Google Cloud Console or you can skip directly to linking your Cloud project to Google Play and Play Integrity API will be enabled for you.

In your [Google Cloud Console](<https://console.cloud.google.com/>), create a new Cloud project or choose an existing Cloud project that you want to use with the Play Integrity API.

1. Navigate to **APIs and services**.
2. Select **Enable APIs and services**.
3. Search for **[Play Integrity API](<https://console.cloud.google.com/marketplace/product/google/playintegrity.googleapis.com>)**.
4. Click **Enable**.

You can now integrate the Play Integrity API into your app. To access advanced features and quota increases, you must proceed to the linking step.

> **Note:** Projects that are enabled in the Google Cloud Console but not linked in the Play Console or Play SDK Console are not eligible for additional configuration options or quota increases.

## Link to Google Play (recommended)

You can link your Google Cloud project to your app or SDK using these instructions.

### For apps and games on Google Play

Apps distributed on Google Play should link their Google Cloud project in the Google Play Console to enable additional features and request increased daily API quota.

1. Open the [Google Play Console](<https://play.google.com/console/developers>) and select your app.
2. Navigate to **[Protected with Play](<https://play.google.com/console/developers/app/protect-with-play>)**.
3. Next to **Play Integrity API**, select the **Get started** button to go to **Play Integrity API settings**.
4. Click the **Link Cloud project** button.
5. Choose the Google Cloud project you plan to use with the Play Integrity API. If the Play Integrity API isn't already enabled for the project, it will be enabled automatically upon linking.

### For SDK providers on Play SDK Console

SDK providers using the [Google Play SDK Console](<https://play.google.com/sdk-console/>) can link their Google Cloud project to attribute API usage to the SDK rather than the individual apps using it, enable additional features, and request increased daily API quota. Note that access to the Google Play SDK Console is subject to [eligibility criteria](<https://support.google.com/googleplay/android-developer/answer/12244916#SDK_eligibility>).

1. Open the [Google Play SDK Console](<https://play.google.com/sdk-console/>) and select your SDK.
2. Navigate to **SDK integrity**
3. Under **Play Integrity API** click **Link a Cloud project**.
4. Choose the Google Cloud project you plan to use with the Play Integrity API; if the Play Integrity API is not already enabled for the project, it will be enabled automatically upon linking.

> **Note:** You can link up to a maximum of five Google Cloud projects to your app or SDK. You should consider linking multiple projects if you need to support different environments for your testing and production.

## Understand Play Integrity API usage limits

Your app or SDK has a default daily limit of 10,000 total requests, tied to the associated Cloud Project Number. If you anticipate a higher volume, you can request a quota increase.

| Action | Daily quota | Notes |
| --- | --- | --- |
| Token requests | 10,000 | Shared between classic requests and standard token preparations |
| Token decryptions on Google's servers | 10,000 | Shared between classic and standard requests |

### Increase your daily maximum number of requests

Quota increase is subject to eligibility criteria. Quota increases apply to both client-side token generation and server-side decryption calls. Processing requests can take up to a week. We recommend monitoring your Play Integrity API usage in your Google Cloud Console and setting [quota alerts](<https://cloud.google.com/docs/quota?&_ga=2.68760982.-685660492.1676978684#monitoring_quota_metrics>) to avoid interruptions to your service.

Even with higher quota, continue to limit [classic requests](<https://developer.android.com/google/play/integrity/classic>) to infrequent, high-value actions to preserve user battery and data usage.

> **Caution:** Very high volume changes should be rolled out gradually. Sudden traffic spikes may cause throttling.

#### For apps and games on Google Play

To be eligible for a quota increase, your app must be available on Google Play in addition to any other distribution channels. You must link your Google Cloud project to your app in the [Play Console](<https://play.google.com/console/developers/app/app-integrity/integrity-api-settings>). Quota requests from unlinked projects will be rejected.

To request an increase:

1. Link the relevant Google Cloud project in the **[Play Console](<https://play.google.com/console/developers/app/app-integrity/integrity-api-settings>)**.
2. Verify you have correctly implemented API logic including proper retry strategies.
3. Submit the [quota request form](<https://support.google.com/googleplay/android-developer/contact/piaqr>).

#### For SDK providers on Play SDK Console

To be eligible for a quota increase, your SDK must be claimed on the Google Play SDK Console and your Cloud project must be linked to your SDK there. Access to the Google Play SDK Console is subject to [eligibility criteria](<https://support.google.com/googleplay/android-developer/answer/12244916#SDK_eligibility>).

To request an increase:

1. Link your Google Cloud project in the **[Google Play SDK Console](<https://play.google.com/sdk-console/>)**.
2. Complete the [developer support form](<https://support.google.com/googleplay/android-developer/answer/10357403>).

In the open comments, provide your SDK details, describe your use case, the type of API requests that you're making (standard, classic, or both), how often you're making requests, and the daily maximum requests that you want.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/setup).
