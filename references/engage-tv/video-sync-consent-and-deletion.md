### Cross-device sync

`SyncAcrossDevices` flag controls whether a user's recommendations cluster data is shared with Google TV and available across their devices such as TV, phone, tablets. In order for the recommendation to work, it must be set to true.

### Obtain consent

The media application must provide a clear setting to enable or disable cross-device syncing. Explain the benefits to the user and store the user's preference once and apply it in `publishRecommendations` Request accordingly. To get the most out of cross-device feature, verify app obtains user consent and enables `SyncAcrossDevices` to `true`.

### Delete the Engage data

To manually delete a user's data from the Google TV server before the standard 60-day retention period, use the `client.deleteClusters()` method. Upon receiving the request, the service deletes all existing Engage data for the account profile, or for the entire account.

The [`DeleteReason`](<https://developer.android.com/reference/com/google/android/engage/service/DeleteReason>) enum defines the reason for data deletion. The following code removes recommendations on logout.

```kotlin
// If the user logs out from your media app, you must make the following call
// to remove recommendations data from the current Google TV device, otherwise,
// the recommendations data persists on the current Google TV device until 60
// days later.
client.deleteClusters(
  DeleteClustersRequest.Builder()
    .setAccountProfile(accountProfile)
    .setDeleteReason(DeleteReason.DELETE_REASON_USER_LOG_OUT)
    .build()
)

// If the user revokes the consent to share data with Google TV, you must make
// the following call to remove recommendations data from all current Google TV
// devices. Otherwise, the recommendations data persists until 60 days later.
client.deleteClusters(
  DeleteClustersRequest.Builder()
    .setAccountProfile(accountProfile)
    .setDeleteReason(DeleteReason.DELETE_REASON_LOSS_OF_CONSENT)
    .build()
)
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/recommendations).
