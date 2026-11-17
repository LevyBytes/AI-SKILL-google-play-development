### Step 0: Migration from existing Media Home SDK integration

This section outlines how to migrate your existing Media Home SDK data models and API calls to the Engage SDK.

#### Map data models from existing integration

If you are migrating from an existing Media Home integration, the following table outlines how to map data models in existing SDKs to the new Engage SDK:

| MediaHomeVideoContract integration equivalent | Engage SDK integration equivalent |
| --- | --- |
| `com.google.android.mediahome.video.PreviewChannel` | ` com.google.android.engage.common.datamodel.RecommendationCluster ` |
| `com.google.android.mediahome.video.PreviewChannel.Builder` | ` com.google.android.engage.common.datamodel.RecommendationCluster.Builder ` |
| `com.google.android.mediahome.video.PreviewChannelHelper` | `com.google.android.engage.video.service.AppEngageVideoClient` |
| `com.google.android.mediahome.video.PreviewProgram` | Divided into separate classes: `EventVideo`, `LiveStreamingVideo`, `Movie`, `TvEpisode`, `TvSeason`, `TvShow`, `VideoClipEntity` |
| `com.google.android.mediahome.video.PreviewProgram.Builder` | Divided into builders in separate classes: `EventVideo`, `LiveStreamingVideo`, `Movie`, `TvEpisode`, `TvSeason`, `TvShow`, `VideoClipEntity` |
| `com.google.android.mediahome.video.VideoContract` | No longer needed. |
| `com.google.android.mediahome.video.WatchNextProgram` | Divided into attributes in separate classes: `EventVideoEntity`, `LiveStreamingVideoEntity`, `MovieEntity`, `TvEpisodeEntity`, `TvSeasonEntity`, `TvShowEntity`, `VideoClipEntity` |
| `com.google.android.mediahome.video.WatchNextProgram.Builder` | Divided into attributes in separate classes: `EventVideoEntity`, `LiveStreamingVideoEntity`, `MovieEntity`, `TvEpisodeEntity`, `TvSeasonEntity`, `TvShowEntity`, `VideoClipEntity` |

#### Publishing clusters in Media Home SDK compared to Engage SDK

With Media Home SDK, clusters and entities were published through separate APIs:

```java
// 1. Fetch existing channels
List<PreviewChannel> channels = PreviewChannelHelper.getAllChannels();

// 2. If there are no channels, publish new channels
long channelId = PreviewChannelHelper.publishChannel(builder.build());

// 3. If there are existing channels, decide whether to update channel contents
PreviewChannelHelper.updatePreviewChannel(channelId, builder.build());

// 4. Delete all programs in the channel
PreviewChannelHelper.deleteAllPreviewProgramsByChannelId(channelId);

// 5. publish new programs in the channel
PreviewChannelHelper.publishPreviewProgram(builder.build());
```

With Engage SDK, cluster and entity publishing are combined into a single API call. All entities that belong to a cluster are published together with that cluster:

**Kotlin**

```kotlin
RecommendationCluster.Builder()
            .addEntity(MOVIE_ENTITY)
            .addEntity(MOVIE_ENTITY)
            .addEntity(MOVIE_ENTITY)
            .setTitle("Top Picks For You")
            .build()
```

**Java**

```java
new RecommendationCluster.Builder()
                        .addEntity(MOVIE_ENTITY)
                        .addEntity(MOVIE_ENTITY)
                        .addEntity(MOVIE_ENTITY)
                        .setTitle("Top Picks For You")
                        .build();
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/watch).
