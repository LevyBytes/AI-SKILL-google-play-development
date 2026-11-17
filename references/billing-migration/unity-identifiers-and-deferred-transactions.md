## Implement Google Play Billing Library features in your game

The Google Play Billing plugin extends Unity IAP services, so you can use the same Unity APIs to manage common purchasing workflows. Note that there are some [minor changes to API behavior](<https://developer.android.com/google/play/billing/unity?hl=en#behavior-changes>) due to differences between the Google Play Billing Library and Unity's standard IAP implementation for other app stores. If you're new to the Unity IAP APIs, see the "Making a Purchase Script" section in the [Unity IAP tutorial](<https://learn.unity.com/tutorial/unity-iap#5c7f8528edbc2a002053b46e>) for an example of how to implement basic purchasing flows.

The Google Play Billing Library also includes some features that are unique to the Google Play store. You can access these features through an extended interface. The rest of this section describes how to implement these unique Google Play Billing Library features in your game.

### Enable deferred purchases

Google Play supports deferred purchases, also called [pending transactions](<https://developer.android.com/google/play/billing/billing_library_overview#pending>) or pending purchases, where users can create a purchase and complete it later using cash in stores.

To enable deferred purchases, use your IAP builder to modify your module's configuration by calling the `EnableDeferredPurchase()` method:

```c#
// Create a builder using a GooglePlayStoreModule.
var configurationBuilder =
    ConfigurationBuilder.Instance(Google.Play.Billing.GooglePlayStoreModule.Instance());
// Enable deferred purchases
configurationBuilder.Configure<Google.Play.Billing.IGooglePlayConfiguration>()
    .EnableDeferredPurchase();
```

Next, implement a deferred purchases callback using the Play Store extensions:

```c#
// Get the plugin extensions for the Google Play Store.
_playStoreExtensions =
    extensions.GetExtension<Google.Play.Billing.IGooglePlayStoreExtensions>();

// Set the deferred purchases callback.
_playStoreExtensions.SetDeferredPurchaseListener(
    delegate(Product product)
    {
        // Do not grant the item here. Instead, record the purchase and remind
        // the user to complete the transaction in the Play Store.
    });
```

### Pass obfuscated account IDs to Google Play

You can pass obfuscated user account IDs to Google Play to facilitate abuse detection, such as detecting if many devices are making purchases on the same account in a short period of time.

> **Note:** This account ID is also returned with purchase data. If you were using developer payload to identify users, you can use this account ID as an alternative.

To pass an obfuscated account ID, call the `SetObfuscatedAccountId()` method from the extensions API:

```c#
// Get the plugin extensions for the Google Play Store.
_playStoreExtensions =
    extensions.GetExtension<Google.Play.Billing.IGooglePlayStoreExtensions>();

// Pass an obfuscated account ID.
_playStoreExtensions.SetObfuscatedAccountId(obfuscatedAccountId);
```

### Pass obfuscated profile IDs to Google Play

You can pass an obfuscated profile ID to Google Play to facilitate fraud detection, such as detecting if many devices are making purchases on the same account in a short period of time. This is similar to [passing an obfuscated user account ID](<https://developer.android.com/google/play/billing/unity?hl=en#obfuscated-account-ids>). In both cases the ID represents a single user, but the profile ID lets you uniquely identify a single user across multiple profiles that they have within a single app. After you send an obfuscated profile ID to Google Play, you can retrieve that ID later in a purchase receipt.

To pass an obfuscated profile ID, use your IAP builder to modify your module's configuration by calling the `SetObfuscatedProfileId()` method:

```c#
// Get the plugin extensions for the Google Play Store.
_playStoreExtensions =
    extensions.GetExtension<Google.Play.Billing.IGooglePlayStoreExtensions>();

// Pass an obfuscated profile ID.
_playStoreExtensions.SetObfuscatedProfileId(obfuscatedProfileId);
```

### Confirm price changes for subscriptions

Google Play allows you to [change the price of an active subscription](<https://developer.android.com/google/play/billing/billing_subscriptions#change-price-sub>). Your game's users must confirm any price change before the change can take effect. To prompt users to confirm a price change for their subscription, call the `ConfirmSubscriptionPriceChange()` method:

```c#
// Get the plugin extensions for the Google Play Store.
_playStoreExtensions =
    extensions.GetExtension<Google.Play.Billing.IGooglePlayStoreExtensions>();

_playStoreExtensions.ConfirmSubscriptionPriceChange(productId,
    delegate (bool success)
    {
        // Returns whether the user has accepted the new price or not.
    });
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/unity).
