Client: `AppEngagePublishClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `deleteUserManagementCluster`

This API is used to delete the content of UserAccountManagement Cluster.

> **Important:** Delete APIs should only be called when there is no content to publish. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently. Reach out to [`engage-developers@google.com`](<mailto:engage-developers@google.com>) before using delete APIs.

**Kotlin**

```kotlin
client.deleteUserManagementCluster()
```

**Java**

```java
client.deleteUserManagementCluster();
```

When the service receives the request, it removes the existing data from the UserAccountManagement Cluster. In case of an error, the entire request is rejected and the existing state is maintained.

> **Note:** This api is available from version 1.1.0 onwards.

#### `deleteClusters`

This API is used to delete the content of a given cluster type.

> **Important:** Delete APIs should only be called when there is no content to publish. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently. Reach out to [`engage-developers@google.com`](<mailto:engage-developers@google.com>) before using delete APIs.

**Kotlin**

```kotlin
client.deleteClusters(
    DeleteClustersRequest.Builder()
      .addClusterType(ClusterType.TYPE_FEATURED)
      .addClusterType(ClusterType.TYPE_RECOMMENDATION)
      ...
      .build())
```

**Java**

```java
client.deleteClusters(
            new DeleteClustersRequest.Builder()
                .addClusterType(ClusterType.TYPE_FEATURED)
                .addClusterType(ClusterType.TYPE_RECOMMENDATION)
                ...
                .build());
```

When the service receives the request, it removes the existing data from all clusters matching the specified cluster types. Clients can choose to pass one or many cluster types. In case of an error, the entire request is rejected and the existing state is maintained.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/listen).
