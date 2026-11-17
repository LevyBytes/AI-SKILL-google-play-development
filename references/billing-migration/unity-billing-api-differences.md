## Changes to Unity API behavior

When you are using the Google Play Billing plugin, most of the APIs behave the same way as Unity's standard IAP implementation for other app stores. However, there are some cases where the APIs will behave differently. This section describes these behavior differences.

### Developer payload is not supported

Google Play deprecated developer payload and is replacing it with alternatives that are more meaningful and contextual. For this reason, developer payload is not supported. For more information on alternatives, see the page about [Developer payload](<https://developer.android.com/google/play/billing/developer-payload>).

You can continue to use the same interfaces that are defined by Unity's standard IAP implementation for other app stores, including `IStoreController`. When you initiate a purchase, you can still use `IStoreController` and call the `InitiatePurchase()` method:

```c#
public void InitiatePurchase(Purchasing.Product product, string payload);
```

However, any payload that you pass in won’t take effect (won’t appear in the final receipt).

### SubscriptionManager is not supported

Unity IAP provides the [`SubscriptionManager`](<https://docs.unity3d.com/Manual/UnityIAPSubscriptionProducts.html>) class for managing subscriptions. Because Unity's standard IAP implementation of this class uses developer payload, this class is not supported. You can still create this class, but you might receive unreliable data when using any of the class's getter methods.

### UpdateSubscription has small API changes

The Google Play Billing plugin does not support using the `SubscriptionManager.UpdateSubscription()` and `SubscriptionManager.UpdateSubscriptionInGooglePlayStore()` methods to upgrade and downgrade your subscriptions. If your game calls these methods, a `GooglePlayStoreUnsupportedException` is thrown.

The Google Play Billing Library provides an alternative API to use in place of these methods. To upgrade or downgrade a subscription, call the `UpdateSubscription()` method using proration mode:

```c#
void UpdateSubscription(Product oldProduct, Product newProduct,
           GooglePlayStoreProrationMode prorationMode = GooglePlayStoreProrationMode.Unknown);
```

You can either wrap this method call with a platform check or in a catch block when `GooglePlayStoreUnsupportedException` is caught.

For more information and examples of how to use proration mode, see [Set proration mode](<https://developer.android.com/google/play/billing/billing_subscriptions#prorate>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/unity).
