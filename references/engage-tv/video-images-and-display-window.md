### Poster images

Poster images require a URI and pixel dimensions (height and width). Target different form factors by providing multiple poster images, but verify all images maintain a 16:9 aspect ratio and a minimum height of 200 pixels for correct display of the "Recommendations" entity, especially within Google's [Entertainment Space](<https://support.google.com/entertainmentspace/answer/10346911>). Images with a height less than 200 pixels may not be shown.

```kotlin
val image1 = Image.Builder()
  .setImageUri(Uri.parse("http://www.example.com/entity_image1.png"))
  .setImageHeightInPixel(300)
  .setImageWidthInPixel(169)
  .build()

val image2 = Image.Builder()
  .setImageUri(Uri.parse("http://www.example.com/entity_image2.png"))
  .setImageHeightInPixel(640)
  .setImageWidthInPixel(360)
  .build()

// And other images for different form factors.
val images = Arrays.asList(image1, image2)
```

### Recommendation reason

Optionally provide a recommendation reason which can be used by Google TV to construct reasons as to why to suggest a specific Movie or TV Show to the user.

[Complete kotlin example: Recommendation reason](<https://developer.android.com/guide/playcore/engage/tv/recommendations#recommendation-reason>).

### Display time window

If an entity should only be available for a limited time, set a custom expiration time. Without an explicit expiration time, entities will automatically expire and be erased after 60 days. So set an expiration time only when the entities need to be expired sooner. Specify multiple such availability windows.

```kotlin
val window1 = DisplayTimeWindow
  .Builder()
  .setStartTimestampMillis(now() + 1.days.toMillis())
  .setEndTimestampMillis(now() + 30.days.toMillis())
  .build()

val window2 = DisplayTimeWindow
  .Builder()
  .setEndTimestampMillis(now() + 30.days.toMillis())
  .build()

val availabilityTimeWindows: List<DisplayTimeWindow> = listOf(window1, window2)
```

### DataFeedElementId

If you have integrated your Media catalogue or Media action feed with Google TV, you need not create separate entities for Movie or TV Show and instead you can create a [`MediaActionFeedEntity`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/MediaActionFeedEntity>) which includes the required field DataFeedElementId. This Id must be unique and must match with the ID in Media Action Feed as it helps to identify ingested feed content and perform media content lookups.

```kotlin
val id = "dataFeedElementId"
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/recommendations).
