Use the [Engage SDK overview](../engage/overview.md) for supported surfaces, participation and integration estimates.

This guide contains instructions for developer partners to deliver audio content (music, podcasts, audiobooks, live radio) to Engage content surfaces.

## Category support and surfaces

Engage SDK surface eligibility is based on your app's content category. Use the following table to determine your eligibility for specific surfaces:

| Status | Content category or use case | Supported surfaces |
| --- | --- | --- |
| **Supported**<br> (Eligible on all surfaces) | Music streaming Audiobooks Podcasts Live radio | Collections Entertainment Space Play Store Apps tab Play Store You tab Play Store store listing page |
| **Partially supported**<br> (Eligible on some surfaces) | Live audio streams | Collections Entertainment Space |
| **Not supported** | MP3 player / library Music maker Audio recorder / converter / tool Music recognition Music education (supported in education) |  |

## Integration detail

This section details the steps, data models, and terminology required to integrate with the Engage SDK for audio content.

### Terminology

This integration includes the following three cluster types: **Recommendation**, **Continuation**, and **Featured**.

- **Recommendation** clusters show personalized suggestions for content to read from an individual developer partner.

  Your recommendations take the following structure:

  - **Recommendation Cluster:** A UI view that contains a group of recommendations from the same developer partner.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/listen-term-1.png>)

    **Figure 1.** Entertainment Space UI showing a Recommendation Cluster from a single partner.
  - **Entity:** An object representing a single item in a cluster. An entity can be a playlist, an audiobook, a podcast, and more. See the [Provide entity data](<https://developer.android.com/guide/playcore/engage/listen?hl=en#provide-entity-data>) section for a list of supported entity types.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/listen-term-2.png>)

    **Figure 2.** Entertainment Space UI showing a single Entity within a single partner's Recommendation Cluster.
- The **Continuation** cluster shows audio content recently engaged by users from multiple developer partners in a single UI grouping. Each developer partner will be allowed to broadcast a maximum of 10 entities in the Continuation cluster.

  ![Image](<https://developer.android.com/static/images/guide/playcore/engage/listen-term-3.png>)

  **Figure 3.** Entertainment Space UI showing a Continuation cluster with unfinished recommendations from multiple partners (only one recommendation is currently visible).
- The **Featured** cluster showcases a selection of items from multiple developer partners in a single UI grouping. There will be a single Featured cluster, which will be surfaced near the top of the UI with a priority placement above all Recommendation clusters. Each developer partner will be allowed to broadcast up to 10 entities in the Featured cluster.

  ![Image](<https://developer.android.com/static/images/guide/playcore/engage/listen-term-4.png>)

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

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/listen).
