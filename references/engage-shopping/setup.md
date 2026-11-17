Use the [Engage SDK overview](../engage/overview.md) for supported surfaces, participation and integration estimates.

This guide contains instructions for developer partners to deliver shopping content to Engage content surfaces.

## Category support and surfaces

Engage SDK surface eligibility is based on your app's content category. Use the following table to determine your eligibility for specific surfaces:

| Status | Content category or use case | Supported surfaces |
| --- | --- | --- |
| **Supported**<br> (Eligible on all surfaces) | Clothes shopping Online marketplace Retailer Food & drink shopping / grocery Discounts & coupons Pet / supplies House & home / Real estate | Collections Play Store Apps tab Play Store You tab Play Store store listing page |
| **Not supported** | Shopper app B2B Shopping Seller / merchant app Receipts scanner rewards Telecom service Buy now pay later |  |

## Integration detail

This section details the steps, data models, and terminology required to integrate with the Engage SDK for shopping content.

### Terminology

This integration includes the following five cluster types: **Recommendation**, **Featured**, **Shopping Cart**, **Shopping List**, **Reorder** and **Shopping Order Tracking**.

- **Recommendation** clusters show personalized shopping suggestions from an individual developer partner. These recommendations can be personalized to the user or generalized (for example, trending items). Use these to feature products, events, sales, promos, and subscriptions.

  Your recommendations take the following structure:

  - **Recommendation Cluster:** A UI view that contains a group of recommendations from the same developer partner.
  - **ShoppingEntity:** An object representing a single item in a cluster.
- The **Featured** cluster showcases a selection of entities from multiple developer partners in one UI grouping. There will be a single Featured cluster, which is surfaced near the top of the UI with a priority placement above all Recommendation clusters. Each developer partner will be allowed to broadcast up to 10 entities in the Featured cluster.
- The **Shopping Cart** cluster shows a sneak peek of shopping carts from many developer partners in one UI grouping, nudging users to complete their outstanding carts. There is a single Shopping Cart cluster, which is surfaced near the top of the UI, with a priority placement above all Recommendation clusters. Each developer partner is allowed to broadcast up to 3 `ShoppingCart` instances in the Shopping Cart cluster.

  Your Shopping Cart takes the following structure:

  - **Shopping Cart Cluster:** A UI view that contains a group of shopping cart previews from many developer partners.
  - **ShoppingCart:** An object representing the shopping cart preview for a single developer partner, to be displayed in the Shopping Cart cluster. The `ShoppingCart` must show the total count of items in the cart and may also include images for some items in the user's cart.
- The **Shopping List** cluster shows a sneak peek of the shopping lists from multiple developer partners in one UI grouping, prompting users to return to the corresponding app to update and complete their lists. There is a single Shopping List cluster.
- The **Reorder** cluster shows a sneak peek of the previous orders from multiple developer partners in one UI grouping, prompting users to reorder. There is a single Reorder cluster.

  - Reorder cluster must show the total count of items in the user's previous order and must also include one of the following:

    - Images for X items in the user's previous order.
    - Labels for X items in the user's previous order.
- The **Shopping Order Tracking** cluster shows a sneak peek of pending or recently completed shopping orders from many developer partners in one UI grouping, allowing users to track their orders.

  There is a single ShoppingOrderTracking cluster that is surfaced near the top of the UI, with a priority placement above all Recommendation clusters. Each developer partner is allowed to broadcast multiple ShoppingOrderTrackingEntity items in the Shopping Order Tracking cluster.

  - Your ShoppingOrderTrackingCluster takes the following structure:

    - **ShoppingOrderTracking Cluster**: A UI view that contains a group of order tracking previews from many developer partners
    - **ShoppingOrderTrackingEntity**: An object representing a shopping order tracking preview for a single developer partner, to be displayed in the Shopping Order Tracking cluster. The ShoppingOrderTrackingEntity must show the status of the order and the order time. We strongly recommend populating the expected delivery time for ShoppingOrderTrackingEntity, as it's displayed to users when provided.

    > **Note:** Provide multiple ShoppingOrderTrackingEntity objects if an order has been split into multiple shipments.

### Pre-work

Minimum API level: 19

Add the `com.google.android.engage:engage-core` library to your app:

```groovy
dependencies {
    // Make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.engage:engage-core:1.6.0'
}
```

For more information, see [Package visibility in Android 11](<https://developer.android.com/about/versions/11/privacy/package-visibility>).

### Summary

The design is based on an implementation of a [bound service](<https://developer.android.com/guide/components/bound-services>).

The data a client can publish is subject to the following limits for different cluster types:

| Cluster type | Cluster limits | Maximum entity limits in a cluster |
| --- | --- | --- |
| Recommendation Cluster(s) | At most 7 | At most 50 `ShoppingEntity` |
| Featured Cluster | At most 1 | At most 20 `ShoppingEntity` |
| Shopping Cart Cluster | At most 1 | At most 3 `ShoppingCart` Multiple carts only expected for apps with separate carts per merchant. |
| Shopping List Cluster | At most 1 | At most 3 `ShoppingList` |
| Shopping Reorder Cluster | At most 1 | At most 1 `ReorderEntity` |
| Shopping Order Tracking Cluster | At most 3 | At most 3 `ShoppingOrderTrackingEntity` |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/shopping).
