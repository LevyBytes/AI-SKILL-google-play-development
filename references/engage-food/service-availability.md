Client: `AppEngageFoodClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `isServiceAvailable`

This API is used to check if the service is available for integration and whether the content can be presented on the device.

##### For Engage SDK v1.6.0 and higher (Recommended)

You can check the service availability for every cluster type that you intend to publish. The `isServiceAvailable` API accepts a request object, `ServiceAvailabilityRequest`, which contains the cluster types for which service availability needs to be checked. You can find the `ClusterType` enum values required for `ServiceAvailabilityRequest` from the following table.

| Cluster Type | Cluster Type Constant | Integer Value |
| --- | --- | --- |
| Unknown | `TYPE_UNKNOWN` | 0 |
| Recommendation Cluster | `TYPE_RECOMMENDATION` | 1 |
| Featured Cluster | `TYPE_FEATURED` | 2 |
| Continuation Cluster | `TYPE_CONTINUATION` | 3 |
| Food Reorder Cluster | `TYPE_FOOD_REORDER` | 5 |
| Food Shopping Cart Cluster | `TYPE_FOOD_SHOPPING_CART` | 6 |
| Food Shopping List Cluster | `TYPE_FOOD_SHOPPING_LIST` | 7 |
| User Management Cluster | `TYPE_ENGAGEMENT` | 8 |
| Subscription Cluster | `TYPE_SUBSCRIPTION` | 12 |

**Kotlin**

```kotlin
val request = ServiceAvailabilityRequest.Builder()
    .addIntendedClusterType(ClusterType.TYPE_CONTINUATION)
    .addIntendedClusterType(ClusterType.TYPE_RECOMMENDATION)
    .build()

client.isServiceAvailable(request).addOnCompleteListener { task ->
    if (task.isSuccessful) {
        val availabilityMap = task.result
        if (availabilityMap[ClusterType.TYPE_CONTINUATION] == true) {
            // Proceed with publishing continuation content
        }
        if (availabilityMap[ClusterType.TYPE_RECOMMENDATION] == true) {
            // Proceed with publishing recommendation content
        }
    } else {
        // The IPC call itself fails, proceed with error handling logic here,
        // such as retry.
    }
}
```

**Java**

```java
ServiceAvailabilityRequest request =
    new ServiceAvailabilityRequest.Builder()
        .addIntendedClusterType(ClusterType.TYPE_CONTINUATION)
        .addIntendedClusterType(ClusterType.TYPE_RECOMMENDATION)
        .build();

client.isServiceAvailable(request).addOnCompleteListener(task -> {
    if (task.isSuccessful()) {
        Map<Integer, Boolean> availabilityMap = task.getResult();
        if (Boolean.TRUE.equals(availabilityMap.get(ClusterType.TYPE_CONTINUATION))) {
            // Proceed with publishing continuation content
        }
        if (Boolean.TRUE.equals(availabilityMap.get(ClusterType.TYPE_RECOMMENDATION))) {
            // Proceed with publishing recommendation content
        }
    } else {
        // The IPC call itself fails, proceed with error handling logic here,
        // such as retry.
    }
});
```

###### Conditional Service Availability Feature

Some integrated apps request a special configuration that enables and disables the Engage service intermittently to reduce serving costs. However, this intermittent content ingestion strategy negatively affects the user experience: stale content won't be presented, and some surfaces won't be served.

Starting with v1.6.0, the Engage SDK allows checking availability for specific cluster types. If your app uses intermittent ingestion:

- **Continuation clusters** (such as Food Shopping Cart, Food Shopping List, and Reorder) remain enabled by default across all supported devices.
- **Other cluster types** (such as Recommendations) are enabled and disabled intermittently.

If this default configuration isn't suitable for your needs, contact engage-developers@google.com.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/food).
