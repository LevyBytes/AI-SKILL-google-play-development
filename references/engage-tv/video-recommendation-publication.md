This guide contains instructions for developers to integrate their recommended video content, using the [Engage SDK](<https://developer.android.com/guide/playcore/engage>), to populate recommendations experiences across Google surfaces, such as TV, mobile, and tablet.

Recommendation leverages the **Recommendation cluster** to show movies and TV shows, from multiple apps in one UI grouping. Each developer partner can broadcast a maximum **of 25 entities** in each recommendations cluster and there can be a maximum **of 7** recommendation clusters per request.

## Pre-work

> **Important:** [Express interest in developing with Engage](<http://g.co/tv/vda>).

Complete the [Pre-work](<https://developer.android.com/guide/playcore/engage/tv/getting-started#pre-work>) instructions in the Getting Started guide.

1. Execute publishing on a foreground service.
2. Publish recommendations data at most once daily, triggered by either of

   - User's first login of the day. (*or*)
   - When the user starts interacting with the application.

## Integration

`AppEngagePublishClient` publishes the recommendation cluster. Use the `publishRecommendationClusters` method to publish a recommendations object.

Make sure to initialize the client and check for service availability as described in the [Getting Started guide](<https://developer.android.com/guide/playcore/engage/tv/getting-started#common-integration>).

```kotlin
client.publishRecommendationClusters(recommendationRequest)
```

### Upserting recommendation clusters

Clusters are logical grouping of the entities. The following code examples explains how to build the clusters based on your preference and how to create a publishing request and upsert all clusters.

The [`RecommendationClusterType`](<https://developer.android.com/reference/com/google/android/engage/common/datamodel/RecommendationClusterType>) determines how the cluster will be displayed.

```kotlin
// cluster for popular movies
val recommendationCluster1 = RecommendationCluster
  .Builder()
  .addEntity(movie1)
  .addEntity(movie2)
  .addEntity(movie3)
  .addEntity(movie4)
  .addEntity(tvShow)
  // This cluster is meant to be used as an individual provider row
  .setRecommendationClusterType(TYPE_PROVIDER_ROW)
  .setTitle("Popular Movies")
  .build()

// cluster for live TV programs
val recommendationCluster2 = RecommendationCluster
  .Builder()
  .addEntity(liveTvProgramEntity1)
  .addEntity(liveTvProgramEntity2)
  .addEntity(liveTvProgramEntity3)
  .addEntity(liveTvProgramEntity4)
  .addEntity(liveTvProgramEntity5)
 // This cluster is meant to be used as an individual provider row
  .setRecommendationClusterType(TYPE_PROVIDER_ROW)
  .setTitle("Popular Live TV Programs")
  .build()

// creating a publishing request
val recommendationRequest = PublishRecommendationClustersRequest
  .Builder()
  .setSyncAcrossDevices(true)
  .setAccountProfile(accountProfile)
  .addRecommendationCluster(recommendationCluster1)
  .addRecommendationCluster(recommendationCluster2)
  .build()
```

When the service receives the request, the following actions occur within one transaction:

- Existing `RecommendationsCluster` data from the developer partner is removed.
- Data from the request is parsed and stored in the updated `RecommendationsCluster`. In case of an error, the entire request is rejected and the existing state is maintained.

> **Note:** Publish APIs are upsert operations, replacing existing content; update entities by republishing the entire cluster. Only publish recommendations for adult accounts. Avoid using delete APIs followed by publish, as the latter inherently replaces content.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/recommendations).
