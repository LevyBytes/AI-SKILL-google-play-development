### Step 1: Provide entity data

The SDK has defined different entities to represent each item type. We support the following entities for the Read category:

1. `EbookEntity`
2. `AudiobookEntity`
3. `BookSeriesEntity`

The following charts outline available attributes and requirements for each type.

#### `EbookEntity`

The `EbookEntity` object represents an ebook (for example, the ebook of *Becoming* by Michelle Obama).

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** |  |
| Poster images | **Required** | At least one image must be provided. See [Image Specifications](<https://developer.android.com/guide/playcore/engage/read?hl=en#image-specs>) for guidance. |
| Author | **Required** | At least one author name must be provided. |
| Action link uri | **Required** | The deep link to the provider app for the ebook.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  |
| Publish date | Optional | In epoch milliseconds if provided. |
| Description | Optional | Must be within 200 characters if provided. |
| Price | Optional | Free text |
| Page count | Optional | Must be a positive integer if provided. |
| Genre | Optional | List of genres associated with the book. |
| Series name | Optional | Name of the series that the ebook belongs to (for example, *Harry Potter*). |
| Series unit index | Optional | The index of the ebook in the series, where 1 is the first ebook in the series. For example, if *Harry Potter and the Prisoner of Azkaban* is the 3rd book in the series, this should be set to 3. |
| Continue book type | Optional | TYPE_CONTINUE - Resume on a unfinished book.<br> TYPE_NEXT - Continue on a new one of a series.<br> TYPE_NEW - Newly released. |
| Last Engagement Time | Conditionally required | Must be provided when the item is in the Continuation cluster. <br> *Newly* acquired ebooks can be a part of the continue reading cluster. <br> In epoch milliseconds. |
| Progress Percentage Complete | Conditionally required | Must be provided when the item is in the Continuation cluster.<br> Value must be greater than 0 and less than 100. |
| **DisplayTimeWindow - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface.<br> In epoch milliseconds. |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface.<br> In epoch milliseconds. |

#### `AudiobookEntity`

The `AudiobookEntity` object represents an audiobook (for example, the audiobook of *Becoming* by Michelle Obama).

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** |  |
| Poster images | **Required** | At least one image must be provided. See [Image Specifications](<https://developer.android.com/guide/playcore/engage/read?hl=en#image-specs>) for guidance. |
| Author | **Required** | At least one author name must be provided. |
| Action link uri | **Required** | The deep link to the provider app for the audiobook.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  |
| Narrator | Optional | At least one narrator's name must be provided. |
| Publish date | Optional | In epoch milliseconds if provided. |
| Description | Optional | Must be within 200 characters if provided. |
| Price | Optional | Free text |
| Duration | Optional | Must be a positive value if provided. |
| Genre | Optional | List of genres associated with the book. |
| Series name | Optional | Name of the series that the audiobook belongs to (for example, *Harry Potter*. |
| Series unit index | Optional | The index of the audiobook in the series, where 1 is the first audiobook in the series. For example, if *Harry Potter and the Prisoner of Azkaban* is the 3rd book in the series, this should be set to 3. |
| Continue book type | Optional | TYPE_CONTINUE - Resume on a unfinished book.<br> TYPE_NEXT - Continue on a new one of a series.<br> TYPE_NEW - Newly released. |
| Last Engagement Time | Conditionally required | Must be provided when the item is in the Continuation cluster.<br> In epoch milliseconds. |
| Progress Percentage Complete | Conditionally required | Must be provided when the item is in the Continuation cluster.<br> *Newly* acquired audiobooks can be a part of the continue reading cluster. <br> Value must be greater than 0 and less than 100. |
| **DisplayTimeWindow - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface.<br> In epoch milliseconds. |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface.<br> In epoch milliseconds. |

#### `BookSeriesEntity`

The `BookSeriesEntity` object represents a book series (for example, the *Harry Potter* book series, which has 7 books).

| Attribute | Requirement | Notes |
| --- | --- | --- |
| Name | **Required** |  |
| Poster images | **Required** | At least one image must be provided. See [Image Specifications](<https://developer.android.com/guide/playcore/engage/read?hl=en#image-specs>) for guidance. |
| Author | **Required** | At least one author name must be present. |
| Action link uri | **Required** | The deep link to the provider app for the audiobook or ebook.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  |
| Book count | **Required** | Number of books in the series. |
| Description | Optional | Must be within 200 characters if provided. |
| Genre | Optional | List of genres associated with the book. |
| Continue book type | Optional | TYPE_CONTINUE - Resume on a unfinished book.<br> TYPE_NEXT - Continue on a new one of a series.<br> TYPE_NEW - Newly released. |
| Last Engagement Time | Conditionally required | Must be provided when the item is in the Continuation cluster.<br> In epoch milliseconds. |
| Progress Percentage Complete | Conditionally required | Must be provided when the item is in the Continuation cluster.<br> *Newly* acquired book series can be a part of the continue reading cluster. <br> Value must be greater than 0 and less than 100. |
| **DisplayTimeWindow - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface.<br> In epoch milliseconds. |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface.<br> In epoch milliseconds. |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/read).
