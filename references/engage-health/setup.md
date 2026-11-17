Use the [Engage SDK overview](../engage/overview.md) for supported surfaces, participation and integration estimates.

This guide contains instructions for developer partners to deliver health and fitness content to Engage content surfaces.

## Category support and surfaces

Engage SDK surface eligibility is based on your app's content category. Use the following table to determine your eligibility for specific surfaces:

| Status | Content category or use case | Supported surfaces |
| --- | --- | --- |
| **Supported**<br> (Eligible on all surfaces) | Fitness classes Fitness routines Relaxation & meditation Routes / trails discovery Meal planning | Collections Play Store Apps tab Play Store You tab Play Store store listing page |
| **Not supported** | BMI calculator Physical activity tracker / Step counter Calorie counter Sleep tracker Tools / Remotes Medical apps |  |

## Integration detail

This section details the steps, data models, and terminology required to integrate with the Engage SDK for health and fitness content.

### Terminology

This integration includes the following three cluster types: **Recommendation**, **Featured**, and **Continuation**.

- **Recommendation** clusters show personalized health and fitness suggestions from an individual developer partner. These recommendations can be personalized to the user or generalized (for example, trending fitness & health). Use these to feature articles or people related to health and fitness.

  - A Recommendation cluster can be made of `ArticleEntity`, `PersonEntity`, or `EventEntity` but not a mix of different entity types.

  Your recommendations take the following structure:

  - **Recommendation Cluster:** A UI view that contains a group of recommendations from the same developer partner.
  - **Entity:** An object representing a single item in a cluster. This integration offers some entities that would be surfaced using the Recommendation Cluster:

    - **ArticleEntity**: ArticleEntity represents a recommendation for text-based content related to health & fitness. It can be used for articles, blogposts, marketing content, news snippets, etc.

      ![Image](<https://developer.android.com/static/images/guide/playcore/engage/article-entity-health-and-fitness.png>)

      **Figure 1:** UI showing a single ArticleEntity within Recommendations cluster.
    - **PersonEntity**: PersonEntity represents a person. The recommendations could be to highlight a coach or any person related to health and fitness, etc.

      ![Image](<https://developer.android.com/static/images/guide/playcore/engage/person-entity-health-and-fitness.png>)

      **Figure 2:** UI showing a single PersonEntity within Recommendations cluster.
    - **EventEntity**: EventEntity represents an event happening in the future. Event start time is a critical piece of information that needs to be conveyed to the users This entity could be used for surfacing events like blood donation camp, training sessions, gym or yoga classes etc. related to health and fitness.

      ![Image](<https://developer.android.com/static/images/guide/playcore/engage/event-entity-health-and-fitness.png>)

      **Figure 3:** UI showing a single EventEntity within Recommendations cluster.
- The **Continuation** cluster shows content recently engaged by users from multiple developer partners in a single UI grouping. Each developer partner will be allowed to broadcast a maximum of 10 entities in the Continuation cluster.

  Your continuation content can take the following structure:

  - **ArticleEntity**: ArticleEntity represents a recommendation for text-based content that is related to health & fitness. This entity can be used to represent unfinished news articles or other content that the user would like to continue consuming from where they left it. Ex: News snippet, blogpost snippet about health or fitness related topics.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/article-entity-continuation-health-and-fitness.png>)

    **Figure 6.** UI showing a single ArticleEntity within a Continuation cluster.
  - **EventReservationEntity**: EventReservationEntity represents reservation for an event and helps users track upcoming or ongoing fitness and health events reservations. Ex: Training sessions

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/event-reservation-entity-health-and-fitness.png>)

    **Figure 8.** UI showing a single EventReservationEntity within a Continuation cluster.
- The **Featured** cluster showcases a selection of entities from multiple developer partners in one UI grouping. There will be a single Featured cluster, which is surfaced near the top of the UI with a priority placement above all Recommendation clusters. Each developer partner will be allowed to broadcast up to 10 entities in the Featured cluster.

  - **GenericFeaturedEntity**: GenericFeaturedEntity differs from Recommendation item in that Featured item should be used for a single top content from developers and should represent the single most important content that will be interesting and relevant to users.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/featured-item-health-and-fitness.png>)

    **Figure 12:** UI showing a single hero GenericFeaturedEntity card within a Featured cluster

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
| Recommendation Cluster(s) | At most 7 | At least 1 | At most 50 (`ArticleEntity`, `PersonEntity`, or `EventEntity`) |
| Continuation Cluster | At most 1 | At least 1 | At most 20 (`ArticleEntity`, or `EventReservationEntity`) |
| Featured Cluster | At most 1 | At least 1 | At most 20 (`GenericFeaturedEntity`) |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/healthandfitness).
