This guide includes a set of guidelines for cluster publishing that developers can use when integrating with Engage SDK.

## Recommendation clusters

### Cluster Title

We recommend providing a unique and relevant cluster title that gives users more insight on the content of the cluster.

Here are some examples of good cluster titles based on the content:

- Shopping-related clusters

  - *Lightning Deals*
  - *Weekly must buys*
  - *Related to your purchase of Pixel Buds*
  - *Women's rain boots*
- Clusters of books on health

  - *Health, mind & body*
  - *Recommended for you in Health*
  - *Best-sellers in Fitness*

### Cluster Content

When publishing recommendation clusters, developers must consider whether or not the user is signed in to the developer's application.

### When user is signed in

If the user is signed in to the developer app, we recommend publishing personalized or user-generated content clusters. Because personalized and user-generated content is more relevant to the user, they are more motivated to visit the developer app from the Google surface.

- Personalized recommendations can be published.

  - Here are some examples of personalized recommendations:

    - Top picks based on the user's watch history.
    - Books similar to books that are in the user's read history.
    - Songs by the user's favorite artists.
- User-generated content libraries can be published.

  - Here are some examples of user-generated content libraries:

    - The user's watchlist from the developer app.
    - A self-reported list of the user's favorite artists from the developer app.

| Recommendation type | Content freshness strategy | Content freshness guideline |
| --- | --- | --- |
| Personalized recommendations | **Lenient** We recommend updating the recommendations once per day so users can see new recommendations daily. | Because users don't have an exact expectation of what the recommendation content will be, the content freshness strategy can be lenient. |
| User-generated content libraries | **Strict** We recommend updating the content library as users exit the developer app. | It's important for this content to be in sync with the data displayed on Google surfaces. This is because unlike personalized recommendations, the user expects an exact set of content. Any significant delay in publishing will confuse users. Therefore, the content freshness strategy must be strict. |

### When user is not signed in

If a user is not signed in to the developer app, we still recommend publishing clusters so that users are encouraged to visit the developer app from the Google surface.

- Non-personalized recommendation clusters should be published.

  - Here are some examples of non-personalized recommendations:

    - Top 10 books read this year.
    - Newly released movies.
    - Trending podcasts.
- Publish a sign-in card.

  - In order to encourage users to sign in to the developer app, developers may choose to publish a sign-in card along with the non-personalized recommendation cluster. Check out the section below for more details on how to publish a [Sign In Card](<https://developer.android.com/guide/playcore/engage/publish?hl=en#user-management-cluster-signin>).

| Recommendation type | Content freshness strategy | Content freshness guideline |
| --- | --- | --- |
| Non-personalized recommendations | **Lenient** We recommend updating the recommendations once per day. | Because users don't have an exact expectation of what the recommendation content will be, the content freshness strategy can be lenient. |
| Sign-in card in recommendations | **Strict** We recommend updating the sign-in card state as users exit the developer app. After users have signed in, developers must delete the card by calling the `deleteUserManagementCluster()` API. | It's important for the sign-in state to be in sync with the Google surface. It's confusing for a user to see a sign-in card on Google's surface when they're already signed in. Therefore, the content freshness strategy must be strict. |

## Continuation clusters

When publishing continuation clusters, developers must consider whether or not the user is signed in to the developer's application.

### When user is signed in

- User-generated continuation clusters should be published.

  - Here are some examples of user-generated continuation clusters:

    - Continue Watching from where the user left off.
    - Continue Reading from where the user left off.

| Continuation type | Content freshness strategy | Content freshness guideline |
| --- | --- | --- |
| User-generated continuation clusters | **Strict** We recommend updating the content library as users exit the developer app. | It's important for this content to be in sync with the data displayed on Google's surfaces. This is because unlike personalized recommendations, the user expects an exact set of content. Any significant delay in publishing will confuse users. Therefore, the content freshness strategy must be strict. |

### When user is not signed in

Continuation journeys are primarily intended for signed-in users; however, you can also publish continuation clusters for signed-out users if your app supports guest sessions.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/publish).
