### `MovieEntity`

Here's an example of creating a `MovieEntity` with all the required fields:

```kotlin
val movieEntity = MovieEntity.Builder()
  .setName("Movie name")
  .setDescription("A sentence describing movie.")
  .addPlatformSpecificPlaybackUris(platformSpecificPlaybackUris)
  .addPosterImages(images)
  // Suppose the duration is 2 hours, it is 72000000 in milliseconds
  .setDurationMillis(72000000)
  .setCallToActionText("Watch Now")
  .addTag("Action")
  .build()
```

You can provide additional data such as genres, content ratings, release date, recommendation reason and availability time windows, which may be used by Google TV for enhanced displays or filtering purposes.

[Complete kotlin example: MovieEntity](<https://developer.android.com/guide/playcore/engage/tv/recommendations#movie-entity>).

### `TvShowEntity`

Here's an example of creating a `TvShowEntity` with all the required fields:

```kotlin
val tvShowEntity = TvShowEntity.Builder()
  .setName("Show title")
  .setDescription("A sentence describing TV Show.")
  .addPlatformSpecificPlaybackUris(platformSpecificPlaybackUris)
  .addPosterImages(images)
  .setCallToActionText("Watch Now")
  .addTag("Drama")
  .build()
```

Optionally provide additional data such as genres, content ratings, recommendation reason, offer price, season count or availability time window, which may be used by Google TV for enhanced displays or filtering purposes.

```kotlin
val genres = Arrays.asList("Action", "Science fiction")
val rating1 = RatingSystem.Builder()
  .setAgencyName("MPAA")
  .setRating("pg-13")
  .build()
val price = Price.Builder()
  .setCurrentPrice("$14.99")
  .setStrikethroughPrice("$16.99")
  .build()
val contentRatings = Arrays.asList(rating1)
val seasonCount = 5
val tvShowEntity = TvShowEntity.Builder()
  ...
  .addGenres(genres)
  .addContentRatings(contentRatings)
  .setRecommendationReason(topOnPartner or watchedSimilarTitles)
  .addAllAvailabilityTimeWindows(availabilityTimeWindows)
  .setSeasonCount(seasonCount)
  .setPrice(price)
  .build()
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/recommendations).
