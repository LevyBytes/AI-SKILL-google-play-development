Use the [Engage SDK overview](../engage/overview.md) for supported surfaces, participation and integration estimates.

This guide contains instructions for developer partners to deliver travel and events content to Engage content surfaces.

## Category support and surfaces

Engage SDK surface eligibility is based on your app's content category. Use the following table to determine your eligibility for specific surfaces:

| Status | Content category or use case | Supported surfaces |
| --- | --- | --- |
| **Supported**<br> (Eligible on all surfaces) | All Travel & local (except unsupported subcategories listed in this table) Events (all subcategories) Pet activity, monitoring, sitting, walking | Collections Play Store Apps tab Play Store You tab Play Store store listing page |
| **Not supported** | Flight trackers |  |

## Integration detail

This section details the steps, data models, and terminology required to integrate with the Engage SDK for travel and events content.

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
| Recommendation Cluster(s) | At most 7 | At least 1 | At most 50 (`ArticleEntity`, `EventEntity`, `LodgingEntity`, `StoreEntity`, or `PointOfInterestEntity`) |
| Reservation Cluster | At most 1 | At least 1 | At most 20 (`RestaurantReservationEntity`, `EventReservationEntity`, `LodgingReservationEntity`, `TransportationReservationEntity`, or `VehicleRentalReservationEntity`) |
| Featured Cluster | At most 1 | At least 1 | At most 20 (`GenericFeaturedEntity`) |
| Continue Search Cluster | At most 1 | At least 1 | At most 3 (`PointOfInterestEntity`) |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/travel).
