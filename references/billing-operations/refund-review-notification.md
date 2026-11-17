## PendingRefundReviewNotification

A `PendingRefundReviewNotification` is sent when a user requests a chargeback for a purchase, and the request requires developer review. When you receive this notification, you should evaluate the request and provide a refund suggestion and purchase usage evidence within 24 hours by calling the [`ReviewRefund`](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders/reviewrefund>) API.

> **Note:** Pending reviews support only `CHARGEBACK` as the refund reason.

A `PendingRefundReviewNotification` contains the following fields:

```json
{
  "version": string,
  "pendingRefundToken": string,
  "orderId": string,
  "refundReason": int,
  "obfuscatedAccountId": string,
  "obfuscatedProfileId": string
}
```

| version | string | The version of this notification. Initially, this is "1.0". This version is distinct from other version fields. |
| --- | --- | --- |
| pendingRefundToken | string | A unique token that identifies the pending refund request under review. Pass this token when calling the [ReviewRefund API](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders/reviewrefund>). |
| orderId | string | The order ID of the purchase that is subject to the pending refund review. |
| refundReason | int | The reason for the refund request. Pending reviews support only `CHARGEBACK` (7) as a refund reason. Your code should handle new reasons as they become available. |
| obfuscatedAccountId | string | (If applicable) The obfuscated developer-specified user account ID that was supplied when the purchase was made. |
| obfuscatedProfileId | string | (If applicable) The obfuscated developer-specified profile ID that was supplied when the purchase was made. |

### Example

Here's an example of a pending refund review notification:

```json
{
  "version":"1.0",
  "packageName":"com.some.thing",
  "eventTimeMillis":"1503350156918",
  "pendingRefundReviewNotification":
  {
    "version":"1.0",
    "pendingRefundToken":"example-token",
    "orderId":"GPA.1234-5678-9012-34567",
    "refundReason":7,
    "obfuscatedAccountId":"user-account-id",
    "obfuscatedProfileId":"user-profile-id"
  }
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/rtdn-reference).
