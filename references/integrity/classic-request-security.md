If you're only planning to make [standard API requests](<https://developer.android.com/google/play/integrity/standard>), which are suitable for the majority of developers, you can skip ahead to [integrity verdicts](<https://developer.android.com/google/play/integrity/verdicts>). This page describes making classic API requests for integrity verdicts, which are supported on Android 4.4 (API level 19) or higher.

## Considerations

### Compare standard and classic requests

You can make standard requests, classic requests, or a combination of the two depending on your app's security and anti-abuse needs. Standard requests are suitable for all apps and games and can be used to check that any action or server call is genuine, while delegating some protection against replayability and exfiltration to Google Play. Classic requests are more expensive to make and you are responsible for correctly implementing them to protect against exfiltration and certain types of attacks. Classic requests should be made less frequently than standard requests, for example as an occasional one-off to check if a highly valuable or sensitive action is genuine.

The following table highlights the key differences between the two types of requests:

|  | **Standard API request** | **Classic API request** |
| --- | --- | --- |
| **Pre-requisites** |  |  |
| Minimum Android SDK required***** | Android 6.0 (API level 23) or higher | Android 6.0 (API level 23) or higher |
| Google Play requirements | Google Play Store and Google Play services | Google Play Store and Google Play services |
| **Integration details** |  |  |
| API warm up required | ✔️ (a few seconds) | ❌ |
| Typical request latency | A few hundred milliseconds | A few seconds |
| Potential request frequency | Frequent (on-demand check for any action or request) | Infrequent (one-off check for highest value actions or most sensitive requests) |
| Timeouts | Most warm ups are under 10s but they involve a server call, so a long timeout is recommended (e.g. 1 minute). Verdict requests happen client-side | Most requests are under 10s but they involve a server call, so a long timeout is recommended (e.g. 1 minute) |
| **Integrity verdict token** |  |  |
| Contains device, app, and account details | ✔️ | ✔️ |
| Token caching | Protected on-device caching by Google Play | Not recommended |
| Decrypt and verify token using a Google Play server | ✔️ | ✔️ |
| Typical decryption server-to-server request latency | 10s of milliseconds with three-nines availability | 10s of milliseconds with three-nines availability |
| Decrypt and verify token locally in a secure server environment | ❌ | ✔️ |
| Decrypt and verify token client-side | ❌ | ❌ |
| Integrity verdict freshness | Some automatic caching and refreshing by Google Play | All verdicts recomputed on each request |
| **Limits** |  |  |
| Requests per app per day | 10,000 by default (an increase can be requested) | 10,000 by default (an increase can be requested) |
| Requests per app instance per minute | Warm ups: 5 per minute<br>Integrity tokens: No public limit****** | Integrity tokens: 5 per minute |
| **Protection** |  |  |
| Mitigate against tampering and similar attacks | Use `requestHash` field | Use `nonce` field with content binding based on request data |
| Mitigate against replay and similar attacks | Automatic mitigation by Google Play | Use `nonce` field with server side logic |

****** For the Play Integrity API library [v1.4.0](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/release-notes#1-4-0>) and later, the minimum supported Android SDK is the same for both request types and is determined by the library's `minSdkVersion`. For [v1.3.0](<https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/release-notes#1-3-0>) and earlier releases, the minimum Android SDK required is Android 5.0 (API level 21) for Standard API requests and Android 4.4 (API level 19) for Classic API requests.*

******* All requests, including those without public limits, are subject to non-public defensive limits at high values.*

### Make classic requests infrequently

Generating an integrity token uses time, data, and battery, and each app has a maximum number of classic requests it can make per day. Therefore you should only make classic requests to check the highest value or most sensitive actions are genuine when you want an additional guarantee to a standard request. You shouldn't make classic requests for high-frequency or low-value actions. Don't make classic requests every time the app goes to the foreground nor every few minutes in the background, and avoid calling from a large number of devices at the same time. An app making too many classic requests calls may be throttled to protect users from incorrect implementations.

### Avoid caching verdicts

Caching a verdict increases the risk of attacks such as exfiltration and replay, where a good verdict is reused from an untrusted environment. If you're considering making a classic request and then caching it for use later, it's recommended instead to perform a standard request on demand. Standard requests involve some caching on the device but Google Play uses additional protection techniques to mitigate the risk of replay attacks and exfiltration.

### Use the nonce field to protect classic requests

The Play Integrity API offers a field called `nonce`, which can be used to further protect your app against certain attacks, such as replay and tampering attacks. The Play Integrity API returns the value you set in this field, inside the signed integrity response. Carefully follow the guidance on [how to generate nonces](<https://developer.android.com/google/play/integrity/classic?hl=en#nonce>) to protect your app from attacks.

> **Caution:** The value passed as the `nonce` is visible in cleartext to your app, and to Google. You should encrypt or hash the data you want to set in this field before passing it to the Play Integrity API.

### Retry classic requests with exponential backoff

Environmental conditions, such as an unstable Internet connection or an overloaded device, can cause device integrity checks to fail. This can lead to no labels being generated for a device that is otherwise trustworthy. To mitigate these scenarios, include a retry option with exponential backoff.

## Overview

![Image](<https://developer.android.com/static/images/google/play/integrity/api-usage.svg>)

**Figure 1.** Sequence diagram that shows the high-level design of the Play Integrity API.

When the user performs a high-value action in your app that you want to protect with an integrity check, complete the following steps:

1. Your app's server-side backend generates and sends a unique value to the client-side logic. The remaining steps refer to this logic as your "app".
2. Your app creates the `nonce` from the unique value and the content of your high-value action. It then calls the Play Integrity API, passing in the `nonce`.
3. Your app receives a signed and encrypted verdict from the Play Integrity API.
4. Your app passes the signed and encrypted verdict to your app's backend.
5. Your app's backend sends the verdict to a Google Play server. The Google Play server decrypts and verifies the verdict, returning the results to your app's backend.
6. Your app's backend determines how to proceed, based on the signals contained in the token payload.
7. Your app's backend sends the decision outcomes to your app.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/integrity/classic).
