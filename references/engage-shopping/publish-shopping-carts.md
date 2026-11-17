Client: `AppEngageShoppingClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `publishShoppingCarts`

This API is used to publish a list of `ShoppingCart` objects. This is applicable to developer partner publishing separate carts per merchant. Include merchant name in the title when using this API.

> **Important:** The publish APIs are upsert APIs; it replaces the existing content. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

**Kotlin**

```kotlin
client.publishShoppingCarts(
            PublishShoppingCartClustersRequest.Builder()
                .addShoppingCart(
                    ShoppingCart.Builder()
                        ...
                        .build())
                .build())
```

**Java**

```java
client.publishShoppingCarts(
            new PublishShoppingCartClustersRequest.Builder()
                .addShoppingCart(
                    new ShoppingCart.Builder()
                        ...
                        .build())
                .build())
```

When the service receives the request, the following actions take place within one transaction:

- Existing `ShoppingCart` data from the developer partner is removed.
- Data from the request is parsed and stored in the updated Shopping Cart Cluster.

In case of an error, the entire request is rejected and the existing state is maintained.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/shopping).
