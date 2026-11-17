## Delete the Engage data

Use the `clearCluster` API to remove the Engage data.

To delete the continuation cluster data, perform a POST request to the `clearCluster` API using the following syntax.

```text
https://tvvideodiscovery.googleapis.com/v1/packages/{package_name}/accounts/{account_id}/profiles/{profile_id}/clearCluster
```

Where:

- `package_name`: The media provider package name.
- `accountId`: The unique ID for the user's account in your system. It must match the `accountId` used in the on-device path.
- `profileId`: The unique ID for the user's profile within the account in your system. It must match the profileId used in the on-device path.

The URL for the account without profile is:

```text
https://tvvideodiscovery.googleapis.com/v1/packages/{package_name}/accounts/{account_id}/clearCluster
```

The payload for the `clearCluster` API contains only one field, `reason`, which contains a [`DeleteReason`](<https://developer.android.com/reference/com/google/android/engage/service/DeleteReason>) that specifies the reason for removing data.

```json
{
  "reason": "DELETE_REASON_LOSS_OF_CONSENT"
}
```

## Testing

After successfully posting data, use a user test account to verify that the expected content appears in the continue watching row on target Google surfaces such as Google TV and the Android and iOS Google TV mobile apps.

In testing, allow a reasonable propagation delay of a few minutes and adhere to the watch requirements, such as watching part of a movie or finishing an episode. Consult the [Watch Next guidelines for app developers](<https://developer.android.com/training/tv/discovery/guidelines-app-developers#unfinished-movies>) for details.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/continue-watching/rest).
