This guide describes the data model and integration steps for publishing video and live TV content using the Engage SDK.

## `MovieEntity` data model

The `MovieEntity` represents a full-length film. The following table summarizes content fields and surface requirements. Exact Java return types and method availability depend on the installed SDK version; consult the linked API declarations for signatures.

| Public Methods | Type | Requirement | Description |
| --- | --- | --- | --- |
| [`getName()`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity#getName()>) | String | Required | The title of the movie (e.g., "Avengers: Endgame") |
| [`getDescription()`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity#getDescription()>) | String | Required | A summary providing context that appears on hover |
| [`getPosterImages()`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity#getPosterImages()>) | `List<Image>` | Required | A list of images used for the movie's poster display |
| [`getPlatformSpecificPlaybackUris()`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity#getPlatformSpecificPlaybackUris()>) | `List<PlatformSpecificUri>` | Required | Deep links for playback on specific platforms |
| [`getDurationMillis()`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity#getDurationMillis()>) | Long | Required | The total duration of the movie in milliseconds |
| `getCallToActionText()` | String | Required (GTV) | Text displayed to prompt user interaction (e.g., "Watch Now") |
| `getTags()` | `List<String>` | Optional | Keywords used for categorization (e.g., "Action/Thriller") |

## `LiveTvProgramEntity` data model

The `LiveTvProgramEntity` represents a program airing or scheduled to air on a specific channel.

| Public Methods | Type | Requirement | Description |
| --- | --- | --- | --- |
| [`getName()`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getName()>) | String | Required | The title of the program (e.g., "NBC CT Late News") |
| [`getDescription()`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getDescription()>) | String | Required | A summary providing context about the program |
| [`getPosterImages()`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getPosterImages()>) | `List<Image>` | Required | Images used for the program's display |
| [`getAvailabilityTimeWindows()`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getAvailabilityTimeWindows()>) | `List<DisplayTimeWindow>` | Required | The scheduled time windows for the program |
| [`getChannelId()`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getChannelId()>) | String | Required | Unique identifier for the TV channel |
| [`getChannelName()`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getChannelName()>) | String | Required | Name of the TV channel |
| [`getChannelLogoImage()`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveTvProgramEntity#getChannelLogoImage()>) | Image | Required | Logo image for the TV channel |
| `getCallToActionText()` | String | Required (GTV) | Interaction prompt text |
| `getTags()` | `List<String>` | Optional | Keywords used for categorization |

> **Note:** These public methods (e.g., `setCallToActionText()`, `addTag()`, `addBadge()`) are also available for other video entities, such as `TvShowEntity`, `TvEpisodeEntity`, and `TvSeasonEntity`.

## API

`publishRecommendationClusters()` will be used to send candidate content to the Feature Carousel. Cluster type should be set as `RecommendationClusterType.TYPE_PROVIDER_ROW`.

### Item limits and targeting

- **Item Limits:** The Featured Carousel displays a maximum of 3 items.
- **Targeting:** You can customize the Featured Carousel content for each individual device. Since the content is published from the client app installed on the device, you can populate it with unique, personalized candidate lists per user or device. However, you're responsible for implementing this targeting logic, as the Engage SDK doesn't provide built-in targeting support.

> **Note:** Make sure you send your complete candidate list, including all recommendation rows, in every `publishRecommendationClusters` call. Each call fully overwrites the previous set of candidates. If you omit recommendation rows, they'll be removed from the display.

## Engage SDK version

Note the minimum Engage SDK version required for this integration:

```text
engage-tv: 1.0.6
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/fc-automation).
