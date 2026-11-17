#### `GenericFeaturedEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) | Uri |
| Poster images | **Required** | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9 **Note:** If a badge is provided, ensure safe space of 24 dps at both the top and bottom of the image | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Title | Optional | Title of the entity. | Free text **Recommended text size: 50 chars** |
| Description | Optional | A single paragraph of text to describe the entity. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size for each subtitle: max 50 chars** |
| Badges | Optional | Each badge is either free text (max 15 chars) or small image. Special UX treatment on top of image/video, for example, as badge overlay on the image "Live update" Article read duration |  |
| Badge - Text | Optional | Title for the badge **Note:** Either text or image is required for the badge | Free text **Recommended text size: max 15 chars** |
| Badge - Image | Optional | Small image Special UX treatment, for example as badge overlay on the image/video thumbnail. **Note:** Either text or image is required for the badge | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Content Categories | Optional | Describe the category of the content in the entity. | List of Enums See the [Content Category section](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#content-category>) for guidance. |

#### `ArticleEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) | Uri |
| Title | **Required** | Title of the entity. | Free text **Recommended text size: Max 50 chars** |
| Poster images | Optional | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9 **Note:** Image is highly recommended. If a badge is provided, ensure safe space of 24 dps at both the top and bottom of the image | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Source - Title | Optional | The name of the author, organization, or reporter | Free text **Recommended text size: Under 25 chars** |
| Source - Image | Optional | An image of the source like the author, the organization, reporter | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Description | Optional | A single paragraph of text to describe the entity. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size for each subtitle: max 50 chars** |
| Badges | Optional | Each badge is either free text (max 15 chars) or small image. Special UX treatment on top of image/video, for example as badge overlay on the image "Live update" Article read duration |  |
| Badge - Text | Optional | Title for the badge **Note:** Either text or image is required for the badge | Free text **Recommended text size: max 15 chars** |
| Badge - Image | Optional | Small image Special UX treatment, for example as badge overlay on the image/video thumbnail. **Note:** Either text or image is required for the badge | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Content Publish Time | Optional | This is the epoch timestamp in milliseconds on when the content was published / updated in the app. | Epoch timestamp in milliseconds |
| Last Engagement Time | Conditionally Required | The epoch timestamp in milliseconds when the user interacted with this entity last time. **Note:** This field is required if this entity is part of the continuation cluster. | Epoch timestamp in milliseconds |
| Progress Percentage | Conditionally Required | The percentage of the full content consumed by the user to date. **Note:** This field is required if this entity is part of the continuation cluster. | An int value between 0~100 inclusive. |
| Content Categories | Optional | Describe the category of the content in the entity. | List of Enums See the [Content Category section](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#content-category>) for guidance. |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/otherverticals).
