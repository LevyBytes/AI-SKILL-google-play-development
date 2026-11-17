#### `TransportationReservationEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Title | **Required** | Title of the entity. | Free text. For example, "SFO to SAN"<br> **Recommended text size: Max 50 chars** |
| Transportation Type | **Required** | The mode/type of transportation for the reservation. | Enum: FLIGHT, TRAIN, BUS, or FERRY |
| Localized Departure Time - Timestamp | **Required** | The epoch timestamp that represents the departure time. | Joda-Time Instant |
| Localized Departure Time - Timezone | **Required** | The timezone of the departure time. | Joda-Time DateTimeZone<br> See [Timezone Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#tz-specs>) for guidance. |
| Localized Arrival Time - Timestamp | **Required** | The epoch timestamp that represents the arrival time. | Joda-Time Instant |
| Localized Arrival Time - Timezone | **Required** | The timezone of the arrival time. | Joda-Time DateTimeZone<br> See [Timezone Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#tz-specs>) for guidance. |
| Transportation Number | **Required** | The flight number, bus number, train number, or ferry/cruise number. | Free text |
| Localized Boarding Time - Timestamp | **Required** | The epoch timestamp that represents the boarding time for the reservation (if applicable) | Joda-Time Instant |
| Localized Boarding Time - Timezone | **Required** | The timezone of the boarding time for the reservation (if applicable) | Joda-Time DateTimeZone<br> See [Timezone Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#tz-specs>) for guidance. |
| Departure Location - Country | Optional | The country of departure. | Free text<br> **Recommended text size: max ~20 chars** |
| Departure Location - City | Optional | The city of departure. | Free text<br> **Recommended text size: max ~20 chars** |
| Departure Location - Display Address | Optional | The location of departure that will be displayed to the user. | Free text<br> **Recommended text size: max ~20 chars** |
| Departure Location - Street Address | Optional | The street address (if applicable) of the departure location. | Free text<br> **Recommended text size: max ~20 chars** |
| Departure Location - State | Optional | The state or province (if applicable) of the departure location. | Free text<br> **Recommended text size: max ~20 chars** |
| Departure Location - Zip code | Optional | The zip code (if applicable) of the departure location. | Free text<br> **Recommended text size: max ~20 chars** |
| Departure Location - Neighborhood | Optional | The neighborhood (if applicable) of the departure location. | Free text<br> **Recommended text size: max ~20 chars** |
| Arrival Location - Country | Optional | The country of arrival. | Free text<br> **Recommended text size: max ~20 chars** |
| Arrival Location - City | Optional | The city of arrival. | Free text<br> **Recommended text size: max ~20 chars** |
| Arrival Location - Display Address | Optional | The location of arrival that will be displayed to the user. | Free text<br> **Recommended text size: max ~20 chars** |
| Arrival Location - Street Address | Optional | The street address (if applicable) of the arrival location. | Free text<br> **Recommended text size: max ~20 chars** |
| Arrival Location - State | Optional | The state or province (if applicable) of the arrival location. | Free text<br> **Recommended text size: max ~20 chars** |
| Arrival Location - Zip code | Optional | The zip code (if applicable) of the arrival location. | Free text<br> **Recommended text size: max ~20 chars** |
| Arrival Location - Neighborhood | Optional | The neighborhood (if applicable) of the arrival location. | Free text<br> **Recommended text size: max ~20 chars** |
| Service Provider - Name | Optional | The name of the service provider.<br> **Note:**Either text or image is required for the service provider.  | Free text. For example, Airline name |
| Service Provider - Image | Optional | The logo/image of the service provider.<br> **Note:**Either text or image is required for the service provider.  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Poster images | Optional | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Description | Optional | A single paragraph of text to describe the entity.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size for each subtitle: max 50 chars** |
| Reservation ID | Optional | The reservation ID for the transportation reservation. | Free text |
| Price - CurrentPrice | Conditionally required | The current price of the reservation.<br> **Must be provided if strikethrough price is provided.**  | Free text |
| Price - StrikethroughPrice | Optional | The original price of the reservation, which is be struck-through in the UI. | Free text |
| Price Callout | Optional | Price callout to feature a promo, event, member discount, if available. | Free text<br> **Recommended text size: under 45 chars (Text that is too long may show ellipses)** |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

#### `VehicleRentalReservationEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Title | **Required** | Title of the entity. | Free text. For example, "Avis Union Square SF"<br> **Recommended text size: Max 50 chars** |
| Localized Pickup Time - Timestamp | **Required** | The epoch timestamp that represents the pick up time for the reservation. | Joda-Time Instant |
| Localized Pickup Time - Timezone | **Required** | The timezone of the pick up time for the reservation. | Joda-Time DateTimeZone<br> See [Timezone Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#tz-specs>) for guidance. |
| Localized Return Time - Timestamp | Optional | The epoch timestamp that represents the check out time for the reservation. | Joda-Time Instant |
| Localized Return Time - Timezone | Optional | The timezone of the check out time for the reservation. | Joda-Time DateTimeZone<br> See [Timezone Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#tz-specs>) for guidance. |
| Pickup Address - Country | Optional | The country of the pickup location. | Free text<br> **Recommended text size: max ~20 chars** |
| Pickup Address - City | Optional | The city of the pickup location. | Free text<br> **Recommended text size: max ~20 chars** |
| Pickup Address - Display Address | Optional | The pickup location that will be displayed to the user. | Free text<br> **Recommended text size: max ~20 chars** |
| Pickup Address - Street Address | Optional | The street address (if applicable) of the pickup location. | Free text<br> **Recommended text size: max ~20 chars** |
| Pickup Address - State | Optional | The state or province (if applicable) of the pickup location. | Free text<br> **Recommended text size: max ~20 chars** |
| Pickup Address - Zip code | Optional | The zip code (if applicable) of the pickup location. | Free text<br> **Recommended text size: max ~20 chars** |
| Pickup Address - Neighborhood | Optional | The neighborhood (if applicable) of the pickup location. | Free text<br> **Recommended text size: max ~20 chars** |
| Return Address - Country | Optional | The country of return location. | Free text<br> **Recommended text size: max ~20 chars** |
| Return Address - City | Optional | The city of return location. | Free text<br> **Recommended text size: max ~20 chars** |
| Return Address - Display Address | Optional | The return location that will be displayed to the user. | Free text<br> **Recommended text size: max ~20 chars** |
| Return Address - Street Address | Optional | The street address (if applicable) of the return location. | Free text<br> **Recommended text size: max ~20 chars** |
| Return Address - State | Optional | The state or province (if applicable) of the return location. | Free text<br> **Recommended text size: max ~20 chars** |
| Return Address - Zip code | Optional | The zip code (if applicable) of the return location. | Free text<br> **Recommended text size: max ~20 chars** |
| Return Address - Neighborhood | Optional | The neighborhood (if applicable) of the return location. | Free text<br> **Recommended text size: max ~20 chars** |
| Service Provider - Name | Optional | The name of the service provider.<br> **Note:**Either text or image is required for the service provider.  | Free text. For example, "Avis Car Rental" |
| Service Provider - Image | Optional | The logo/image of the service provider.<br> **Note:**Either text or image is required for the service provider.  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Poster images | Optional | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/travel?hl=en#image-specs>) for guidance. |
| Description | Optional | A single paragraph of text to describe the entity.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size for each subtitle: max 50 chars** |
| Confirmation ID | Optional | The confirmation ID for the vehicle rental reservation. | Free text |
| Price - CurrentPrice | Conditionally required | The current price of the reservation.<br> **Must be provided if strikethrough price is provided.**  | Free text |
| Price - StrikethroughPrice | Optional | The original price of the reservation, which is be struck-through in the UI. | Free text |
| Price Callout | Optional | Price callout to feature a promo, event, member discount, if available. | Free text<br> **Recommended text size: under 45 chars (Text that is too long may show ellipses)** |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/travel).
