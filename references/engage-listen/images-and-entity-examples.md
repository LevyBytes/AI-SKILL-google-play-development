#### Image specifications

The following table lists the required specifications for image assets:

| Aspect ratio | Requirement | Minimum pixels | Recommended pixels |
| --- | --- | --- | --- |
| Square (1x1) | **Required** | 300x300 | 1200x1200 |
| Landscape (1.91x1) | Optional | 600x314 | 1200x628 |
| Portrait (4x5) | Optional | 480x600 | 960x1200 |

*File formats*

PNG, JPG, static GIF, WebP

*Maximum file size*

5120 KB

*Additional recommendations*

- **Image safe area:** Put your important content in the center 80% of the image.

#### Examples

```java
MusicAlbumEntity musicAlbumEntity =
        new MusicAlbumEntity.Builder()
            .setName(NAME)
             .addPosterImage(new Image.Builder()
                  .setImageUri(Uri.parse("http://www.x.com/image.png"))
                  .setImageHeightInPixel(960)
                  .setImageWidthInPixel(408)
                  .build())
            .setPlayBackUri(Uri.parse("https://play.google/album/play"))
            .setInfoPageUri(Uri.parse("https://play.google/album/info"))
            .setDescription("A description of this album.")
            .addArtist("Artist")
            .addGenre("Genre")
            .addMusicLabel("Label")
            .setSongsCount(960)
            .setReleaseDateEpochMillis(1633032895L)
            .setDurationMillis(1633L)
            .build();
```

```java
AudiobookEntity audiobookEntity =
        new AudiobookEntity.Builder()
            .setName("Becoming")
            .addPosterImage(new Image.Builder()
                 .setImageUri(Uri.parse("http://www.x.com/image.png"))
                 .setImageHeightInPixel(960)
                 .setImageWidthInPixel(408)
                  .build())
            .addAuthor("Michelle Obama")
            .addNarrator("Michelle Obama")
            .setActionLinkUri(
               Uri.parse("https://play.google/audiobooks/1"))
            .setDurationMillis(16335L)
            .setPublishDateEpochMillis(1633032895L)
            .setDescription("An intimate, powerful, and inspiring memoir")
            .setPrice("$16.95")
            .addGenre("biography")
            .build();
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/listen).
