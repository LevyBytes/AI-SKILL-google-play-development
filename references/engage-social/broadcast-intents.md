Client: `AppEngageSocialClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

### Step 3: Handle broadcast intents

In addition to making publish content API calls through a job, it is also required to set up a [`BroadcastReceiver`](<https://developer.android.com/reference/android/content/BroadcastReceiver>) to receive the request for a content publish.

The goal of broadcast intents is mainly for app reactivation and forcing data sync. Broadcast intents are not designed to be sent very frequently. It is only triggered when the Engage Service determines the content might be stale (for example, a week old). That way, there is more confidence that the user can have a fresh content experience, even if the application has not been executed for a long period of time.

The `BroadcastReceiver` must be set up in the following two ways:

- Dynamically register an instance of the `BroadcastReceiver` class using `Context.registerReceiver()`. This enables communication from applications that are still live in memory.

**Kotlin**

```kotlin
class AppEngageBroadcastReceiver : BroadcastReceiver(){
  // Trigger recommendation cluster publish when PUBLISH_RECOMMENDATION
  // broadcast is received
}

fun registerBroadcastReceivers(context: Context){
  var  context = context
  context = context.applicationContext

// Register Recommendation Cluster Publish Intent
  context.registerReceiver(AppEngageBroadcastReceiver(),
                           IntentFilter(Intents.ACTION_PUBLISH_RECOMMENDATION),
                           com.google.android.engage.service.BroadcastReceiverPermissions.BROADCAST_REQUEST_DATA_PUBLISH_PERMISSION,
                           /*scheduler=*/null)
}
```

**Java**

```java
class AppEngageBroadcastReceiver extends BroadcastReceiver {
// Trigger recommendation cluster publish when PUBLISH_RECOMMENDATION broadcast
// is received
}

public static void registerBroadcastReceivers(Context context) {

context = context.getApplicationContext();

// Register Recommendation Cluster Publish Intent
context.registerReceiver(new AppEngageBroadcastReceiver(),
                         new IntentFilter(com.google.android.engage.service.Intents.ACTION_PUBLISH_RECOMMENDATION),
                         com.google.android.engage.service.BroadcastReceiverPermissions.BROADCAST_REQUEST_DATA_PUBLISH_PERMISSION,
                         /*scheduler=*/null);
}
```

- Statically declare an implementation with the `<receiver>` tag in your `AndroidManifest.xml` file. This allows the application to receive broadcast intents when it is not running, and also allows the application to publish the content.

```xml
<application>
   <receiver
      android:name=".AppEngageBroadcastReceiver"
      android:permission="com.google.android.engage.REQUEST_ENGAGE_DATA"
      android:exported="true"
      android:enabled="true">
      <intent-filter>
         <action android:name="com.google.android.engage.action.PUBLISH_RECOMMENDATION" />
      </intent-filter>
   </receiver>
</application>

```

The following [intents](<https://developer.android.com/reference/android/content/Intent>) will be sent by the service:

- `com.google.android.engage.action.PUBLISH_RECOMMENDATION` It is recommended to start a `publishRecommendationClusters` call when receiving this intent.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/social).
