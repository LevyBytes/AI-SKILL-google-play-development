Client: `AppEngageShoppingClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `publishShoppingLists`

This API is used to publish a list of `ShoppingList` objects.

> **Important:** The publish APIs are upsert APIs; it replaces the existing content. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

**Kotlin**

```kotlin
client.publishShoppingLists(
            PublishShoppingListsRequest.Builder()
                .addShoppingList(
                    ShoppingList.Builder()
                        ...
                        .build())
                .build())
```

**Java**

```java
client.publishShoppingLists(
            new PublishShoppingListsRequest.Builder()
                .addShoppingList(
                    new ShoppingList.Builder()
                        ...
                        .build())
                .build());
```

When the service receives the request, the following actions take place within one transaction:

- Existing `ShoppingList` data from the developer partner is removed.
- Data from the request is parsed and stored in the updated Shopping List Cluster.

In case of an error, the entire request is rejected and the existing state is maintained.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/shopping).
