### Account and Profile Questions

#### My app uses anonymous user logins. Is AccountProfile still required for Engage?

`AccountProfile` is designed for apps that use individual user accounts. However, we understand that some apps, like yours, may rely on anonymous logins. Here's how Engage works in this scenario:

- `AccountProfile` is technically required, but you can still integrate Engage even if your app doesn't have a user account system.
- Limited to on-device use: The cross-device capabilities of Engage relies on identifying users across different devices. Since anonymous logins don't provide this, the feature will be limited to the user's current device.
- How to configure: To set this up, you'll need to disable cross-device syncing. This makes sure that continuation entries only appear on the specific device where the content was started.

In summary: While you can integrate Engage with anonymous logins, users will only be able to resume content on the same device.

#### Can I use AccountProfile with only `accountId` and no `profileId`, even when my app supports both accountId and `profileId`?

AccountProfile requires both `accountId` and `profileId` to function correctly. Here's why:

- Consistent identification: `accountId` identifies the user, while `profileId` distinguishes between different profiles within that user's account (if applicable). Providing both makes sure that Engage accurately tracks and displays content for each individual profile.
- Preventing errors: Using `accountId` and `profileId` inconsistently across different API calls can lead to unexpected behavior and errors. For example, if you include both when adding content to Engage but only use `accountId` when deleting content, the system may not be able to correctly identify and remove the intended items.

#### Is `profileId` required for Engage?

- `accountId` is required. This identifies the user across devices.
- `profileId` is crucial for a good user experience. While technically optional, `profileId` is strongly recommended if your service supports multiple profiles (like many streaming services do). Why is it so important? Because without `profileId`, the continue watching row may show content from other profiles on the same account. This can lead to a confusing and frustrating experience for your users.
- In short: Providing `profileId` makes sure that content provided to the continue watching row accurately reflects each individual's viewing history. Unless your app doesn't support the concept of profile within an account, you should provide it.

#### How does Google use the `profileId` on their side?

If the service offers different profiles to watch content, `accountId` and `profileId` would be used to associate the content watched on the device to the signed-in Google Account on the device. Google would record the ContinueWatching data against the combination of `accountId` and `profileId`. Any Google device that has that same Google Account logged in, would get the latest updated data from the same associated `accountId` and `profileId`, in its ContinueWatching row.

#### Is account linking required to implement Engage?

Account Linking is not needed. It is being deprioritized and all related use cases will be covered by the new Device Entitlements API.

### Sync Across Devices Questions

#### What does "sync across devices" mean when users give consent?

With the user's "sync across device" consent, the content they're watching will be saved to Google TV servers, letting them seamlessly pick up where they left off on any signed-in device. Without consent, their watch history remains local to the current device.

#### Can we set "sync across devices" to false?

The `setUserConsentToSyncAcrossDevices` flag controls whether a user's ContinuationCluster data is synchronized across their devices (TV, phone, tablet, etc.). If this flag is set to false, then continue watching content is only surfaced on same device.

To get the most out of our cross-device feature, we strongly advise your app to obtain user consent and set SyncAcrossDevices to true.

#### How is user consent for sharing watch history obtained on non-Android

devices? What data points are shared to 3P servers from non-Android devices?

The consent is collected at the user level (profile or account level). Once consent is obtained, the continue watching payloads based on engagement can be sent anywhere so Google can reflect the users' ubiquity resumption state across all entities that they have partial or next engagement with, on any device (without having to re-ask consent on every device or platform). Partners will send the users latest continue watching state (as per spec) associated with profile ID (that was deposited on android).

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/faq).
