Client: `AppEngageSocialClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `publishRecommendationClusters`

This API is used to publish a list `RecommendationCluster` objects.

A `RecommendationCluster` object can have the following attributes:

| Attribute | Requirement | Description |
| --- | --- | --- |
| List of SocialPostEntity, or PortraitMediaEntity | **Required** | A list of entities that make up the recommendations for this Recommendation Cluster. Entities in a single cluster must be of the same type. |
| Title | **Required** | The title for the Recommendation Cluster (for example, *Latest from your friends*). **Recommended text size: under 25 chars** (Text that is too long may show ellipses) |
| Subtitle | Optional | The subtitle for the Recommendation Cluster. |
| Action Uri | Optional | The deep link to the page in the partner app where users can see the complete list of recommendations. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |

> **Important:** The publish APIs are upsert APIs; it replaces the existing content. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

> **Important:** For social apps, it's critical to update recommendations after each app usage. Social app users are more interested in the most recent recommendations and ideally would like to see a post at most once.

**Kotlin**

```kotlin
client.publishRecommendationClusters(
            PublishRecommendationClustersRequest.Builder()
                .addRecommendationCluster(
                    RecommendationCluster.Builder()
                        .addEntity(entity1)
                        .addEntity(entity2)
                        .setTitle("Latest from your friends")
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
                        .setTitle("Latest from your friends")
                        .build())
                .build());
```

When the service receives the request, the following actions take place within one transaction:

- All existing Recommendation Cluster data is removed.
- Data from the request is parsed and stored in new Recommendation Clusters.

In case of an error, the entire request is rejected and the existing state is maintained.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/social).
