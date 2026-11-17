## VoidedPurchaseNotification

A `VoidedPurchaseNotification` contains the following fields:

| `purchaseToken` | `string` | The token associated with the purchase that has been voided. This information is provided to the developer when a new purchase occurs. |
| --- | --- | --- |
| `orderId` | `string` | The unique order ID associated with the transaction that has been voided. For one time purchases, this represents the only order ID generated for the purchase. For auto-renewing subscriptions, a new order ID is generated for each renewal transaction. |
| `productType` | `int` | The `productType` for a voided purchase can have the following values: (1) `PRODUCT_TYPE_SUBSCRIPTION` - A subscription purchase has been voided. (2) `PRODUCT_TYPE_ONE_TIME` - A one-time purchase has been voided. |
| `refundType` | `int` | The `refundType` for a voided purchase can have the following values: (1) `REFUND_TYPE_FULL_REFUND` - The purchase has been fully voided. (2) `REFUND_TYPE_QUANTITY_BASED_PARTIAL_REFUND` - The purchase has been partially voided by a quantity-based partial refund, applicable only to multi-quantity purchases. A purchase can be partially voided multiple times. Note when the remaining total quantity of a multi-quantity purchase is refunded, the `refundType` will be `REFUND_TYPE_FULL_REFUND`. |

### Example

Here's an example of a notification for a new voided purchase:

```json
{
  "version":"1.0",
  "packageName":"com.some.app",
  "eventTimeMillis":"1503349566168",
  "voidedPurchaseNotification":
  {
    "purchaseToken":"PURCHASE_TOKEN",
    "orderId":"GS.0000-0000-0000",
    "productType":1
    "refundType":1
  }
}
```

### Consuming VoidedPurchaseNotification

When your RTDN client receives a `VoidedPurchaseNotification`, note the following information:

- **`packageName`**: Identifies the app.
- **`eventTimeMillis`**: Informs you of the time the status change occurred.
- **`purchaseToken`**: The token provided to the user's device when the product was purchased.
- **`orderId`**: Identifies the order associated with the voided transaction.
- **`productType`**: Indicates if the voided purchase was an in-app purchase or a subscription.
- **`refundType`**: Specifies the type of refund that voided the purchase.

> **Tip:** If you only need to locate the right purchase and order for entitlement adjustments, the information provided in the `VoidedPurchaseNotification` is sufficient. For additional data about voided purchases, use the [Google Play Voided Purchases API](<https://developers.google.com/android-publisher/voided-purchases>). This API provides a pull model for retrieving voided purchase data within a specified timestamp range.

> **Note:** For partially voided multi-quantity purchases, the `refundableQuantity` field provided by [`purchases.productsv2`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.productsv2>) contains the remaining number of purchased products that have not been voided.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/rtdn-reference).
