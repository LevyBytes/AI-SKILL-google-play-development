Client: `AppEngagePublishClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing. Dynamic registration and [static manifest registration](static-broadcast-receiver.md) are both required.

### Step 3: Handle broadcast intents

In addition to making publish content API calls through a job, it is also required to set up a [`BroadcastReceiver`](<https://developer.android.com/reference/android/content/BroadcastReceiver>) to receive the request for a content publish.

The goal of broadcast intents is mainly for app reactivation and forcing data sync. Broadcast intents are not designed to be sent very frequently. It is only triggered when the Engage Service determines the content might be stale (for example, a week old). That way, there is more confidence that the user can have a fresh content experience, even if the application has not been executed for a long period of time.

The `BroadcastReceiver` must be set up in the following two ways:

- Dynamically register an instance of the `BroadcastReceiver` class using `Context.registerReceiver()`. This enables communication from applications that are still live in memory.

**Kotlin**

```kotlin
class AppEngageBroadcastReceiver : BroadcastReceiver(){
  // Trigger recommendation cluster publish when PUBLISH_RECOMMENDATION broadcast
  // is received
  // Trigger featured cluster publish when PUBLISH_FEATURED broadcast is received
  // Trigger continuation cluster publish when PUBLISH_CONTINUATION broadcast is
  // received
}

fun registerBroadcastReceivers(context: Context){
  var  context = context
  context = context.applicationContext

// Register Recommendation Cluster Publish Intent
  context.registerReceiver(AppEngageBroadcastReceiver(),
                           IntentFilter(Intents.ACTION_PUBLISH_RECOMMENDATION),
                           com.google.android.engage.service.BroadcastReceiverPermissions.BROADCAST_REQUEST_DATA_PUBLISH_PERMISSION,
                           /*scheduler=*/null)

// Register Featured Cluster Publish Intent
  context.registerReceiver(AppEngageBroadcastReceiver(),
                           IntentFilter(Intents.ACTION_PUBLISH_FEATURED),
                           com.google.android.engage.service.BroadcastReceiverPermissions.BROADCAST_REQUEST_DATA_PUBLISH_PERMISSION,
                           /*scheduler=*/null)

// Register Continuation Cluster Publish Intent
  context.registerReceiver(AppEngageBroadcastReceiver(),
                           IntentFilter(Intents.ACTION_PUBLISH_CONTINUATION),
                           com.google.android.engage.service.BroadcastReceiverPermissions.BROADCAST_REQUEST_DATA_PUBLISH_PERMISSION,
                           /*scheduler=*/null)
}
```

**Java**

```java
class AppEngageBroadcastReceiver extends BroadcastReceiver {
// Trigger recommendation cluster publish when PUBLISH_RECOMMENDATION broadcast
// is received

// Trigger featured cluster publish when PUBLISH_FEATURED broadcast is received

// Trigger continuation cluster publish when PUBLISH_CONTINUATION broadcast is
// received
}

public static void registerBroadcastReceivers(Context context) {

context = context.getApplicationContext();

// Register Recommendation Cluster Publish Intent
context.registerReceiver(new AppEngageBroadcastReceiver(),
                         new IntentFilter(com.google.android.engage.service.Intents.ACTION_PUBLISH_RECOMMENDATION),
                         com.google.android.engage.service.BroadcastReceiverPermissions.BROADCAST_REQUEST_DATA_PUBLISH_PERMISSION,
                         /*scheduler=*/null);

// Register Featured Cluster Publish Intent
context.registerReceiver(new AppEngageBroadcastReceiver(),
                         new IntentFilter(com.google.android.engage.service.Intents.ACTION_PUBLISH_FEATURED),
                         com.google.android.engage.service.BroadcastReceiverPermissions.BROADCAST_REQUEST_DATA_PUBLISH_PERMISSION,
                         /*scheduler=*/null);

// Register Continuation Cluster Publish Intent
context.registerReceiver(new AppEngageBroadcastReceiver(),
                         new IntentFilter(com.google.android.engage.service.Intents.ACTION_PUBLISH_CONTINUATION),
                         com.google.android.engage.service.BroadcastReceiverPermissions.BROADCAST_REQUEST_DATA_PUBLISH_PERMISSION,
                         /*scheduler=*/null);

}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/read).
