#### Image specifications

Required specifications for image assets are listed in this table:

| Aspect ratio | Minimum pixels | Recommended pixels |
| --- | --- | --- |
| Square (1x1)**Preferred** | 300x300 | 1200x1200 |
| Landscape (1.91x1) | 600x314 | 1200x628 |
| Portrait (4x5) | 480x600 | 960x1200 |

The images are required to be hosted on public CDNs so that Google can access them.

*File formats*

PNG, JPG, static GIF, WebP

*Maximum file size*

5120 KB

*Additional recommendations*

- **Image safe area:** Put your important content in the center 80% of the image.
- Use a transparent background so that the image can be properly displayed in Dark and Light theme settings.

#### Timezone specifications

Prefer ID (for example, "America/Los_Angeles") over offset (for example, "-07:00").

Sample usage: `DateTimeZone.forID("America/Los_Angeles")`

#### Content Category

The content category allows apps to publish content belonging to multiple categories. This maps the content with some of the predefined categories namely:

- `TYPE_EDUCATION`
- `TYPE_SPORTS`
- `TYPE_MOVIES_AND_TV_SHOWS`
- `TYPE_BOOKS`
- `TYPE_AUDIOBOOKS`
- `TYPE_MUSIC`
- `TYPE_DIGITAL_GAMES`
- `TYPE_TRAVEL_AND_LOCAL`
- `TYPE_HOME_AND_AUTO`
- `TYPE_BUSINESS`
- `TYPE_NEWS`
- `TYPE_FOOD_AND_DRINK`
- `TYPE_SHOPPING`
- `TYPE_HEALTH_AND_FITENESS`
- `TYPE_MEDICAL`
- `TYPE_PARENTING`
- `TYPE_DATING`

The images are required to be hosted on public CDNs so that Google can access them.

*Guidelines to use the content categories*

1. Some entities like **ArticleEntity** and **GenericFeaturedEntity** are eligible to use any of the content categories. For other entities like **EventEntity**, **EventReservationEntity**, **PointOfInterestEntity**, only a subset of these categories are eligible. Check the list of categories eligible for an entity type before populating the list.
2. Use the specific entity type for some content categories over a combination of the Generic entities and the ContentCategory:

   - TYPE_MOVIES_AND_TV_SHOWS - Check out the entities from [Watch integration guide](<https://developer.android.com/guide/playcore/engage/watch>) before using the generic entities.
   - TYPE_BOOKS - Check out the [EbookEntity](<https://developer.android.com/guide/playcore/engage/read#ebookentity>) before using the generic entities.
   - TYPE_AUDIOBOOKS - Check out [AudiobookEntity](<https://developer.android.com/guide/playcore/engage/read#audiobookentity>) before using the generic entities.
   - TYPE_SHOPPING - Check out [ShoppingEntity](<https://developer.android.com/guide/playcore/engage/shopping#shoppingentity>) before using the generic entities.
   - TYPE_FOOD_AND_DRINK - Check out entities from [Food Integration guide](<https://developer.android.com/guide/playcore/engage/food>) before using the generic entities.
3. The ContentCategory field is optional and should be left blank if the content doesn't belong to any of the categories mentioned earlier.
4. In case multiple content categories are provided, provide them in the order of relevance to the content with the most relevant content category placed first in the list.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/travel).
