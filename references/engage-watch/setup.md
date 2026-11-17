> **Important:** Engage SDK has superseded Media Home, which is now deprecated. If you have an existing Media Home integration, follow the instructions in these guides to migrate your content to Engage SDK, which allows your content to be published to more devices and form factors. Please contact [`engage-developers@google.com`](<mailto:engage-developers@google.com>) if you have any questions.

Use Engage SDK to publish Continue Watching content and personalized recommendations on supported Google surfaces, including [Collections](<https://developer.android.com/guide/playcore/engage>), [Entertainment Space](<https://blog.google/products/android/entertainment-space/>) and the Play Store. This guide's integration estimate is less than 50 KB added to the average compressed APK and about a developer week; measure your app's actual size and integration work. Review [program participation](<http://play.google.com/console/about/programs/EngageSDK>) separately.

This guide contains instructions for developer partners to integrate their video content, using the Engage SDK to populate both this new surface area and existing Google surfaces.

> **Note:** Check the [TV integration guide](<https://developer.android.com/guide/playcore/engage/tv>) to learn more about the Continue Watching experience on Google TV.

## Category support and surfaces

Engage SDK surface eligibility is based on your app's content category. Use the following table to determine your eligibility for specific surfaces:

| Status | Content category or use case | Supported surfaces |
| --- | --- | --- |
| **Supported**<br> (Eligible on all surfaces) | Movies & TV streaming Live TV / Sports On demand video clips Sports videos Drama Shorts Video podcasts | Collections Entertainment Space Play Store Apps tab Play Store You tab Play Store store listing page |
| **Partially supported**<br> (Eligible on some surfaces) | Video clips from news apps | Collections Entertainment Space |
| **Not supported** | Remote controls Video downloaders, players, and editors Movie & TV reviews Movie tickets TV guides Video calls & chatrooms |  |

## Integration detail

This section details the steps, data models, and terminology required to integrate with the Engage SDK for video content.

### Terminology

This integration includes the following three cluster types: **Recommendation**, **Continuation**, and **Featured**.

- **Recommendation** clusters show personalized suggestions for content to watch from an individual developer partner.

  Your recommendations take the following structure:

  - **Recommendation Cluster:** A UI view that contains a group of recommendations from the same developer partner.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/watch-term-1.png>)

    **Figure 1.** Entertainment Space UI showing a Recommendation Cluster from a single partner.
  - **Entity:** An object representing a single item in a cluster. An entity can be a movie, a TV show, a TV series, live video, and more. See the [Provide entity data](<https://developer.android.com/guide/playcore/engage/watch?hl=en#provide-entity-data>) section for a list of supported entity types.

    ![Image](<https://developer.android.com/static/images/guide/playcore/engage/watch-term-2.png>)

    **Figure 2.** Entertainment Space UI showing a single Entity within a single partner's Recommendation Cluster.
- The **Continuation** cluster shows unfinished videos and relevant newly released episodes from multiple developer partners in one UI grouping. Each developer partner will be allowed to broadcast a maximum of 10 entities in the Continuation cluster. Research has shown that personalized recommendations along with personalized Continuation content creates the best user engagement.

  ![Image](<https://developer.android.com/static/images/guide/playcore/engage/watch-term-3.png>)

  **Figure 3.** Entertainment Space UI showing a Continuation cluster with unfinished recommendations from multiple partners (only one recommendation is currently visible).
- The **Featured** cluster showcases a selection of entities from multiple developer partners in one UI grouping. There will be a single Featured cluster, which is surfaced near the top of the UI with a priority placement above all Recommendation clusters. Each developer partner will be allowed to broadcast up to 10 entities in the Featured cluster.

  ![Image](<https://developer.android.com/static/images/guide/playcore/engage/watch-term-4.png>)

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

For more information, see [Package visibility in Android 11](<https://developer.android.com/about/versions/11/privacy/package-visibility>).

### Summary

The design is based on an implementation of a [bound service](<https://developer.android.com/guide/components/bound-services>).

The data a client can publish is subject to the following limits for different cluster types:

| Cluster type | Cluster limits | Maximum entity limits in a cluster |
| --- | --- | --- |
| Recommendation Cluster(s) | At most 7 | At most 50 |
| Continuation Cluster | At most 1 | At most 20 |
| Featured Cluster | At most 1 | At most 20 |

> **Important:** Engage SDK has superseded Media Home, which is now deprecated. If you have an existing Media Home integration, follow the instructions in [Step 0](<https://developer.android.com/guide/playcore/engage/watch?hl=en#migration>) to migrate your content to Engage SDK, which allows your content to be published to more devices and form factors. Contact [`engage-developers@google.com`](<mailto:engage-developers@google.com>). If you don't have an existing Media Home integration, skip to [Step 1](<https://developer.android.com/guide/playcore/engage/watch?hl=en#provide-entity-data>).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/watch).
