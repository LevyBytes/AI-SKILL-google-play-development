### Testing

This section provides a step-by-step guide for testing subscription implementation. Verify data accuracy and proper functionality before launch.

#### Publish Integration checklist

1. Publishing should happen when the app is in the foreground and user the actively interacting with it.
2. Publish when:

   - User logs in for the first time.
   - User changes profile (if profiles are supported).
   - User purchases new subscription.
   - User upgrades subscription.
   - User subscription expires.
3. Check if app is correctly calling `isServiceAvailable` and `publishClusters` APIs in logcat, on the publishing events.
4. Verify that data is visible in the verification app. The verification app should display subscription as a separate row. When the publish API is invoked, the data should show up in the verification app.

   > **Important:** Verify that the [Engage Service Flag](<https://developer.android.com/guide/playcore/engage/workflow#switch-to-prod>) is **not** set to production.
5. Go to app and perform each of the following actions:

   - Sign in.
   - Switch between profiles (if supported).
   - Purchase a new subscription.
   - Upgrade an existing subscription.
   - Expire the subscription.

#### Verify integration

To test your integration, use the [verification app](<https://developer.android.com/guide/playcore/engage/tv/getting-started#testing>).

1. For each of the events, check if app has invoked the `publishSubscription` API. Verify the published data in the verification app. **Verify that everything is green in verification app**
2. If all the entity's information is correct, it shows an "All Good" green check in all entities.

   ![Verification App Success Screenshot](<https://developer.android.com/static/images/guide/playcore/engage/ett-va-success.png>)

   **Figure 1.** Successful subscription
3. Problems are also highlighted in verification app

   ![Verification App Error Screenshot](<https://developer.android.com/static/images/guide/playcore/engage/ett-va-error.png>)

   **Figure 2.**Subscription unsuccessful
4. To see the problems in the bundled subscription, use the TV remote to focus on that specific bundled subscription and click to see the problems. You might have to first focus on the row and move to the right to find Bundled Subscription card. The problems are highlighted as red as shown in Fig 3. Also, use the remote to move down to see problems in the entitlements within bundled subscription

   ![Verification App Error Details Screenshot](<https://developer.android.com/static/images/guide/playcore/engage/ett-va-error-details.png>)

   **Figure 3.**Subscription Errors
5. To see the problems in the entitlement, use the TV remote to focus on that specific entitlement and click to see the problems. The problems are highlighted as red.

   ![Verification App Error Screenshot](<https://developer.android.com/static/images/guide/playcore/engage/ett-va-details.png>)

   **Figure 4.**Subscription Error Details

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/entitlements).
