This guide covers how to integrate Continue Watching into your Android TV app using the Engage SDK.

## Pre-work

> **Important:** [Express interest in developing with Engage](<http://g.co/tv/vda>).

Complete the [Pre-work](<https://developer.android.com/guide/playcore/engage/tv/getting-started#pre-work>) instructions in the Getting Started guide.

## Integration

> **Note:** The Continue Watching API works differently from the [Watch Next API](<https://developer.android.com/training/tv/discovery/watch-next-add-programs>). Instead of adding or removing items one by one, it replaces the entire list of "continue watching" items each time it updates. This means you need to send all the items you want to show every time you update. You should display as many entities as possible in the continue watching row, but no more than 10. Also, the new API combines the steps for publishing the list and the items into one, making it simpler. Keep in mind that Google TV might not show all the items you send, as it combines lists from different apps.

### Create entities

The SDK has defined different entities to represent each item type. Continuation cluster supports following entities:

1. [`MovieEntity`](<https://developer.android.com/guide/playcore/engage/watch#movieentity>)
2. [`TvEpisodeEntity`](<https://developer.android.com/guide/playcore/engage/watch#tvepisodeentity>)
3. [`LiveStreamingVideoEntity`](<https://developer.android.com/guide/playcore/engage/watch#livestreamingvideoentity>)
4. [`VideoClipEntity`](<https://developer.android.com/guide/playcore/engage/watch#videoclipentity>)

> **Note:** [`TvShowEntity`](<https://developer.android.com/guide/playcore/engage/watch#tvshowentity>) and [`TvSeasonEntity`](<https://developer.android.com/guide/playcore/engage/watch#tvseasonentity>) are not supported for the Continuation cluster for continue watching. When a user finishes one TV Episode, the next `TvEpisodeEntity` should be published for the user to continue watching the next episode.

Specify the platform-specific URIs and poster images for these entities.

Also, create playback URIs for each platform, such as Android TV, Android, or iOS, if you haven't already. So when a user continues watching on each platform, the app uses a targeted playback URI to play the video content.

> **Note:** In the rare case when the playback URIs are identical for all platforms, you will still have to repeat it for every platform that you want to continue watching to happen.

```kotlin
// Required. Set this when you want continue watching entities to show up on
// Google TV
val playbackUriTv = PlatformSpecificUri.Builder()
    .setPlatformType(PlatformType.TYPE_ANDROID_TV)
    .setActionUri(Uri.parse("https://www.example.com/entity_uri_for_tv"))
    .build()

// Required. Set this when you want continue watching entities to show up on
// Google TV Android app, Entertainment Space, Playstore Widget
val playbackUriAndroid = PlatformSpecificUri.Builder()
    .setPlatformType(PlatformType.TYPE_ANDROID_MOBILE)
    .setActionUri(Uri.parse("https://www.example.com/entity_uri_for_android"))
    .build()

// Optional. Set this when you want continue watching entities to show up on
// Google TV iOS app
val playbackUriIos = PlatformSpecificUri.Builder()
    .setPlatformType(PlatformType.TYPE_IOS)
    .setActionUri(Uri.parse("https://www.example.com/entity_uri_for_ios"))
    .build()

val platformSpecificPlaybackUris =
    Arrays.asList(playbackUriTv, playbackUriAndroid, playbackUriIos)
```

Poster images require a URI and pixel dimensions (height and width). Target different form factors by providing multiple poster images, but verify that all images maintain a 16:9 aspect ratio and a minimum height of 200 pixels for correct display of the "Continue Watching" entity, especially within Google's [Entertainment Space](<https://support.google.com/entertainmentspace/answer/10346911>). Images with a height less than 200 pixels may not be shown.

```kotlin
val images = Arrays.asList(
    Image.Builder()
        .setImageUri(Uri.parse("http://www.example.com/entity_image1.png"))
        .setImageHeightInPixel(300)
        .setImageWidthInPixel(169)
        .build(),
    Image.Builder()
        .setImageUri(Uri.parse("http://www.example.com/entity_image2.png"))
        .setImageHeightInPixel(640)
        .setImageWidthInPixel(360)
        .build()
    // Consider adding other images for different form factors
)
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/continue-watching/client).
