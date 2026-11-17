Client: `AppEngageTravelClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `publishReservationCluster`

This API is used to publish a `ReservationCluster` object.

> **Important:** The publish APIs are upsert APIs; it replaces the existing content. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

**Kotlin**

```kotlin
client.publishReservationCluster(
    PublishReservationClusterRequest.Builder()
      .setReservationCluster(
        ReservationCluster.Builder()
          .addLodgingReservationEntity(lodgingReservationEntity)
          .addVehicleRentalReservationEntity(vehicleRentalReservationEntity)
          .addTransportationReservationEntity(transportationReservationEntity)
          .addEventReservationEntity(eventReservationEntity)
          .addRestaurantReservationEntity(restaurantReservationEntity)
          .build())
      .build())
```

**Java**

```java
client.publishReservationCluster(
            new PublishReservationClusterRequest.Builder()
                .setReservationCluster(
                    new ReservationCluster.Builder()
                        .addLodgingReservationEntity(lodgingReservationEntity)
                        .addVehicleRentalReservationEntity(vehicleRentalReservationEntity)
                        .addTransportationReservationEntity(transportationReservationEntity)
                        .addEventReservationEntity(eventReservationEntity)
                        .addRestaurantReservationEntity(restaurantReservationEntity)
                        .build())
                .build());
```

When the service receives the request, the following actions take place within one transaction:

- Existing `ReservationCluster` data from the developer partner is removed.
- Data from the request is parsed and stored in the updated Reservation Cluster.

In case of an error, the entire request is rejected and the existing state is maintained.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/travel).
