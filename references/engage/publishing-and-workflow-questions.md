## Publish FAQs

#### Who manages the content publishing job?

The app developer manages the content publishing job and sends requests to the Engage Service. In this way, developer partners have more control over when and how to publish content to the users. This avoids waking up the partner app too frequently to publish content.

#### Does a developer need to publish all cluster types?

While technically developers are free to publish just one cluster, we **strongly advise** including more. Otherwise, developers miss the opportunity to drive better engagement with their content. We **highly recommend** publishing all cluster types for each vertical.

#### How often should the developer partner be publishing data using the work manager while the app is running?

This is to be decided by the developer partner. Google recommends publishing once or twice per day for general recommendation content, and to use an event-driven methodology for shopping cart, reorder, and other continuation content (for example, start the worker as a callback of the user adding items to the cart or the user stopping a movie halfway). For **social** apps, it's critical to publish updated recommendation clusters **after each app usage**. Social app users are more interested in the most recent recommendations and ideally would like to see a post at most once.

#### When should the developer call delete APIs?

Delete APIs should only be called when there is no content to publish. **Don't** call delete and publish APIs subsequently to replace content; the publish APIs remove the earlier content automatically.

## Broadcast Intent FAQs

#### Why do Android app developers need to register for broadcast intents?

In order to serve fresh content to the user, you should use broadcast intents to trigger a data sync in cases where users might not use the app frequently.

#### Unable to test broadcast intent

The verification app doesn't support testing broadcast intent with permission. You have to remove permissions while testing and add them back before switching the SDK to prod version in [Step 6](<https://developer.android.com/guide/playcore/engage/workflow#switch-to-prod>).

#### Background execution not allowed

While registering the broadcast intent, you may come across the following error:

```text
Background execution not allowed: receiving Intent
{ act=com.google.android.engage.action.PUBLISH_RECOMMENDATION .. }
```

You need to register the broadcast receivers dynamically.

```java
class AppEngageBroadcastReceiver extends BroadcastReceiver {
// Trigger recommendation cluster publish when PUBLISH_RECOMMENDATION broadcast
// is received
}

public static void registerBroadcastReceivers(Context context) {

context = context.getApplicationContext();

// Register Recommendation Cluster Publish Intent
context.registerReceiver(new AppEngageBroadcastReceiver(),
                         new IntentFilter(com.google.android.engage.service.Intents.ACTION_PUBLISH_RECOMMENDATION,
                         com.google.android.engage.service.BroadcastReceiverPermissions.BROADCAST_REQUEST_DATA_PUBLISH_PERMISSION,
                         /*scheduler=*/null));
...

}
```

## Workflow FAQs

While integrating with the SDK, you may come across the following errors:

#### Validation errors at the app, cluster, entity level

Summaries at the app, cluster, and entity levels display a count of validation errors. These errors correspond to missing required fields or invalid values provided. Error messages show up in red beneath each relevant field. Fix all validation errors and check for correctness before sharing the APK.

#### Testing Deep links

The deep links are associated with the package name. A good way to test deep links is using the adb tool.

```bash
adb shell am start -W -a android.intent.action.VIEW -d <DEEPLINK URI> <PACKAGE NAME>
```

#### How can I calculate the impact of the integration?

The deep links are a great way to track the attribution. The deep link URLs that take users to your app can be included with additional tracking params. For example - "http://xx/deeplink?source_tag=engage".

Developers can add their own tracking params and provide attribution to calculate impact.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/faq).
