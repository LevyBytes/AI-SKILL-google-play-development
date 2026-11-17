Client: `AppEngagePublishClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `publishRecommendationClusters`

This API is used to publish a list of `RecommendationCluster` objects.

> **Important:** The publish APIs are upsert APIs; it replaces the existing content. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

**Kotlin**

```kotlin
client.publishRecommendationClusters(
            PublishRecommendationClustersRequest.Builder()
                .addRecommendationCluster(
                    RecommendationCluster.Builder()
                        .addEntity(entity1)
                        .addEntity(entity2)
                        .setTitle("Trending music")
                        .build())
                .build())
```

**Java**

```java
client.publishRecommendationClusters(
            new PublishRecommendationClustersRequest.Builder()
                .addRecommendationCluster(
                    new RecommendationCluster.Builder()
                        .addEntity(entity1)
                        .addEntity(entity2)
                        .setTitle("Trending music")
                        .build())
                .build());
```

When the service receives the request, the following actions take place within one transaction:

- Existing `RecommendationCluster` data from the developer partner is removed.
- Data from the request is parsed and stored in the updated Recommendation Cluster.

In case of an error, the entire request is rejected and the existing state is maintained.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/listen).
