Client: `AppEngagePublishClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `publishUserAccountManagementRequest`

This API is used to publish a Sign In card . The signin action directs users to the app's sign in page so that the app can publish content (or provide more personalized content)

The following metadata is part of the Sign In Card -

| Attribute | Requirement | Description |
| --- | --- | --- |
| Action Uri | Required | Deeplink to Action (i.e. navigates to app sign in page) |
| Image | Optional - If not provided, Title must be provided | Image Shown on the Card 16x9 aspect ratio images with a resolution of 1264x712 |
| Title | Optional - If not provided, Image must be provided | Title on the Card |
| Action Text | Optional | Text Shown on the CTA (i.e. Sign in) |
| Subtitle | Optional | Optional Subtitle on the Card |

> **Important:** The publish APIs are upsert APIs; it replaces the existing content. **Don't** call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

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

client.publishUserAccountManagementRequest(
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

client.publishUserAccountManagementRequest(
            new PublishUserAccountManagementRequest.Builder()
                .setSignInCardEntity(SIGN_IN_CARD_ENTITY)
                .build());
```

When the service receives the request, the following actions take place within one transaction:

- Existing `UserAccountManagementCluster` data from the developer partner is removed.
- Data from the request is parsed and stored in the updated UserAccountManagementCluster Cluster.

In case of an error, the entire request is rejected and the existing state is maintained.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/watch).
