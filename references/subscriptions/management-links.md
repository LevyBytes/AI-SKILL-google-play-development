## Use deep links to allow users to manage a subscription

Your app should include a link on a settings or preferences screen that allows users to manage their subscriptions, which you can incorporate into your app's natural look and feel.

You can include a deep link from your app to the Google Play subscriptions center for non-expired subscriptions, which you can determine using the `subscriptionState` field of the [subscription resource](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2>). Based on this, there are several ways you can deep link into the Play Store subscriptions center.

### Link to the subscriptions center

Use the following URL to direct users to the page that shows all of their subscriptions, as shown in figures 1 and 2:

```text
https://play.google.com/store/account/subscriptions
```

![The Play Store subscriptions screen shows status for all of a user's Google Play-billed subscriptions.](<https://developer.android.com/static/images/google/play/billing/sub_center_general.png>)

**Figure 1.** The Play Store subscriptions screen shows status for all of a user's Google Play-billed subscriptions.

<br>

![Tap on a subscription to see additional details.](<https://developer.android.com/static/images/google/play/billing/sub_management_mock_general.png>)

**Figure 2.** Tap on a subscription to see additional details.

This deep link could be useful to help a user restore a canceled subscription from the Play Store subscriptions center.

### Link to a specific subscription management page (recommended)

To directly link to the management page for a non-expired subscription, indicate the package name and `productId` associated with the purchased subscription. To programmatically determine the `productId` for an existing subscription, query your app's backend or call [`BillingClient.queryPurchasesAsync()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>) for a list of subscriptions associated with a particular user. Each subscription contains the corresponding `productId` as part of the subscription status information. Each [`SubscriptionPurchaseLineItem`](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2#subscriptionpurchaselineitem>) object associated with a subscription purchase contains the `productId` value associated with the subscription that the user purchased in that line item.

> **Note:** You set the product ID in the Play Console when you define the subscription, or using the Google Play Developer API as part of the [`Subscription`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions#resource:-subscription>) object sent in [monetization.subscriptions.create](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/create>) and [monetization.subscriptions.patch](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/patch>).

Use the following URL to direct users to a specific subscription management screen, replacing "your-sub-product-id" and "your-app-package" with the `productId` and app package name respectively:

```text
https://play.google.com/store/account/subscriptions?sku=your-sub-product-id&package=your-app-package
```

The user is then able to manage their payment methods and access features including cancellation, resubscription, and pause.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscriptions).
