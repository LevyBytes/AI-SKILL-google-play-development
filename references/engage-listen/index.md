Use audio entity models and client contracts. Setup and service availability precede publishing; both dynamic and static broadcast registration are required.

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
| Setup | [Engage SDK Listen: Third-party technical integration instructions](setup.md) |
| Album and artist models | [Engage SDK Listen: Third-party technical integration instructions](album-and-artist-models.md) |
| Music and playlist models | [Engage SDK Listen: Third-party technical integration instructions](music-and-playlist-models.md) |
| Spoken audio and radio models | [Engage SDK Listen: Third-party technical integration instructions](spoken-audio-and-radio-models.md) |
| Images and entity examples | [Engage SDK Listen: Third-party technical integration instructions](images-and-entity-examples.md) |
| Service availability | [Engage SDK Listen: Third-party technical integration instructions](service-availability.md) |
| Legacy service availability | [Engage SDK Listen: Third-party technical integration instructions](legacy-service-availability.md) |
| Publish recommendations | [Engage SDK Listen: Third-party technical integration instructions](publish-recommendations.md) |
| Publish featured and continuation | [Engage SDK Listen: Third-party technical integration instructions](publish-featured-and-continuation.md) |
| Publish user management | [Engage SDK Listen: Third-party technical integration instructions](publish-user-management.md) |
| Publish status | [Engage SDK Listen: Third-party technical integration instructions](publish-status.md) |
| Delete content clusters | [Engage SDK Listen: Third-party technical integration instructions](delete-content-clusters.md) |
| Delete user and all clusters | [Engage SDK Listen: Third-party technical integration instructions](delete-user-and-all-clusters.md) |
| Error handling | [Engage SDK Listen: Third-party technical integration instructions](error-handling.md) |
| Dynamic broadcast receiver | [Engage SDK Listen: Third-party technical integration instructions](dynamic-broadcast-receiver.md) |
| Static broadcast receiver | [Engage SDK Listen: Third-party technical integration instructions](static-broadcast-receiver.md) |
| Integration acceptance | [Engage SDK Listen: Third-party technical integration instructions](integration-acceptance.md) |

Related workflows:

- [Engage SDK integration](../engage/index.md).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/listen).
