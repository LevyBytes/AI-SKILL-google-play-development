#### `LiveStreamingVideoEntity`

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** |  |
| Poster images | **Required** | At least one image is required, and must be provided with an aspect ratio. (Landscape is preferred but passing both portrait and landscape images for different scenarios is recommended.) See [Image Specifications](<https://developer.android.com/guide/playcore/engage/watch?hl=en#image-specs>) for guidance. |
| Playback uri | **Required** for mobile | The deep link to the provider app to start playing the video. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Platform specific playback URIs | Optional for mobile; required for Google TV | Platform-specific deep links to the provider app to start playing the video. |
| Broadcaster | Optional | Free text |
| Start time | Optional | In epoch milliseconds. |
| End time | Optional | In epoch milliseconds. |
| View count | Optional | Free text, must be localized. |
| Call to action text | Optional | Free text to be displayed as a call to action. |
| Tags | Optional | List of tags associated with the entity. |
| Watch next type | Conditionally required | Must be provided when the item is in the Continuation cluster and must be one of the following four types: CONTINUE: The user has already watched more than 1 minute of this content. NEW: The user has watched all available episodes from some episodic content, but a new episode has become available and there is exactly one unwatched episode. This works for episodic content such as TV shows or recorded soccer matches in a series. NEXT: The user has watched one or more complete episodes from some episodic content, but there remains either more than one episode remaining or exactly one episode remaining where the last episode is not "NEW" and was released before the user started watching the episodic content. WATCHLIST: The user has explicitly elected to add a movie, event, or series to a watchlist to manually curate what they want to watch next. |
| Last engagement time | Conditionally required | Must be provided when the item is in the Continuation cluster. In epoch milliseconds. |
| Last playback position time | Conditionally required | Must be provided when the item is in the Continuation cluster and WatchNextType is CONTINUE. In epoch milliseconds. |

#### `VideoClipEntity`

The `VideoClipEntity` object represents a video entity coming from social media, such as TikTok or YouTube.

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** |  |
| Poster images | **Required** | At least one image is required, and must be provided with an aspect ratio. (Landscape is preferred but passing both portrait and landscape images for different scenarios is recommended.) See [Image Specifications](<https://developer.android.com/guide/playcore/engage/watch?hl=en#image-specs>) for guidance. |
| Playback uri | **Required** for mobile | The deep link to the provider app to start playing the video. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Platform specific playback URIs | Optional for mobile; required for Google TV | Platform-specific deep links to the provider app to start playing the video. |
| Created time | Optional | In epoch milliseconds. |
| Duration | **Required** | Must be a positive value in milliseconds. |
| Creator | Optional | Free text |
| Creator image | Optional | Image of the Creator avatar |
| View count | Optional | Free text, must be localized. |
| Call to action text | Optional | Free text to be displayed as a call to action. |
| Tags | Optional | List of tags associated with the entity. |
| Watch next type | Conditionally required | Must be provided when the item is in the Continuation cluster and must be one of the following four types: CONTINUE: The user has already watched more than 1 minute of this content. NEW: The user has watched all available episodes from some episodic content, but a new episode has become available and there is exactly one unwatched episode. This works for episodic content such as TV shows or recorded soccer matches in a series. NEXT: The user has watched one or more complete episodes from some episodic content, but there remains either more than one episode remaining or exactly one episode remaining where the last episode is not "NEW" and was released before the user started watching the episodic content. WATCHLIST: The user has explicitly elected to add a movie, event, or series to a watchlist to manually curate what they want to watch next. |
| Last engagement time | Conditionally required | Must be provided when the item is in the Continuation cluster. In epoch milliseconds. |
| Last playback position time | Conditionally required | Must be provided when the item is in the Continuation cluster and WatchNextType is CONTINUE. In epoch milliseconds. |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/watch).
