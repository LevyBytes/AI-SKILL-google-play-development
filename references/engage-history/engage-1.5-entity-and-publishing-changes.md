## Engage SDK 1.5.12 Release

This version contains the following changes.

### Summary of changes

- Added `PlatformSpecificPlaybackUris`, `RecommendationReason` and `CommentsSummary` to `PortraitMediaEntity`.
- Added `CountWithOptionalLabel` to `Interactions`.
- Added `CallToActionText` and `Tags` to `MovieEntity`, `TvShowEntity`, `TvEpisodeEntity`, `MediaActionFeedEntity`, `VideoClipEntity`, `LiveTvChannelEntity` and `LiveTvProgramEntity`.

## Engage SDK 1.5.11 Release

This version contains the following changes.

### Summary of changes

- Added last user interaction timestamp in `FoodShoppingCart`, `FoodShoppingList`, and `ShoppingList`.
- Added APIs to publish multiple shopping carts and lists.

  - `AppEngageFoodClient.publishFoodShoppingCarts`
  - `AppEngageFoodClient.publishFoodShoppingLists`
  - `AppEngageShoppingClient.publishShoppingLists`

## Engage SDK 1.5.10 Release

This version contains the following changes.

### Summary of changes

- Added `LiveTvChannelEntity` and `LiveTvProgramEntity` to engage video data model.

## Engage SDK 1.5.9 Release

This version contains the following changes.

### Summary of changes

- Added `RecommendationClusterType` to `RecommendationCluster`.
- Added `Description`, `Genre`, `ContentRatings` and `RecommendationReason` to `LiveStreamingVideoEntity`.

## Engage SDK 1.5.8 Release

This version contains the following changes.

### Summary of changes

- Added `AccountProfile` and `syncAcrossDevices` to `PublishRecommendationClustersRequest`.
- Added `Locale` to the `AccountProfile`.
- Added `MediaActionFeedEntity` to engage video data model.
- Added `PlatformSpecificPlaybackUri` to `TVShowEntity`.
- Added `description` field to `MovieEntity` and `TVShowEntity`.
- Added `RecommendationReason` to `MovieEntity` and `TVShowEntity`.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/release).
