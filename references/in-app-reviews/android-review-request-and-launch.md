## Request a ReviewInfo object

Follow the guidance about [when to request in-app reviews](<https://developer.android.com/guide/playcore/in-app-review#when-to-request>) to determine good points in your app's user flow to prompt the user for a review (for example, when the user completes a level in a game). When your app reaches one of these points, use the [`ReviewManager`](<https://developer.android.com/reference/com/google/android/play/core/review/ReviewManager>) instance to create a request task. If successful, the API returns the [`ReviewInfo`](<https://developer.android.com/reference/com/google/android/play/core/review/ReviewInfo>) object needed to start the in-app review flow.

**Kotlin**

```kotlin
val request = manager.requestReviewFlow()
request.addOnCompleteListener { task ->
    if (task.isSuccessful) {
        // Got the ReviewInfo object
        val reviewInfo = task.result
    } else {
        // There was some problem, log or handle the error code.
        @ReviewErrorCode val reviewErrorCode = (task.getException() as ReviewException).errorCode
    }
}
```

**Java**

```java
ReviewManager manager = ReviewManagerFactory.create(this);
Task<ReviewInfo> request = manager.requestReviewFlow();
request.addOnCompleteListener(task -> {
    if (task.isSuccessful()) {
        // Get the ReviewInfo object
        ReviewInfo reviewInfo = task.getResult();
    } else {
        // There was some problem, log or handle the error code.
        @ReviewErrorCode int reviewErrorCode = ((ReviewException) task.getException()).getErrorCode();
    }
});
```

> **Note:** The [`ReviewInfo`](<https://developer.android.com/reference/com/google/android/play/core/review/ReviewInfo>) object is only valid for a limited amount of time. Your app should request a `ReviewInfo` object ahead of time (pre-cache) but only once you are certain that your app will launch the in-app review flow.

## Launch the in-app review flow

Use the [`ReviewInfo`](<https://developer.android.com/reference/com/google/android/play/core/review/ReviewInfo>) instance to launch the in-app review flow. Wait until the user has completed the in-app review flow before your app continues its normal user flow (such as advancing to the next level).

**Kotlin**

```kotlin
val flow = manager.launchReviewFlow(activity, reviewInfo)
flow.addOnCompleteListener { _ ->
    // The flow has finished. The API doesn't indicate whether the user
    // reviewed or not, or even whether the review dialog was shown. Thus, no
    // matter the result, continue your app flow.
}
```

**Java**

```java
Task<Void> flow = manager.launchReviewFlow(activity, reviewInfo);
flow.addOnCompleteListener(task -> {
    // The flow has finished. The API doesn't indicate whether the user
    // reviewed or not, or even whether the review dialog was shown. Thus, no
    // matter the result, continue your app flow.
});
```

> **Important:** If an error occurs during the in-app review flow, don't inform the user or change your app's normal user flow. Continue your app's normal user flow after `onComplete` is called.

## Next steps

[Test your app's in-app review flow](<https://developer.android.com/guide/playcore/in-app-review/test>) to verify that your integration is working correctly.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-review/kotlin-java).
