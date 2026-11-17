Client: `AppEngagePublishClient`. [Setup](setup.md) establishes dependencies; check [service availability](service-availability.md) before publishing. Static manifest registration and [dynamic registration](dynamic-broadcast-receiver.md) are both required.

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
         <action android:name="com.google.android.engage.action.PUBLISH_CONTINUATION" />
      </intent-filter>
   </receiver>
</application>
```

The following [intents](<https://developer.android.com/reference/android/content/Intent>) is sent by the service:

- `com.google.android.engage.action.PUBLISH_RECOMMENDATION` It is recommended to start a `publishRecommendationClusters` call when receiving this intent.
- `com.google.android.engage.action.PUBLISH_FEATURED` It is recommended to start a `publishFeaturedCluster` call when receiving this intent.
- `com.google.android.engage.action.PUBLISH_CONTINUATION` It is recommended to start a `publishContinuationCluster` call when receiving this intent.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/watch).
