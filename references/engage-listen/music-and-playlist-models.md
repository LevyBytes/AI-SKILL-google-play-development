#### `MusicTrackEntity`

The `MusicTrackEntity` object represents a music track (for example, *Yellow* by Coldplay).

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** | Title of the music track. |
| Poster images | **Required** | At least one image must be provided. See [Image Specifications](<https://developer.android.com/guide/playcore/engage/listen?hl=en#image-specs>) for guidance. |
| Playback uri | **Required** | A deep link that starts playing the music track in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Artists | **Required** | List of artists for the music track. |
| Info page uri | Optional | A deep link to the provider app for details about the music track. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Description | Optional | Must be within 200 characters if provided. |
| Duration | Optional | The duration of the track in milliseconds. |
| Album | Optional | The name of the album to which the song belongs. |
| Downloaded on Device | Optional | Boolean indicating if the music track is downloaded on device. |
| Explicit | Optional | A boolean indicating if the content is explicit or not Items that contain explicit material or have a parental advisory warning should be set to TRUE. Explicit items appears with an "E" tag. |
| Last engagement time | Optional | Recommended for items in the Continuation Cluster. May be used for ranking. In epoch milliseconds |
| Progress percentage complete | Optional | Recommended for items in the Continuation Cluster. Integer between 0 and 100 |

#### `MusicVideoEntity`

The `MusicVideoEntity` object represents a music video (for example, *The Weeknd - Take My Breath (Official Music Video)*).

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** | Title of the music video. |
| Poster images | **Required** | At least one image must be provided. See [Image Specifications](<https://developer.android.com/guide/playcore/engage/listen?hl=en#image-specs>) for guidance. |
| Playback uri | **Required** | A deep link that starts playing the music video in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Info page uri | Optional | A deep link to the provider app for details about the music video. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Duration | Optional | The duration of the video in milliseconds. |
| View count | Optional | The number of views on the video in free text format. |
| Artists | Optional | List of artists of the music video. |
| Content rating | Optional | List of content ratings of the track. |
| Description | Optional | Must be within 200 characters if provided. |
| Downloaded on Device | Optional | Boolean indicating if the music video is downloaded on device. |
| Explicit | Optional | A boolean indicating if the content is explicit or not Items that contain explicit material or have a parental advisory warning should be set to TRUE. Explicit items appears with an "E" tag. |
| Last engagement time | Optional | Recommended for items in the Continuation Cluster. May be used for ranking. In epoch milliseconds |
| Progress percentage complete | Optional | Recommended for items in the Continuation Cluster. Integer between 0 and 100 |

#### `PlaylistEntity`

The `PlaylistEntity` object represents a music playlist (for example, the US Top 10 Playlist).

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** | Title of the playlist. |
| Poster images | **Required** | At least one image must be provided. See [Image Specifications](<https://developer.android.com/guide/playcore/engage/listen?hl=en#image-specs>) for guidance. |
| Playback uri | **Required** | A deep link that starts playing the music playlist in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Info page uri | Optional | A deep link to the provider app for details about the music playlist. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Duration | Optional | The duration of the playlist in milliseconds. |
| Songs count | Optional | The number of songs in the music playlist. |
| Description | Optional | Must be within 200 characters if provided. |
| Downloaded on Device | Optional | Boolean indicating if the playlist is downloaded on device. |
| Explicit | Optional | A boolean indicating if the content is explicit or not Items that contain explicit material or have a parental advisory warning should be set to TRUE. Explicit items appears with an "E" tag. |
| Last engagement time | Optional | Recommended for items in the Continuation Cluster. May be used for ranking. In epoch milliseconds |
| Progress percentage complete | Optional | Recommended for items in the Continuation Cluster. Integer between 0 and 100 |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/listen).
