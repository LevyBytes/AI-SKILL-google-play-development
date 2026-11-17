> **Warning:** Rewarded products are no longer supported.

One method of unlocking in-app products and benefits for your users is to create *rewarded products*, or items that users receive after they watch a video advertisement. By providing rewarded products, you allow users to obtain in-app rewards and benefits without them having to make direct purchases.

This document explains how to implement functionality specific to rewarded products. The [workflow diagram](<https://developer.android.com/google/play/billing/billing_rewarded_products?hl=en#workflow-diagram>) section of this page illustrates the process.

## Identify your app's rewarded products

Rewarded products have a [`SkuType`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.SkuType>) of [`INAPP`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient.SkuType#INAPP()>). To ensure users are able to watch multiple ads and get multiple rewards, the products need to be consumed.

Before you can offer a rewarded product to a user, you must obtain the [`SkuDetails`](<https://developer.android.com/reference/com/android/billingclient/api/SkuDetails>) for the product. To do this, call `querySkuDetailsAsync()` with `SkuType.INAPP` as the product type.

## Declare age-appropriate ads

To help facilitate compliance with legal obligations related to children and to underage users, including the [Children's Online Privacy Protection Act (COPPA)](<https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy>) and the [General Data Protection Regulation (GDPR)](<http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679>), your app should declare which ads should be treated as child-directed in the United States and which ads are directed at users who are under [the applicable age of consent in their country](<https://support.google.com/accounts/answer/1350409>). The AdMob Help Center explains when you should tag your ad requests for [child-directed treatment](<https://support.google.com/admob/answer/6219315>) and when you should tag them for [under-the-age-of-consent treatment](<https://support.google.com/admob/answer/9009425>), as well as the effects of doing so.

As you create your app's billing client, consider whether the rewarded ad requests should be treated as child-directed or whether they should be directed at users who are under the age of consent. If the ad requests should have these restrictions in place, call the `setChildDirected()` and `setUnderAgeOfConsent()` methods, passing appropriate values into each method.

The following code snippet shows how to declare that video ads should be suitable for children or for users who are under the age of consent:

**Kotlin**

```kotlin
val billingClient = BillingClient.newBuilder(context)
        .setListener(this)
        .setChildDirected(ChildDirected.CHILD_DIRECTED)
        .setUnderAgeOfConsent(UnderAgeOfConsent.UNDER_AGE_OF_CONSENT)
        .build()
```

**Java**

```java
BillingClient billingClient =
    BillingClient.newBuilder(context)
        .setListener(this)
        .setChildDirected(ChildDirected.CHILD_DIRECTED)
        .setUnderAgeOfConsent(UnderAgeOfConsent.UNDER_AGE_OF_CONSENT)
        .build();
```

> **Note:** After you've created a billing client, you cannot change the values for `childDirected` and `underAgeOfConsent`. If you need to use different values, such as when the user switches game accounts, disconnect your current billing client, make a new instance of the client, and connect that new instance to the Google Play Billing Library.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/billing_rewarded_products).
