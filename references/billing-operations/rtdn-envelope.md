This document lists and describes the types of [Real-time developer notifications](<https://developer.android.com/google/play/billing/getting-ready#configure-rtdn>) that you can receive from Google Play.

> **Note:** You must call the [Google Play Developer API](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) after receiving Real-time developer notifications to get the complete status and update your own backend state. These notifications tell you only that the purchase state changed. They do not give you complete information about the purchase.

## Encoding

Each publish made to a Cloud Pub/Sub topic contains a single base64-encoded data field.

```json
{
  "message": {
    "attributes": {
      "key": "value"
    },
    "data": "eyAidmVyc2lvbiI6IHN0cmluZywgInBhY2thZ2VOYW1lIjogc3RyaW5nLCAiZXZlbnRUaW1lTWlsbGlzIjogbG9uZywgIm9uZVRpbWVQcm9kdWN0Tm90aWZpY2F0aW9uIjogT25lVGltZVByb2R1Y3ROb3RpZmljYXRpb24sICJzdWJzY3JpcHRpb25Ob3RpZmljYXRpb24iOiBTdWJzY3JpcHRpb25Ob3RpZmljYXRpb24sICJ0ZXN0Tm90aWZpY2F0aW9uIjogVGVzdE5vdGlmaWNhdGlvbiB9",
    "messageId": "136969346945"
  },
  "subscription": "projects/myproject/subscriptions/mysubscription"
}
```

> **Note:** The `messageId` field is a unique identifier for the notification. However, it's recommend that you check the uniqueness of these IDs to avoid processing duplicate notifications and making redundant backend API calls, which helps optimize your API quota usage.

After you decode the base64-encoded data field, the `DeveloperNotification` contains the following fields:

```json
{
  "version": string,
  "packageName": string,
  "eventTimeMillis": long,
  "oneTimeProductNotification": OneTimeProductNotification,
  "subscriptionNotification": SubscriptionNotification,
  "voidedPurchaseNotification": VoidedPurchaseNotification,
  "pendingRefundReviewNotification": PendingRefundReviewNotification,
  "testNotification": TestNotification
}
```

These fields are described in the following table.

| version | string | The version of this notification. Initially, this is "1.0". This version is distinct from other version fields. |
| --- | --- | --- |
| packageName | string | The package name of the application that this notification relates to (for example, `com.some.thing`). |
| eventTimeMillis | long | The timestamp when the event occurred, in milliseconds since the Epoch. |
| subscriptionNotification | SubscriptionNotification | If this field is present, then this notification is related to a subscription, and this field contains additional information related to the subscription.Note that this field is mutually exclusive with pendingRefundReviewNotification, oneTimeProductNotification, voidedPurchaseNotification, and testNotification. |
| oneTimeProductNotification | OneTimeProductNotification | If this field is present, then this notification is related to a one-time purchase, and this field contains additional information related to the purchase.Note that this field is mutually exclusive with pendingRefundReviewNotification, subscriptionNotification, voidedPurchaseNotification, and testNotification. |
| voidedPurchaseNotification | VoidedPurchaseNotification | If this field is present, then this notification is related to a voided purchase, and this field contains additional information related to the voided purchase.Note that this field is mutually exclusive with pendingRefundReviewNotification, oneTimeProductNotification, subscriptionNotification, and testNotification. |
| pendingRefundReviewNotification | PendingRefundReviewNotification | If this field is present, this notification relates to a chargeback request for which you can suggest a resolution. Respond to this notification by calling the `ReviewRefund` API. Note that this field is mutually exclusive with subscriptionNotification, oneTimeProductNotification, voidedPurchaseNotification, and testNotification. |
| testNotification | TestNotification | If this field is present, then this notification is related to a test publish. These are sent only through the Google Play Developer Console.Note that this field is mutually exclusive with pendingRefundReviewNotification, oneTimeProductNotification, subscriptionNotification, and voidedPurchaseNotification. |

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/rtdn-reference).
