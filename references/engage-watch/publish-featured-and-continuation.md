Client: `AppEngagePublishClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `publishFeaturedCluster`

This API is used to publish a list of `FeaturedCluster` objects.

> **Important:** The publish APIs are upsert APIs; it replaces the existing content. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

**Kotlin**

```kotlin
client.publishFeaturedCluster(
    PublishFeaturedClusterRequest.Builder()
      .setFeaturedCluster(
        FeaturedCluster.Builder()
          .addEntity(entity1)
          .addEntity(entity2)
          .build())
      .build())
```

**Java**

```java
client.publishFeaturedCluster(
            new PublishFeaturedClusterRequest.Builder()
                .setFeaturedCluster(
                    new FeaturedCluster.Builder()
                        .addEntity(entity1)
                        .addEntity(entity2)
                        .build())
                .build());
```

When the service receives the request, the following actions take place within one transaction:

- Existing `FeaturedCluster` data from the developer partner is removed.
- Data from the request is parsed and stored in the updated Featured Cluster.

In case of an error, the entire request is rejected and the existing state is maintained.

#### `publishContinuationCluster`

This API is used to publish a `ContinuationCluster` object.

> **Important:** The publish APIs are upsert APIs; it replaces the existing content. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

**Kotlin**

```kotlin
client.publishContinuationCluster(
    PublishContinuationClusterRequest.Builder()
      .setContinuationCluster(
        ContinuationCluster.Builder()
          .addEntity(entity1)
          .addEntity(entity2)
          .build())
      .build())
```

**Java**

```java
client.publishContinuationCluster(
            new PublishContinuationClusterRequest.Builder()
                .setContinuationCluster(
                    new ContinuationCluster.Builder()
                        .addEntity(entity1)
                        .addEntity(entity2)
                        .build())
                .build());
```

When the service receives the request, the following actions take place within one transaction:

- Existing `ContinuationCluster` data from the developer partner is removed.
- Data from the request is parsed and stored in the updated Continuation Cluster.

In case of an error, the entire request is rejected and the existing state is maintained.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/watch).
