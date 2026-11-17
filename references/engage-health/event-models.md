#### `EventEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) | Uri |
| Title | **Required** | Title of the entity. | String **Recommended text size: Max 50 chars** |
| Start time | **Required** | The epoch timestamp when the event is expected to start. **Note:**This will be represented in milliseconds. | Epoch timestamp in milliseconds |
| Event mode | **Required** | A field to indicate whether the event will be virtual, in-person or both. | Enum: VIRTUAL, IN_PERSON, or HYBRID |
| Poster images | **Required** | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9 **Note:** Image is highly recommended. If a badge is provided, please ensure safe space of 24 dps at both the top and bottom of the image | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/healthandfitness?hl=en#image-specs>) for guidance. |
| Location - Country | Conditionally Required | The country in which the event is happening. **Note:** This is required for events which are IN_PERSON or HYBRID | Free text **Recommended text size: max ~20 chars** |
| Location - City | Conditionally Required | The city in which the event is happening. **Note:** This is required for events which are IN_PERSON or HYBRID | Free text **Recommended text size: max ~20 chars** |
| Location - Display Address | Conditionally Required | The address or venue name where the event will take place that should be displayed to the user. **Note:** This is required for events which are IN_PERSON or HYBRID | Free text **Recommended text size: max ~20 chars** |
| Location - Street Address | Optional | The street address (if applicable) of the location at which event is being hosted. | Free text **Recommended text size: max ~20 chars** |
| Location - State | Optional | The state or province (if applicable) in which the event is being hosted. | Free text **Recommended text size: max ~20 chars** |
| Location - Zip code | Optional | The zip code (if applicable) of the location in which the event is being hosted. | Free text **Recommended text size: max ~20 chars** |
| Location - Neighborhood | Optional | The neighborhood (if applicable) in which the event is being hosted. | Free text **Recommended text size: max ~20 chars** |
| End time | Optional | The epoch timestamp when the event is expected to end. **Note:**This will be represented in milliseconds. | Epoch timestamp in milliseconds |
| Description | Optional | A single paragraph of text to describe the entity. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size for each subtitle: max 50 chars** |
| Badges | Optional | Each badge is either free text (max 15 chars) or small image. |  |
| Badge - Text | Optional | Title for the badge **Note:** Either text or image is required for the badge | Free text **Recommended text size: max 15 chars** |
| Badge - Image | Optional | Small image Special UX treatment, for example as badge overlay on the image/video thumbnail. **Note:** Either text or image is required for the badge | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/healthandfitness?hl=en#image-specs>) for guidance. |
| Price - CurrentPrice | Conditionally required | The current price of the ticket/pass for the event. **Must be provided if strikethrough price is provided.** | Free text |
| Price - StrikethroughPrice | Optional | The original price of the ticket/pass for the event. | Free text |
| Price Callout | Optional | Price callout to feature a promo, event, member discount, if available. | Free text **Recommended text size: under 45 chars (Text that is too long may show ellipses)** |
| Content Categories | Optional | Describe the category of the content in the entity. | List of Eligible Enums TYPE_MOVIES_AND_TV_SHOWS (Example - Cinema) TYPE_DIGITAL_GAMES (Example - eSports) TYPE_MUSIC (Example - Concert) TYPE_TRAVEL_AND_LOCAL (Example - Tour, festival) TYPE_HEALTH_AND_FITENESS (Example - Yoga class) TYPE_EDUCATION (Example - Class) TYPE_SPORTS (Example - Football game) TYPE_DATING (Example - meetup) See the [Content Category section](<https://developer.android.com/guide/playcore/engage/healthandfitness?hl=en#content-category>) for guidance. |

#### `EventReservationEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) | Uri |
| Title | **Required** | Title of the entity. | String **Recommended text size: Max 50 chars** |
| Start time | **Required** | The epoch timestamp when the event is expected to start. **Note:**This will be represented in milliseconds. | Epoch timestamp in milliseconds |
| Event mode | **Required** | A field to indicate whether the event will be virtual, in-person or both. | Enum: VIRTUAL, IN_PERSON, or HYBRID |
| Location - Country | Conditionally Required | The country in which the event is happening. **Note:** This is required for events which are IN_PERSON or HYBRID | Free text **Recommended text size: max ~20 chars** |
| Location - City | Conditionally Required | The city in which the event is happening. **Note:** This is required for events which are IN_PERSON or HYBRID | Free text **Recommended text size: max ~20 chars** |
| Location - Display Address | Conditionally Required | The address or venue name where the event will take place that should be displayed to the user. **Note:** This is required for events which are IN_PERSON or HYBRID | Free text **Recommended text size: max ~20 chars** |
| Location - Street Address | Optional | The street address (if applicable) of the location at which event is being hosted. | Free text **Recommended text size: max ~20 chars** |
| Location - State | Optional | The state or province (if applicable) in which the event is being hosted. | Free text **Recommended text size: max ~20 chars** |
| Location - Zip code | Optional | The zip code (if applicable) of the location in which the event is being hosted. | Free text **Recommended text size: max ~20 chars** |
| Location - Neighborhood | Optional | The neighborhood (if applicable) in which the event is being hosted. | Free text **Recommended text size: max ~20 chars** |
| Poster images | Optional | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9 **Note:** Image is highly recommended. If a badge is provided, please ensure safe space of 24 dps at both the top and bottom of the image | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/healthandfitness?hl=en#image-specs>) for guidance. |
| End time | Optional | The epoch timestamp when the event is expected to end. **Note:**This will be represented in milliseconds. | Epoch timestamp in milliseconds |
| Service Provider - Name | Optional | The name of the service provider. **Note:**Either text or image is required for the service provider. | Free text. For example, name of the event organizer/tour |
| Service Provider - Image | Optional | The logo/image of the service provider. **Note:**Either text or image is required for the service provider. | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/healthandfitness?hl=en#image-specs>) for guidance. |
| Description | Optional | A single paragraph of text to describe the entity. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size for each subtitle: max 50 chars** |
| Badges | Optional | Each badge is either free text (max 15 chars) or small image. |  |
| Badge - Text | Optional | Title for the badge **Note:** Either text or image is required for the badge | Free text **Recommended text size: max 15 chars** |
| Badge - Image | Optional | Small image Special UX treatment, for example as badge overlay on the image/video thumbnail. **Note:** Either text or image is required for the badge | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/healthandfitness?hl=en#image-specs>) for guidance. |
| Reservation ID | Optional | The reservation ID for the event reservation. | Free text |
| Price - CurrentPrice | Conditionally required | The current price of the ticket/pass for the event. **Must be provided if strikethrough price is provided.** | Free text |
| Price - StrikethroughPrice | Optional | The original price of the ticket/pass for the event. | Free text |
| Price Callout | Optional | Price callout to feature a promo, event, member discount, if available. | Free text **Recommended text size: under 45 chars (Text that is too long may show ellipses)** |
| Rating - Max value | Optional | The maximum value of the rating scale. **Must be provided if current value of rating is also provided.** | Number >= 0.0 |
| Rating - Current value | Optional | The current value of the rating scale. **Must be provided if maximum value of rating is also provided.** | Number >= 0.0 |
| Rating - Count | Optional | The count of the ratings for the event. **Note:** Provide this field if your app wants to control how this is displayed to the users. Please provide the concise string that can be displayed to the user. For example, if the count is 1,000,000, consider using abbreviations like 1M, so that it won't be truncated on smaller display sizes. | String |
| Rating - Count Value | Optional | The count of the ratings for the event. **Note:** Provide this field if you don't want to handle the display abbreviation logic yourself. If both Count and Count Value are present, we will use the Count to display to users | Long |
| Content Categories | Optional | Describe the category of the content in the entity. | List of Eligible Enums TYPE_MOVIES_AND_TV_SHOWS (Example - Cinema) TYPE_DIGITAL_GAMES (Example - eSports) TYPE_MUSIC (Example - Concert) TYPE_TRAVEL_AND_LOCAL (Example - Tour, festival) TYPE_HEALTH_AND_FITENESS (Example - Yoga class) TYPE_EDUCATION (Example - Class) TYPE_SPORTS (Example - Football game) TYPE_DATING (Example - meetup) See the [Content Category section](<https://developer.android.com/guide/playcore/engage/healthandfitness?hl=en#content-category>) for guidance. |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/healthandfitness).
