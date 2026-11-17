### Terminology

This integration includes the following cluster types: **Recommendation**, **Featured**, **Reservation** and **Continue Search**.

- **Recommendation** clusters show personalized travel & event suggestions from an individual developer partner. These recommendations can be personalized to the user or generalized (for example, trending items). Use these to feature articles, events, lodging, or places of interest recommendations.

  - A Recommendation cluster can be made of `ArticleEntity`, `EventEntity`, `LodgingEntity`, `PointOfInterestEntity`, or `StoreEntity` listings, but not a mix of different entity types.

  Your recommendations take the following structure:

  - **Recommendation Cluster:** A UI view that contains a group of recommendations from the same developer partner.
  - **Entity:** An object representing a single item in a cluster. This integration offers some entities that would be surfaced using the Recommendation Cluster:

    - **ArticleEntity**: ArticleEntity represents a recommendation for text-based content related to travel & events. It can be used for articles, blogposts, marketing content, news snippets, etc.

      ![Image](<https://developer.android.com/static/images/guide/playcore/engage/article-entity-travel.png>)

      **Figure 1:** UI showing a single ArticleEntity within Recommendations cluster.
    - **EventEntity**: EventEntity represents an event happening in the future. Event start time is a critical piece of information that needs to be conveyed to the users.

      ![Image](<https://developer.android.com/static/images/guide/playcore/engage/event-entity-travel.png>)

      **Figure 2:** UI showing a single EventEntity within Recommendations cluster.
    - **LodgingEntity**: LodgingEntity represents an accommodation, such as a hotel, apartment, vacation home for short term and long term rental.

      ![Image](<https://developer.android.com/static/images/guide/playcore/engage/lodging-entity-travel.png>)

      **Figure 3:** UI showing a single LodgingEntity within Recommendations cluster.
    - **StoreEntity**: StoreEntity represents a store, restaurant, cafe etc. It highlights content where a dining venue or store is the critical piece of information that needs to be conveyed to the users.

      ![Image](<https://developer.android.com/static/images/guide/playcore/engage/store-entity-travel.png>)

      **Figure 4:** UI showing a single StoreEntity within Recommendations cluster.
    - **PointOfInterestEntity**: PointOfInterestEntity represents a place of interest like, a gas station, event venue, theme park, museum, tourist attraction, hiking trail etc. It highlights content where location is a critical piece of information that needs to be conveyed to the users. It shouldn't be used for lodging, a store or a dining venue.

      ![Image](<https://developer.android.com/static/images/guide/playcore/engage/poi-entity-travel.png>)

      **Figure 5:** UI showing a single PointOfInterestEntity within Recommendations cluster.
- The **Reservation** cluster shows content recently engaged by users from multiple developer partners in a single UI grouping. Each developer partner will be allowed to broadcast a maximum of 10 entities in the Reservation cluster.

  Your reservation content can take the following structure:

  - **RestaurantReservationEntity**: RestaurantReservationEntity represents a reservation for a restaurant or cafe and helps users track upcoming or ongoing restaurant reservations.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/restaurant-reservation-entity-travel.png>)

    **Figure 6.** UI showing a single RestaurantReservationEntity within a Reservation cluster.
  - **EventReservationEntity**: EventReservationEntity represents a reservation for an event and helps users track upcoming or ongoing events reservations. Events could include, but not limited to the following:

    - Sports events like reservation for a football match
    - Gaming events like reservation for eSports
    - Entertainment events like reservation for movies in a cinema, concert, theater, book signing
    - Travel or point of interest reservations like guided tours, museum tickets
    - Social / Seminar / Conferences reservations
    - Education / Training sessions reservations

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/event-reservation-entity-travel.png>)

    **Figure 7.** UI showing a single EventReservationEntity within a Reservation cluster.
  - **LodgingReservationEntity**: LodgingEntityReservation represents a reservation for travel lodging and helps users track upcoming or ongoing hotel or vacation rental reservations.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/lodging-reservation-entity-travel.png>)

    **Figure 8.** UI showing a single LodgingReservationEntity within a Reservation cluster.
  - **TransportationReservationEntity**: TransportationReservationEntity represents reservation for transportation by any mode and helps users track reservations for upcoming or ongoing flight, ferry, train, bus, ride-hailing, or cruise.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/transportation-reservation-entity-travel.png>)

    **Figure 9.** UI showing a single TransportationReservationEntity within a Reservation cluster.
  - **VehicleRentalReservationEntity**: VehicleRentalReservationEntity represents vehicle rental reservation and helps users track upcoming or ongoing vehicle rental reservations.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/vehicle-rental-reservation-entity-travel.png>)

    **Figure 10.** UI showing a single VehicleRentalReservationEntity within a Reservation cluster.
- The **Featured** cluster showcases a selection of entities from multiple developer partners in one UI grouping. There will be a single Featured cluster, which is surfaced near the top of the UI with a priority placement above all Recommendation clusters. Each developer partner will be allowed to broadcast up to 10 entities in the Featured cluster.

  - **GenericFeaturedEntity**: GenericFeaturedEntity differs from Recommendation item in that Featured item should be used for a single top content from developers and should represent the single most important content that will be interesting and relevant to users.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/featured-cluster-travel.png>)

    **Figure 11:** UI showing a FeaturedCluster with a list of GenericFeaturedEntity
- The **Continue Search** cluster helps users resume their previous travel search journey by showcasing a list of search queries that the user has recently searched for across all their travel apps. The cluster will be pinned in second position, after reservations and before featured and recommendation clusters. Each developer partner will be allowed to broadcast up to 3 entities in the Continue Search cluster.

  - **PointOfInterestEntity:** PointOfInterestEntity represents a place of interest like, a gas station, event venue, theme park, museum, tourist attraction, hiking trail etc. It highlights content the user has previously searched for.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/travel).
