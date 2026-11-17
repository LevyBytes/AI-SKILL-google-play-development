## Create entities

The SDK has defined different entities to represent each item type. Following entities are supported for the Recommendation cluster:

1. [`MediaActionFeedEntity`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/MediaActionFeedEntity>)
2. [`MovieEntity`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity>)
3. [`TvShowEntity`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/TvShowEntity>)
4. [`LiveTvChannelEntity`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvChannelEntity>)
5. [`LiveTvProgramEntity`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity>)

### Provide descriptions

Provide a short description for each entity; this description will be displayed when users hover over the entity, providing them with additional details.

### Call to action text

Provide an optional call to action text for each entity. This text will be displayed to the user to encourage engagement.

### Tags

Optionally provide a list of tags for each entity. Tags can be used for categorization and filtering.

### Platform specific playBack URIs

Create playback URIs for each supported platform: Android TV, Android, or iOS. This allows the system to select the appropriate URI for video playback on the respective platform.

In the rare case when the playback URIs are identical for all platforms, repeat it for every platform.

```kotlin
// Required. Set this when you want recommended entities to show up on
// Google TV
val playbackUriTv = PlatformSpecificUri
  .Builder()
  .setPlatformType(PlatformType.TYPE_ANDROID_TV)
  .setActionUri(Uri.parse("https://www.example.com/entity_uri_for_tv"))
  .build()

// Optional. Set this when you want recommended entities to show up on
// Google TV Android app
val playbackUriAndroid = PlatformSpecificUri
  .Builder()
  .setPlatformType(PlatformType.TYPE_ANDROID_MOBILE)
  .setActionUri(Uri.parse("https://www.example.com/entity_uri_for_android"))
  .build()

// Optional. Set this when you want recommended entities to show up on
// Google TV iOS app
val playbackUriIos = PlatformSpecificUri
  .Builder()
  .setPlatformType(PlatformType.TYPE_IOS)
  .setActionUri(Uri.parse("https://www.example.com/entity_uri_for_ios"))
  .build()

val platformSpecificPlaybackUris =
  Arrays.asList(playbackUriTv, playbackUriAndroid, playbackUriIos)

// Provide appropriate rating for the system.
val contentRating = RatingSystem
  .Builder()
  .setAgencyName("MPAA")
  .setRating("PG-13")
  .build()
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/recommendations).
