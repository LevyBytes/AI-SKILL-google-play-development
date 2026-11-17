#### `PodcastSeriesEntity`

The `PodcastSeriesEntity` object represents a podcast series (for example, *This American Life*).

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** | Title of the podcast series. |
| Poster images | **Required** | At least one image must be provided. See [Image Specifications](<https://developer.android.com/guide/playcore/engage/listen?hl=en#image-specs>) for guidance. |
| Info page uri | **Required** | A deep link to the provider app for details about the podcast series. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Playback uri | Optional | A deep link that starts playing the podcast series in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Episode count | Optional | The number of episodes in the podcast series. |
| Production name | Optional | The name of the production of the podcast series. |
| Hosts | Optional | List of hosts of the podcast series. |
| Genres | Optional | List of genres of the podcast series. |
| Downloaded on device | Optional | Boolean indicating if the podcast is downloaded on the device. |
| Description | Optional | Must be within 200 characters if provided. |
| Explicit | Optional | A boolean indicating if the content is explicit or not Items that contain explicit material or have a parental advisory warning should be set to TRUE. Explicit items appears with an "E" tag. |
| Last engagement time | Optional | Recommended for items in the Continuation Cluster. May be used for ranking. In epoch milliseconds |

#### `PodcastEpisodeEntity`

The `PodcastEpisodeEntity` object represents a podcast series (for example, *Spark Bird, Episode 754: This American Life*).

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** | Title of the podcast episode. |
| Poster images | **Required** | At least one image must be provided. See [Image Specifications](<https://developer.android.com/guide/playcore/engage/listen?hl=en#image-specs>) for guidance. |
| Playback uri | **Required** | A deep link that starts playing the podcast episode in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Podcast series title | **Required** | The name of the podcast series to which the episode belongs. |
| Duration | **Required** | The duration of the podcast episode in milliseconds. |
| Publish Date | **Required** | Publish date of the podcast (in epoch milliseconds) |
| Info page uri | Optional | A deep link to the provider app for details about the podcast episode. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Production name | Optional | The name of the production of the podcast series. |
| Episode index | Optional | The index of the episode in the series (first index is 1). |
| Hosts | Optional | List of hosts of the podcast episode. |
| Genres | Optional | List of genres of the podcast episode. |
| Downloaded on device | Optional | Boolean indicating if the podcast episode is downloaded on the device. |
| Description | Optional | Must be within 200 characters if provided. |
| Video Podcast | Optional | Boolean indicating if the podcast episode has video content |
| Explicit | Optional | A boolean indicating if the content is explicit or not Items that contain explicit material or have a parental advisory warning should be set to TRUE. Explicit items appears with an "E" tag. |
| Listen Next Type | Optional | Recommended for Items in the Continuation Cluster TYPE_CONTINUE - Resume on a unfinished audio item. TYPE_NEXT - Continue on a new one of a series. TYPE_NEW - Newly released. |
| Last engagement time | Optional | Recommended for items in the Continuation Cluster. May be used for ranking. In epoch milliseconds |
| Progress percentage complete | Optional | Recommended for items in the Continuation Cluster. Integer between 0 and 100 |

#### `LiveRadioStationEntity`

The `LiveRadioStationEntity` object represents a live radio station (for example, 98.1 The Breeze).

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** | Title of the live radio station. |
| Poster images | **Required** | At least one image must be provided. See [Image Specifications](<https://developer.android.com/guide/playcore/engage/listen?hl=en#image-specs>) for guidance. |
| Playback uri | **Required** | A deep link that starts playing the radio station in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Info page uri | Optional | A deep link to the provider app for details about the radio station. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Frequency | Optional | The frequency at which the radio station is broadcasted (for example, "98.1 FM"). |
| Show title | Optional | The current show that is playing on the radio station. |
| Hosts | Optional | List of hosts of the radio station. |
| Description | Optional | Must be within 200 characters if provided. |
| Last engagement time | Optional | Recommended for items in the Continuation Cluster. May be used for ranking. In epoch milliseconds |

#### `AudiobookEntity`

The `AudiobookEntity` object represents an audiobook (for example, the audiobook of *Becoming* by Michelle Obama).

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** |  |
| Poster images | **Required** | At least one image must be provided. See [Image Specifications](<https://developer.android.com/guide/playcore/engage/listen?hl=en#image-specs>) for guidance. |
| Author | **Required** | At least one author name must be provided. |
| Action link uri | **Required** | The deep link to the provider app for the audiobook.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  |
| Narrator | Optional | At least one narrator's name must be provided. |
| Publish date | Optional | In epoch milliseconds if provided. |
| Description | Optional | Must be within 200 characters if provided. |
| Price | Optional | Free text |
| Duration | Optional | Must be a positive value if provided. |
| Genre | Optional | List of genres associated with the book. |
| Series name | Optional | Name of the series that the audiobook belongs to (for example, *Harry Potter*. |
| Series unit index | Optional | The index of the audiobook in the series, where 1 is the first audiobook in the series. For example, if *Harry Potter and the Prisoner of Azkaban* is the 3rd book in the series, this should be set to 3. |
| Continue book type | Optional | TYPE_CONTINUE - Resume on a unfinished book.<br> TYPE_NEXT - Continue on a new one of a series.<br> TYPE_NEW - Newly released. |
| Last Engagement Time | Conditionally required | Must be provided when the item is in the Continuation cluster.<br> In epoch milliseconds. |
| Progress Percentage Complete | Conditionally required | Must be provided when the item is in the Continuation cluster.<br> *Newly* acquired audiobooks can be a part of the continue reading cluster. <br> Value must be greater than 0 and less than 100. |
| **DisplayTimeWindow - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface.<br> In epoch milliseconds. |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface.<br> In epoch milliseconds. |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/listen).
