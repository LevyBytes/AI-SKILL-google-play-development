Use the actual entity model for content that falls outside a dedicated vertical. Dependencies, service availability, publishing and both broadcast registration modes remain required.

### Step 2: Provide Cluster data

It is recommended to have the content publish job executed in the background (for example, using [WorkManager](<https://developer.android.com/topic/libraries/architecture/workmanager>)) and scheduled on a regular basis or on an event basis (for example, every time the user opens the app or when the user just added something to their cart).

`AppEngagePublishClient` is responsible for publishing clusters.

There are following APIs to publish clusters in the client:

- [`isServiceAvailable`](service-availability.md)
- [`publishRecommendationClusters`](publish-recommendations.md)
- [`publishFeaturedCluster`](publish-featured-and-continuation.md)
- [`publishContinuationCluster`](publish-featured-and-continuation.md)
- [`publishUserAccountManagementRequest`](publish-user-management.md)
- [`updatePublishStatus`](publish-status.md)
- [`deleteRecommendationsClusters`](delete-content-clusters.md)
- [`deleteFeaturedCluster`](delete-content-clusters.md)
- [`deleteContinuationCluster`](delete-content-clusters.md)
- [`deleteUserManagementCluster`](delete-user-and-all-clusters.md)
- [`deleteClusters`](delete-user-and-all-clusters.md)

| Task or contract | Reference |
| --- | --- |
| Cluster types | [Engage SDK Other Verticals: Third-party technical integration instructions](cluster-types.md) |
| Dependencies and entity types | [Engage SDK Other Verticals: Third-party technical integration instructions](dependencies-and-entity-types.md) |
| Featured and article models | [Engage SDK Other Verticals: Third-party technical integration instructions](featured-and-article-models.md) |
| Event and lodging models | [Engage SDK Other Verticals: Third-party technical integration instructions](event-and-lodging-models.md) |
| Store and point of interest models | [Engage SDK Other Verticals: Third-party technical integration instructions](store-and-point-of-interest-models.md) |
| Person model | [Engage SDK Other Verticals: Third-party technical integration instructions](person-model.md) |
| Venue reservation models | [Engage SDK Other Verticals: Third-party technical integration instructions](venue-reservation-models.md) |
| Transport reservation models | [Engage SDK Other Verticals: Third-party technical integration instructions](transport-reservation-models.md) |
| Images and content categories | [Engage SDK Other Verticals: Third-party technical integration instructions](images-and-content-categories.md) |
| Service availability | [Engage SDK Other Verticals: Third-party technical integration instructions](service-availability.md) |
| Legacy service availability | [Engage SDK Other Verticals: Third-party technical integration instructions](legacy-service-availability.md) |
| Publish recommendations | [Engage SDK Other Verticals: Third-party technical integration instructions](publish-recommendations.md) |
| Publish featured and continuation | [Engage SDK Other Verticals: Third-party technical integration instructions](publish-featured-and-continuation.md) |
| Publish user management | [Engage SDK Other Verticals: Third-party technical integration instructions](publish-user-management.md) |
| Publish status | [Engage SDK Other Verticals: Third-party technical integration instructions](publish-status.md) |
| Delete content clusters | [Engage SDK Other Verticals: Third-party technical integration instructions](delete-content-clusters.md) |
| Delete user and all clusters | [Engage SDK Other Verticals: Third-party technical integration instructions](delete-user-and-all-clusters.md) |
| Error handling | [Engage SDK Other Verticals: Third-party technical integration instructions](error-handling.md) |
| Dynamic broadcast receiver | [Engage SDK Other Verticals: Third-party technical integration instructions](dynamic-broadcast-receiver.md) |
| Static broadcast receiver | [Engage SDK Other Verticals: Third-party technical integration instructions](static-broadcast-receiver.md) |
| Integration acceptance | [Engage SDK Other Verticals: Third-party technical integration instructions](integration-acceptance.md) |

Related workflows:

- [Engage SDK integration](../engage/index.md).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/otherverticals).
