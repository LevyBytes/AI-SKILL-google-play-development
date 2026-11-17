Use social-post and portrait-media models with their publishing contracts. Setup and service availability precede publishing; broadcast registration and acceptance complete the integration.

### Step 2: Provide Cluster data

It is recommended to have the content publish job executed in the background (for example, using [WorkManager](<https://developer.android.com/topic/libraries/architecture/workmanager>)) and scheduled on a regular basis or on an event basis (for example, every time the user opens the app or when the user just followed a new account)

`AppEngageSocialClient` is responsible for publishing social clusters.

There are following APIs to publish clusters in the client:

- [`isServiceAvailable`](service-availability.md)
- [`publishRecommendationClusters`](publish-recommendations.md)
- [`publishUserAccountManagementRequest`](publish-user-management.md)
- [`updatePublishStatus`](publish-status.md)
- [`deleteRecommendationsClusters`](delete-clusters.md)
- [`deleteUserManagementCluster`](delete-clusters.md)
- [`deleteClusters`](delete-clusters.md)

| Task or contract | Reference |
| --- | --- |
| Setup | [Engage SDK Social: Third-party technical integration instructions](setup.md) |
| Social entity models and images | [Engage SDK Social: Third-party technical integration instructions](social-entity-models-and-images.md) |
| Service availability | [Engage SDK Social: Third-party technical integration instructions](service-availability.md) |
| Legacy service availability | [Engage SDK Social: Third-party technical integration instructions](legacy-service-availability.md) |
| Publish recommendations | [Engage SDK Social: Third-party technical integration instructions](publish-recommendations.md) |
| Publish user management | [Engage SDK Social: Third-party technical integration instructions](publish-user-management.md) |
| Publish status | [Engage SDK Social: Third-party technical integration instructions](publish-status.md) |
| Delete clusters | [Engage SDK Social: Third-party technical integration instructions](delete-clusters.md) |
| Error handling | [Engage SDK Social: Third-party technical integration instructions](error-handling.md) |
| Broadcast intents | [Engage SDK Social: Third-party technical integration instructions](broadcast-intents.md) |
| Integration acceptance | [Engage SDK Social: Third-party technical integration instructions](integration-acceptance.md) |

Related workflows:

- [Engage SDK integration](../engage/index.md).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/social).
