### Provide subscription set

Run the content publish job while the app is in the foreground.

Use the `publishSubscriptionCluster()` method, from the `AppEngagePublishClient` class, to publish a `SubscriptionCluster` object.

Make sure to initialize the client and check for service availability as described in the [Getting Started guide](<https://developer.android.com/guide/playcore/engage/tv/getting-started#common-integration>).

```kotlin
client.publishSubscription(
  PublishSubscriptionRequest.Builder()
    .setAccountProfile(accountProfile)
    .setSubscription(subscription)
    .build()
)
```

Use `setSubscription()` to verify that user should have only one subscription to the service.

Use `addLinkedSubscription()`, or `addLinkedSubscriptions()` which accept a list of linked subscriptions, to enable user to have zero or more linked subscriptions.

When the service receives the request, a new entry is created and the old entry is automatically deleted after 60 days. The system always uses the latest entry. In case of an error, the entire request is rejected and the existing state is maintained.

### Keep subscription up-to-date

1. To provide immediate updates upon changes, call `publishSubscriptionCluster` whenever a user's subscription state changes like activation, deactivation, upgrades, downgrades.
2. To provide regular validation for ongoing accuracy, call `publishSubscriptionCluster` at least once per month.

   > **Note:** As Google TV automatically deletes historical data beyond 60 days to safeguard user privacy, publishing user subscription data at least once per month verify the validity of data. Unlike `publishContinuationCluster` for continue watching data, don't set `syncAcrossDevices` flag, as subscription information is by default used to provide content across all devices.
3. To delete the Engage data, manually delete a user's data from the Google TV server before the standard 60-day retention period, use the `client.deleteClusters` method. This deletes all existing Engage data for the account profile, or for the entire account depending on the given [`DeleteReason`](<https://developer.android.com/reference/com/google/android/engage/service/DeleteReason>).

   The following code snippet shows how to remove a user subscription:

   ```kotlin
   // If the user logs out from your media app, you must make the following call
   // to remove subscription and other Engage data from the current
   // google TV device.
   client.deleteClusters(
     DeleteClustersRequest.Builder()
       .setAccountProfile(accountProfile)
       .setDeleteReason(DeleteReason.DELETE_REASON_USER_LOG_OUT)
       .build()
   )
   ```

   The following code snippet demonstrates removal of user subscription when user revokes the consent:

   ```kotlin
   // If the user revokes the consent to share across device, make the call
   // to remove subscription and other Engage data from all google
   // TV devices.
   client.deleteClusters(
     DeleteClustersRequest.Builder()
       .setAccountProfile(accountProfile)
       .setDeleteReason(DeleteReason.DELETE_REASON_LOSS_OF_CONSENT)
       .build()
   )
   ```

   Following code demonstrates how to remove subscription data on user profile deletion.

   ```kotlin
   // If the user delete a specific profile, you must make the following call
   // to remove subscription data and other Engage data.
   client.deleteClusters(
     DeleteClustersRequest.Builder()
       .setAccountProfile(accountProfile)
       .setDeleteReason(DeleteReason.DELETE_REASON_ACCOUNT_PROFILE_DELETION)
       .build()
   )
   ```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/entitlements).
