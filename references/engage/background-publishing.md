## WorkManager for cluster publishing

We recommend using [WorkManager](<https://developer.android.com/develop/background-work/background-tasks/persistent>) to publish clusters, because it is the recommended solution for background work where the execution must be both opportunistic and reliable.

- WorkManager performs your background work as soon as it can.
- WorkManager handles the logic to start your work under a variety of conditions, even if a user navigates away from your app.

When the user navigates away from the app, we recommend starting a background job that publishes continuation clusters along with recommendation clusters. A good place to handle this logic is [`Activity.onStop()`](<https://developer.android.com/reference/android/app/Activity#onStop()>), which is called when the user navigates away from the app.

We suggest using [`PeriodicWorkRequest`](<https://developer.android.com/reference/androidx/work/PeriodicWorkRequest>) to schedule a recurring job that publishes clusters every 24 hours. By using a [`CANCEL_AND_REENQUEUE`](<https://developer.android.com/reference/androidx/work/ExistingPeriodicWorkPolicy#CANCEL_AND_REENQUEUE>) policy for triggering the work, developers can ensure that WorkManager sends the updated data every time a user navigates away from the app. This helps prevent users from seeing stale data.

The following example demonstrates this:

[Complete java example: WorkManager for cluster publishing](<https://developer.android.com/guide/playcore/engage/publish#workmanager>).

## Handle broadcast intents

In addition to making publish content API calls through a job, it is also required to set up a [`BroadcastReceiver`](<https://developer.android.com/reference/android/content/BroadcastReceiver>) to receive the request for a content publish.

However, **developers must be careful not to rely solely on broadcasts**, because they are only triggered in certain scenarios, mainly, for app reactivation and forcing a data sync. **They are only triggered when the Engage Service determines that the content might be stale.** That way, there is greater confidence that the user will have a fresh content experience, even if the application has not been opened for a long time.

The `BroadcastReceiver` must be set up in the following two ways:

- Dynamically register an instance of the `BroadcastReceiver` class using `Context.registerReceiver()`. This enables communication from applications that are still live in memory.
- Statically declare an implementation with the `<receiver>` tag in your `AndroidManifest.xml` file. This allows the application to receive broadcast intents when it is not running, and also allows the application to publish the content.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/publish).
