### Step 1: Provide entity data

The SDK has defined different entities to represent each item type. We support the following entities for the Travel & Events category:

1. `GenericFeaturedEntity`
2. `ArticleEntity`
3. `EventEntity`
4. `LodgingEntity`
5. `StoreEntity`
6. `PointOfInterestEntity`
7. `RestaurantReservationEntity`
8. `EventReservationEntity`
9. `LodgingReservationEntity`
10. `TransportationReservationEntity`
11. `VehicleRentalReservationEntity`

The following charts outline available attributes and requirements for each type.

#### `GenericFeaturedEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Poster images | **Required** | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9<br> **Note:** If a badge is provided, ensure safe space of 24 dps at both the top and bottom of the image | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Title | Optional | Title of the entity. | Free text<br> **Recommended text size: 50 chars** |
| Description | Optional | A single paragraph of text to describe the entity.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size for each subtitle: max 50 chars** |
| Badges | Optional | Each badge is either free text (max 15 chars) or small image.<br> Special UX treatment on top of image/video, For example, as badge overlay on the image<br> "Live update"<br> Article read duration<br>  |  |
| Badge - Text | Optional | Title for the badge<br> **Note:** Either text or image is required for the badge  | Free text<br> **Recommended text size: max 15 chars** |
| Badge - Image | Optional | Small image<br> Special UX treatment, for example as badge overlay on the image/video thumbnail.<br> **Note:** Either text or image is required for the badge  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Content Categories | Optional | Describe the category of the content in the entity. | List of Enums<br> See the [Content Category section](<https://developer.android.com/guide/playcore/engage/travel?hl=en#content-category>) for guidance. |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

#### `ArticleEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Title | **Required** | Title of the entity. | Free text<br> **Recommended text size: Max 50 chars** |
| Poster images | Optional | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9<br> **Note:** Image is highly recommended. If a badge is provided, ensure safe space of 24 dps at both the top and bottom of the image | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Source - Title | Optional | The name of the author, organization, or reporter | Free text<br> **Recommended text size: Under 25 chars** |
| Source - Image | Optional | An image of the source like the author, the organization, reporter | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Description | Optional | A single paragraph of text to describe the entity.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size for each subtitle: max 50 chars** |
| Badges | Optional | Each badge is either free text (max 15 chars) or small image.<br> Special UX treatment on top of image/video, for example, as badge overlay on the image<br> "Live update"<br> Article read duration<br>  |  |
| Badge - Text | Optional | Title for the badge<br> **Note:** Either text or image is required for the badge  | Free text<br> **Recommended text size: max 15 chars** |
| Badge - Image | Optional | Small image<br> Special UX treatment, for example as badge overlay on the image/video thumbnail.<br> **Note:** Either text or image is required for the badge  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Content Publish Time | Optional | This is the epoch timestamp in milliseconds on when the content was published / updated in the app. | Epoch timestamp in milliseconds |
| Last Engagement Time | Optional | The epoch timestamp in milliseconds when the user interacted with this entity last time.  | Epoch timestamp in milliseconds |
| Progress Percentage | Optional | The percentage of the full content consumed by the user to date. | An int value between 0~100 inclusive. |
| Content Categories | Optional | Describe the category of the content in the entity. | List of Enums<br> See the [Content Category section](<https://developer.android.com/guide/playcore/engage/travel?hl=en#content-category>) for guidance. |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/travel).
