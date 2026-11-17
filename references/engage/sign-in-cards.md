## User Management Cluster

The main aim of the User Management Cluster is to nudge users to perform certain actions on the provider app. The signin action directs users to the app's sign in page so that the app can publish content (or provide more personalized content)

### Sign In Card

| Attribute | Requirement | Description |
| --- | --- | --- |
| Action Uri | Required | Deeplink to Action (i.e. navigates to app sign in page) |
| Image | Optional - If not provided, Title must be provided | Image Shown on the Card 16x9 aspect ratio images with a resolution of 1264x712 |
| Title | Optional - If not provided, Image must be provided | Title on the Card |
| Action Text | Optional | Text Shown on the CTA (i.e. Sign in) |
| Subtitle | Optional | Optional Subtitle on the Card |

**Kotlin**

```kotlin
var SIGN_IN_CARD_ENTITY =
      SignInCardEntity.Builder()
          .addPosterImage(
              Image.Builder()
                  .setImageUri(Uri.parse("http://www.x.com/image.png"))
                  .setImageHeightInPixel(500)
                  .setImageWidthInPixel(500)
                  .build())
          .setActionText("Sign In")
          .setActionUri(Uri.parse("http://xx.com/signin"))
          .build()

appEngagePublishClient.publishUserAccountManagementRequest(
            PublishUserAccountManagementRequest.Builder()
                .setSignInCardEntity(SIGN_IN_CARD_ENTITY)
                .build());
```

**Java**

```java
SignInCardEntity SIGN_IN_CARD_ENTITY =
      new SignInCardEntity.Builder()
          .addPosterImage(
              new Image.Builder()
                  .setImageUri(Uri.parse("http://www.x.com/image.png"))
                  .setImageHeightInPixel(500)
                  .setImageWidthInPixel(500)
                  .build())
          .setActionText("Sign In")
          .setActionUri(Uri.parse("http://xx.com/signin"))
          .build();

appEngagePublishClient.publishUserAccountManagementRequest(
            new PublishUserAccountManagementRequest.Builder()
                .setSignInCardEntity(SIGN_IN_CARD_ENTITY)
                .build());
```

After users have signed in, developers must delete the card by calling the `deleteUserManagementCluster()` API.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/publish).
