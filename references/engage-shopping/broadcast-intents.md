Client: `AppEngageShoppingClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing.

### Step 3: Handle broadcast intents

In addition to making publish content API calls through a job, it is also required to set up a [`BroadcastReceiver`](<https://developer.android.com/reference/android/content/BroadcastReceiver>) to receive the request for a content publish.

The goal of broadcast intents is mainly for app reactivation and forcing data sync. Broadcast intents are not designed to be sent very frequently. It is only triggered when the Engage Service determines the content might be stale (for example, a week old). That way, there is more confidence that the user can have a fresh content experience, even if the application has not been executed for a long period of time.

The `BroadcastReceiver` must be set up in the following two ways:

- Dynamically register an instance of the `BroadcastReceiver` class using `Context.registerReceiver()`. This enables communication from applications that are still live in memory.

**Kotlin**

[Complete kotlin example: Step 3: Handle broadcast intents](<https://developer.android.com/guide/playcore/engage/shopping#broadcast-intents>).

**Java**

[Complete java example: Kotlin](<https://developer.android.com/guide/playcore/engage/shopping#kotlin_19>).

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
      <intent-filter>
         <action android:name="com.google.android.engage.action.PUBLISH_FEATURED" />
      </intent-filter>
      <intent-filter>
         <action android:name="com.google.android.engage.action.shopping.PUBLISH_SHOPPING_CART" />
      </intent-filter>
      <intent-filter>
         <action android:name="com.google.android.engage.action.shopping.PUBLISH_SHOPPING_LIST" />
      </intent-filter>
      <intent-filter>
         <action android:name="com.google.android.engage.action.shopping.PUBLISH_REORDER_CLUSTER" />
      </intent-filter>
      <intent-filter>
         <action android:name="com.google.android.engage.action.shopping.PUBLISH_SHOPPING_ORDER_TRACKING_CLUSTER" />
      </intent-filter>
   </receiver>
</application>
```

The following [intents](<https://developer.android.com/reference/android/content/Intent>) are sent by the service:

- `com.google.android.engage.action.PUBLISH_RECOMMENDATION` It is recommended to start a `publishRecommendationClusters` call when this intent is received.
- `com.google.android.engage.action.PUBLISH_FEATURED` It is recommended to start a `publishFeaturedCluster` call when this intent is received.
- `com.google.android.engage.action.shopping.PUBLISH_SHOPPING_CART` It is recommended to start a `publishShoppingCarts` call when this intent is received.
- `com.google.android.engage.action.shopping.PUBLISH_SHOPPING_LIST` It is recommended to start a `publishShoppingLists` call when this intent is received.
- `com.google.android.engage.action.shopping.PUBLISH_REORDER_CLUSTER` It is recommended to start a `publishReorderCluster` call when this intent is received.
- `com.google.android.engage.action.shopping.PUBLISH_SHOPPING_ORDER_TRACKING_CLUSTER` It is recommended to start a `publishShoppingOrderTrackingCluster` call when this intent is received.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/shopping).
