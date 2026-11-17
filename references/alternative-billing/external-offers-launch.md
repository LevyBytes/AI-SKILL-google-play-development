The [program-specific client setup](external-offers-client-setup.md) establishes the connection and eligibility checks for this flow.

## Launch external offer flow

To start an external offer flow, your eligible app must call the [`launchExternalLink()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchExternalLink(android.app.Activity,com.android.billingclient.api.LaunchExternalLinkParams,com.android.billingclient.api.LaunchExternalLinkResponseListener)>) API from your app's main thread. This API takes an input of an [`LaunchExternalLinkParams`](<https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams>) object. To create an `LaunchExternalLinkParams` object, use the [`LaunchExternalLinkParams.Builder`](<https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams.Builder>) class. This class contains the following parameters:

- **linkUri** - The link to the external website where the digital content or app download is offered. For app downloads, this link must be registered and approved in the Play Developer Console.
- **linkType** - The type of content being offered to the user.
- **launchMode** - Specifies how the link is launched. For app downloads, you must set this to `LAUNCH_IN_EXTERNAL_BROWSER_OR_APP`.
- **billingProgram** - Set this to `BillingProgram.EXTERNAL_OFFER`.

When you call [`launchExternalLink()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchExternalLink(android.app.Activity,com.android.billingclient.api.LaunchExternalLinkParams,com.android.billingclient.api.LaunchExternalLinkResponseListener)>), it might show additional information dialogs to the user based on their user settings. Depending on the `launchMode` parameter, Play either launches the link URI in an external browser or returns the flow to your app to launch the URI. In most cases, you can use the [`LAUNCH_IN_EXTERNAL_BROWSER_OR_APP`](<https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams.LaunchMode#LAUNCH_IN_EXTERNAL_BROWSER_OR_APP()>) mode where Play will launch the URI for you. If you want to have more customized behavior, such as launching the URI in a webview or opening the URI in a specific browser, you can use the [`CALLER_WILL_LAUNCH_LINK`](<https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams.LaunchMode#CALLER_WILL_LAUNCH_LINK()>) mode. To protect user privacy, make sure no personally identifiable information (PII) is passed in the URI.

> **Note:** Users might not return to your app after the link URI is opened in an external browser or app. Execute any necessary in-app tasks before calling [`launchExternalLink()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchExternalLink(android.app.Activity,com.android.billingclient.api.LaunchExternalLinkParams,com.android.billingclient.api.LaunchExternalLinkResponseListener)>).

**Kotlin**

```kotlin
// An activity reference from which the external offers flow will be launched.
val activity = this.activity

val params =
    LaunchExternalLinkParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_OFFER)
        // You can pass along the external transaction token from
        // BillingProgramReportingDetails as a URL parameter in the URI
        .setLinkUri(yourLinkUri)
        .setLinkType(LaunchExternalLinkParams.LinkType.LINK_TO_APP_DOWNLOAD)
        .setLaunchMode(
            LaunchExternalLinkParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP
        )
        .build()

val listener: LaunchExternalLinkResponseListener =
    LaunchExternalLinkResponseListener { billingResult ->
        if (billingResult.responseCode == BillingResponseCode.OK) {
            // Proceed with the rest of the external offer flow. If the user
            // purchases an item, be sure to report the transaction to Google Play.
        } else {
            // Handle failures such as retrying due to network errors.
        }
    }

billingClient.launchExternalLink(activity, params, listener)
```

**Java**

```java

// An activity reference from which the external offers flow will be launched.
Activity activity = ...;

LaunchExternalLinkParams params = LaunchExternalLinkParams.newBuilder()
  .setBillingProgram(BillingProgram.EXTERNAL_OFFER)
  // You can pass along the external transaction token from  
  // BillingProgramReportingDetails as a URL parameter in the URI
  .setLinkUri(yourLinkUri)
  .setLinkType(LaunchExternalLinkParams.LinkType.LINK_TO_APP_DOWNLOAD)
  .setLaunchMode(
    LaunchExternalLinkParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
  .build();

LaunchExternalLinkResponseListener listener =
  new LaunchExternalLinkResponseListener() {
    @Override
    public void onLaunchExternalLinkResponse(BillingResult billingResult) {
      if (billingResult.responseCode == BillingResponseCode.OK) {
        // Proceed with the rest of the external offer flow. If the user
        // purchases an item, be sure to report the transaction to Google
        // Play.
      } else {
        // Handle failures such as retrying due to network errors.
      }
    }
  }

billingClient.launchExternalLink(activity, params, listener);

```

If you set `LaunchMode` to `CALLER_WILL_LAUNCH_LINK`, you should direct the user outside of the app only if `onLaunchExternalLinkResponse` provides `BillingResponseCode.OK`.

### Report transactions to Google Play

> **Note:** See [Enrolling in the external offers program](<https://support.google.com/googleplay/android-developer/answer/14372887>) for transaction reporting requirements.

You must report all external transactions to Google Play by calling the Google Play Developer API from your backend. When you report a transaction, you must provide an `externalTransactionToken` obtained from the [`createBillingProgramReportingDetailsAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#createBillingProgramReportingDetailsAsync(com.android.billingclient.api.BillingProgramReportingDetailsParams,com.android.billingclient.api.BillingProgramReportingDetailsListener)>) API. If a user makes multiple purchases, you can use the same `externalTransactionToken` to report each purchase. To learn how to report a transaction, see the [backend integration guide](<https://developer.android.com/google/play/billing/outside-gpb-backend>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/external/integration).
