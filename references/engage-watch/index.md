Use video entity models and client contracts, with the Media Home migration when applicable. Setup and service availability precede publishing; both dynamic and static broadcast registration are required.

### Step 2: Provide Cluster data

It's recommended to have the content publish job executed in the background (for example, using [WorkManager](<https://developer.android.com/topic/libraries/architecture/workmanager>)) and scheduled on a regular basis or on an event basis (for example, every time the user opens the app or when the user just added something to their cart).

`AppEngagePublishClient` is responsible for publishing clusters. Following APIs are available in the client:

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
| Setup | [Engage SDK Watch: Third-party technical integration instructions](setup.md) |
| Media home migration | [Engage SDK Watch: Third-party technical integration instructions](media-home-migration.md) |
| Movie and show models | [Engage SDK Watch: Third-party technical integration instructions](movie-and-show-models.md) |
| Season and episode models | [Engage SDK Watch: Third-party technical integration instructions](season-and-episode-models.md) |
| Streaming and clip models | [Engage SDK Watch: Third-party technical integration instructions](streaming-and-clip-models.md) |
| Images and entity examples | [Engage SDK Watch: Third-party technical integration instructions](images-and-entity-examples.md) |
| Service availability | [Engage SDK Watch: Third-party technical integration instructions](service-availability.md) |
| Legacy service availability | [Engage SDK Watch: Third-party technical integration instructions](legacy-service-availability.md) |
| Publish recommendations | [Engage SDK Watch: Third-party technical integration instructions](publish-recommendations.md) |
| Publish featured and continuation | [Engage SDK Watch: Third-party technical integration instructions](publish-featured-and-continuation.md) |
| Publish user management | [Engage SDK Watch: Third-party technical integration instructions](publish-user-management.md) |
| Publish status | [Engage SDK Watch: Third-party technical integration instructions](publish-status.md) |
| Delete content clusters | [Engage SDK Watch: Third-party technical integration instructions](delete-content-clusters.md) |
| Delete user and all clusters | [Engage SDK Watch: Third-party technical integration instructions](delete-user-and-all-clusters.md) |
| Error handling | [Engage SDK Watch: Third-party technical integration instructions](error-handling.md) |
| Dynamic broadcast receiver | [Engage SDK Watch: Third-party technical integration instructions](dynamic-broadcast-receiver.md) |
| Static broadcast receiver | [Engage SDK Watch: Third-party technical integration instructions](static-broadcast-receiver.md) |
| Integration acceptance | [Engage SDK Watch: Third-party technical integration instructions](integration-acceptance.md) |

Related workflows:

- [Engage SDK integration](../engage/index.md).
- [Engage integrations for Google TV](../engage-tv/index.md).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/watch).
