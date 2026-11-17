The [module configuration](on-demand-configuration.md) and [install request](on-demand-request.md) establish the delivery context for this operation.

### Obtain user confirmation

In some cases, Google Play may require user confirmation before satisfying a download request. For example, if your app has not been installed by Google Play or if you are attempting a large download over mobile data. In such cases, the status for the request reports `REQUIRES_USER_CONFIRMATION`, and your app needs to obtain user confirmation before the device is able to download and install the modules in the request. To obtain confirmation, your app should prompt the user as follows:

**Kotlin**

```kotlin
override fun onSessionStateUpdate(state: SplitInstallSessionState) {
    if (state.status() == SplitInstallSessionStatus.REQUIRES_USER_CONFIRMATION) {
        // Displays a confirmation for the user to confirm the request.
        splitInstallManager.startConfirmationDialogForResult(
          state,
          // an activity result launcher registered via registerForActivityResult
          activityResultLauncher)
    }
    ...
 }
```

**Java**

```java
@Override void onSessionStateUpdate(SplitInstallSessionState state) {
    if (state.status() == SplitInstallSessionStatus.REQUIRES_USER_CONFIRMATION) {
        // Displays a confirmation for the user to confirm the request.
        splitInstallManager.startConfirmationDialogForResult(
          state,
          // an activity result launcher registered via registerForActivityResult
          activityResultLauncher);
    }
    ...
 }
```

You can register an activity result launcher using the builtin [`ActivityResultContracts.StartIntentSenderForResult`](<https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.StartIntentSenderForResult>) contract. See [Activity Result APIs](<https://developer.android.com/training/basics/intents/result>).

The status for the request is updated depending on the user response:

- If the user accepts the confirmation, the request status changes to `PENDING` and the download proceeds.
- If the user denies the confirmation, the request status changes to `CANCELED`.
- If the user does not make a selection before the dialog is destroyed, the request status remains as `REQUIRES_USER_CONFIRMATION`. Your app can prompt the user again to complete the request.

To receive a callback with the user's response, you can override the ActivityResultCallback as shown below.

**Kotlin**

```kotlin
registerForActivityResult(StartIntentSenderForResult()) { result: ActivityResult -> {
        // Handle the user's decision. For example, if the user selects "Cancel",
        // you may want to disable certain functionality that depends on the module.
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
            // Handle the user's decision. For example, if the user selects "Cancel",
            // you may want to disable certain functionality that depends on the module.
        }
    });
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/feature-delivery/on-demand).
