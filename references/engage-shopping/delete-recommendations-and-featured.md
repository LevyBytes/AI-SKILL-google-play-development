Client: `AppEngageShoppingClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `deleteRecommendationsClusters`

This API is used to delete the content of Recommendation Clusters.

> **Important:** Delete APIs should only be called when there is no content to publish. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently. Reach out to [`engage-developers@google.com`](<mailto:engage-developers@google.com>) before using delete APIs.

**Kotlin**

```kotlin
client.deleteRecommendationsClusters()
```

**Java**

```java
client.deleteRecommendationsClusters();
```

When the service receives the request, it removes the existing data from the Recommendation Clusters. In case of an error, the entire request is rejected and the existing state is maintained.

> **Note:** This api is available from version 1.1.0 onwards.

#### `deleteFeaturedCluster`

This API is used to delete the content of Featured Cluster.

> **Important:** Delete APIs should only be called when there is no content to publish. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently. Reach out to [`engage-developers@google.com`](<mailto:engage-developers@google.com>) before using delete APIs.

**Kotlin**

```kotlin
client.deleteFeaturedCluster()
```

**Java**

```java
client.deleteFeaturedCluster();
```

When the service receives the request, it removes the existing data from the Featured Cluster. In case of an error, the entire request is rejected and the existing state is maintained.

> **Note:** This api is available from version 1.1.0 onwards.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/shopping).
