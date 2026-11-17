### Step 1: Provide entity data

The SDK has defined different entities to represent each item type. The SDK supports the following entities for the Social category:

1. `PortraitMediaEntity`
2. `SocialPostEntity`

The following charts outline available attributes and requirements for each type.

#### `PortraitMediaEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action URI | **Required** for all surfaces other than Google TV | Deep Link to the entity in the provider app. <br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | URI |
| PlatformSpecificPlayback | **Required** for Google TV surface | Deep Link to the entity in the provider app for platforms like Google TV and Mobile.  | List of PlatformSpecificPlayback objects |
| Recommendation Reason | Optional | The justification for recommending the content to the user. | RecommendationReason object |
| Comments Summary | Optional | Summary of comments for the post. | String |
| **Post related metadata (Required)** | **Post related metadata (Required)** | **Post related metadata (Required)** | **Post related metadata (Required)** |
| Image(s) | Required | Image(s) should be in **portrait aspect ratio.** <br> The UI may show only 1 image when multiple images are provided. However, the UI may provide visual indication that there are more images in the app. <br> *If the post is a video, the provider should provide a thumbnail of the video to be shown as an image.*  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/social?hl=en#image-specs>) for guidance. |
| Text content | Optional | The main text of a post, update, etc. | String (recommended max 140 chars) |
| Timestamp | Optional | Time when the post was published. | Epoch timestamp in milliseconds |
| Is video content | Optional | Is the post a video? | boolean |
| Video duration | Optional | The duration of the video in milliseconds. | Long |
| **Profile related metadata (Optional)** | **Profile related metadata (Optional)** | **Profile related metadata (Optional)** | **Profile related metadata (Optional)** |
| Name | Required | Profile name or id or handle, eg "John Doe", "@TeamPixel" | String(recommended max 25 chars) |
| Avatar | Required | Profile picture or avatar image of the user. <br> **Square 1:1 image**  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/social?hl=en#image-specs>) for guidance. |
| Additional Image | Optional | Profile badge. for example - verified badge <br> **Square 1:1 image**  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/social?hl=en#image-specs>) for guidance. |
| **Interactions related metadata (Optional)** | **Interactions related metadata (Optional)** | **Interactions related metadata (Optional)** | **Interactions related metadata (Optional)** |
| Count | Optional | Indicate the number of interactions, for example - "3.7 M.".<br> **Note:** If both Count and Count Value are provided, Count will be used. <br> **Note:** Partners should use either **Count** or **CountWithOptionalLabel**.  | String |
| CountWithOptionalLabel | Optional | Indicate the number of interactions with an optional label, for example - "3.7 M Likes.".<br> **Note:** If both CountWithOptionalLabel and Count Value are provided, one of them will be used. <br> **Note:** Partners should use either **Count** or **CountWithOptionalLabel**.  | String |
| Count Value | Optional | The number of interactions as a value.<br> **Note:** Provide Count Value instead of Count if your app doesn't handle logic on how a large number should be optimized for different display sizes. If both Count and Count Value are provided, Count is used.  | Long |
| Label | Optional | Indicate what the interaction label is for. For example - "Likes". | String |
| Visual | Optional | Indicate what the interaction is for. For example - Image showing Likes icon, emoji.<br> Can provide more than 1 image, though not all may not be shown on all form factors.<br> **Note:** Must be Square 1:1 image | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/social?hl=en#image-specs>) for guidance. |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

#### `SocialPostEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action URI | **Required** | Deep Link to the entity in the provider app. <br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | URI |
| PlatformSpecificPlayback URIs | **Required** for Google TV surface | Deep Link to the entity in the provider app for platforms like Google TV and Mobile.  | List of PlatformSpecificPlayback objects |
| Recommendation Reason | Optional | The justification for recommending the content to the user. | RecommendationReason object |
| Comments Summary | Optional | Summary of comments for the post. | String |
| **Post related metadata (Required)** <br> At least one of TextContent, Image or WebContent is required  | **Post related metadata (Required)** <br> At least one of TextContent, Image or WebContent is required  | **Post related metadata (Required)** <br> At least one of TextContent, Image or WebContent is required  | **Post related metadata (Required)** <br> At least one of TextContent, Image or WebContent is required  |
| Image(s) | Optional | Image(s) should be in **portrait aspect ratio.** <br> The UI may show only 1 image when multiple images are provided. However, the UI may provide visual indication that there are more images in the app. <br> *If the post is a video, the provider should provide a thumbnail of the video to be shown as an image.*  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/social?hl=en#image-specs>) for guidance. |
| Text content | Optional | The main text of a post, update, etc. | String (recommended max 140 chars) |
| **Video Content (Optional)** | **Video Content (Optional)** | **Video Content (Optional)** | **Video Content (Optional)** |
| Duration | Required | The duration of the video in milliseconds. | Long |
| Image | Required | Preview image of the video content. | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/social?hl=en#image-specs>) for guidance. |
| **Link Preview (Optional)** | **Link Preview (Optional)** | **Link Preview (Optional)** | **Link Preview (Optional)** |
| Link Preview - Title | Required | Text to indicate the title of the web page content | String |
| Link Preview - Hostname | Required | Text to indicate the web page owner, eg "INSIDER" | String |
| Link Preview - Image | Optional | Hero image for the web content | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/social?hl=en#image-specs>) for guidance. |
| Timestamp | Optional | Time when the post was published. | Epoch timestamp in milliseconds |
| **Profile related metadata (Optional)** | **Profile related metadata (Optional)** | **Profile related metadata (Optional)** | **Profile related metadata (Optional)** |
| Name | Required | Profile name or id or handle, eg "John Doe", "@TeamPixel." | String(recommended max 25 chars) |
| Additional Text | Optional | Could be used as profile id or handle or additional metadata <br> For example "@John-Doe", "5M followers", "You might like", "Trending", "5 new posts"  | String(recommended max 40 chars) |
| Avatar | Required | Profile picture or avatar image of the user. <br> **Square 1:1 image**  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/social?hl=en#image-specs>) for guidance. |
| Additional Image | Optional | Profile badge, for example - verified badge <br> **Square 1:1 image**  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/social?hl=en#image-specs>) for guidance. |
| **Interactions related metadata (Optional)** | **Interactions related metadata (Optional)** | **Interactions related metadata (Optional)** | **Interactions related metadata (Optional)** |
| Count | Required | Indicate the number of interactions, for example - "3.7 M."<br> **Note:** Partners should use either **Count** or **CountWithOptionalLabel**.  | String |
| CountWithOptionalLabel | Required | Indicate the number of interactions with an optional label, for example - "3.7 M Likes."<br> **Note:** Partners should use either **Count** or **CountWithOptionalLabel**.  | String |
| Label | Optional <br> If not provided, **Visual** must be provided.  | Indicate what the interaction is for. For example - "Likes." | String (recommended max 20 chars for count + label combined) |
| Visual | Optional <br> If not provided, **Label** must be provided.  | Indicate what the interaction is for. For example - Image showing Likes icon, emoji. <br> Can provide more than 1 image, though not all may not be shown on all form factors. <br> **Square 1:1 image**  | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/social?hl=en#image-specs>) for guidance. |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

#### Image specifications

The images are required to be hosted on public CDNs so that Google can access them.

*File formats*

PNG, JPG, static GIF, WebP

*Maximum file size*

5120 KB

*Additional recommendations*

- **Image safe area:** Put your important content in the center 80% of the image.
- Use a transparent background so that the image can be properly displayed in Dark and Light theme settings.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/social).
