#### `TransportationReservationEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) | Uri |
| Title | **Required** | Title of the entity. | Free text. For example, "SFO to SAN" **Recommended text size: Max 50 chars** |
| Transportation Type | **Required** | The mode/type of transportation for the reservation. | Enum: FLIGHT, TRAIN, BUS, or FERRY |
| Departure Time | **Required** | The epoch timestamp in milliseconds that represents the departure time. | Epoch timestamp in milliseconds |
| Arrival Time | **Required** | The epoch timestamp in milliseconds that represents the arrival time. | Epoch timestamp in milliseconds |
| Departure Location - Country | Optional | The country of departure. | Free text **Recommended text size: max ~20 chars** |
| Departure Location - City | Optional | The city of departure. | Free text **Recommended text size: max ~20 chars** |
| Departure Location - Display Address | Optional | The location of departure that will be displayed to the user. | Free text **Recommended text size: max ~20 chars** |
| Departure Location - Street Address | Optional | The street address (if applicable) of the departure location. | Free text **Recommended text size: max ~20 chars** |
| Departure Location - State | Optional | The state or province (if applicable) of the departure location. | Free text **Recommended text size: max ~20 chars** |
| Departure Location - Zip code | Optional | The zip code (if applicable) of the departure location. | Free text **Recommended text size: max ~20 chars** |
| Departure Location - Neighborhood | Optional | The neighborhood (if applicable) of the departure location. | Free text **Recommended text size: max ~20 chars** |
| Arrival Location - Country | Optional | The country of arrival. | Free text **Recommended text size: max ~20 chars** |
| Arrival Location - City | Optional | The city of arrival. | Free text **Recommended text size: max ~20 chars** |
| Arrival Location - Display Address | Optional | The location of arrival that will be displayed to the user. | Free text **Recommended text size: max ~20 chars** |
| Arrival Location - Street Address | Optional | The street address (if applicable) of the arrival location. | Free text **Recommended text size: max ~20 chars** |
| Arrival Location - State | Optional | The state or province (if applicable) of the arrival location. | Free text **Recommended text size: max ~20 chars** |
| Arrival Location - Zip code | Optional | The zip code (if applicable) of the arrival location. | Free text **Recommended text size: max ~20 chars** |
| Arrival Location - Neighborhood | Optional | The neighborhood (if applicable) of the arrival location. | Free text **Recommended text size: max ~20 chars** |
| Service Provider - Name | Optional | The name of the service provider. **Note:**Either text or image is required for the service provider. | Free text. For example, Airline name |
| Service Provider - Image | Optional | The logo/image of the service provider. **Note:**Either text or image is required for the service provider. | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Poster images | Optional | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9 | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Description | Optional | A single paragraph of text to describe the entity. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size for each subtitle: max 50 chars** |
| Reservation ID | Optional | The reservation ID for the transportation reservation. | Free text |
| Price - CurrentPrice | Conditionally required | The current price of the reservation. **Must be provided if strikethrough price is provided.** | Free text |
| Price - StrikethroughPrice | Optional | The original price of the reservation, which is be struck-through in the UI. | Free text |
| Price Callout | Optional | Price callout to feature a promo, event, member discount, if available. | Free text **Recommended text size: under 45 chars (Text that is too long may show ellipses)** |
| Transportation Number | Required | The flight number, bus number, train number, or ferry/cruise number. | Free text |
| Boarding Time | Required | The epoch timestamp that represents the boarding time for the reservation (if applicable) | Epoch timestamp in milliseconds |

#### `VehicleRentalReservationEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | Deep Link to the entity in the provider app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) | Uri |
| Title | **Required** | Title of the entity. | Free text. For example, "Avis Union Square SF" **Recommended text size: Max 50 chars** |
| Pickup Time | **Required** | The epoch timestamp that represents the pick up time for the reservation. | Epoch timestamp in milliseconds |
| Return Time | Optional | The epoch timestamp that represents the check out time for the reservation. | Epoch timestamp in milliseconds |
| Pickup Address - Country | Optional | The country of the pickup location. | Free text **Recommended text size: max ~20 chars** |
| Pickup Address - City | Optional | The city of the pickup location. | Free text **Recommended text size: max ~20 chars** |
| Pickup Address - Display Address | Optional | The pickup location that will be displayed to the user. | Free text **Recommended text size: max ~20 chars** |
| Pickup Address - Street Address | Optional | The street address (if applicable) of the pickup location. | Free text **Recommended text size: max ~20 chars** |
| Pickup Address - State | Optional | The state or province (if applicable) of the pickup location. | Free text **Recommended text size: max ~20 chars** |
| Pickup Address - Zip code | Optional | The zip code (if applicable) of the pickup location. | Free text **Recommended text size: max ~20 chars** |
| Pickup Address - Neighborhood | Optional | The neighborhood (if applicable) of the pickup location. | Free text **Recommended text size: max ~20 chars** |
| Return Address - Country | Optional | The country of return location. | Free text **Recommended text size: max ~20 chars** |
| Return Address - City | Optional | The city of return location. | Free text **Recommended text size: max ~20 chars** |
| Return Address - Display Address | Optional | The return location that will be displayed to the user. | Free text **Recommended text size: max ~20 chars** |
| Return Address - Street Address | Optional | The street address (if applicable) of the return location. | Free text **Recommended text size: max ~20 chars** |
| Return Address - State | Optional | The state or province (if applicable) of the return location. | Free text **Recommended text size: max ~20 chars** |
| Return Address - Zip code | Optional | The zip code (if applicable) of the return location. | Free text **Recommended text size: max ~20 chars** |
| Return Address - Neighborhood | Optional | The neighborhood (if applicable) of the return location. | Free text **Recommended text size: max ~20 chars** |
| Service Provider - Name | Optional | The name of the service provider. **Note:**Either text or image is required for the service provider. | Free text. For example, "Avis Car Rental" |
| Service Provider - Image | Optional | The logo/image of the service provider. **Note:**Either text or image is required for the service provider. | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Poster images | Optional | We will show only 1 image when multiple images are provided. Recommended aspect ratio is 16:9 | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/otherverticals?hl=en#image-specs>) for guidance. |
| Description | Optional | A single paragraph of text to describe the entity. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text. **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text **Recommended text size for each subtitle: max 50 chars** |
| Confirmation ID | Optional | The confirmation ID for the vehicle rental reservation. | Free text |
| Price - CurrentPrice | Conditionally required | The current price of the reservation. **Must be provided if strikethrough price is provided.** | Free text |
| Price - StrikethroughPrice | Optional | The original price of the reservation, which is be struck-through in the UI. | Free text |
| Price Callout | Optional | Price callout to feature a promo, event, member discount, if available. | Free text **Recommended text size: under 45 chars (Text that is too long may show ellipses)** |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/otherverticals).
