Client: `AppEngageFoodClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `deleteFoodShoppingCartCluster`

This API is used to delete the content of Food Shopping Cart Cluster.

> **Important:** Delete APIs should only be called when there is no content to publish. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently. Reach out to [`engage-developers@google.com`](<mailto:engage-developers@google.com>) before using delete APIs.

**Kotlin**

```kotlin
client.deleteFoodShoppingCartCluster()
```

**Java**

```java
client.deleteFoodShoppingCartCluster();
```

When the service receives the request, it removes the existing data from the Food Shopping Cart Cluster. In case of an error, the entire request is rejected and the existing state is maintained.

> **Note:** This api is availaile from version 1.1.0 onwards.

#### `deleteFoodShoppingListCluster`

This API is used to delete the content of Food Shopping List Cluster.

> **Important:** Delete APIs should only be called when there is no content to publish. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently. Reach out to [`engage-developers@google.com`](<mailto:engage-developers@google.com>) before using delete APIs.

**Kotlin**

```kotlin
client.deleteFoodShoppingListCluster()
```

**Java**

```java
client.deleteFoodShoppingListCluster();
```

When the service receives the request, it removes the existing data from the Food Shopping List Cluster. In case of an error, the entire request is rejected and the existing state is maintained.

> **Note:** This api is available from version 1.1.0 onwards.

#### `deleteReorderCluster`

This API is used to delete the content of FoodReorderCluster.

> **Important:** Delete APIs should only be called when there is no content to publish. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently. Reach out to [`engage-developers@google.com`](<mailto:engage-developers@google.com>) before using delete APIs.

**Kotlin**

```kotlin
client.deleteReorderCluster()
```

**Java**

```java
client.deleteReorderCluster();
```

When the service receives the request, it removes the existing data from the Reorder Cluster. In case of an error, the entire request is rejected and the existing state is maintained.

> **Note:** This api is available from version 1.1.0 onwards.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/food).
