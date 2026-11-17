Use the [Engage SDK overview](../engage/overview.md) for supported surfaces, participation and integration estimates.

This guide contains instructions for developer partners to deliver food content (food ordering, food or restaurant reviews & discovery, meal subscriptions, recipes) to Engage content surfaces.

## Category support and surfaces

Engage SDK surface eligibility is based on your app's content category. Use the following table to determine your eligibility for specific surfaces:

| Status | Content category or use case | Supported surfaces |
| --- | --- | --- |
| **Supported**<br> (Eligible on all surfaces) | Food / coffee / drink ordering or delivery Restaurant / Food discovery, reviews, & reservations Meal subscriptions Recipes & Cooking | Collections Play Store Apps tab Play Store You tab Play Store store listing page |
| **Not supported** | Driver / deliverer app Cooking tools / controls |  |

## Integration detail

This section details the steps, data models, and terminology required to integrate with the Engage SDK for food content.

### Terminology

This integration includes the following five cluster types: **Recommendation**, **Featured**, **Food Shopping Cart**, **Food Shopping List**, and **Reorder**.

- **Recommendation** clusters show personalized food-related suggestions from an individual developer partner. These recommendations can be personalized to the user or generalized (for example, new on sale). Use them to feature items such as recipes, stores, dishes, or groceries.

  - A Recommendation cluster can be made of `ProductEntity`, `StoreEntity`, or `RecipeEntity` listings, but not a mix of different entity types.

  ![Image](<https://developer.android.com/static/images/guide/playcore/engage/food-entities.png>)

  **Figure :**`ProductEntity`, `StoreEntity`, and `RecipeEntity`. (*UI for illustrative purposes only)
- The **Featured** cluster showcases a selection of entities from multiple developer partners in one UI grouping. There will be a single Featured cluster, which is surfaced near the top of the UI with a priority placement above all Recommendation clusters. Each developer partner will be allowed to broadcast up to 10 entities in the Featured cluster.

  ![Image](<https://developer.android.com/static/images/guide/playcore/engage/food-featured.png>)

  **Figure :** Featured cluster with the `RecipeEntity`. (*UI for illustrative purposes only)
- The **Food Shopping Cart** cluster shows a sneak peek of grocery shopping carts from multiple developer partners in one UI grouping, prompting users to complete their outstanding carts. There is a single Food Shopping Cart cluster.

  - Food Shopping Cart Cluster must show the total count of items in the cart and may also include images for X items in the user's cart.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/food-shopping-cart.png>)

    **Figure:** Food Shopping Cart cluster from a single partner. (*UI for illustrative purposes only)
- The **Food Shopping List** cluster shows a sneak peek of the grocery shopping lists from multiple developer partners in one UI grouping, prompting users to return to the corresponding app to update and complete their lists. There is a single Food Shopping List cluster.

  ![Image](<https://developer.android.com/static/images/guide/playcore/engage/food-shopping-list.png>)

  **Figure:** Food Shopping List cluster from a single partner. (*UI for illustrative purposes only)
- The **Reorder** cluster shows a sneak peek of the previous orders from multiple developer partners in one UI grouping, prompting users to reorder. There is a single Reorder cluster.

  - Reorder cluster must show the total count of items in the user's previous order and must also include one of the following:

    - Images for X items in the user's previous order.
    - Labels for X items in the user's previous order.

  ![Image](<https://developer.android.com/static/images/guide/playcore/engage/food-reorder-cluster.png>)

  **Figure:** Food Reorder cluster from a single partner. (*UI for illustrative purposes only)

### Pre-work

Minimum API level: 19

Add the `com.google.android.engage:engage-core` library to your app:

```groovy
dependencies {
    // Make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.engage:engage-core:1.6.0'
}
```

### Summary

The design is based on an implementation of a [bound service](<https://developer.android.com/guide/components/bound-services>).

The data a client can publish is subject to the following limits for different cluster types:

| Cluster type | Cluster limits | Maximum entity limits in a cluster |
| --- | --- | --- |
| Recommendation Cluster(s) | At most 7 | At most 50 (`ProductEntity`, `RecipeEntity`, or `StoreEntity`) |
| Featured Cluster | At most 1 | At most 20 (`ProductEntity`, `RecipeEntity`, or `StoreEntity`) |
| Food Shopping Cart Cluster | At most 1 | At most 3 `FoodShoppingCart` |
| Food Shopping List Cluster | At most 1 | At most 3 `FoodShoppingList` |
| Food Reorder Cluster | At most 1 | At most 1 `ReorderEntity` |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/food).
