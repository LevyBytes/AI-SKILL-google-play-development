### Enable Real-time developer notifications for your app

To enable Real-time developer notifications for your app, do the following:

1. Open the [Google Play Console](<https://play.google.com/console/>).
2. Select your app.
3. Go to **Monetize > Monetization setup**.
4. Go to the **Real-time developer notifications** section at the top of the page.

   ![Real-time developer notifications section in Play Console.](<https://developer.android.com/static/images/google/play/billing/rtdn-section.png>)

   **Figure 4.** Real-time developer notifications section.
5. Select **Enable real-time notifications**.
6. In the **Topic name** field, enter the full Cloud Pub/Sub topic name that you configured earlier. The topic name should be in the format of `projects/{project_id}/topics/{topic_name}` where `project_id` is the unique identifier for your project, and `topic_name` is the name of the topic created earlier.
7. Click **Send Test Message** to send a test message. Performing a test publish helps to ensure that everything is set up and configured properly. If the test publish succeeds, a message is displayed stating that the test publish was successful. If you have attached a subscription for this topic, you should receive the test message.

   For a pull subscription, go to the subscription in Cloud Console, click **View Messages**, and proceed to pull messages. You should acknowledge any message you have pulled to avoid repeated delivery by Cloud Pub/Sub. For a [push subscription](<https://cloud.google.com/pubsub/docs/push>), check if the test message is delivered to your push endpoint. A successful response code will serve as a message acknowledgement.

   If the publish fails, an error is shown. Ensure that the topic name is correct and that the `google-play-developer-notifications@system.gserviceaccount.com` service account has **Pub/Sub Publisher** access to the topic.
8. Choose which notification types you'd like to receive.

   - **Get notifications for subscriptions and all voided purchases** - receive real-time developer notifications related to subscriptions and voided purchases. You won't receive notifications for one-time product purchases.
   - **Get all notifications for subscriptions and one-time products** - receive notifications for all subscription and voided purchase events. You'll also receive one-time product purchase events, such as `ONE_TIME_PRODUCT_PURCHASED` and `ONE_TIME_PRODUCT_CANCELED`. See [One-time purchase lifecycle](<https://developer.android.com/google/play/billing/lifecycle/one-time>) to learn more about these purchase events.
9. Click **Save changes**.

### Verifying your configuration

To receive Real-time developer notifications, you should create a secure backend server to consume the messages sent to your Cloud Pub/Sub topic.

You can test your configuration by using the **Send Test Message** button in the Google Play Console as described in the previous section. If you have not configured a backend server to consume notifications, you can use the `gcloud` command line tool to verify the configuration. For instructions on processing messages using `gcloud`, see [Pull the message from the subscription](<https://cloud.google.com/pubsub/docs/quickstart-console#pull_the_message_from_the_subscription>).

## Next steps

- [Integrate the library into your app](<https://developer.android.com/google/play/billing/integrate>)

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/getting-ready).
