### Pre-work

Minimum API level: 19

Add the `com.google.android.engage:engage-core` library to your app:

```groovy
dependencies {
    // Make sure you also include that repository in your project's build.gradle file.
    implementation 'com.google.android.engage:engage-core:1.6.0'
}
```

### Summary

The design is based on an implementation of a [bound service](<https://developer.android.com/guide/components/bound-services>).

The data a client can publish is subject to the following limits for different cluster types:

| Cluster type | Cluster limits | Minimum entity limits in a cluster | Maximum entity limits in a cluster |
| --- | --- | --- | --- |
| Recommendation Cluster(s) | At most 7 | At least 1 | At most 50 (`ArticleEntity`, `EventEntity`, `LodgingEntity`, `StoreEntity`, `PointOfInterestEntity`, or `PersonEntity`) |
| Continuation Cluster | At most 1 | At least 1 | At most 20 (`ArticleEntity`, `EventReservationEntity`, `LodgingReservationEntity`, `TransportationReservationEntity`, or `VehicleRentalReservationEntity`) |
| Featured Cluster | At most 1 | At least 1 | At most 20 (`GenericFeaturedEntity`) |

### Step 1: Provide entity data

The SDK has defined different entities to represent each item type. We support the following entities for the others category:

1. `GenericFeaturedEntity`
2. `ArticleEntity`
3. `EventEntity`
4. `LodgingEntity`
5. `StoreEntity`
6. `PointOfInterestEntity`
7. `PersonEntity`
8. `RestaurantReservationEntity`
9. `EventReservationEntity`
10. `LodgingReservationEntity`
11. `TransportationReservationEntity`
12. `VehicleRentalReservationEntity`

The following charts outline available attributes and requirements for each type.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/otherverticals).
