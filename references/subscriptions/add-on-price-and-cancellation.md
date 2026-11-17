## Real-time developer notifications

The `subscriptionId` field isn't provided in [RTDN](<https://developer.android.com/google/play/billing/rtdn-reference>) for purchases of subscription with add-ons, which contain multiple item entitlements. Instead, your can use the Play Developer APIs to get the purchase and see the associated item entitlements.

## Price changes for existing subscribers

Changing subscription prices for existing subscribers of a subscription with add-ons purchase is similar to changing the prices of single subscription as described in [Change subscription prices](<https://developer.android.com/google/play/billing/price-changes>). However, there are some limitations and functional differences as described in this section.

### End a legacy price cohort

[Ending a legacy cohort](<https://developer.android.com/google/play/billing/price-changes#end-legacy>) also impacts subscription with add-on purchases. The following rules apply:

- All outstanding opt-in price increases should have the same renewal time with the new price. If an item in a subscription with add-ons purchase has an opt-in price increase which is not yet confirmed by the user, any new opt-in price increase for other items in the purchase will be ignored unless it results in the same renewal time of new price application as the existing price increase in [OUTSTANDING](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#pricechangestate>) state. Once the user confirms the price increase any newer price changes would be registered. And users can only accept all unconfirmed opt-in price increases at once.

  Example:

  - Consider a monthly subscription with add-on items A and B.
  - Item A has an outstanding migration from $7 to $10, scheduled for the upcoming renewal.
  - A new migration changes item B from $5 to $6. Its 37-day lead time puts its earliest eligible charge after item A's scheduled renewal, so item B would first qualify at the following monthly renewal.

  In this scenario, until the user accepts the price change for item A (until it is in [CONFIRMED](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#pricechangestate>) state), price change for item B isn't registered for this subscription purchase, and [SubscriptionPurchaseV2](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>) doesn't return price change details for item B. After the user confirms the price change for item A, the price change of item B starts. The user receives the item B opt-in price increase only after accepting the opt-in increase for item A.
- Google Play's email contains a list of all the items with price increases or decreases taking effect on the same day.

## Cancel subscription with add-ons

Users can cancel the entire purchase of a subscription with add-ons on Play Subscription Center, and you can only cancel the entire purchase of a subscription with add-ons by using the Google Play Developer API.

When a subscription purchase is canceled without being revoked, none of the items in the purchase will auto-renew, but the user will continue to have access to the entitled items, including any free trials, until the corresponding billing periods end.

## Revoke and refund subscriptions with add-ons

The following are some of the guidelines for revoking and refunding subscriptions:

- Use Play Console to issue an amount based refund for a specific Order without revoking access to the subscription.
- Call [`orders.refund`](<https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund>) to fully refund specific subscription payments the user has made without revoking access to the subscription.

  > **Note:** Don't call [`purchases.subscriptions.refund (deprecated)`](<https://developers.google.com/android-publisher/deprecated-apis/purchases.subscriptions/refund>) for a subscription with add-ons.
- Call [`purchases.subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) to immediately revoke access to all subscription items. With this API, you can:

  - Revoke access to all the items and provide a [prorated](<https://developer.android.com/google/play/billing/manage-purchases#prorate_refunds>) refund.
  - When revoking a subscription with add-ons using prorated refunds, a refund will be issued for the latest order of each item with a prorated amount based on the time remaining until the next renewal.
  - Revoke access for all the items and provide a [FullRefund](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke#revocationcontext>).
  - [Revoke individual item's](<https://developer.android.com/google/play/billing/subscription-with-addons?hl=en#revoke-item>) access with full refund on the item.

### Revoke individual item in a subscription with add-ons

To revoke individual subscription items in a subscription with add-ons without revoking the entire purchase, call [`purchases.subscriptionsv2.revoke`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/revoke>) with `ItemBasedRefund` field set in the `RevocationContext`. The `productId` of the item that should be revoked and refunded can be set in the `ItemBasedRefund` field.

The `ItemBasedRefund` field can be set for purchases with one or more auto-renewing subscription items.

- If there are still active items remaining in the subscription purchase after revoking the item specified in `ItemBasedRefund`, only the item will be revoked, and fully refunded without interrupting the subscription status.
- If there are no active items remaining in the subscription purchase after revoking the item specified in `ItemBasedRefund`, the item is revoked, fully refunded, and the subscription is canceled.

#### Considerations

- When using the `ItemBasedRefund` only one item can be revoked at a time. The request can be called multiple times if different items need to be revoked.
- When the subscription purchase is in any of the payment declined states, or the item specified in `ItemBasedRefund` is not owned or expired, the item turn down is blocked.
- Item turn down isn't supported in prepaid subscription.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscription-with-addons).
