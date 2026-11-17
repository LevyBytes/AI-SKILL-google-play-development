#### `FoodShoppingCart`

![Image](<https://developer.android.com/static/images/guide/playcore/engage/food-shopping-cart-attributes.png>)

**Figure:** Food Shopping Cart cluster attributes.

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | The deep link to the shopping cart in the partner's app.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Number of items | **Required** | The number of items (not just number of products) in the shopping cart.<br> **For example: If there are 3 oranges and 1 apple in the cart, this number should be 4.** | Integer &gt;= 1 |
| Last user interaction timestamp | **Required** | Number of milliseconds elapsed from the epoch, identifying the last time when user interacted with the shopping cart. | Epoch timestamp in milliseconds |
| Title | Optional | The title of the cart (for example, *Your cart*).<br> **If no title is provided by the developer, *Your cart* is the default.** | Free text<br> **Recommended text size: under 25 chars** (Text that is too long may show ellipses) |
| Action Text | Optional | The call to action text of the button on the Shopping Cart (for example, *Your Shopping Bag*). <br> **If no action text is provided by the developer, *View Cart* is the default.** <br> This attribute is supported in version 1.1.0 onwards.  | String |
| Cart images | Optional | Images of each product in the cart.<br> **Up to 10 images can be provided in order of priority; the actual number of images displayed depends on the device form factor.** | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/food?hl=en#image-specs>) for guidance. |
| Item labels | Optional | The list of labels for items on the shopping list.<br> **The actual number of labels displayed depends on the device form factor.** | List of free text labels<br> **Recommended text size: under 20 chars** (Text that is too long may show ellipses) |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

#### `FoodShoppingList`

![Image](<https://developer.android.com/static/images/guide/playcore/engage/food-shopping-list.png>)

**Figure:** Food Shopping List cluster.

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | The deep link to the shopping list in the partner's app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) | Uri |
| Number of items | **Required** | The number of items in the shopping list. | Integer >= 1 |
| Last user interaction timestamp | **Required** | Number of milliseconds elapsed from the epoch, identifying the last time when user interacted with the shopping list. | Epoch timestamp in milliseconds |
| Title | Optional | The title of the list (for example, *Your Grocery List*). **If no title is provided by the developer, *Shopping list* is the default.** | Free text **Recommended text size: under 25 chars** (Text that is too long may show ellipses) |
| Item labels | **Required** | The list of labels for items on the shopping list. **At least 1 label must be provided and up to 10 labels can be provided in order of priority; the actual number of labels displayed depends on the device form factor.** | List of free text labels **Recommended text size: under 20 chars** (Text that is too long may show ellipses) |

#### `FoodReorderCluster`

![Image](<https://developer.android.com/static/images/guide/playcore/engage/food-reorder-cluster.png>)

**Figure:** Food Reorder cluster.

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | The deep link to reorder in the partner's app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) | Uri |
| Action Text | Optional | The call to action text of the button on the Reorder (for example, *Order again*). **If no action text is provided by the developer, *Reorder* is the default.** This attribute is supported in version 1.1.0 onwards. | String |
| Number of items | **Required** | The number of items (not just number of products) in the previous order. **For example: If there were 3 small coffees and 1 croissant in the previous order, this number should be 4.** | Integer >= 1 |
| Title | **Required** | The title of the reorder item. | Free text **Recommended text size: under 40 chars** (Text that is too long may show ellipses) |
| Item labels | Optional (If not provided, poster images should be provided) | The list of item labels for the previous order. **Up to 10 labels can be provided in order of priority; the actual number of labels displayed depends on the device form factor.** | List of free text **Recommended text size per label: under 20 chars** (Text that is too long may show ellipses) |
| Poster images | Optional (If not provided, item labels should be provided) | Images of the items in the previous order. **Up to 10 images can be provided in order of priority; the actual number of images displayed depends on the device form factor.** | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/food?hl=en#image-specs>) for guidance. |

#### Image specifications

The following table lists the required specifications for image assets:

| Aspect ratio | Minimum pixels | Recommended pixels |
| --- | --- | --- |
| Square (1x1)**Preferred** | 300x300 | 1200x1200 |
| Landscape (1.91x1) | 600x314 | 1200x628 |
| Portrait (4x5) | 480x600 | 960x1200 |

*File formats*

PNG, JPG, static GIF, WebP

*Maximum file size*

5120 KB

*Additional recommendations*

- **Image safe area:** Put your important content in the center 80% of the image.
- Use a transparent background so that the image can be properly displayed in Dark and Light theme settings.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/food).
