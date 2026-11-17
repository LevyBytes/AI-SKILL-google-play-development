### Verification App Questions

#### Is it mandatory to test my app with the verification app before submission?

Yes, testing your app with the verification app is essential before submitting your APK.

While we understand you might be confident in your implementation, the Engage integration has many intricate components. The verification app acts as a safety net, catching potential issues early on and saving you valuable time and effort in the long run.

Think of it as a quick checkup that helps guarantee a smooth launch and a great user experience.

By identifying and addressing any problems beforehand, you can avoid the frustration of rejections and resubmissions.

To submit your APK, you'll need to include a screenshot showing that your app has passed the verification process.

#### What are some common mistakes to watch out for during integration?

The verification app is designed to catch potential issues with your Engage integration. Here are some common mistakes that developers often encounter:

For all content types (movies, TV episodes, live streams, video clips):

- Missing Links: Make sure you provide valid platform-specific URIs (links) for your content. These links tell the system where to find your content on each platform.
- Missing Titles: Don't forget to include titles for all your content. This helps users identify what they were watching.
- Image Aspect Ratios: Verify all images associated with your content have an aspect ratio close to 16:9. This makes sure your images display correctly on different screens.

For TV Episodes:

- Complete Episode Information: Make sure to include the show title, episode number, and season number. This helps organize episodes and allows users to navigate within a series.
- Accurate Playback Position: Double-check that the last playback position is less than or equal to the total duration of the episode. This makes sure users resume from the correct spot.

For Movies:

- Accurate Playback Position: Similar to TV episodes, verify the last playback position is accurate.

For Live Streaming Videos:

- Broadcaster Information: Include the broadcaster's name for live streams.

For Video Clips:

- Creator Information: Specify the creator of the video clip.

Remember: The verification app will flag these issues, allowing you to fix them before submitting your app. This saves you time and ensures a smoother experience for your users.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/faq).
