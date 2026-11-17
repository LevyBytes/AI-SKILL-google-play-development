## In-app messaging

If you've enabled in-app messaging with [`InAppMessageCategoryId.TRANSACTIONAL`](<https://developer.android.com/reference/com/android/billingclient/api/InAppMessageParams.InAppMessageCategoryId#TRANSACTIONAL>), Google Play will show a message to users when there is a payment issue or an outstanding opt-in price increase.

![Snackbar notifying the user to fix their payment](<https://developer.android.com/static/images/google/play/billing/subscriptions-in-app-messaging-snackbar.png>)

**Figure 20.** Snackbar notifying the user to fix their payment.

We recommend that you call this API whenever the user opens the app to determine whether the message should be shown.

If the user successfully recovered their subscription or confirmed the price increase, you will receive a response code of [`SUBSCRIPTION_STATUS_UPDATED`](<https://developer.android.com/reference/com/android/billingclient/api/InAppMessageResult.InAppMessageResponseCode#SUBSCRIPTION_STATUS_UPDATED>) along with a purchase token. You should then use this purchase token to call the Google Play Developer API and refresh the subscription status in your app.

### Integrate in-app messaging

To show in-app messaging to user, use [`BillingClient.showInAppMessages()`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#showInAppMessages>).

Here is an example of triggering the in-app messaging flow:

**Kotlin**

```kotlin
val inAppMessageParams = InAppMessageParams.newBuilder()
    .addInAppMessageCategoryToShow(InAppMessageCategoryId.TRANSACTIONAL)
    .build()

// Note: To display the in-app message, PBL requires an activity instance that
// can provide a valid window token. This token is necessary for the Play Store
// to display the message overlay correctly on top of the application's window.
// The passed Activity must be in a state where its window is created and
// attached to the WindowManager.
billingClient.showInAppMessages(
    activity,
    inAppMessageParams,
    object : InAppMessageResponseListener {
        override fun onInAppMessageResponse(inAppMessageResult: InAppMessageResult) {
            if (inAppMessageResult.responseCode == InAppMessageResponseCode.NO_ACTION_NEEDED) {
                // The flow has finished and there is no action needed from developers.
            } else if (inAppMessageResult.responseCode
                == InAppMessageResponseCode.SUBSCRIPTION_STATUS_UPDATED
            ) {
                // The subscription status changed. For example, a subscription
                // is recovered from a suspended state, or a user confirms a
                // price increase. Developers should expect the purchase
                // token to be returned with this response code and use
                // the purchase token with the Google Play Developer API.
            }
        }
    }
)
```

**Java**

```java
InAppMessageParams inAppMessageParams = InAppMessageParams.newBuilder()
        .addInAppMessageCategoryToShow(InAppMessageCategoryId.TRANSACTIONAL)
        .build();

// Note: To display the in-app message, PBL requires an activity instance that
// can provide a valid window token. This token is necessary for the Play Store
// to display the message overlay correctly on top of the application's window.
// The passed Activity must be in a state where its window is created and
// attached to the WindowManager.
billingClient.showInAppMessages(activity,
        inAppMessageParams,
        new InAppMessageResponseListener() {
            @Override
            public void onInAppMessageResponse(InAppMessageResult inAppMessageResult) {
                if (inAppMessageResult.responseCode
                        == InAppMessageResponseCode.NO_ACTION_NEEDED) {
                    // The flow has finished and there is no action needed from developers.
                } else if (inAppMessageResult.responseCode
                        == InAppMessageResponseCode.SUBSCRIPTION_STATUS_UPDATED) {
                    // The subscription status changed. For example, a subscription
                    // is recovered from a suspended state, or a user confirms a
                    // price increase. Developers should expect the purchase
                    // token to be returned with this response code and use
                    // the purchase token with the Google Play Developer API.
                }
            }
        });
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/subscriptions).
