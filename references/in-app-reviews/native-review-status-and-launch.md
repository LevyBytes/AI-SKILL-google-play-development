## Handle statuses and launch the in-app review flow

Whenever a request has started or the in-app review flow is launched, you can check the status using [`ReviewManager_getReviewStatus`](<https://developer.android.com/reference/native/play/core/group/review#reviewmanager_getreviewstatus>). This lets you define the logic depending on the API status. One way to approach this is to keep the status as a global variable and check whether the status is `REVIEW_REQUEST_FLOW_COMPLETED` when the user performs a certain action (for example, tapping a "Next Level" button in a game), as shown in the following example:

```c
ReviewStatus status;
ReviewErrorCode error_code = ReviewManager_getReviewStatus(&status);
if (error_code != REVIEW_NO_ERROR) {
    // There was an error with the most recent operation.
    return;
}

switch (status) {
    case REVIEW_REQUEST_FLOW_PENDING:
        // Request is ongoing. The flow can't be launched yet.
        break;
    case REVIEW_REQUEST_FLOW_COMPLETED:
        // Request completed. The flow can be launched now.
        break;
    case REVIEW_LAUNCH_FLOW_PENDING:
        // The review flow is ongoing, meaning the dialog might be displayed.
        break;
    case REVIEW_LAUNCH_FLOW_COMPLETED:
        // The review flow has finished. Continue with your app flow (for
        // example, move to the next screen).
        break;
    default:
        // Unknown status.
        break;
}
```

When the status is `REVIEW_REQUEST_FLOW_COMPLETED` and your app is ready, launch the in-app review flow:

```c
// This call uses android_native_app_glue.h.
ReviewErrorCode error_code = ReviewManager_launchReviewFlow(app->activity->clazz);
if (error_code != REVIEW_NO_ERROR) {
    // There was an error while launching the flow.
    return;
}
```

After launching the in-app review flow, keep checking the status for completion and continue with your app flow. A common way to handle this, would be by following the [Game Loop](<https://developer.android.com/games/develop/gameloops>) pattern.

## Free resources

Don't forget to free resources by calling the [`ReviewManager_destroy`](<https://developer.android.com/reference/native/play/core/group/review#reviewmanager_destroy>) function once your app has finished using the API (for example, after the in-app review flow is completed).

```c
void ReviewManager_destroy();
```

## Next steps

[Test your app's in-app review flow](<https://developer.android.com/guide/playcore/in-app-review/test>) to verify that your integration is working correctly.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-review/native).
