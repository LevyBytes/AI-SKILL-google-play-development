### Create an account profile

`AccountProfile` identifies the user. You can specify an account ID, and optionally a profile ID and locale.

```kotlin
val accountProfile = AccountProfile.Builder()
    .setAccountId("your_users_account_id")
    .setProfileId("your_users_profile_id") // Optional
    .setLocale(Locale.US.toLanguageTag())  // Optional, e.g., "en-US"
    .build()
```

An `AccountProfile` must be provided with an account ID in order for content to be synchronized between devices. See [Cross-device syncing](<https://developer.android.com/guide/playcore/engage/tv/continue-watching/client#cross-device_syncing>).

## Testing

To test your integration, download the verification app:

[Download verification app](<https://developer.android.com/guide/playcore/engage/tv/getting-started?hl=en#lightbox-trigger>)

The verification app is an Android app with capabilities to help you test your integration. It let you to check data accuracy and proper functionality by verifying published data and broadcast intents before launch.

1. Install and open the Engage Verification app.
2. If the value of `isServiceAvailable` is `false` in the verification app, click the **Toggle** button within the verification app to set it to `true`.
3. Enter the package name of your app. It automatically shows the published data.
4. Run your app and perform publishing actions, such as logging in or watching a video.
5. Verify that the data shows up in the verification app.

## Download

Before downloading, you must agree to the following terms and conditions.

Review and accept the [SDK terms and conditions](<https://developer.android.com/guide/playcore/engage/tv/getting-started>) before downloading or using the SDK.

[Download](<https://dl.google.com/developers/android/channels/verify_app_multiplatform_public_20260701.apk>)

*verify_app_multiplatform_public_20260701.apk*

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/getting-started).
