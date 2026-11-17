### Step 1: Provide entity data

The SDK has defined different entities to represent each item type. We support the following entities for the Listen category:

1. `MusicAlbumEntity`
2. `MusicArtistEntity`
3. `MusicTrackEntity`
4. `MusicVideoEntity`
5. `PlaylistEntity`
6. `PodcastSeriesEntity`
7. `PodcastEpisodeEntity`
8. `LiveRadioStationEntity`
9. `AudiobookEntity`

The following charts outline available attributes and requirements for each type.

#### `MusicAlbumEntity`

The `MusicAlbumEntity` object represents a music album (for example, *Midnights* by Taylor Swift).

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** | The title of the music album. |
| Poster images | **Required** | At least one image must be provided. See [Image Specifications](<https://developer.android.com/guide/playcore/engage/listen?hl=en#image-specs>) for guidance. |
| Info page uri | **Required** | The deep link to the provider app for details about the music album. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Artists | **Required** | List of artists in the music album. |
| Playback uri | Optional | A deep link that starts playing the album in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Description | Optional | Must be within 200 characters if provided. |
| Songs count | Optional | The number of songs in the music album. |
| Genres | Optional | List of genres in the music album. |
| Album Format | Optional | ALBUM (includes LP and double LP) EP SINGLE Mixtape |
| Music labels | Optional | List of music labels associated with the album. |
| Downloaded on Device | Optional | Boolean indicating if the music album is downloaded on device. |
| Explicit | Optional | A boolean indicating if the content is explicit or not Items that contain explicit material or have a parental advisory warning should be set to TRUE. Explicit items appears with an "E" tag. |
| Release date | Optional | The release date of the album in epoch milliseconds. |
| Duration | Optional | The duration of the album in milliseconds. |
| Last engagement time | Optional | Recommended for items in the Continuation Cluster. May be used for ranking. In epoch milliseconds |
| Progress percentage complete | Optional | Recommended for items in the Continuation Cluster. Integer between 0 and 100 |

#### `MusicArtistEntity`

The `MusicArtistEntity` object represents a music arist (for example, Adele).

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** | Name of the music artist. |
| Poster images | **Required** | At least one image must be provided. See [Image Specifications](<https://developer.android.com/guide/playcore/engage/listen?hl=en#image-specs>) for guidance. |
| Info page uri | **Required** | The deep link to the provider app for details about the music artist. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Playback uri | Optional | The deep link which starts playing the artist's songs in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) |
| Description | Optional | Must be within 200 characters if provided. |
| Last engagement time | Optional | Recommended for items in the Continuation Cluster. May be used for ranking. In epoch milliseconds |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/listen).
