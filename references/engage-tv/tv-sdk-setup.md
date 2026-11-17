[Engage SDK](<https://developer.android.com/guide/playcore/engage>) lets you deliver personalized recommendations and continuation content directly to users on Google TV.

This guide covers how to get started with Engage SDK integrations for TV. After you complete the pre-work on this page, you can integrate one or more of the TV features:

- [Publish continue watching data](<https://developer.android.com/guide/playcore/engage/tv/continue-watching>)
- [Publish device entitlements](<https://developer.android.com/guide/playcore/engage/tv/entitlements>)
- [Publish recommendations](<https://developer.android.com/guide/playcore/engage/tv/recommendations>)

## Pre-work

Before you begin, complete the following steps:

1. [Express interest in developing with Engage SDK](<http://g.co/tv/engage>) to enroll in the program, if eligible.
2. Verify that your app targets Android 4.4 (API level 19) or higher for this integration.
3. Add the `com.google.android.engage` library to your app:

   There are separate SDKs to use in the integration: one for mobile apps and one for TV apps.

   ### Mobile

   ```groovy
   dependencies {
     implementation 'com.google.android.engage:engage-core:1.6.0'
   }
   ```

   ### TV

   ```groovy
   dependencies {
     implementation 'com.google.android.engage:engage-tv:1.1.0'
   }
   ```
4. Add permission for `WRITE_EPG_DATA` for TV APK

   ```xml
   <uses-permission android:name="com.android.providers.tv.permission.WRITE_EPG_DATA" />
   ```
5. Verify reliable content publishing by using a background service, such as `androidx.work`, for scheduling.
6. Test your implementation using the verification app as outlined in the [Testing section](<https://developer.android.com/guide/playcore/engage/tv/getting-started?hl=en#testing>).
7. In your production app, set the Engage service environment to production by adding the `<meta-data>` element directly under the `<application>` tag in your `AndroidManifest.xml` file. Don't place this tag inside an `<activity>`.

   ```xml
   <application ...>
       <!-- Other application configurations -->

       <meta-data
           android:name="com.google.android.engage.service.ENV"
           android:value="PRODUCTION" />
   </application>
   ```

   > **Important:** The Engage service environment declaration is only needed for your release build. For your local testing with the verification app, don't include this element.

## Common integration steps

### Initialize the client

Use `AppEngagePublishClient` to interact with the service. Always check if the service is available before publishing.

You can check the service availability for every cluster type that you intend to publish. The `isServiceAvailable` API accepts a request object, `ServiceAvailabilityRequest`, which contains the cluster types for which service availability needs to be checked. You can find the `ClusterType` enum values required for `ServiceAvailabilityRequest` from the following table.

| Cluster Type | Cluster Type Constant | Integer Value |
| --- | --- | --- |
| Unknown | `TYPE_UNKNOWN` | 0 |
| Recommendation Cluster | `TYPE_RECOMMENDATION` | 1 |
| Continuation Cluster | `TYPE_CONTINUATION` | 3 |

```kotlin
val client = AppEngagePublishClient(context)

val request = ServiceAvailabilityRequest.Builder()
    .addIntendedClusterType(ClusterType.TYPE_CONTINUATION)
    .addIntendedClusterType(ClusterType.TYPE_RECOMMENDATION)
    .build()

client.isServiceAvailable(request).addOnCompleteListener { task ->
  if (task.isSuccessful) {
    val availabilityMap = task.result
    if (availabilityMap[ClusterType.TYPE_CONTINUATION] == true) {
      // Proceed with publishing continuation content
    }
    if (availabilityMap[ClusterType.TYPE_RECOMMENDATION] == true) {
      // Proceed with publishing recommendation content
    }
  } else {
    // Service is not available or call failed
  }
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/getting-started).
