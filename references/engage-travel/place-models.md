#### `StoreEntity`

The `StoreEntity` object represents an individual store that developer partners want to publish, such as a popular dining place or eatery that are relevant to one's travel experience.

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Poster images | **Required** | At least one image must be provided. | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Action Uri | **Required** | Deep Link to the entity in the provider app.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Title | Optional | The name of the store. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Location | Optional | The location of the store. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Callout | Optional | Callout to feature a promo, event, or update for the store, if available. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Callout fine print | Optional | Fine print text for the callout. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Description | Optional | A description of the store. | Free text<br> **Recommended text size: under 90 chars** (Text that is too long may show ellipses) |
| Category | Optional | Category of a store, in the context of dining places, it can be cuisine like "french", "new american", "ramen", "fine dining". | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Rating - Max value | Optional | The maximum value of the rating scale.<br> **Must be provided if current value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Current value | Optional | The current value of the rating scale.<br> **Must be provided if maximum value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Count | Optional | The count of the ratings for the lodging.<br> **Note:** Provide this field if your app wants to control how this is displayed to the users. Provide the concise string that can be displayed to the user. For example, if the count is 1,000,000, consider using abbreviations like 1M, so that it won't be truncated on smaller display sizes. | String |
| Rating - Count Value | Optional | The count of the ratings for the lodging.<br> **Note:** Provide this field if you don't want to handle the display abbreviation logic yourself. If both Count and Count Value are present, we will use the Count to display to users | Long |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

#### `PointOfInterestEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Title | **Required** | Title of the entity. | String<br> **Recommended text size: Max 50 chars** |
| Poster images | Conditionally required | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9<br> **Note:** Image is required if the entity is part of recommendation cluster. If a badge is provided, ensure safe space of 24 dps at both the top and bottom of the image | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Last Engagement Time | Conditionally required | The epoch timestamp when the user last interacted with this entity.<br> **Note:** This field is required if the entity is part of continue search cluster. | Joda-Time Instant |
| Location - Country | Conditionally required | The country in which the point of interest is happening.<br> **Note:** This field is required if the entity is part of recommendation cluster. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - City | Conditionally required | The city in which the point of interest is happening.<br> **Note:** This field is required if the entity is part of recommendation cluster. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - Display Address | Conditionally required | The address that will be displayed to the user. Provide a succinct address, using abbreviations where possible (for example, "St" for "Street", "Ave" for "Avenue"). This string may be truncated depending on the user's device and settings. Include the city name for clear identification.<br> **Note:** This field is required if the entity is part of recommendation cluster. | Free text<br> **Recommended text size: max ~35 chars** |
| Location - Street Address | Optional | The street address (if applicable) of the point of interest. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - State | Optional | The state or province (if applicable) in which the point of interest is located. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - Zip code | Optional | The zip code (if applicable) of the point of interest. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - Neighborhood | Optional | The neighborhood (if applicable) of the point of interest. | Free text<br> **Recommended text size: max ~20 chars** |
| AvailabilityTimeWindow - Localized Start Time - Timestamp | Optional | The epoch timestamp when the point of interest is expected to be open/available. | Joda-Time Instant |
| AvailabilityTimeWindow - Localized Start Time - Timezone | Optional | The timezone in which the point of interest is expected to be open/available. | Joda-Time DateTimeZone<br> See [Timezone Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#tz-specs>) for guidance. |
| AvailabilityTimeWindow - Localized End Time - Timestamp | Optional | The epoch timestamp until which the point of interest is expected to be open/available. | Joda-Time Instant |
| AvailabilityTimeWindow - Localized End Time - Timezone | Optional | The timezone in which the point of interest is expected to be open/available. | Joda-Time DateTimeZone<br> See [Timezone Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#tz-specs>) for guidance. |
| Badges | Optional | Each badge is either free text (max 15 chars) or small image. |  |
| Badge - Text | Optional | Title for the badge<br> **Note:** Either text or image is required for the badge  | Free text<br> **Recommended text size: max 15 chars** |
| Badge - Image | Optional | Small image<br> Special UX treatment, for example as badge overlay on the image/video thumbnail.<br> **Note:** Either text or image is required for the badge  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Description | Optional | A single paragraph of text to describe the entity.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size for each subtitle: max 50 chars** |
| Rating - Max value | Optional | The maximum value of the rating scale.<br> **Must be provided if current value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Current value | Optional | The current value of the rating scale.<br> **Must be provided if maximum value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Count | Optional | The count of the ratings for the point of interest.<br> **Note:** Provide this field if your app wants to control how this is displayed to the users. Provide the concise string that can be displayed to the user. For example, if the count is 1,000,000, consider using abbreviations like 1M, so that it won't be truncated on smaller display sizes. | String |
| Rating - Count Value | Optional | The count of the ratings for the point of interest.<br> **Note:** Provide this field if you don't want to handle the display abbreviation logic yourself. If both Count and Count Value are present, we will use the Count to display to users | Long |
| Price - CurrentPrice | Conditionally required | The current price of the tickets/entry pass for the point of interest. <br> **Must be provided if strikethrough price is provided.**  | Free text |
| Price - StrikethroughPrice | Optional | The original price of the tickets/entry pass for the point of interest. | Free text |
| Price Callout | Optional | Price callout to feature a promo, event, member discount, if available. | Free text<br> **Recommended text size: under 45 chars (Text that is too long may show ellipses)**  |
| Content Categories | Optional | Describe the category of the content in the entity. | List of Eligible Enums<br> TYPE_TRAVEL_AND_LOCAL<br> TYPE_MOVIES_AND_TV_SHOWS (Example - theater)<br> TYPE_MEDICAL (Example - hospital)<br> TYPE_EDUCATION (Example - school)<br> TYPE_SPORTS (Example - stadium)<br> <br> See the [Content Category section](<https://developer.android.com/guide/playcore/engage/travel?hl=en#content-category>) for guidance. |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/travel).
