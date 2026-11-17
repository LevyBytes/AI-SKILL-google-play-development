Use the [Engage SDK overview](../engage/overview.md) for supported surfaces, participation and integration estimates.

This document contains instructions for developer partners to integrate new content like reservations, events, lodging, places of interest, people and other content that might not belong to any of these categories.

## Integration detail

This section details the steps, data models, and terminology required to integrate with the Engage SDK for other content categories.

### Terminology

This integration includes the following three cluster types: **Recommendation**, **Featured**, and **Continuation**.

- **Recommendation** clusters show personalized suggestions from an individual developer partner. It is a UI view that contains a group of recommendations from the same developer partner.

  - **ArticleEntity**: ArticleEntity that represents a text-based recommendation for content that is relevant to more than one category of content. ArticleEntity item allows developers to provide a variety of text and image content with more metadata to articulate the information to the users compared to GenericFeaturedEntity. Ex: Marketing content, News snippet

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
  - **PersonEntity**: PersonEntity represents a person. The recommendations could be to highlight a person in categories like health and fitness, sports, dating, etc.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/person-entity-dating.png>)

    **Figure 5:** UI showing a single PersonEntity within Recommendations cluster.
- The **Continuation** cluster shows content recently engaged by users from multiple developer partners in a single UI grouping. Each developer partner will be allowed to broadcast a maximum of 10 entities in the Continuation cluster.

  Your continuation content can take the following structure:

  - **ArticleEntity**: ArticleEntity that represents a text-based recommendation for content that is relevant to more than one category of content. This entity can be used to represent unfinished news articles or other content that the user would like to continue consuming from where they left it. Ex: Marketing content, News snippet

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/article-entity-continuation-travel.png>)

    **Figure 6.** UI showing a single ArticleEntity within a Continuation cluster.
  - **RestaurantReservationEntity**: RestaurantReservationEntity represents a reservation for a restaurant or cafe and helps users track upcoming or ongoing restaurant reservations.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/restaurant-reservation-entity-travel.png>)

    **Figure 7.** UI showing a single RestaurantReservationEntity within a Continuation cluster.
  - **EventReservationEntity**: EventReservationEntity represents a reservation for an event and helps users track upcoming or ongoing events reservations. Events could include, but not limited to the following:

    - Sports events like reservation for a football match
    - Gaming events like reservation for eSports
    - Entertainment events like reservation for movies in a cinema, concert, theater, book signing
    - Travel or point of interest reservations like guided tours, museum tickets
    - Social / Seminar / Conferences reservations
    - Education / Training sessions reservations

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/event-reservation-entity-travel.png>)

    **Figure 8.** UI showing a single EventReservationEntity within a Continuation cluster.
  - **LodgingReservationEntity**: LodgingEntityReservation represents a reservation for a travel lodging and helps users track upcoming or ongoing hotel or vacation rental reservations.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/lodging-reservation-entity-travel.png>)

    **Figure 9.** UI showing a single LodgingReservationEntity within a Continuation cluster.
  - **TransportationReservationEntity**: TransportationReservationEntity represents a reservation for transportation by any mode and helps users track reservations for upcoming or ongoing flight, ferry, train, bus, ride-hailing, or cruise.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/transportation-reservation-entity-travel.png>)

    **Figure 10.** UI showing a single TransportationReservationEntity within a Continuation cluster.
  - **VehicleRentalReservationEntity**: VehicleRentalReservationEntity represents a vehicle rental reservation and helps users track upcoming or ongoing vehicle rental reservations.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/vehicle-rental-reservation-entity-travel.png>)

    **Figure 11.** UI showing a single VehicleRentalReservationEntity within a Continuation cluster.
- The **Featured** cluster is a UI view that showcases the chosen hero `GenericFeaturedEntity` from many developer partners in one UI grouping. There is a single Featured cluster, which is surfaced near the top of the UI, with a priority placement above all Recommendation clusters. Each developer partner is allowed to broadcast a single entity of a supported type in Featured, with many entities (potentially of different types) from multiple app developers in the Featured cluster.

  - **GenericFeaturedEntity**: GenericFeaturedEntity differs from Recommendation item in that Featured item should be used for a single top content from developers and should represent the single most important content that will be interesting and relevant to users.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/featured-item-health-and-fitness.png>)

    **Figure 12:** UI showing a single hero GenericFeaturedEntity card within a Featured cluster

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/otherverticals).
