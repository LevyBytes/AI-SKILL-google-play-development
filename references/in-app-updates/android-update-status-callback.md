### Get a callback for update status

After starting an update, registered activity result launcher callback gets the confirmation dialog result:

**Kotlin**

```kotlin
registerForActivityResult(StartIntentSenderForResult()) { result: ActivityResult ->
    // handle callback
    if (result.resultCode != RESULT_OK) {
        log("Update flow failed! Result code: " + result.resultCode);
        // If the update is canceled or fails,
        // you can request to start the update again.
    }
}
```

**Java**

```java
registerForActivityResult(
    new ActivityResultContracts.StartIntentSenderForResult(),
    new ActivityResultCallback<ActivityResult>() {
        @Override
        public void onActivityResult(ActivityResult result) {
            // handle callback
            if (result.getResultCode() != RESULT_OK) {
                log("Update flow failed! Result code: " + result.getResultCode());
                // If the update is canceled or fails,
                // you can request to start the update again.
            }
        }
    });
```

There are several values you might receive from the `onActivityResult()` callback:

- [`RESULT_OK`](<https://developer.android.com/reference/android/app/Activity#RESULT_OK>): The user has accepted the update. For immediate updates, you might not receive this callback because the update should already be finished by the time control is given back to your app.
- [`RESULT_CANCELED`](<https://developer.android.com/reference/android/app/Activity#RESULT_CANCELED>): The user has denied or canceled the update.
- [`ActivityResult.RESULT_IN_APP_UPDATE_FAILED`](<https://developer.android.com/reference/com/google/android/play/core/install/model/ActivityResult#RESULT_IN_APP_UPDATE_FAILED>): Some other error prevented either the user from providing consent or the update from proceeding.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java).
