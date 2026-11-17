#### Delete the Engage data

To manually delete a user's data from the Google TV server before the standard 60-day retention period, use the `deleteClusters` method. Upon receiving the request, the service will delete all existing Engage data for the account profile, or for the entire account.

> **Important:** It is important to set syncAcrossDevices flag to true even in the delete requests so that the data is deleted from the server (even when the delete reason is USER_LOGOUT).

The [`DeleteReason`](<https://developer.android.com/reference/com/google/android/engage/service/DeleteReason>) enum defines the reason for data deletion. The following code removes continue watching data on logout.

```kotlin

// If the user logs out from your media app, you must make the following call
// to remove continue watching data from the current google TV device,
// otherwise, the continue watching data will persist on the current
// google TV device until 60 days later.
client.deleteClusters(
    DeleteClustersRequest.Builder()
        .setAccountProfile(accountProfile)
        .setDeleteReason(DeleteReason.DELETE_REASON_USER_LOG_OUT)
        .setSyncAcrossDevices(true)
        .build()
)
```

> **Warning:** Don't call delete and publish APIs subsequently to replace the content as the publish APIs do that inherently.

## Testing

Use the [verification app](<https://developer.android.com/guide/playcore/engage/tv/getting-started#testing>) to verify that Engage SDK integration is working correctly.

> **Note:** Check if your app is correctly calling `isServiceAvailable` and `publishClusters` APIs in logcat. Before submitting the APK, check if you are able to see `publishClusters` is called logs in your logcat during development to verify that you are calling the APIs at the correct events.

After you invoke the publish API, confirm that your data is being correctly published by checking the verification app. Your continuation cluster should be displayed as a distinct row within the app's interface.

- Test these actions in your app:

  - Sign in.
  - Switch between profiles(if applicable).
  - Start, then pause a video, or return to the home page.
  - Close the app during video playback.
  - Remove an item from the "Continue Watching" row (if supported).
- After each action, confirm that your app invoked the `publishContinuationClusters` API and that the data is correctly displayed in the verification app.
- The verification app shows a green "All Good" check mark for correctly implemented entities.

  ![Verification App Success Screenshot](<https://developer.android.com/static/images/guide/playcore/engage/va-success.png>)

  **Figure 1.** Verification App Success
- The verification app will flag any problematic entities.

  ![Verification App Error Screenshot](<https://developer.android.com/static/images/guide/playcore/engage/va-error.png>)

  **Figure 2.** Verification App Error
- To troubleshoot entities with errors, use your TV remote to select and click the entity in the verification app. The specific problems will be displayed and highlighted in red for your review (see example below).

  ![Verification App error details](<https://developer.android.com/static/images/guide/playcore/engage/va-error-details.png>)

  **Figure 3.** Verification App Error Details

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/continue-watching/client).
