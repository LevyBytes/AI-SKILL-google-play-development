Engage SDK offers a REST API to provide a consistent continue watching experience across non-Android platforms such as iOS and Roku TV. The API allows developers to update the "Continue-Watching" status for opted-in users from non-Android platforms.

## Prerequisites

> **Important:** [Express interest in developing with Engage](<http://g.co/tv/engage>).

- You must first finish the [on-device Engage SDK-based](<https://developer.android.com/guide/playcore/engage/tv/continue-watching/client>) integration. This critical step establishes the necessary association between Google's user ID and your app's `AccountProfile`.
- API Access and Authentication: To view and enable the API in your Google Cloud Project, you must go through an allowlist process. All API requests require authentication.

## Gain Access

To gain access to view and enable the API in your Google Cloud Console, your account needs to be enrolled.

1. Google Workspace Customer ID should be available. If not available, you may need to set up a Google Workspace as well as any Google Accounts you want to use to call the API.
2. Set up an account with Google Cloud Console using an email associated with the Google Workspace.
3. [Create a new project](<https://support.google.com/googleapi/answer/6251787?ref_topic=7014522#zippy=%2Ccreate-a-project>).
4. Create a [service account](<https://developers.google.com/identity/protocols/oauth2/service-account>) for API Authentication. Once you create the service account, you will have two items:

   - A service account ID.
   - A JSON file with your service account key. Keep this file secure. You'll need it to authenticate your client to the API later.
5. Workspace and associated Google Accounts can now be able to use REST APIs. Once the change has propagated you will be notified whether the API is ready to be called by your service accounts.
6. Follow these [steps](<https://developers.google.com/identity/protocols/oauth2/service-account#authorizingrequests>) to prepare to make a delegated API call.

## Publish Continuation Cluster

To publish the Engage data, perform a POST request to the `publishContinuationCluster` API using the following syntax.

```text
https://tvvideodiscovery.googleapis.com/v1/packages/{package_name}/accounts/{account_id}/profiles/{profile_id}/publishContinuationCluster
```

Where:

- `package_name`: The media provider package name
- `accountId`: The unique ID for the user's account in your system. It must match the `accountId` used in the on-device path.
- `profileId`: The unique ID for the user's profile within the account in your system. It must match the profileId used in the on-device path.

The URL for the account without profile is:

```text
https://tvvideodiscovery.googleapis.com/v1/packages/{package_name}/accounts/{account_id}/publishContinuationCluster
```

The payload to the request is represented in the `entities` field. `entities` represents a list of content entities, which can consist of one or more of the following: `MovieEntity`, `TVEpisodeEntity`, `LiveStreamingVideoEntity` or `VideoClipEntity`. This is a required field.

### Request Body

| **Field** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| entities | List of MediaEntity Objects | Yes | List of content entities with a maximum of 5. Only the top five will be retained and the rest dropped. An empty list is allowed to signify the user has finished watching all entities. |

Field `entities` contains individual `movieEntity`, `tvEpisodeEntity`, `liveStreamingVideoEntity`, and `videoClipEntity`.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| movieEntity | MovieEntity | An object representing a movie within the ContinuationCluster. |
| tvEpisodeEntity | TvEpisodeEntity | An object representing a TV episode within the ContinuationCluster. |
| liveStreamingVideoEntity | LiveStreamingVideoEntity | An object representing a live streaming video within the ContinuationCluster. |
| videoClipEntity | VideoClipEntity | An object representing a video clip within the ContinuationCluster. |

Each object in the entities array must be one of the available MediaEntity types namely [`MovieEntity`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/MovieEntity>), [`TvEpisodeEntity`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/TvEpisodeEntity>), [`LiveStreamingVideoEntity`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/LiveStreamingVideoEntity>), or [`VideoClipEntity`](<https://developer.android.com/reference/com/google/android/engage/video/datamodel/VideoClipEntity>), along with common and type-specific fields.

The following code snippet showcases the request body payload for the `publishContinuationCluster` API.

[Complete json example: Request Body](<https://developer.android.com/guide/playcore/engage/tv/continue-watching/rest#request-body>).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/continue-watching/rest).
