### Step 1: Provide entity data

The SDK has defined different entities to represent each item type. The following entities are supported for the Shopping category:

1. `ShoppingEntity`
2. `ShoppingCart`
3. `ShoppingList`
4. `Reorder`
5. `ShoppingOrderTracking`

The following charts outline available attributes and requirements for each type.

#### `ShoppingEntity`

The `ShoppingEntity` object represents a product, promotion, deal, subscription, or event that developer partners want to publish.

##### `ShoppingEntity`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Poster images | **Required** | At least one image must be provided. | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/shopping?hl=en#image-specs>) for guidance. |
| Action Uri | **Required** | The deep link to the page in the app displaying details about the entity.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Title | Optional | The name of the entity. | Free text<br> **Recommended text size: under 90 chars** (Text that is too long may show ellipses) |
| Price - current | Conditionally required | The current price of the entity.<br> **Must be provided if strikethrough price is provided.**  | Free text |
| Price - strikethrough | Optional | The original price of the entity, which is be struck-through in the UI. | Free text |
| Callout | Optional | Callout to feature a promo, event, or update for the entity, if available. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| Callout fine print | Optional | Fine print text for the callout. | Free text<br> **Recommended text size: under 45 chars** (Text that is too long may show ellipses) |
| **Rating (Optional) - Note: All ratings are displayed using our standard star rating system.** | **Rating (Optional) - Note: All ratings are displayed using our standard star rating system.** | **Rating (Optional) - Note: All ratings are displayed using our standard star rating system.** | **Rating (Optional) - Note: All ratings are displayed using our standard star rating system.** |
| Rating - Max value | Optional | The maximum value of the rating scale.<br> **Must be provided if current value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Current value | Optional | The current value of the rating scale.<br> **Must be provided if maximum value of rating is also provided.** | Number &gt;= 0.0 |
| Rating - Count | Optional | The count of the ratings for the entity.<br> **Note:** Provide this field if your app controls how the count is displayed to the users. Use a concise string. For example, if the count is 1,000,000, consider using an abbreviation like 1M so that the count isn't truncated on smaller display sizes.  | String |
| Rating - Count Value | Optional | The count of the ratings for the entity.<br> **Note:** Provide this field if you don't handle the display abbreviation logic yourself. If both Count and Count Value are present, Count is displayed to users. | Long |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

#### `ShoppingCart`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | The deep link to the shopping cart in the partner's app.<br> Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>)  | Uri |
| Number of items | **Required** | The number of items (not just number of products) in the shopping cart. <br> **For example: If there are 3 identical shirts and 1 hat in the cart, this number should be 4.**  | Integer &gt;= 1 |
| Action Text | Optional | The call to action text of the button on the Shopping Cart (for example, *Your Shopping Bag*). <br> **If no action text is provided by the developer, *View Cart* is the default.** <br> This attribute is supported in version 1.1.0 onwards.  | String |
| Title | Optional | The title of the cart (for example, *Your Shopping Bag*).<br> **If no title is provided by the developer, *Your cart* is the default.**<br> **If developer partner publishes a separate cart per merchant, please include *merchant name* in the title.** | Free text<br> **Recommended text size: under 25 chars** (Text that is too long may show ellipses) |
| Cart images | Optional | Images of each product in the cart.<br> **Up to 10 images can be provided in order of priority; the actual number of images displayed depends on the device form factor.** | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/shopping?hl=en#image-specs>) for guidance. |
| Item labels | Optional | The list of labels for items on the shopping list.<br> **The actual number of labels displayed depends on the device form factor.** | List of free text labels<br> **Recommended text size: under 20 chars** (Text that is too long may show ellipses) |
| Last user interaction timestamp | Optional | Number of milliseconds elapsed from the epoch, identifying the last time when user interacted with the cart. **This will be passed as input by the developer partners publishing separate cart per merchant and maybe used for ranking.** | Epoch timestamp in milliseconds |
| **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** | **DisplayTimeWindow (Optional) - Set a time window for a content to be shown on the surface** |
| Start Timestamp | Optional | The epoch timestamp after which the content should be shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |
| End Timestamp | Optional | The epoch timestamp after which the content is no longer shown on the surface.<br> If not set, content is eligible to be shown on the surface. | Epoch timestamp in milliseconds |

#### `ShoppingList`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | The deep link to the shopping list in the partner's app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) | Uri |
| Number of items | **Required** | The number of items in the shopping list. | Integer >= 1 |
| Title | Optional | The title of the list (for example, *Your Grocery List*). **If no title is provided by the developer, *Shopping list* is the default.** | Free text **Recommended text size: under 25 chars** (Text that is too long may show ellipses) |
| Item labels | **Required** | The list of labels for items on the shopping list. **At least 1 label must be provided and up to 10 labels can be provided in order of priority; the actual number of labels displayed depends on the device form factor.** | List of free text labels **Recommended text size: under 20 chars** (Text that is too long may show ellipses) |
| Last user interaction timestamp | **Required** | Number of milliseconds elapsed from the epoch, identifying the last time when user interacted with the shopping list. | Epoch timestamp in milliseconds |

#### `ShoppingReorderCluster`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Action Uri | **Required** | The deep link to reorder in the partner's app. Note: You can use deep links for attribution. [Refer to this FAQ](<https://developer.android.com/guide/playcore/engage/faq#deeplinks-attribution>) | Uri |
| Action Text | Optional | The call to action text of the button on the Reorder (for example, *Order again*). **If no action text is provided by the developer, *Reorder* is the default.** This attribute is supported in version 1.1.0 onwards. | String |
| Number of items | **Required** | The number of items (not just number of products) in the previous order. **For example: If there were 3 small coffees and 1 croissant in the previous order, this number should be 4.** | Integer >= 1 |
| Title | **Required** | The title of the reorder item. | Free text **Recommended text size: under 40 chars** (Text that is too long may show ellipses) |
| Item labels | Optional (If not provided, poster images should be provided) | The list of item labels for the previous order. **Up to 10 labels can be provided in order of priority; the actual number of labels displayed depends on the device form factor.** | List of free text **Recommended text size per label: under 20 chars** (Text that is too long may show ellipses) |
| Poster images | Optional (If not provided, item labels should be provided) | Images of the items in the previous order. **Up to 10 images can be provided in order of priority; the actual number of images displayed depends on the device form factor.** | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/shopping?hl=en#image-specs>) for guidance. |

#### `ShoppingOrderTrackingCluster`

| Attribute | Requirement | Description | Format |
| --- | --- | --- | --- |
| Title | **Required** | A short title of the package/items being tracked or the tracking number. | Free text<br> **Recommended text size: 50 chars (Text that is too long will show ellipses)**  |
| Order Type | **Required** | A short title of the package/items being tracked or the tracking number. | Enum: IN_STORE_PICKUP, SAME_DAY_DELIVERY, MULTI_DAY_DELIVERY |
| Status | **Required** | The current status of the order.<br> **For example: "Running late", "In transit", "Delayed", "Shipped", "Delivered", "Out of stock", "Order ready"** | Free text<br> **Recommended text size: 25 chars (Text that is too long will show ellipses)**  |
| Order Time | **Required** | The epoch timestamp in milliseconds at which the order was placed.<br> **Order time will be displayed if expected delivery time window is not present** | Epoch timestamp in milliseconds |
| Action Uri | **Required** | Deep link to the order tracking in the partner's app. | Uri |
| **OrderDeliveryTimeWindow (Optional) - Set a time window for the order that is being tracked from the time the order was placed to the time of expected/actual delivery.** | **OrderDeliveryTimeWindow (Optional) - Set a time window for the order that is being tracked from the time the order was placed to the time of expected/actual delivery.** | **OrderDeliveryTimeWindow (Optional) - Set a time window for the order that is being tracked from the time the order was placed to the time of expected/actual delivery.** | **OrderDeliveryTimeWindow (Optional) - Set a time window for the order that is being tracked from the time the order was placed to the time of expected/actual delivery.** |
| OrderDeliveryTimeWindow - Start Time | Optional | The epoch timestamp in milliseconds on/after which the order will be delivered or be ready for pickup. | Epoch timestamp in milliseconds |
| OrderDeliveryTimeWindow - End Time | Optional | The epoch timestamp in milliseconds on/before which the order will be delivered or be ready for pickup.  | Epoch timestamp in milliseconds |
| Poster images | Optional | Image of one item/product that is part of the order.<br> Recommended aspect ratio is 1:1 | See [Image Specifications](<https://developer.android.com/guide/playcore/engage/shopping?hl=en#image-specs>) for guidance. |
| Number of items | Optional | The number of items in the order. | Integer &gt;= 1 |
| Description | Optional | A single paragraph of text to describe the items in the order.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size: 180 chars** |
| Subtitle list | Optional | Up to 3 subtitles, with each subtitle a single line of text.<br> **Note:** Either description or subtitle list will be displayed to the user, not both. | Free text<br> **Recommended text size for each subtitle: max 50 chars** |
| Order Value - CurrentPrice | Optional | The current value of the order. | Free text |
| Order number | Optional | The order number/ID that can be used to uniquely identify the order. | Free text<br> **Recommended text size: max 25 chars** |
| Tracking number | Optional | The tracking number for the order/parcel delivery in case the order requires a delivery. | Free text<br> **Recommended text size: max 25 chars** |

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/shopping).
