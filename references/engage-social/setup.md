Use the [Engage SDK overview](../engage/overview.md) for supported surfaces, participation and integration estimates.

This guide contains instructions for developer partners to deliver social media content to Engage content surfaces.

## Category support and surfaces

Engage SDK surface eligibility is based on your app's content category. Use the following table to determine your eligibility for specific surfaces:

| Status | Content category or use case | Supported surfaces |
| --- | --- | --- |
| **Supported**<br> (Eligible on all surfaces) | Social networks Image / memes Video clips / short-form video IRL meetups Cloud photo storage | Collections Play Store Apps tab Play Store You tab Play Store store listing page |
| **Not supported** | Live Video Chat Instant messaging, sharing online presence, or live data File-sharing & downloaders Dating Avatar generators |  |

## Integration detail

Integration continues with [social entity models](social-entity-models-and-images.md) and [publishing and receiver registration](index.md).

### Terminology

***Recommendation*** clusters show personalized suggestions from an individual developer partner.

Your recommendations take the following structure:

**Recommendation Cluster**: UI view that contains a group of recommendations from the same developer partner.

Each Recommendation Cluster consists of one of the following two types of entities :

- PortraitMediaEntity
- SocialPostEntity

**PortraitMediaEntity** must contain 1 portrait image for the post. Profile and Interaction related metadata are optional.

- Post

  - Image in portrait mode and Timestamp, or
  - Image in portrait mode + text content and Timestamp
- Profile

  - Avatar, Name or Handle, Additional image
- Interactions

  - Count and label only, or
  - Count and visual (icon)

**SocialPostEntity** contains profile, post and interaction related metadata.

- Profile

  - Avatar, Name or Handle, additional text, additional image
- Post

  - Text and Timestamp, or
  - Rich media (image or rich URL) and Timestamp, or
  - Text and rich media (image or rich URL) and Timestamp, or
  - Video preview (thumbnail and duration) and Timestamp
- Interactions

  - Count & label only, or
  - Count & visual (icon)

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
| Recommendation Cluster(s) | At most 7 | At least 1 (`PortraitMediaEntity`, or `SocialPostEntity`) | At most 50 (`PortraitMediaEntity`, or `SocialPostEntity`) |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/social).
