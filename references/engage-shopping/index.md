Use AppEngageShoppingClient with product, cart, list, reorder and tracking models. Setup and service availability precede publishing; broadcast registration and acceptance complete the integration.

### Step 2: Provide Cluster data

It is recommended to have the content publish job executed in the background (for example, using [WorkManager](<https://developer.android.com/topic/libraries/architecture/workmanager>)) and scheduled on a regular basis or on an event basis (for example, every time the user opens the app or when the user just added something to their cart).

`AppEngageShoppingClient` is responsible for publishing shopping clusters.

Following APIs are exposed to publish clusters in the client:

- [`isServiceAvailable`](service-availability.md)
- [`publishRecommendationClusters`](publish-recommendations.md)
- [`publishFeaturedCluster`](publish-featured.md)
- [`publishShoppingCarts`](publish-shopping-carts.md)
- [`publishShoppingLists`](publish-shopping-lists.md)
- [`publishShoppingReorderCluster`](publish-reorders.md)
- [`publishShoppingOrderTrackingCluster`](publish-order-tracking.md)
- [`publishUserAccountManagementRequest`](publish-user-management.md)
- [`updatePublishStatus`](publish-status.md)
- [`deleteRecommendationsClusters`](delete-recommendations-and-featured.md)
- [`deleteFeaturedCluster`](delete-recommendations-and-featured.md)
- [`deleteShoppingCartCluster`](delete-cart-list-and-reorder.md)
- [`deleteShoppingListCluster`](delete-cart-list-and-reorder.md)
- [`deleteReorderCluster`](delete-cart-list-and-reorder.md)
- [`deleteShoppingOrderTrackingCluster`](delete-tracking-and-user-state.md)
- [`deleteUserManagementCluster`](delete-tracking-and-user-state.md)
- [`deleteClusters`](delete-all-clusters.md)

| Task or contract | Reference |
| --- | --- |
| Setup | [Engage SDK Shopping: Third-party technical integration instructions](setup.md) |
| Shopping entity models | [Engage SDK Shopping: Third-party technical integration instructions](shopping-entity-models.md) |
| Image specifications | [Engage SDK Shopping: Third-party technical integration instructions](image-specifications.md) |
| Service availability | [Engage SDK Shopping: Third-party technical integration instructions](service-availability.md) |
| Legacy service availability | [Engage SDK Shopping: Third-party technical integration instructions](legacy-service-availability.md) |
| Publish recommendations | [Engage SDK Shopping: Third-party technical integration instructions](publish-recommendations.md) |
| Publish featured | [Engage SDK Shopping: Third-party technical integration instructions](publish-featured.md) |
| Publish shopping carts | [Engage SDK Shopping: Third-party technical integration instructions](publish-shopping-carts.md) |
| Publish shopping lists | [Engage SDK Shopping: Third-party technical integration instructions](publish-shopping-lists.md) |
| Publish reorders | [Engage SDK Shopping: Third-party technical integration instructions](publish-reorders.md) |
| Publish order tracking | [Engage SDK Shopping: Third-party technical integration instructions](publish-order-tracking.md) |
| Publish user management | [Engage SDK Shopping: Third-party technical integration instructions](publish-user-management.md) |
| Publish status | [Engage SDK Shopping: Third-party technical integration instructions](publish-status.md) |
| Delete recommendations and featured | [Engage SDK Shopping: Third-party technical integration instructions](delete-recommendations-and-featured.md) |
| Delete cart list and reorder | [Engage SDK Shopping: Third-party technical integration instructions](delete-cart-list-and-reorder.md) |
| Delete tracking and user state | [Engage SDK Shopping: Third-party technical integration instructions](delete-tracking-and-user-state.md) |
| Delete all clusters | [Engage SDK Shopping: Third-party technical integration instructions](delete-all-clusters.md) |
| Error handling | [Engage SDK Shopping: Third-party technical integration instructions](error-handling.md) |
| Broadcast intents | [Engage SDK Shopping: Third-party technical integration instructions](broadcast-intents.md) |
| Integration acceptance | [Engage SDK Shopping: Third-party technical integration instructions](integration-acceptance.md) |

Related workflows:

- [Engage SDK integration](../engage/index.md).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/shopping).
