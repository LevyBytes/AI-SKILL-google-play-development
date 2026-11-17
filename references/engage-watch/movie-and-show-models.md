### Step 1: Provide entity data

The SDK has defined different entities to represent each item type. We support the following entities for the Watch category:

1. [`MovieEntity`](<https://developer.android.com/guide/playcore/engage/watch?hl=en#movieentity>)
2. [`TvShowEntity`](<https://developer.android.com/guide/playcore/engage/watch?hl=en#tvshowentity>)
3. [`TvSeasonEntity`](<https://developer.android.com/guide/playcore/engage/watch?hl=en#tvseasonentity>)
4. [`TvEpisodeEntity`](<https://developer.android.com/guide/playcore/engage/watch?hl=en#tvepisodeentity>)
5. [`LiveStreamingVideoEntity`](<https://developer.android.com/guide/playcore/engage/watch?hl=en#livestreamingvideoentity>)
6. [`VideoClipEntity`](<https://developer.android.com/guide/playcore/engage/watch?hl=en#videoclipentity>)

The following chart outlines attributes and requirements for each type.

#### `MovieEntity`

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** |  |
| Poster images | **Required** | At least one image is required, and must be provided with an aspect ratio. (Landscape is preferred but passing both portrait and landscape images for different scenarios is recommended.) See [Image Specifications](<https://developer.android.com/guide/playcore/engage/watch?hl=en#image-specs>) for guidance. |
| Playback uri | **Required** for mobile | The deep link to the provider app to start playing the movie. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Platform specific playback URIs | Optional for mobile; required for Google TV | Platform-specific deep links to the provider app to start playing the movie. |
| Info page uri | Optional | The deep link to the provider app to show details about the movie. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Release date | Optional | In epoch milliseconds. |
| Availability | Optional | AVAILABLE: The content is available to the user without any further action. FREE_WITH_SUBSCRIPTION: The content is available after the user purchases a subscription. PAID_CONTENT: The content requires user purchase or rental. PURCHASED: The content has been purchased or rented by the user. |
| Offer price | Optional | Free text |
| Duration | **Required** | In milliseconds. |
| Genre | Optional | Free text |
| Content ratings | Optional | Free text, follow the industry standard. ([Example](<https://www.spectrum.net/support/tv/tv-and-movie-ratings-descriptions>)) |
| Call to action text | Optional | Free text to be displayed as a call to action. |
| Tags | Optional | List of tags associated with the entity. |
| Watch next type | Conditionally required | Must be provided when the item is in the Continuation cluster and must be one of the following four types: CONTINUE: The user has already watched more than 1 minute of this content. NEW: The user has watched all available episodes from some episodic content, but a new episode has become available and there is exactly one unwatched episode. This works for episodic content such as TV shows or recorded soccer matches in a series. NEXT: The user has watched one or more complete episodes from some episodic content, but there remains either more than one episode remaining or exactly one episode remaining where the last episode is not "NEW" and was released before the user started watching the episodic content. WATCHLIST: The user has explicitly elected to add a movie, event, or series to a watchlist to manually curate what they want to watch next. |
| Last engagement time | Conditionally required | Must be provided when the item is in the Continuation cluster. In epoch milliseconds. |
| Last playback position time | Conditionally required | Must be provided when the item is in the Continuation cluster and WatchNextType is CONTINUE. In epoch milliseconds. |

#### `TvShowEntity`

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** |  |
| Poster images | **Required** | At least one image is required, and must be provided with an aspect ratio. (Landscape is preferred but passing both portrait and landscape images for different scenarios is recommended.) See [Image Specifications](<https://developer.android.com/guide/playcore/engage/watch?hl=en#image-specs>) for guidance. |
| Info page uri | **Required** | The deep link to the provider app to show the details of the TV show. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Playback uri | Optional | The deep link to the provider app to start playing the TV show. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Platform specific playback URIs | Optional for mobile; required for Google TV | Platform-specific deep links to the provider app to start playing the TV show. |
| First episode air date | Optional | In epoch milliseconds. |
| Latest episode air date | Optional | In epoch milliseconds. |
| Availability | Optional | AVAILABLE: The content is available to the user without any further action. FREE_WITH_SUBSCRIPTION: The content is available after the user purchases a subscription. PAID_CONTENT: The content requires user purchase or rental. PURCHASED: The content has been purchased or rented by the user. |
| Offer price | Optional | Free text |
| Season count | Optional | Positive integer |
| Genre | Optional | Free text |
| Content ratings | Optional | Free text, follow the industry standard. ([Example](<https://www.spectrum.net/support/tv/tv-and-movie-ratings-descriptions>)) |
| Call to action text | Optional | Free text to be displayed as a call to action. |
| Tags | Optional | List of tags associated with the entity. |
| Watch next type | Conditionally required | Must be provided when the item is in the Continuation cluster and must be one of the following four types: CONTINUE: The user has already watched more than 1 minute of this content. NEW: The user has watched all available episodes from some episodic content, but a new episode has become available and there is exactly one unwatched episode. This works for episodic content such as TV shows or recorded soccer matches in a series. NEXT: The user has watched one or more complete episodes from some episodic content, but there remains either more than one episode remaining or exactly one episode remaining where the last episode is not "NEW" and was released before the user started watching the episodic content. WATCHLIST: The user has explicitly elected to add a movie, event, or series to a watchlist to manually curate what they want to watch next. |
| Last engagement time | Conditionally required | Must be provided when the item is in the Continuation cluster. In epoch milliseconds. |
| Last playback position time | Conditionally required | Must be provided when the item is in the Continuation cluster and WatchNextType is CONTINUE. In epoch milliseconds. |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/watch).
