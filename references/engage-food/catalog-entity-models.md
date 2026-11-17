### Step 1: Provide entity data

The SDK has defined different entities to represent each item type. We support the following entities for the Food category:

1. `ProductEntity`
2. `StoreEntity`
3. `RecipeEntity`
4. `FoodShoppingCart`
5. `FoodShoppingList`
6. `FoodReorderCluster`

The following charts outline available attributes and requirements for each type.

#### `ProductEntity`

The `ProductEntity` object represents an individual item (such as a grocery item, dish from a restaurant, or a promotion) that developer partners want to publish.

![Image](<https://developer.android.com/static/images/guide/playcore/engage/food-product-entity.png>)

**Figure :**Attributes of `ProductEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Poster images | **Required** | At least one image must be provided. | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/food?hl=en#image-specs>) for guidance. |
| Action Uri | **Required** | The deep link to the page in the app displaying details about the product.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Title | Optional | The name of the product. | Free text<br> **Recommended text size: under 90 chars** (Text that is too long may show ellipses) |
| Price - current | Conditionally required | The current price of the product.<br> **Must be provided if strikethrough price is provided.**  | Free text |
| Price - strikethrough | Optional | The original price of the entity, which is struck-through in the UI. | Free text |
| Callout | Optional | Callout to feature a promo, event, or update for the product, if available. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Callout fine print | Optional | Fine print text for the callout. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| **Rating (Optional) - Note: All ratings are displayed using our standard star rating system.** | **Rating (Optional) - Note: All ratings are displayed using our standard star rating system.** | **Rating (Optional) - Note: All ratings are displayed using our standard star rating system.** | **Rating (Optional) - Note: All ratings are displayed using our standard star rating system.** |
| Rating - Max value | Optional | The maximum value of the rating scale.<br> **Must be provided if current value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Current value | Optional | The current value of the rating scale.<br> **Must be provided if maximum value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Count | Optional | The count of the ratings for the product.<br> **Note:** Provide this field if your app controls how the count is displayed to the users. Use a concise string. For example, if the count is 1,000,000, consider using an abbreviation like 1M so that the count isn't truncated on smaller display sizes. | String |
| Rating - Count Value | Optional | The count of the ratings for the product.<br> **Note:** Provide this field if you don't handle the display abbreviation logic yourself. If both Count and Count Value are present, Count is displayed to users. | Long |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

#### `StoreEntity`

The `StoreEntity` object represents an individual store that developer partners want to publish, such as a restaurant or a grocery store.

![Image](<https://developer.android.com/static/images/guide/playcore/engage/food-store-entity.png>)

**Figure :**Attributes of `StoreEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Poster images | **Required** | At least one image must be provided. | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/food?hl=en#image-specs>) for guidance. |
| Action Uri | **Required** | The deep link to the page in the app displaying details about the store.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Title | Optional | The name of the store. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Location | Optional | The location of the store. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Callout | Optional | Callout to feature a promo, event, or update for the store, if available. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Callout fine print | Optional | Fine print text for the callout. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Description | Optional | A description of the store. | Free text<br> **Recommended text size: under 90 chars** (Text that is too long may show ellipses) |
| Category | Optional | Category of a store, in the context of dining places, it can be cuisine like "french", "new american", "ramen", "fine dining". | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| **Note: All ratings is displayed using our standard star rating system.** | **Note: All ratings is displayed using our standard star rating system.** | **Note: All ratings is displayed using our standard star rating system.** | **Note: All ratings is displayed using our standard star rating system.** |
| Rating - Max value | Optional | The maximum value of the rating scale.<br> **Must be provided if current value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Current value | Optional | The current value of the rating scale.<br> **Must be provided if maximum value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Count | Optional | The count of the ratings for the store.<br> **Note:** Provide this field if your app wants to control how this is displayed to the users. Provide the concise string that can be displayed to the user. For example, if the count is 1,000,000, consider using abbreviations like 1M, so that it won't be truncated on smaller display sizes. | String |
| Rating - Count Value | Optional | The count of the ratings for the store.<br> **Note:** Provide this field if you don't want to handle the display abbreviation logic yourself. If both Count and Count Value are present, we will use the Count to display to users | Long |

#### `RecipeEntity`

The `RecipeEntity` object represents a recipe item that developer partners want to publish.

![Image](<https://developer.android.com/static/images/guide/playcore/engage/food-recipe-entity.png>)

**Figure :**Attributes of `RecipeEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Poster images | **Required** | At least one image must be provided. | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/food?hl=en#image-specs>) for guidance. |
| Action Uri | **Required** | The deep link to the page in the app displaying details about the recipe.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Title | Optional | The name of the recipe. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Author | Optional | The author of the recipe. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Cook/Preparation time | Optional | The cooking time of the recipe. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Callout | Optional | Callout to feature a promo, event, or update for the recipe, if available. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Category | Optional | The category of the recipe. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Description | Optional | A description of the recipe. | Free text<br> **Recommended text size: under 90 chars** (Text that is too long may show ellipses) |
| **Note: All ratings are displayed using our standard star rating system.** | **Note: All ratings are displayed using our standard star rating system.** | **Note: All ratings are displayed using our standard star rating system.** | **Note: All ratings are displayed using our standard star rating system.** |
| Rating - Max value | Optional | The maximum value of the rating scale.<br> **Must be provided if current value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Current value | Optional | The current value of the rating scale.<br> **Must be provided if maximum value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Count | Optional | The count of the ratings for the recipe.<br> **Note:** Provide this field if your app wants to control how this is displayed to the users. Provide the concise string that can be displayed to the user. For example, if the count is 1,000,000, consider using abbreviations like 1M, so that it won't be truncated on smaller display sizes. | String |
| Rating - Count Value | Optional | The count of the ratings for the recipe.<br> **Note:** Provide this field if you don't want to handle the display abbreviation logic yourself. If both Count and Count Value are present, we will use the Count to display to users | Long |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/food).
