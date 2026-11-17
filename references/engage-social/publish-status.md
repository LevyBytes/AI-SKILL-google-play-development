Client: `AppEngageSocialClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

#### `updatePublishStatus`

If for any internal business reason, none of the clusters is published, we **strongly recommend** updating the publish status using the **updatePublishStatus** API. This is important because :

- Providing the status in all scenarios, even when the content is published (STATUS == PUBLISHED), is critical to populate dashboards that use this explicit status to convey the health and other metrics of your integration.
- If no content is published but the integration status isn't broken (STATUS == NOT_PUBLISHED), Google can avoid triggering alerts in the app health dashboards. It confirms that content is not published due to an **expected** situation from the provider's standpoint.
- It helps developers provide insights into when the data is published versus not.
- Google may use the status codes to nudge the user to do certain actions in the app so they can see the app content or overcome it.

The list of eligible publish status codes are :

```text
// Content is published
AppEngagePublishStatusCode.PUBLISHED,

// Content is not published as user is not signed in
AppEngagePublishStatusCode.NOT_PUBLISHED_REQUIRES_SIGN_IN,

// Content is not published as user is not subscribed
AppEngagePublishStatusCode.NOT_PUBLISHED_REQUIRES_SUBSCRIPTION,

// Content is not published as user location is ineligible
AppEngagePublishStatusCode.NOT_PUBLISHED_INELIGIBLE_LOCATION,

// Content is not published as there is no eligible content
AppEngagePublishStatusCode.NOT_PUBLISHED_NO_ELIGIBLE_CONTENT,

// Content is not published as the feature is disabled by the client
// Available in v1.3.1
AppEngagePublishStatusCode.NOT_PUBLISHED_FEATURE_DISABLED_BY_CLIENT,

// Content is not published as the feature due to a client error
// Available in v1.3.1
AppEngagePublishStatusCode.NOT_PUBLISHED_CLIENT_ERROR,

// Content is not published as the feature due to a service error
// Available in v1.3.1
AppEngagePublishStatusCode.NOT_PUBLISHED_SERVICE_ERROR,

// Content is not published due to some other reason
// Reach out to engage-developers@ before using this enum.
AppEngagePublishStatusCode.NOT_PUBLISHED_OTHER
```

If the content is not published due to a user not logged in, Google would recommend publishing the Sign In Card. If for any reason providers are not able to publish the Sign In Card then we recommend calling the **updatePublishStatus** API with the status code **NOT_PUBLISHED_REQUIRES_SIGN_IN**

**Kotlin**

```kotlin
client.updatePublishStatus(
   PublishStatusRequest.Builder()
     .setStatusCode(AppEngagePublishStatusCode.NOT_PUBLISHED_REQUIRES_SIGN_IN)
     .build())
```

**Java**

```java
client.updatePublishStatus(
    new PublishStatusRequest.Builder()
        .setStatusCode(AppEngagePublishStatusCode.NOT_PUBLISHED_REQUIRES_SIGN_IN)
        .build());
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/social).
