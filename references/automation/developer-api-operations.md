## Reporting API

The [Reporting API](<https://developers.google.com/play/developer/reporting>) is for developers who want to build automated workflows on top of Play Console data, or developers who use Play Console data for internal business reporting and analysis, potentially alongside other datasets. This gives you programmatic access to app-level data and metrics for internal reporting, analysis, and automation.

The reporting API offers access to Android vitals data, including crash rate, ANR rate, wake-up and wake-lock issues, and error stack traces.

### Best practices

- This version of the Reporting API has a default limit of 10 queries per second. You can view your quota usage in the [Quotas section](<https://console.cloud.google.com/apis/api/playdeveloperreporting.googleapis.com/quotas>) of the Google Cloud Console. If you need to exceed this limit, submit a request using the [Google Play Developer Reporting API quota request form](<https://support.google.com/googleplay/android-developer/contact/apiqr>).

## Reply to Reviews API

The [Reply to Reviews API](<https://developers.google.com/android-publisher/reply-to-reviews>) lets you view user feedback for your app and reply to this feedback. You can use this API to interact with users directly within your existing customer support toolkit, such as a CRM system.

The Reply to Reviews API lets you access feedback only for production versions of your app. If you want to see feedback on alpha or beta versions of your app, use the Google Play Console instead. Also, note that the API shows only the reviews that include comments. If a user rates your app but doesn't provide a comment, their feedback isn't accessible from the API.

## Permissions API

The Permissions API gives developers the ability to [automate permission management](<https://developers.google.com/android-publisher/api-ref/rest/v3/users/list>) within the Play Console. This can allow you flexible control over who has access to your developer account, without manual involvement.

With the Permissions API, you can perform administrative functions such as:

- Removing users' access when they leave your company.
- Granting access to an app when a user joins the relevant team.

## Voided purchases API

The [Voided Purchases API](<https://developers.google.com/android-publisher/voided-purchases>) provides a list of orders that are associated with purchases that a user has voided. You can use information from this list to implement a revocation system that prevents the user from accessing products from those orders.

This API applies to one-time in-app orders and app subscriptions.

A purchase can be voided in the following ways:

- The user requests a refund for their order.
- The user cancels their order.
- An order is charged back.
- Developer cancels or refunds order. Note: only revoked orders will be shown in the Voided Purchases API. If developer refunds without setting the revoke option, orders won't show up in the API.
- Google cancels or refunds order.

By using this API, you help create a more balanced and fair experience for all of your app's users, particularly if your app is a game.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/developer-api).
