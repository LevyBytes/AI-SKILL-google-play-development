### REST API Questions

#### Is there documentation on the REST API?

Check the [current Engage documentation](<https://developer.android.com/guide/playcore/engage/faq>) for REST availability for the specific vertical and publishing workflow you intend to use. A planned release estimate does not establish that the required API is available.

### Legacy Watch Next Questions

#### Is Engage replacing the Watch Next API?

Engage will be backward compatible on all Android TV devices that support the Watch Next API. To integrate on Google TV and other surfaces that support Engage, developers should use the Engage SDK.

### Testing and Integration Questions

#### What is the difference between LastPlayBackPositionTimeMillis and duration?

LastPlayBackPositionTimeMillis should reflect the playback duration in milliseconds where the user stopped watching (e.g., 605000 ms for 10 minutes and 5 seconds). It should never be greater than the entity's total duration.

Whereas, **LastEngagementTime** is the timestamp when the user last engaged with the content.

#### What are the test cases we should perform?

The following are test cases for Google TV that our QA performs. Similar test cases can be performed on other surfaces as well.

1. Watch a video, which is longer than 20 minutes for about 5 minutes. Exit app. The video card should be displayed in the continue watching row. Note: We only display 5 cards per 3p app in CW
2. Selecting the newly appeared card in the continue watching row should continue playing the video from the right point in the video.Note: Any New or old content should resume playback from where it was left off last
3. Changing accounts on the GTV device should change the cards on the continue watching row. Only videos from the current account should show up. Sorted in recent order. 3p app profile CW will be intermixed. Note: CW for GoogleAccount2 will show 3P contents that GoogleAccount2 was engaged watching
4. Exit the app with BACK button > Verify card is displayed in the "Continue watching" row
5. Hide the video in the continue watching row, it shouldn't show again Test if hidden content stays hidden beyond 24 hours and even after the app opens after 24 hrs. Confirm hiding one item does not hide multiple items.
6. Content availability in the continue watching row with full metadata: Card image, App name, title, season episode # for TV contents
7. Check Progress displays in the progress bar
8. User watched the content until ending credits - content does not display in the continue watching row
9. Confirm no unwatched items show up in the continue watching row
10. Confirm that the CW items are arranged chronologically based on when watch activity happened and not when the app was last opened or last day
11. Confirm that episode and season details on CW card match what was watched on episodic content
12. Confirm completed (items at credits or beyond) items don't show up in the continue watching row
13. Turn off the device halfway through watching the episode/movie/show. "Turn off the device halfway through watching the episode/movie/show. Verify on turning on the device and on other TV, CW displays the right card , at the right position and progress bar"
14. Turn off the device after completely watching episode 1, verify
15. episode 1 drops and doesn't reappear in continue watching row [on second device and on turning on the test device]

    1. episode 2 (if available), should appear in continue watching row [on second device and on turning on the test device]
16. First scenario: TV1: GoogleAccount: mom, 3p account / profile: account 1 / profile_1. Watch content and verify CW data displays contents watched by 3P account_1/profile_1
17. TV2: GoogleAccount: mom. Verify CW data from the first scenario. Now login to the 3p app as a different account. 3p account / profile: account_2 / profile_2. Watch content and verify CW data displays contents watched by 3p account_2/profile_2
18. GoogleAccount: mom. New device case /3P app not installed. On a new device(FDR the device), Verify CW displays data from the last used 3P app that was used by the GoogleAccount. Note: CW row shouldn't show 3P contents if the GAIA is not yet associated with a 3P profile on other device

    1. GoogleAccount: mom. New device case /3P app installed but not logged in. On a new device(FDR the device), Verify CW displays data from the last used 3P app that was used by the GoogleAccount.
19. > **Note:** When the app is installed and logged in, the CW state would reflect the active 3P user logged into the 3P app.

    1. Note: the continue watching row shouldn't show 3P contents if the GoogleAccount is not yet associated with a 3P profile

#### We are not seeing continuation content showing up on Google TV iOS app. What happened?

You will need to send iOS deeplinks for content to appear in the continue watching row on iOS devices.

#### How often should I update content information for the continue watching row? Should I update it frequently, like every 15 seconds?

No, frequent updates are not recommended. Here's why:

- Performance Impact: Continuously sending updates puts unnecessary strain on our servers, potentially slowing down the system for everyone.
- Unnecessary Data: While a user is actively watching, their playback position changes constantly. Sending updates every few seconds creates a lot of redundant data that isn't helpful for resuming playback.

When to update content information for the continue watching row:

Focus on capturing meaningful changes in the user's viewing progress. Here are the key scenarios:

- Playback Paused or Stopped: When a user pauses or stops watching, send an update to store their current position.
- App Closed or Backgrounded: If a user exits the app or switches to another app while watching a video, send an update to save their progress.
- When user removes an item from their continue watching row within app

How to efficiently update:

Instead of timed updates, utilize events within your video player or app lifecycle to trigger updates. For example:

- `onPause`, `onStop`: When the video playback pauses or stops.
- `onAppClose`, `onAppBackgrounded`: When the app closes or moves to the background.

By following these guidelines, you'll ensure efficient use of resources while still providing a seamless experience in the continue watching row for your users.

> **Note:** Please contact [`engage-developers@google.com`](<mailto:engage-developers@google.com>) if you have any questions that are not covered here.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/faq).
