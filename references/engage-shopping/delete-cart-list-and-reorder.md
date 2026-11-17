Client: `AppEngageShoppingClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `deleteShoppingCartCluster`

This API is used to delete the content of Shopping Cart Cluster.

> **Important:** Delete APIs should only be called when there is no content to publish. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently. Reach out to [`engage-developers@google.com`](<mailto:engage-developers@google.com>) before using delete APIs.

**Kotlin**

```kotlin
client.deleteShoppingCartCluster()
```

**Java**

```java
client.deleteShoppingCartCluster();
```

When the service receives the request, it removes the existing data from the Shopping Cart Cluster. In case of an error, the entire request is rejected and the existing state is maintained.

> **Note:** This api is available from version 1.1.0 onwards.

#### `deleteShoppingListCluster`

This API is used to delete the content of Shopping List Cluster.

> **Important:** Delete APIs should only be called when there is no content to publish. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently. Reach out to [`engage-developers@google.com`](<mailto:engage-developers@google.com>) before using delete APIs.

**Kotlin**

```kotlin
client.deleteShoppingListCluster()
```

**Java**

```java
client.deleteShoppingListCluster();
```

When the service receives the request, it removes the existing data from the Shopping List Cluster. In case of an error, the entire request is rejected and the existing state is maintained.

> **Note:** This api is available from version 1.1.0 onwards.

#### `deleteReorderCluster`

This API is used to delete the content of Shopping Reorder Cluster.

> **Important:** Delete APIs should only be called when there is no content to publish. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently. Reach out to [`engage-developers@google.com`](<mailto:engage-developers@google.com>) before using delete APIs.

**Kotlin**

```kotlin
client.deleteReorderCluster()
```

**Java**

```java
client.deleteReorderCluster();
```

When the service receives the request, it removes the existing data from the Shopping Reorder Cluster. In case of an error, the entire request is rejected and the existing state is maintained.

> **Note:** This api is available from version 1.1.0 onwards.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/shopping).
