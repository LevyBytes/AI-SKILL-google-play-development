#### Image specifications

The following section lists the required specifications for image assets:

*File formats*

PNG, JPG, static GIF, WebP

*Maximum file size*

5120 KB

*Additional recommendations*

- **Image safe area:** Put your important content in the center 80% of the image.

#### Example

**Kotlin**

```kotlin
var movie = MovieEntity.Builder()
    .setName("Avengers")
    .addPosterImage(Image.Builder()
                          .setImageUri(Uri.parse("http://www.x.com/image.png"))
                          .setImageHeightInPixel(960)
                          .setImageWidthInPixel(408)
                          .build())
    .setPlayBackUri(Uri.parse("http://tv.com/playback/1"))
    .setReleaseDateEpochMillis(1633032895L)
    .setAvailability(ContentAvailability.AVAILABILITY_AVAILABLE)
    .setDurationMillis(12345678L)
    .addGenre("action")
    .addContentRating("R")
    .setWatchNextType(WatchNextType.TYPE_NEW)
    .setLastEngagementTimeMillis(1664568895L)
    .setCallToActionText("Watch Now")
    .addTag("Action")
    .build()
```

**Java**

```java
MovieEntity movie = new MovieEntity.Builder()
                  .setName("Avengers")
                  .addPosterImage(
                      new Image.Builder()
                          .setImageUri(Uri.parse("http://www.x.com/image.png"))
                          .setImageHeightInPixel(960)
                          .setImageWidthInPixel(408)
                          .build())
                  .setPlayBackUri(Uri.parse("http://tv.com/playback/1"))
                  .setReleaseDateEpochMillis(1633032895L)
                  .setAvailability(ContentAvailability.AVAILABILITY_AVAILABLE)
                  .setDurationMillis(12345678L)
                  .addGenre("action")
                  .addContentRating("R")
                  .setWatchNextType(WatchNextType.TYPE_NEW)
                  .setLastEngagementTimeMillis(1664568895L)
                  .setCallToActionText("Watch Now")
                  .addTag("Action")
                  .build();
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/watch).
