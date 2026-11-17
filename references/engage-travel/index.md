Use venue, place and reservation models with their client contracts. Setup and service availability precede publishing; broadcast registration and acceptance complete the integration.

### Step 2: Provide Cluster data

It is recommended to have the content publish job executed in the background (for example, using [WorkManager](<https://developer.android.com/topic/libraries/architecture/workmanager>)) and scheduled on a regular basis or on an event basis (for example, every time the user opens the app or when the user just added something to their cart).

`AppEngageTravelClient` is responsible for publishing clusters.

There are following APIs to publish clusters in the client:

- [`isServiceAvailable`](service-availability.md)
- [`publishRecommendationClusters`](publish-recommendations.md)
- [`publishFeaturedCluster`](publish-featured.md)
- [`publishReservationCluster`](publish-reservations.md)
- [`publishContinueSearchCluster`](publish-continue-search.md)
- [`publishUserAccountManagementRequest`](publish-user-management.md)
- [`updatePublishStatus`](publish-status.md)
- [`deleteRecommendationsClusters`](delete-content-clusters.md)
- [`deleteFeaturedCluster`](delete-content-clusters.md)
- [`deleteReservationCluster`](delete-content-clusters.md)
- [`deleteContinueSearchCluster`](delete-user-and-search-clusters.md)
- [`deleteUserManagementCluster`](delete-user-and-search-clusters.md)
- [`deleteClusters`](delete-all-clusters.md)

| Task or contract | Reference |
| --- | --- |
| Setup | [Engage SDK Travel: Third-party technical integration instructions](setup.md) |
| Cluster types | [Engage SDK Travel: Third-party technical integration instructions](cluster-types.md) |
| Featured and article models | [Engage SDK Travel: Third-party technical integration instructions](featured-and-article-models.md) |
| Venue models | [Engage SDK Travel: Third-party technical integration instructions](venue-models.md) |
| Place models | [Engage SDK Travel: Third-party technical integration instructions](place-models.md) |
| Venue reservation models | [Engage SDK Travel: Third-party technical integration instructions](venue-reservation-models.md) |
| Transport reservation models | [Engage SDK Travel: Third-party technical integration instructions](transport-reservation-models.md) |
| Images timezones and categories | [Engage SDK Travel: Third-party technical integration instructions](images-timezones-and-categories.md) |
| Service availability | [Engage SDK Travel: Third-party technical integration instructions](service-availability.md) |
| Legacy service availability | [Engage SDK Travel: Third-party technical integration instructions](legacy-service-availability.md) |
| Publish recommendations | [Engage SDK Travel: Third-party technical integration instructions](publish-recommendations.md) |
| Publish featured | [Engage SDK Travel: Third-party technical integration instructions](publish-featured.md) |
| Publish reservations | [Engage SDK Travel: Third-party technical integration instructions](publish-reservations.md) |
| Publish continue search | [Engage SDK Travel: Third-party technical integration instructions](publish-continue-search.md) |
| Publish user management | [Engage SDK Travel: Third-party technical integration instructions](publish-user-management.md) |
| Publish status | [Engage SDK Travel: Third-party technical integration instructions](publish-status.md) |
| Delete content clusters | [Engage SDK Travel: Third-party technical integration instructions](delete-content-clusters.md) |
| Delete user and search clusters | [Engage SDK Travel: Third-party technical integration instructions](delete-user-and-search-clusters.md) |
| Delete all clusters | [Engage SDK Travel: Third-party technical integration instructions](delete-all-clusters.md) |
| Error handling | [Engage SDK Travel: Third-party technical integration instructions](error-handling.md) |
| Broadcast intents | [Engage SDK Travel: Third-party technical integration instructions](broadcast-intents.md) |
| Integration acceptance | [Engage SDK Travel: Third-party technical integration instructions](integration-acceptance.md) |

Related workflows:

- [Engage SDK integration](../engage/index.md).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/travel).
