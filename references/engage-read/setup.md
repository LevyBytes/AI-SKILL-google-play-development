> **Important:** Engage SDK has superseded Media Home, which is now deprecated. If you have an existing Media Home integration, follow the instructions in these guides to migrate your content to Engage SDK, which allows your content to be published to more devices and form factors. Please contact [`engage-developers@google.com`](<mailto:engage-developers@google.com>) if you have any questions.

Use the [Engage SDK overview](../engage/overview.md) for supported surfaces, participation and integration estimates.

This guide contains instructions for developer partners to deliver reading content (eBooks, Audiobooks, Comics/Manga, Blogs, News and Magazines) to Engage content surfaces.

## Category support and surfaces

Engage SDK surface eligibility is based on your app's content category. Use the following table to determine your eligibility for specific surfaces:

| Status | Content category or use case | Supported surfaces |
| --- | --- | --- |
| **Supported**<br> (Eligible on all surfaces) | eBooks Comics & Manga Audiobooks UGC long-form reading services Blogs | Collections Entertainment Space Play Store Apps tab Play Store You tab (Personalized recommendations & continuation only) Play Store store listing page |
| **Partially supported**<br> (Eligible on some surfaces) | News & Magazines* | Collections Entertainment Space |
| **Not supported** | eBook or PDF reader Book reviews Encyclopedia / Dictionary Translator Religious text |  |

### News apps

News apps provide diverse content, each subject to unique eligibility rules. Because Engage SDK content on the Play Store aligns with Play Premium Growth Tools, news articles and video clips from news apps are ineligible for the Play Store, though they are eligible for Collections and Entertainment Space. Conversely, non-traditional news content, like podcasts and recipes, may be eligible for the Play Store:

| Entity type | Eligible for Collections | Eligible for Entertainment Space | Eligible for Play Store |
| --- | --- | --- | --- |
| News article | *Yes (Read tab)* | *Yes (Read tab)* | No |
| Video clip | *Yes (Watch tab)* | *Yes (Watch tab)* | No |
| Podcast | *Yes (Listen tab)* | *Yes (Listen tab)* | *Yes* |
| Recipe | *Yes (Food tab)* | No | *Yes* |

> **Note:** Play Store eligibility aligns with the supported categories for [Play Premium Growth Tools](<https://play.google.com/console/about/guides/premium-growth-tools/>). If your news app has additional forms of content not listed in the preceding table, contact [`engage-developers@google.com`](<mailto:engage-developers@google.com>) to clarify its eligibility for the Play Store.

## Integration detail

This section details the steps, data models, and terminology required to integrate with the Engage SDK for reading content.

### Terminology

This integration includes the following three cluster types: **Recommendation**, **Continuation**, and **Featured**.

- **Recommendation** clusters show personalized suggestions for content to read from an individual developer partner.

  Your recommendations take the following structure:

  - **Recommendation Cluster:** A UI view that contains a group of recommendations from a single developer partner.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/read-term-1.png>)

    **Figure 1.** Entertainment Space UI showing a Recommendation Cluster from a single partner.
  - **Entity:** An object representing a single item in a cluster. An entity can be an ebook, an audio book, a book series, and more. See the [Provide entity data](<https://developer.android.com/guide/playcore/engage/read?hl=en#provide-entity-data>) section for a list of supported entity types.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/read-term-2.png>)

    **Figure 2.** Entertainment Space UI showing a single Entity within a single partner's Recommendation Cluster.
- The **Continuation** cluster shows unfinished books from multiple developer partners in a single UI grouping. Each developer partner will be allowed to broadcast a maximum of 10 entities in the Continuation cluster.

  ![Image](<https://developer.android.com/static/images/guide/playcore/engage/read-term-3.png>)

  **Figure 3.** Entertainment Space UI showing a Continuation cluster with unfinished recommendations from multiple partners (only one recommendation is currently visible).
- The **Featured** cluster showcases a selection of items from multiple developer partners in a single UI grouping. There will be a single Featured cluster, which is surfaced near the top of the UI with a priority placement above all Recommendation clusters. Each developer partner will be allowed to broadcast up to 10 entities in the Featured cluster.

  ![Image](<https://developer.android.com/static/images/guide/playcore/engage/read-term-4.png>)

  **Figure 4.** Entertainment Space UI showing a Featured cluster with recommendations from multiple partners (only one recommendation is currently visible).

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

| Cluster type | Cluster limits | Maximum entity limits in a cluster |
| --- | --- | --- |
| Recommendation Cluster(s) | At most 7 | At most 50 |
| Continuation Cluster | At most 1 | At most 20 |
| Featured Cluster | At most 1 | At most 20 |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/read).
