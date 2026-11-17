#### `PersonEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) | Uri |
| Profile - Name | **Required** | Profile name or id or handle, eg "John Doe", "@TeamPixel", etc. | String **Recommended text size: Max 50 chars** |
| Profile - Avatar | **Required** | Profile picture or avatar image of the user. **Note:**Must be Square 1:1 image. | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Profile - Additional Text | Optional | Free text like the profile handle. | Free text **Recommended text size: Max 15 chars** |
| Profile - Additional Image | Optional | Small image like a verified badge. | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Header image | Optional | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9 **Note:** Image is highly recommended. If a badge is provided, ensure safe space of 24 dps at both the top and bottom of the image | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Popularity - Count | Optional | Indicate the number of followers or popularity value, for example - "3.7 M". **Note:** If both Count and Count Value are provided, Count will be used | String **Recommended text size: max 20 chars for count + label combined** |
| Popularity - Count Value | Optional | The number of followers or popularity value. **Note:** Provide Count Value if your app doesn't want to handle logic on how a large number should be optimized for different display sizes. If both Count and Count Value are provided, Count will be used. | Long |
| Popularity - Label | Optional | Indicate what the popularity label is. For example - "Likes". | String **Recommended text size: Max 20 chars for count + label combined** |
| Popularity - Visual | Optional | Indicate what the interaction is for. For example - Image showing Likes icon, emoji. Can provide more than 1 image, though not all may not be shown on all form factors. **Note:** Must be Square 1:1 image | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Rating - Max value | Required | The maximum value of the rating scale. **Must be provided if current value of rating is also provided.** | Number >= 0.0 |
| Rating - Current value | Required | The current value of the rating scale. **Must be provided if maximum value of rating is also provided.** | Number >= 0.0 |
| Rating - Count | Optional | The count of the ratings for the entity. **Note:** Provide this field if your app wants to control how this is displayed to the users. Provide the concise string that can be displayed to the user. For example, if the count is 1,000,000, consider using abbreviations like 1M, so that it won't be truncated on smaller display sizes. | String |
| Rating - Count Value | Optional | The count of the ratings for the entity. **Note:** Provide this field if you don't want to handle the display abbreviation logic yourself. If both Count and Count Value are present, we will use the Count to display to users | Long |
| Location - Country | Optional | The country where the person is located or serving. | Free text **Recommended text size: max ~20 chars** |
| Location - City | Optional | The city where the person is located or serving. | Free text **Recommended text size: max ~20 chars** |
| Location - Display Address | Optional | The address where the person is located or serving will be displayed to the user. | Free text **Recommended text size: max ~20 chars** |
| Location - Street Address | Optional | The street address (if applicable) where the person is located or serving. | Free text **Recommended text size: max ~20 chars** |
| Location - State | Optional | The state (if applicable) where the person is located or serving. | Free text **Recommended text size: max ~20 chars** |
| Location - Zip code | Optional | The zip code (if applicable) where the person is located or serving. | Free text **Recommended text size: max ~20 chars** |
| Location - Neighborhood | Optional | The neighborhood (if applicable) where the person is located or serving. | Free text **Recommended text size: max ~20 chars** |
| Badges | Optional | Each badge is either free text (max 15 chars) or small image. |  |
| Badge - Text | Optional | Title for the badge **Note:** Either text or image is required for the badge | Free text **Recommended text size: max 15 chars** |
| Badge - Image | Optional | Small image Special UX treatment, for example as badge overlay on the image/video thumbnail. **Note:** Either text or image is required for the badge | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Description | Optional | A single paragraph of text to describe the entity. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size for each subtitle: max 50 chars** |
| Content Categories | Optional | Describe the category of the content in the entity. | List of Eligible Enums TYPE_HEALTH_AND_FITENESS (Example - Yoga/fitness trainer) TYPE_HOME_AND_AUTO (Example - Plumber) TYPE_SPORTS (Example - Player) TYPE_DATING See the [Content Category section](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#content-category>) for guidance. |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/otherverticals).
