## Include review.h

After integrating the Play Core Native SDK into your project, include the following line in files that will contain API calls:

```c
#include "play/review.h"
```

## Initialize the Review API

Whenever you want to use the API, you must initialize it first by calling the [`ReviewManager_init`](<https://developer.android.com/reference/native/play/core/group/review#reviewmanager_init>) function, as shown in the following example built with [`android_native_app_glue.h`](<https://developer.android.com/ndk/guides/concepts#naa>):

```c
void android_main(android_app* app) {
  app->onInputEvent = HandleInputEvent;

  ReviewErrorCode error_code = ReviewManager_init(app->activity->vm, app->activity->clazz);
  if (error_code == REVIEW_NO_ERROR) {
    // You can use the API.
  }
}
```

## Request the in-app review flow

Follow the guidance about [when to request in-app reviews](<https://developer.android.com/guide/playcore/in-app-review#when-to-request>) to determine good points in your app's user flow to prompt the user for a review (for example, after a user dismisses the summary screen at the end of a level in a game). When your app gets close one of these points, call [`ReviewManager_requestReviewFlow`](<https://developer.android.com/reference/native/play/core/group/review#reviewmanager_requestreviewflow>) to asynchronously request the information that your app needs to launch an in-app review flow. Monitor the progress of the `ReviewManager_requestReviewFlow` operation by calling [`ReviewManager_getReviewStatus`](<https://developer.android.com/reference/native/play/core/group/review#reviewmanager_getreviewstatus>), for example once every frame. This might take up to a couple of seconds, so you should start this process before your app reaches the point when you want to show the in-app review flow.

```c
ReviewErrorCode error_code = ReviewManager_requestReviewFlow();
if (error_code == REVIEW_NO_ERROR) {
    // The request has successfully started, check the status using
    // ReviewManager_getReviewStatus.
} else {
    // Error such as REVIEW_PLAY_STORE_NOT_FOUND indicating that the in-app
    // review isn't currently possible.
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-review/native).
