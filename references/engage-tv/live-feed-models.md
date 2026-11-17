### `MediaActionFeedEntity`

Here's an example of creating an `MediaActionFeedEntity` with all the required fields:

```kotlin
val mediaActionFeedEntity = MediaActionFeedEntity.Builder()
  .setDataFeedElementId(id)
  .setCallToActionText("Watch Now")
  .addTag("Action")
  .build()
```

Optionally provide additional data such as description, recommendation reason and display time window, which may be used by Google TV for enhanced displays or filtering purposes.

```kotlin
val mediaActionFeedEntity = MediaActionFeedEntity.Builder()
  .setName("Movie name or TV Show name")
  .setDescription("A sentence describing an entity")
  .setRecommendationReason(topOnPartner or watchedSimilarTitles)
  .addPosterImages(images)
  .build()

```

### `LiveTvChannelEntity`

This represents a live TV channel. Here's an example of creating a `LiveTvChannelEntity` with all the required fields:

```kotlin
val liveTvChannelEntity = LiveTvChannelEntity.Builder()
  .setName("Channel Name")
  // ID of the live TV channel
  .setEntityId("https://www.example.com/channel/12345")
  .setDescription("A sentence describing this live TV channel.")
  // channel playback uri must contain at least PlatformType.TYPE_ANDROID_TV
  .addPlatformSpecificPlaybackUris(channelPlaybackUris)
  .setLogoImage(logoImage)
  .setCallToActionText("Watch Now")
  .addTag("News")
  .build()
```

Optionally provide additional data such as content ratings or recommendation reason.

```kotlin
val rating1 = RatingSystem.Builder()
  .setAgencyName("MPAA")
  .setRating("pg-13")
  .build()
val contentRatings = Arrays.asList(rating1)

val liveTvChannelEntity = LiveTvChannelEntity.Builder()
  ...
  .addContentRatings(contentRatings)
  .setRecommendationReason(topOnPartner)
  .build()
```

### `LiveTvProgramEntity`

This represents a live TV program card airing or scheduled to air on a live TV channel. Here's an example of creating a `LiveTvProgramEntity` with all the required fields:

[Complete kotlin example: LiveTvProgramEntity](<https://developer.android.com/guide/playcore/engage/tv/recommendations#livetvprogramentity>).

Optionally provide additional data such as content ratings, genres, or recommendation reason.

```kotlin
val rating1 = RatingSystem.Builder()
  .setAgencyName("MPAA")
  .setRating("pg-13")
  .build()
val contentRatings = Arrays.asList(rating1)
val genres = Arrays.asList("Action", "Science fiction")

val liveTvProgramEntity = LiveTvProgramEntity.Builder()
  ...
  .addContentRatings(contentRatings)
  .addGenres(genres)
  .setRecommendationReason(topOnPartner)
  .build()
```

> **Note:** If the additional fields are provided directly within the entity, these values will be prioritized. The locale, if provided in the Account Profile, will be used to fetch the remaining entity metadata from Google's database in the language consistent with the request.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/recommendations).
