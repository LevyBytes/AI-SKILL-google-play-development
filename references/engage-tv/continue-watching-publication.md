### Provide Continuation cluster data

`AppEngagePublishClient` is responsible for publishing the Continuation cluster. You use the `publishContinuationCluster` method to publish a `ContinuationCluster` object.

Make sure to initialize the client and check for service availability as described in the [Getting Started guide](<https://developer.android.com/guide/playcore/engage/tv/getting-started#common-integration>).

```kotlin
client.publishContinuationCluster(
    PublishContinuationClusterRequest
        .Builder()
        .setContinuationCluster(
            ContinuationCluster.Builder()
                .setAccountProfile(accountProfile)
                .addEntity(movieEntity1)
                .addEntity(movieEntity2)
                .addEntity(tvEpisodeEntity1)
                .addEntity(tvEpisodeEntity2)
                .setSyncAcrossDevices(true)
                .build()
        )
        .build()
)
```

When the service receives the request, the following actions take place within one transaction:

- Existing `ContinuationCluster` data from the developer partner is removed.
- Data from the request is parsed and stored in the updated `ContinuationCluster`.

In case of an error, the entire request is rejected and the existing state is maintained.

The publish APIs are upsert APIs; it replaces the existing content. If you need to update a specific entity in the continuation cluster, you will need to publish all entities again.

Continuation cluster data should only be provided for adult accounts. Publish only when the account profile belongs to an adult.

> **Warning:** Don't call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

#### Cross-device syncing

`setSyncAcrossDevices` controls whether a user's `ContinuationCluster` data is synchronized across devices such as TV, phone, tablets, etc. Cross-device syncing is disabled by default.

Values:

- `true`: Continuation cluster data is shared across all the user's devices for a seamless viewing experience. We strongly recommend this option for the best cross-device experience.
- `false`: Continuation cluster data is restricted to the current device.

Additionally, you must provide an `AccountProfile` with an account ID in order for the content to be synchronized between devices. See [Create an account profile](<https://developer.android.com/guide/playcore/engage/tv/getting-started#common-integration>).

#### Obtain Consent

The media application must provide a clear setting to enable or disable cross-device syncing. Explain the benefits to the user and store the user's preference once and apply it in `publishContinuationCluster` accordingly.

```kotlin
// Example to allow cross device syncing.
client.publishContinuationCluster(
    PublishContinuationClusterRequest
        .Builder()
        .setContinuationCluster(
            ContinuationCluster.Builder()
                .setAccountProfile(accountProfile)
                .setSyncAcrossDevices(true)
                .build()
        )
        .build()
)
```

To get the most out of our cross-device feature, verify that the app obtains user consent and enable `SyncAcrossDevices` to `true`. This allows content to seamlessly sync across devices, leading to a better user experience and increased engagement. For example, a partner who implemented this saw a 40% increase in "continue watching" clicks because their content was surfaced on multiple devices.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/continue-watching/client).
