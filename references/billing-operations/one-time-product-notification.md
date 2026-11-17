## OneTimeProductNotification

> **Note:** A `OneTimeProductNotification` is sent only if you've chosen to receive one-time product purchase events. For more information, see [Enable real-time developer notifications for your app](<https://developer.android.com/google/play/billing/getting-ready#enable-rtdn>).

A `OneTimeProductNotification` contains the following fields:

```json
{
  "version": string,
  "notificationType": int,
  "purchaseToken": string,
  "sku": string
}
```

| version | string | The version of this notification. Initially, this will be "1.0". This version is distinct from other version fields. |
| --- | --- | --- |
| notificationType | int | The type of notification. It can have the following values: (1) ONE_TIME_PRODUCT_PURCHASED - A one-time product was successfully purchased by a user. (2) ONE_TIME_PRODUCT_CANCELED - A one-time product purchase has been canceled or revoked. |
| purchaseToken | string | The token provided to the user's device when purchase was made. |
| sku | string | The purchased one-time product ID (for example, "sword_001") |

### Example

Here's an example of a notification for a new one-time purchase:

```json
{
  "version":"1.0",
  "packageName":"com.some.thing",
  "eventTimeMillis":"1503349566168",
  "oneTimeProductNotification":
  {
    "version":"1.0",
    "notificationType":1,
    "purchaseToken":"PURCHASE_TOKEN",
    "sku":"my.sku"
  }
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/rtdn-reference).
