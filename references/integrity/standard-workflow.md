This page describes making standard API requests for integrity verdicts, which are supported on Android 5.0 (API level 21) or higher. You can make a standard API request for an integrity verdict whenever your app is making a server call to check whether the interaction is genuine.

## Overview

![Image](<https://developer.android.com/static/images/google/play/integrity/play-integrity-api-standard.svg>)

**Figure 1.** Sequence diagram that shows the high-level design of the Play Integrity API.

A standard request consists of two parts:

- **Prepare the integrity token provider (one off)**: You need to call the Integrity API to prepare the integrity token provider well before you need to obtain the integrity verdict. For example, you can do this when your app launches or in the background before the integrity verdict is needed.
- **Request an integrity token (on demand)**: Whenever your app makes a server request that you want to check is genuine, you request an integrity token and send it to your app's backend server for decryption and verification. Then your backend server can determine how to act.

Prepare the integrity token provider (one off):

1. Your app calls the integrity token provider with your Google Cloud project number.
2. Your app holds the integrity token provider in memory for further attestation check calls.

Request an integrity token (on demand):

1. For the user action which needs to be protected, your app computes the hash (using any suitable hash algorithm such as SHA256) of the request to be made.
2. Your app requests an integrity token, passing the request hash.
3. Your app receives the signed and encrypted integrity token from the Play Integrity API.
4. Your app passes the integrity token to your app's backend.
5. Your app's backend sends the token to a Google Play server. The Google Play server decrypts and verifies the verdict, returning the results to your app's backend.
6. Your app's backend determines how to proceed, based on the signals contained in the token payload.
7. Your app's backend sends the decision outcomes to your app.

## Protect requests against tampering (recommended)

When you're checking a user action in your app with the Play Integrity API, you can leverage the `requestHash` field to mitigate against tampering attacks. For example, a game may want to report the player's score to the game's backend server, and your server wants to ensure this score has not been tampered with by a proxy server. The Play Integrity API returns the value you set in the `requestHash` field, inside the signed integrity response. Without the `requestHash`, the integrity token will be bound only to the device, but not to the specific request, which opens up the possibility of attack. The following instructions describe how to make use of the `requestHash` field effectively:

When you request an integrity verdict:

- Compute a digest of all relevant request parameters (e.g. SHA256 of a stable request serialization) from the user action or server request that is happening. The value set in the `requestHash` field has a maximum length of 500 bytes. Include any app request data in the `requestHash` that is crucial or relevant to the action that you are checking or protecting. The `requestHash` field is included in the integrity token verbatim, so long values may increase the request size.
- Provide the digest as the `requestHash` field to the Play Integrity API, and obtain the integrity token.

> **Caution:** Never put any sensitive information as plain-text into the `requestHash` argument. Instead, hash all the input by default.

When you receive an integrity verdict:

- Decode the integrity token, and extract the `requestHash` field.
- Compute a digest of the request in the same manner as in the app (e.g. SHA256 of a stable request serialization).
- Compare the app-side and server-side digests. If they do not match, the request is not trustworthy.

> **Note:** Standard requests are [automatically protected against replay attacks](<https://developer.android.com/google/play/integrity/standard#replay-protection>).

## Decrypt and verify the integrity verdict

After you request an integrity verdict, the Play Integrity API provides an encrypted response token. To obtain the device integrity verdicts, you must decrypt the integrity token on Google's servers. To do so, complete these steps:

1. [Create a service account](<https://cloud.google.com/iam/docs/service-accounts-create>) within the Google Cloud project that's linked to your app.
2. On your app's server, fetch the access token from your service account credentials using the playintegrity scope, and make the following request:

   ```text
   playintegrity.googleapis.com/v1/PACKAGE_NAME:decodeIntegrityToken -d \
   '{ "integrity_token": "INTEGRITY_TOKEN" }'
   ```

   > **Note:** To access the API's REST interface, you can use the [Google API Client Library](<https://developers.google.com/api-client-library>), which is available in many programming languages, [including Java](<https://github.com/googleapis/google-api-java-client-services/tree/main/clients/google-api-services-playintegrity/v1>).
3. Read the JSON response.

The resulting payload is a plain-text token that contains [integrity verdicts](<https://developer.android.com/google/play/integrity/verdicts>).

### Automatic replay protection

To mitigate replay attacks, Google Play automatically prevents integrity tokens from being reused many times. Attempting to repeatedly decrypt the same token will result in cleared verdicts as follows:

- The device recognition verdict will be empty.
- The app recognition verdict and app licensing verdict will be set to `UNEVALUATED`.
- Any of the optional verdicts that are enabled using the Play Console will be set to `UNEVALUATED` (or to an empty verdict if it is a multi-value verdict).

## Remediate verdict issues with a Google Play prompt (optional)

After your server receives an integrity verdict, it can determine how to proceed. If the verdict indicates there's an issue, such as the app being unlicensed, tampered with, or the device being compromised, you can give users a chance to fix the issue themselves.

The Play Integrity API provides an option to show a Google Play dialog that prompts the user to take action, for example, to get the official version of your app from Google Play.

To learn how to trigger these dialogs from your app based on the server's response, see [Remediation dialogs](<https://developer.android.com/google/play/integrity/remediation>).

> **Tip:** At any time, users can [check their device's Play Protect certified status and troubleshoot issues](<https://support.google.com/googleplay/answer/7165974>) in the Play Store app. You can point your users to this support page if they need help troubleshooting a device integrity issue.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/standard).
