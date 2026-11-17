The [program-specific client setup](external-content-client-setup.md) establishes the connection and eligibility checks for this flow.

## Launch the external link

After the external transaction token is ready, the user may be linked outside of the app to a digital content offer or app download by calling [`launchExternalLink`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#launchExternalLink(android.app.Activity,com.android.billingclient.api.LaunchExternalLinkParams,com.android.billingclient.api.LaunchExternalLinkResponseListener)>) method. Google Play might render additional information dialogs to the user depending on their user settings when you call this API.

When calling the `launchExternalLink` method, details of the external link must be provided through [`LaunchExternalLinkParams`](<https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams>). This class contains the following parameters:

- **Link URI** - The link to the external website where the digital content or app download is offered. For app downloads, this link must be registered and approved in the Play Developer Console.
- **Link Type** - The type of content being offered to the user.
- **Launch Mode** - Specifies how the link is launched. For app downloads, you must set this to `LAUNCH_IN_EXTERNAL_BROWSER_OR_APP`.
- **Billing Program** - Set this to `BillingProgram.EXTERNAL_CONTENT_LINK`.

**Kotlin**

```kotlin
val params =
    LaunchExternalLinkParams.newBuilder()
        .setBillingProgram(BillingProgram.EXTERNAL_CONTENT_LINK)
        .setLinkUri(Uri.parse("https://www.myapprovedsite.com"))
        .setLinkType(LaunchExternalLinkParams.LinkType.LINK_TO_APP_DOWNLOAD)
        .setLaunchMode(
            LaunchExternalLinkParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP
        )
        .build()

val listener: LaunchExternalLinkResponseListener =
    object : LaunchExternalLinkResponseListener {
        override fun onLaunchExternalLinkResponse(
            billingResult: BillingResult
        ) {
            if (billingResult.responseCode != BillingResponseCode.OK) {
                // Handle failures such as retrying due to network errors.
                return
            }

            // If Launch Mode was set to LAUNCH_IN_EXTERNAL_BROWSER_OR_APP, the
            // user was directed outside of the app by Play. This does not give
            // any information on the user's actions during the link out, such
            // as if a transaction was completed.

            // If Launch Mode was set to CALLER_WILL_LAUNCH_LINK, then your app
            // may proceed to direct the user to the external website.
        }
    }

billingClient.launchExternalLink(activity, params, listener)
```

**Java**

```java
LaunchExternalLinkParams params =
  LaunchExternalLinkParams.newBuilder()
    .setBillingProgram(BillingProgram.EXTERNAL_CONTENT_LINK)
    .setLinkUri(Uri.parse("https://www.myapprovedsite.com"))
    .setLinkType(LaunchExternalLinkParams.LinkType.LINK_TO_APP_DOWNLOAD)
    .setLaunchMode(
      LaunchExternalLinkParams.LaunchMode.LAUNCH_IN_EXTERNAL_BROWSER_OR_APP)
    .build()

LaunchExternalLinkResponseListener listener =
  new LaunchExternalLinkResponseListener() {
    @Override
    public void onLaunchExternalLinkResponse(BillingResult billingResult) {
        if (billingResult.getResponseCode() != BillingResponseCode.OK) {
            // Handle failures such as retrying due to network errors.
            return;
        }

        // If Launch Mode was set to LAUNCH_IN_EXTERNAL_BROWSER_OR_APP, the
        // user was directed outside of the app by Play. This does not give
        // any information on the user's actions during the link out, such
        // as if a transaction was completed.

        // If Launch Mode was set to CALLER_WILL_LAUNCH_LINK, then your app
        // may proceed to direct the user to the external website.
    }
  }

billingClient.launchExternalLink(activity, params, listener);
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/externalcontentlinks/integration).
