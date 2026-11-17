Use AppEngageFoodClient with the food entity and cluster contracts. Setup and service availability precede publishing; broadcast registration and acceptance complete the integration.

### Step 2: Provide Cluster data

It is recommended to have the content publish job executed in the background (for example, using [WorkManager](<https://developer.android.com/topic/libraries/architecture/workmanager>)) and scheduled on a regular basis or on an event basis (for example, every time the user opens the app or when the user just added something to their cart).

`AppEngageFoodClient` is responsible for publishing food clusters.

There are following APIs to publish clusters in the client:

- [`isServiceAvailable`](service-availability.md)
- [`publishRecommendationClusters`](publish-recommendations.md)
- [`publishFeaturedCluster`](publish-featured.md)
- [`publishFoodShoppingCarts`](publish-shopping-carts.md)
- [`publishFoodShoppingLists`](publish-shopping-lists.md)
- [`publishReorderCluster`](publish-reorders.md)
- [`publishUserAccountManagementRequest`](publish-user-management.md)
- [`updatePublishStatus`](publish-status.md)
- [`deleteRecommendationsClusters`](delete-recommendations-and-featured.md)
- [`deleteFeaturedCluster`](delete-recommendations-and-featured.md)
- [`deleteFoodShoppingCartCluster`](delete-shopping-state.md)
- [`deleteFoodShoppingListCluster`](delete-shopping-state.md)
- [`deleteReorderCluster`](delete-shopping-state.md)
- [`deleteUserManagementCluster`](delete-user-and-all-clusters.md)
- [`deleteClusters`](delete-user-and-all-clusters.md)

| Task or contract | Reference |
| --- | --- |
| Setup | [Engage SDK Food: Third-party technical integration instructions](setup.md) |
| Catalog entity models | [Engage SDK Food: Third-party technical integration instructions](catalog-entity-models.md) |
| Shopping actions and images | [Engage SDK Food: Third-party technical integration instructions](shopping-actions-and-images.md) |
| Service availability | [Engage SDK Food: Third-party technical integration instructions](service-availability.md) |
| Legacy service availability | [Engage SDK Food: Third-party technical integration instructions](legacy-service-availability.md) |
| Publish recommendations | [Engage SDK Food: Third-party technical integration instructions](publish-recommendations.md) |
| Publish featured | [Engage SDK Food: Third-party technical integration instructions](publish-featured.md) |
| Publish shopping carts | [Engage SDK Food: Third-party technical integration instructions](publish-shopping-carts.md) |
| Publish shopping lists | [Engage SDK Food: Third-party technical integration instructions](publish-shopping-lists.md) |
| Publish reorders | [Engage SDK Food: Third-party technical integration instructions](publish-reorders.md) |
| Publish user management | [Engage SDK Food: Third-party technical integration instructions](publish-user-management.md) |
| Publish status | [Engage SDK Food: Third-party technical integration instructions](publish-status.md) |
| Delete recommendations and featured | [Engage SDK Food: Third-party technical integration instructions](delete-recommendations-and-featured.md) |
| Delete shopping state | [Engage SDK Food: Third-party technical integration instructions](delete-shopping-state.md) |
| Delete user and all clusters | [Engage SDK Food: Third-party technical integration instructions](delete-user-and-all-clusters.md) |
| Error handling | [Engage SDK Food: Third-party technical integration instructions](error-handling.md) |
| Broadcast intents | [Engage SDK Food: Third-party technical integration instructions](broadcast-intents.md) |
| Integration acceptance | [Engage SDK Food: Third-party technical integration instructions](integration-acceptance.md) |

Related workflows:

- [Engage SDK integration](../engage/index.md).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/food).
