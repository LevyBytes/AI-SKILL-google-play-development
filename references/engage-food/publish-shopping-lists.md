Client: `AppEngageFoodClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `publishFoodShoppingLists`

This API is used to publish a list of `FoodShoppingList` objects.

> **Important:** The publish APIs are upsert APIs; it replaces the existing content. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

**Kotlin**

```kotlin
client.publishFoodShoppingLists(
            PublishFoodShoppingListsRequest.Builder()
                .addFoodShoppingList(
                    FoodShoppingList.Builder()
                        ...
                        .build())
                .build())
```

**Java**

```java
client.publishFoodShoppingLists(
            new PublishFoodShoppingListsRequest.Builder()
                .addFoodShoppingList(
                    new FoodShoppingList.Builder()
                        ...
                        .build())
                .build());
```

When the service receives the request, the following actions take place within one transaction:

- Existing `FoodShoppingList` data from the developer partner is removed.
- Data from the request is parsed and stored in the updated Shopping List Cluster.

In case of an error, the entire request is rejected and the existing state is maintained.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/food).
