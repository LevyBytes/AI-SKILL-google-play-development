#### MovieEntity

This example show how to create a `MovieEntity` with all the required fields:

[Complete kotlin example: MovieEntity](<https://developer.android.com/guide/playcore/engage/tv/continue-watching/client#movieentity>).

Providing details like genres and content ratings gives Google TV the power to showcase your content in more dynamic ways and connect it with the right viewers.

```kotlin
val genres = Arrays.asList("Action", "Science fiction")
val rating1 = RatingSystem.Builder().setAgencyName("MPAA").setRating("PG-13").build()
val contentRatings = Arrays.asList(rating1)
val movieEntity = MovieEntity.Builder()
    ...
    .addGenres(genres)
    .addContentRatings(contentRatings)
    .build()
```

Entities automatically remain available for 60 days unless you specify a shorter expiration time. Only set a custom expiration if you need the entity to be removed before this default period.

```kotlin
// Set the expiration time to be now plus 30 days in milliseconds
val expirationTime = DisplayTimeWindow.Builder()
    .setEndTimestampMillis(now().toMillis()+2592000000).build()
val movieEntity = MovieEntity.Builder()
    ...
    .addAvailabilityTimeWindow(expirationTime)
    .build()
```

#### TvEpisodeEntity

This example show how to create a `TvEpisodeEntity` with all the required fields:

[Complete kotlin example: TvEpisodeEntity](<https://developer.android.com/guide/playcore/engage/tv/continue-watching/client#tvepisodeentity>).

Episode number string (such as `"2"`), and season number string (such as `"1"`) will be expanded to the proper form before being displayed on the continue watching card. Note that they should be a numeric string, don't put "e2", or "episode 2", or "s1" or "season 1".

If a particular TV show has a single season, set season number as 1.

To maximize the chances of viewers finding your content on Google TV, consider providing additional data such as genres, content ratings, and availability time windows, as these details can enhance displays and filtering options.

```kotlin
val genres = Arrays.asList("Action", "Science fiction")
val rating1 = RatingSystem.Builder().setAgencyName("MPAA").setRating("PG-13").build()
val contentRatings = Arrays.asList(rating1)
val tvEpisodeEntity = TvEpisodeEntity.Builder()
    ...
    .addGenres(genres)
    .addContentRatings(contentRatings)
    .setSeasonTitle("Season Title")
    .setShowTitle("Show Title")
    .build()
```

#### VideoClipEntity

Here's an example of creating a `VideoClipEntity` with all the required fields.

`VideoClipEntity` represents a user generated clip like a Youtube video.

[Complete kotlin example: VideoClipEntity](<https://developer.android.com/guide/playcore/engage/tv/continue-watching/client#videoclipentity>).

You can optionally set the creator, creator image, created time in milliseconds, or availability time window .

#### LiveStreamingVideoEntity

Here's an example of creating an `LiveStreamingVideoEntity` with all the required fields.

[Complete kotlin example: LiveStreamingVideoEntity](<https://developer.android.com/guide/playcore/engage/tv/continue-watching/client#livestreamingvideoentity>).

Optionally, you can set the start time, broadcaster, broadcaster icon, or availability time window for the live streaming entity.

For detailed information on attributes and requirements, see the [API reference](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/package-summary>).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/continue-watching/client).
