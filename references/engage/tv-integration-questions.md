## Engage for TV 2.0 FAQs

### General Questions

#### What is Engage?

Engage takes the "pick up where you left off" experience to the next level! It's a significant upgrade that allows viewers to seamlessly resume their content across a wider range of devices. Imagine starting a movie on your Google TV and then effortlessly continuing it on your phone during your commute – that's the power of Engage.

This new system is designed to boost viewer engagement and retention by providing a smooth, frictionless experience across the entire Google ecosystem.

#### Is Video Discovery API the same as Engage?

Yes, they are the same. The Engage SDK is a library that includes support for the continue watching row. Engage supports more content entity types than video, which is why the integration is no longer named "Video Discovery".

#### What are the benefits of using Engage?

Answer: Engage makes it easier than ever for viewers to pick up where they left off on your content, no matter what device they're using. Here's how it works:

- Seamless experience across Google: Start watching on your Google TV, and continue seamlessly on your Android phone, iPhone, or Android tablet. It even works on devices where you haven't installed the app yet!
- Increased engagement and retention: Engage helps bring users back to your app, even on new devices. By letting users resume their favorite shows, you increase the chances they'll keep watching.
- Wider reach: Beyond Google TV, Engage works across other Android media experiences, like Play Collections and other Google media apps.
- Backward compatible: If you're already using the older "[Watch Next](<https://developer.android.com/training/tv/discovery/watch-next-add-programs>)" feature, no problem! Engage is backward compatible, so your existing integration will still work.

Important Note: All new Continue Watching integrations must use Engage. The older "Cross Device Play Next" system is being phased out.

#### What surfaces support Engage?

1. Google TV
2. Android TV (on-device only but supports Engage SDK)
3. Google TV Android mobile app
4. Google TV iOS mobile app
5. Play Collections
6. Google entertainment space
7. iOS devices (with REST API integration).

#### Is Engage SDK for Continue Watching?

Yes, the Engage SDK supports content for the continue watching row. It is required to integrate with Engage.

#### Is Engage available for everyone?

Engage is being rolled out in phases.

- Early Access: We're initially granting access to a select group of partners through an Early Access Program (EAP).
- Expanding Access: We're working hard to make Engage available to all developers soon.

For a smooth and successful launch, we have safeguards in place to manage the rollout. This involves both an allowlist on the Engage side and a separate check within the Engage SDK. Whether you are an EAP partner or wants to be onboard soon, please contact us so that we can set up the access permissions before you begin with Engage SDK integration.

#### Is there a recommended image size we should provide?

Image requirements have been updated in the [Create Entities](<https://developer.android.com/guide/playcore/engage/watch#image-specs>) section.

#### With this new API documentation, will the Continue Watching data pulled by the Google server from the client and will it be reflected in all the devices?

The new API offers significant improvements for content on the continue watching row, including:

- **Seamless experience across Google TVs:** Users can start watching on one Google TV and resume on any other Google TV logged in with the same account. This feature also works with older Android TV versions.
- **Mobile app integration:** Content from Engage is surfaced on the Google TV mobile app for Android and iOS, allowing users to seamlessly switch between their TV and mobile devices.
- **Enhanced user retention:** Even on devices without the app installed or where the user isn't logged in, content in the continue watching row encourages users to re-engage with your app, boosting retention.
- **Expansion to other platforms:** Engage extends to other Google media platforms like Android, Play Collections, tablets, and other Google media apps & surfaces on Android, maximizing user engagement across devices.

#### What is the limit on the number of entities I can publish to the Continuation cluster?

Each developer partner is limited to a maximum of 5 entities in the Continuation cluster. This limit is for fair distribution of content on the "continue watching" row on Google TV, which is a shared space for multiple media providers.

#### What happens if I try to publish more than 5 entities?

Engage SDK will reject your publish request if it exceeds the 5-entity limit. You'll need to reduce the number of entities in your request to successfully publish. You should only include the entities where the users have left off watching, so in most cases, there will be only a few such entities. When there are more than 5 such entities, you could choose the more recent ones to publish.

#### Why is there a limit on the number of entities?

The continue watching row on Google TV displays content from various media providers. Limiting the number of entities per provider so that users see a diverse selection of content from all their favorite sources, promoting a fair and balanced user experience.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/faq).
