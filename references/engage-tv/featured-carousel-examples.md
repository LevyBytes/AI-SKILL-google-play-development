## Builder usage examples

### `MovieEntity` example

See [MovieEntity.Builder](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity.Builder>).

```java
MovieEntity movie = new MovieEntity.Builder()
    .setName("La hora 25")
    .setDescription("Brogan tiene 24 horas para revalorar su vida antes de ser encarcelado")
    .addPosterImage(new Image.Builder()
        .setImageUri(Uri.parse("https://www.example.com/movie_poster.png"))
        .build())
    .addPlatformSpecificPlaybackUri(new PlatformSpecificUri.Builder()
        .setActionUri(Uri.parse("https://www.example.com"))
        .setPlatformType(PlatformType.TYPE_ANDROID_TV)
        .build())
    .setDurationMillis(7200000L)
    .setCallToActionText("Watch Now")
    .addTag("Action/Thriller")
    .build();
```

### `LiveTvProgramEntity` example

See [LiveTvProgramEntity.Builder](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity.Builder>).

```java
LiveTvProgramEntity liveProgram = new LiveTvProgramEntity.Builder()
    .setName("3:30AM: NBC CT Late News")
    .setDescription("The latest local news, weather and investigative stories.")
    .setChannelId("https://www.example.com")
    .setChannelName("Tastemade")
    .setChannelLogoImage(new Image.Builder()
        .setImageUri(Uri.parse("https://example.com/v1/channels/logo.png"))
        .build())
    .addAvailabilityTimeWindow(new DisplayTimeWindow.Builder()
        .setStartTimestampMillis(1756713600000L)
        .setEndTimestampMillis(1756715400000L)
        .build())
    .addPosterImage(new Image.Builder()
        .setImageUri(Uri.parse("https://example.com/v1/assets/image.jpg"))
        .build())
    .setCallToActionText("Watch Now")
    .addTag("News")
    .build();
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/fc-automation).
