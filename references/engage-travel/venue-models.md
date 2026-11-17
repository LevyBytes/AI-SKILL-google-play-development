#### `EventEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Title | **Required** | Title of the entity. | String<br> **Recommended text size: Max 50 chars** |
| Localized Start time - Timestamp | **Required** | The epoch timestamp when the event is expected to start. | Joda-Time Instant |
| Localized Start time - Timezone | **Required** | The timezone in which the event is expected to start. | Joda-Time DateTimeZone<br> See [Timezone Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#tz-specs>) for guidance. |
| Event mode | **Required** | A field to indicate whether the event will be virtual, in-person or both. | Enum: VIRTUAL, IN_PERSON, or HYBRID |
| Poster images | **Required** | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9<br> **Note:** Image is highly recommended. If a badge is provided, ensure safe space of 24 dps at both the top and bottom of the image | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Location - Country | Conditionally required | The country in which the event is happening.<br> **Note:** This is required for events which are IN_PERSON or HYBRID | Free text<br> **Recommended text size: max ~20 chars** |
| Location - City | Conditionally required | The city in which the event is happening.<br> **Note:** This is required for events which are IN_PERSON or HYBRID | Free text<br> **Recommended text size: max ~20 chars** |
| Location - Display Address | Conditionally required | The address or venue name where the event will take place that should be displayed to the user.<br> **Note:** This is required for events which are IN_PERSON or HYBRID | Free text<br> **Recommended text size: max ~20 chars** |
| Location - Street Address | Optional | The street address (if applicable) of the location at which event is being hosted. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - State | Optional | The state or province (if applicable) in which the event is being hosted. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - Zip code | Optional | The zip code (if applicable) of the location in which the event is being hosted. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - Neighborhood | Optional | The neighborhood (if applicable) in which the event is being hosted. | Free text<br> **Recommended text size: max ~20 chars** |
| End time | Optional | The epoch timestamp when the event is expected to end.<br> **Note:**This will be represented in milliseconds. | Epoch timestamp in milliseconds |
| Description | Optional | A single paragraph of text to describe the entity.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size for each subtitle: max 50 chars** |
| Badges | Optional | Each badge is either free text (max 15 chars) or small image. |  |
| Badge - Text | Optional | Title for the badge<br> **Note:** Either text or image is required for the badge  | Free text<br> **Recommended text size: max 15 chars** |
| Badge - Image | Optional | Small image<br> Special UX treatment, for example as badge overlay on the image/video thumbnail.<br> **Note:** Either text or image is required for the badge  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Price - CurrentPrice | Conditionally required | The current price of the ticket/pass for the event.<br> **Must be provided if strikethrough price is provided.**  | Free text |
| Price - StrikethroughPrice | Optional | The original price of the ticket/pass for the event. | Free text |
| Price Callout | Optional | Price callout to feature a promo, event, member discount, if available. | Free text<br> **Recommended text size: under 45 chars (Text that is too long may show ellipses)** |
| Content Categories | Optional | Describe the category of the content in the entity. | List of Eligible Enums<br> TYPE_MOVIES_AND_TV_SHOWS (Example - Cinema)<br> TYPE_DIGITAL_GAMES (Example - eSports)<br> TYPE_MUSIC (Example - Concert)<br> TYPE_TRAVEL_AND_LOCAL (Example - Tour, festival)<br> TYPE_HEALTH_AND_FITENESS (Example - Yoga class)<br> TYPE_EDUCATION (Example - Class)<br> TYPE_SPORTS (Example - Football game)<br> TYPE_DATING (Example - meetup)<br> <br> See the [Content Category section](<https://developer.android.com/guide/playcore/engage/travel?hl=en#content-category>) for guidance. |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

#### `LodgingEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Title | **Required** | Title of the entity. | String<br> **Recommended text size: Max 50 chars** |
| Poster images | **Required** | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9 <br> **Note:** If a badge is provided, ensure safe space of 24 dps at both the top and bottom of the image  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Location - Country | **Required** | The country in which the lodging is happening. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - City | **Required** | The city in which the lodging is happening. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - Display Address | **Required** | The address that will be displayed to the user. We recommend including the city name and possibly state or country for most use cases. Only include the street address or neighborhood if the user is near the location, the user is familiar with the location, or the city is included in the cluster title. If you include the street address, provide a succinct address, using abbreviations where possible (for example, "St" for "Street", "Ave" for "Avenue"). | Free text<br> **Recommended text size: max ~20 chars** |
| Location - Street Address | Optional | The street address (if applicable) of the lodging. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - State | Optional | The state or province (if applicable) in which the lodging is located. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - Zip code | Optional | The zip code (if applicable) of the lodging. | Free text<br> **Recommended text size: max ~20 chars** |
| Location - Neighborhood | Optional | The neighborhood (if applicable) of the lodging. | Free text<br> **Recommended text size: max ~20 chars** |
| Badges | Optional | Each badge is either free text (max 15 chars) or small image. |  |
| Badge - Text | Optional | Title for the badge<br> **Note:** Either text or image is required for the badge  | Free text<br> **Recommended text size: max 15 chars** |
| Badge - Image | Optional | Small image<br> Special UX treatment, for example as badge overlay on the image/video thumbnail.<br> **Note:** Either text or image is required for the badge  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Description | Optional | A single paragraph of text to describe the entity.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size for each subtitle: max 50 chars** |
| AvailabilityTimeWindow - Localized Start Time - Timestamp | Optional | The epoch timestamp when the lodging is expected to be open/available. | Joda-Time Instant |
| AvailabilityTimeWindow - Localized Start Time - Timezone | Optional | The timezone in which the lodging is expected to be open/available. | Joda-Time DateTimeZone<br> See [Timezone Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#tz-specs>) for guidance. |
| AvailabilityTimeWindow - Localized End Time - Timestamp | Optional | The epoch timestamp until which the lodging is expected to be open/available. | Joda-Time Instant |
| AvailabilityTimeWindow - Localized End Time - Timezone | Optional | The timezone in which the lodging is expected to be open/available. | Joda-Time DateTimeZone<br> See [Timezone Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#tz-specs>) for guidance. |
| Rating - Max value | Optional | The maximum value of the rating scale.<br> **Must be provided if current value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Current value | Optional | The current value of the rating scale.<br> **Must be provided if maximum value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Count | Optional | The count of the ratings for the lodging.<br> **Note:** Provide this field if your app wants to control how this is displayed to the users. Provide the concise string that can be displayed to the user. For example, if the count is 1,000,000, consider using abbreviations like 1M, so that it won't be truncated on smaller display sizes. | String |
| Rating - Count Value | Optional | The count of the ratings for the lodging.<br> **Note:** Provide this field if you don't want to handle the display abbreviation logic yourself. If both Count and Count Value are present, we will use the Count to display to users | Long |
| Price - CurrentPrice | Conditionally required | The current price of the lodging.<br> **Must be provided if strikethrough price is provided.**  | Free text |
| Price - StrikethroughPrice | Optional | The original price of the lodging, which is be struck-through in the UI. | Free text |
| Price Callout | Optional | Price callout to feature a promo, event, member discount, if available. | Free text<br> **Recommended text size: under 45 chars (Text that is too long may show ellipses)** |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/travel).
