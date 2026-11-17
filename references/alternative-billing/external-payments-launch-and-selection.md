The [program-specific client setup](external-payments-client-setup.md) establishes the connection and eligibility checks for this flow.

## Launching the external payments flow

Launch the external payments flow by calling [`launchBillingFlow()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchBillingFlow(android.app.Activity,com.android.billingclient.api.BillingFlowParams)>) similar to [launching a purchase flow](<https://developer.android.com/google/play/billing/integrate#launch>) with a Google Play billing system integration but with an additional parameter [`DeveloperBillingOptionParams`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperBillingOptionParams>) provided indicating your app would like to enable the external payments flow for this purchase.

`DeveloperBillingOptionParams` must contain the following:

- `billingProgram` set to `EXTERNAL_PAYMENTS` billing program
- `linkURI` set to the link destination
- `launchMode` set to [`LAUNCH_IN_EXTERNAL_BROWSER_OR_APP`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperBillingOptionParams.LaunchMode#LAUNCH_IN_EXTERNAL_BROWSER_OR_APP()>) if Google Play should launch the link or [`CALLER_WILL_LAUNCH_LINK`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperBillingOptionParams.LaunchMode#CALLER_WILL_LAUNCH_LINK()>) if your app will launch the link.

When your app calls `launchBillingFlow()` with `DeveloperBillingOptionParams` provided, the Google Play billing system performs the following check:

- The system checks if the user's [Google Play country](<https://support.google.com/googleplay/answer/7431675>) is a country that supports external payments (i.e. a supported country). If the user's Google Play country is supported, Google Play checks whether external payments is enabled based on the configuration of the BillingClient and whether `DeveloperBillingOptionParams` is provided.

  - If external payments have been enabled, the purchase flow shows the user choice UX.
  - If external payments are not enabled, the purchase flow shows the standard Google Play billing system UX, without user choice.
- If the user's Google Play country is not a supported country, the purchase flow shows the standard Google Play billing system UX, without user choice.

|  | User's Play country is a supported country | User's Play country is not a supported country |
| --- | --- | --- |
| External payments enabled ([BillingClient setup](<https://developer.android.com/google/play/billing/externalpaymentlinks/integration?hl=en#setup>) and [launchBillingFlow](<https://developer.android.com/google/play/billing/externalpaymentlinks/integration?hl=en#launching-external>)) | User sees user choice UX | User sees standard Google Play billing system UX |
| External payments not enabled (either not enabled during BillingClient setup or DeveloperBillingOptionParams not provided to launchBillingFlow) | User sees standard Google Play billing system UX | User sees standard Google Play billing system UX |

The following snippet demonstrates how to construct `DeveloperBillingOptionParams`:

**Kotlin**

```kotlin
val developerBillingOptionParams =
    DeveloperBillingOptionParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_PAYMENTS)
        .setLinkUri("https://www.example.com/external/purchase".toUri())
        .setLaunchMode(
            DeveloperBillingOptionParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP
        )
        .build()
```

**Java**

```java
DeveloperBillingOptionParams developerBillingOptionParams =
    DeveloperBillingOptionParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_PAYMENTS)
        .setLinkUri(Uri.parse("https://www.example.com/external/purchase"))
        .setLaunchMode(
            DeveloperBillingOptionParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
        .build();
```

## Handle the user selection

How you handle the rest of the purchase flow differs depending on whether the user selected Google Play's billing system or to pay on your website.

### When the user selects to pay on your website or on a payment app

If the user chooses to pay on your website, Google Play calls the `DeveloperProvidedBillingListener` to notify the app that the user chose to pay on your website or on a payment app. In particular, the [`onUserSelectedDeveloperBilling()`](<https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingListener#onUserSelectedDeveloperBilling(com.android.billingclient.api.DeveloperProvidedBillingDetails)>) method is called.

If your app sets `launchMode` to `LAUNCH_IN_EXTERNAL_BROWSER_OR_APP` then Google Play will launch the link. If `launchMode` was set to `CALLER_WILL_LAUNCH_LINK` your app is responsible for launching the link. When linking users to a payment app, you are responsible for checking that the user has the payment app already installed on their device.

Use this token to report any transaction resulting from this choice as explained in the [backend integration guide](<https://developer.android.com/google/play/billing/outside-gpb-backend>).

### When the user selects Google Play's billing system

If the user chooses Google Play's billing system, they continue with the purchase through Google Play.

- See [Processing purchases](<https://developer.android.com/google/play/billing/integrate#process>) in the library integration guide for more information about how to handle new in-app purchases through Google Play's billing system.
- See [New subscriptions](<https://developer.android.com/google/play/billing/subscriptions#new>) in the subscription management guide for additional guidance for subscription purchases.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/externalpaymentlinks/integration).
