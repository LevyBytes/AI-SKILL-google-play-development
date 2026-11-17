## Configure Real-time developer notifications

Real-time developer notifications (RTDN) is a mechanism to receive notifications from Google whenever there is a change in a user's entitlement within your app. RTDN uses [Google Cloud Pub/Sub](<https://cloud.google.com/pubsub/docs/overview>), which lets you receive data that is either pushed to a URL that you set or is polled using a [client library](<https://cloud.google.com/pubsub/docs/reference/libraries>). These notifications let you react immediately to subscription state changes, avoiding the need to poll the Google Play Developer API. Note that inefficient use of the Google Play Developer API can lead to API quota restrictions.

> **Note:** You must call the [Google Play Developer API](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get>) after receiving Real-time developer notifications to get the complete status and update your own backend state. These notifications tell you only that the purchase state changed. They do not give you complete information about the purchase.

[Cloud Pub/Sub](<https://cloud.google.com/pubsub/>) is a fully-managed real-time messaging service that you can use to send and receive messages between independent applications. Google Play uses Cloud Pub/Sub to publish push notifications on topics to which you subscribe.

To receive notifications, you need to create a backend server to consume the messages sent to your topic. Your server can then consume these messages by responding to HTTPS requests to a registered endpoint or by using the [Cloud Pub/Sub Client Libraries](<https://cloud.google.com/pubsub/docs/reference/libraries>). These libraries are available in a variety of languages. More information can also be found in the [Create a Pub/Sub subscription](<https://developer.android.com/google/play/billing/getting-ready?hl=en#create-sub>) section in this document.

### Determine pricing and quotas

For details on pricing and quotas, refer to [pricing](<https://cloud.google.com/pubsub/pricing>) and [quotas](<https://cloud.google.com/pubsub/quotas>).

#### Estimate data usage

The data portion of the subscription notification is approximately 1KB of data per request. Each publish and pull requires a separate request, or approximately 2KB of data per notification. The number of notifications per month depends on your billing cycle and your users' behavior. You should expect *at least* one notification for each user during a billing cycle.

### Setup Cloud Pub/Sub

To enable Real-time developer notifications, you must first set up Cloud Pub/Sub using your own Google Cloud project and then enable the notifications for your app.

To use Cloud Pub/Sub, you must have a Google Cloud project with the Cloud Pub/Sub API enabled. If you are not familiar with Google Cloud and Cloud Pub/Sub, see the [Quickstart guide](<https://cloud.google.com/pubsub/docs/quickstart-console>).

> **Note:** You must configure Real-time developer notifications for *each* Android app separately. This means that you can choose to use the same Google Cloud project as the one used to access the Play Developer API, or you can create a new Google Cloud project for each app. If you have multiple apps, you must use the same Google Cloud Console project for the Google Play Developer API, but you can use different Google Cloud Console projects for each individual app.

### Create a topic

To start receiving notifications, you must create a [topic](<https://cloud.google.com/pubsub/architecture#the_basics_of_a_publishsubscribe_service>) to which Google Play should publish the notifications. To create a topic, follow the instructions in [Create the topic](<https://cloud.google.com/pubsub/docs/quickstart-console#create_a_topic>).

### Create a Pub/Sub subscription

To receive messages published to a topic, you must create a Pub/Sub subscription to that topic. To create a Pub/Sub subscription, do the following:

1. Read the [Cloud Pub/Sub Subscriber Guide](<https://cloud.google.com/pubsub/subscriber>) to determine whether to configure the subscription as either a *push subscription* or a *pull subscription*.

   - A push subscription allows Cloud Pub/Sub to send notifications to your secure backend by issuing HTTPS requests.
   - A pull subscription requires your secure backend server to initiate requests to the Cloud Pub/Sub server to retrieve messages.
2. Follow the instructions in [Add a subscription](<https://cloud.google.com/pubsub/docs/quickstart-console#add_a_subscription>) to create a subscription.

> **Note:** Pull subscriptions are commonly used to optimize resource utilization when a large number of messages are processed, which generally don't apply to RTDN. If you are unsure whether to start with push or pull, we suggest you use push, as it is generally easier to implement. See [Pull or push delivery](<https://cloud.google.com/pubsub/docs/subscriber#push_pull>) to help decide whether a push or pull subscription is best for your app.

### Grant publish rights on your topic

[Cloud Pub/Sub](<https://cloud.google.com/pubsub/>) requires that you grant Google Play privileges to publish notifications to your topic.

1. Open the [Google Cloud Console](<https://console.cloud.google.com/>).
2. Select your project, and then click **Pub/Sub** in the left-hand navigation.
3. Find your topic, and open the permissions details.

   ![accessing configuration for the permissions topic](<https://developer.android.com/static/images/google/play/billing/permissions-link.png>)

   **Figure 1.** Accessing configuration for the *Permissions* topic.
4. Add the service account `google-play-developer-notifications@system.gserviceaccount.com`, and grant it the role of **Pub/Sub Publisher**.

   ![adding google play service account as pub/sub publisher](<https://developer.android.com/static/images/google/play/billing/add-service-account.png>)

   **Figure 2.** Adding Google Play service account as Pub/Sub publisher.
5. Click **Save** to complete the topic set up.

   ![A configured Cloud Pub/Sub topic in Google Cloud Console.](<https://developer.android.com/static/images/google/play/billing/configured-topic.png>)

   **Figure 3.** A configured topic.

> **Note:** If your organization's [domain restricted sharing](<https://cloud.google.com/resource-manager/docs/organization-policy/domain-restricted-sharing#how-drs-works>) configuration prevents you from granting publish permissions, you must [add an exception](<https://cloud.google.com/resource-manager/docs/organization-policy/restricting-domains#configure-exceptions>) for the Google Play service account.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/getting-ready).
