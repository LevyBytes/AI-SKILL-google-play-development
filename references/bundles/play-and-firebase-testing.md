## Test your app bundle on Play

While the other testing strategies described on this page don't require you to upload your app to Play, testing using the Play Console provides the most accurate representation of the user experience. Whether you want to share your app with your internal stakeholders, your internal QA team, a closed group of alpha testers, or a wider audience of beta testers, the Play Console provides you with several testing strategies.

Use the Play Console to test your app for the following reasons:

- You want the most accurate representation of the user experience of downloading your app and, optionally, installing features on demand.
- You want to provide easy access to a group of testers.
- You want to scope tests to QA, alpha, and beta testers.
- You want to access a history of app uploads that you can test on a device. For example, if you want to compare versions for performance regressions.

### Quickly share your app with a URL

While the Play Console test tracks provide a method of progressing your app through formal testing stages, sometimes you want to quickly share your app with trusted testers over less formal channels, such as email or a text message.

By uploading your app bundle to the Play Console [quick sharing](<https://play.google.com/console/internal-app-sharing/>) page, you can generate a URL that you can easily share with others. Sharing your app this way provides these benefits:

- Authorize anyone on your team to upload test builds, without giving them access to your app in Play Console.
- Testers get access only to the specific test version of your app that was shared with them.
- Test builds can be signed with any key or not signed at all, so uploaders also don't need access to your production or upload key.
- Version codes don't need to be unique, so you can reuse an existing version code and don't need to increment it to upload.
- Test custom delivery options, such as downloading features on demand and [in-app updates](<https://developer.android.com/guide/playcore/in-app-updates#internal-app-sharing>).
- Capture important data and logs by sharing a debuggable version of your app.

When users click the URL from their Android-powered device, the device automatically opens the Google Play Store to download the test version of your app. To get started, and learn more about the capabilities and restrictions of this testing strategy, see [Share your app with a URL](<https://support.google.com/googleplay/android-developer/answer/9303479>) or watch the following video.

### Download historical versions of your app

You and your testers can also download historical versions of your app that you've uploaded to a production or test track. This can be useful if, for example, you want to quickly test an earlier version of your app to check for performance regressions.

Visit the Play Console **Latest releases and bundles** page and navigate to the download tab of any version you want to download to copy the install link. Alternatively, if you know the package name and version code for the version of your app you want to test, simply visit the following link from your test device:

```text

https://play.google.com/apps/test/package-name/version-code
```

> **Note:** Only authorized users can access historical versions of your app. You can configure the set of authorized users in the Play Console on the quick sharing access tab.

### Upload your app to a test track

When you upload your app and create a release in the Play Console, you can progress your release through multiple testing stages before pushing to production:

- **Internal test:** Create an internal test release to quickly distribute your app for internal testing and quality assurance checks.
- **Closed:** Create a closed release to test pre-release versions of your app with a larger set of testers. Once you've tested with a smaller group of employees or trusted users, you can expand your test to an open release. On your App releases page, an Alpha track will be available as your initial closed test. If needed, you can also create and name additional closed tracks.
- **Open:** Create an open release after you've tested a closed release. Your open release can include a wider range of users for testing, before your app goes live in production.

Progressing your app through each of these testing stages lets you open your app to wider audiences of testers before releasing your app to production. For more information about Play Console test tracks, see [Set up an open, closed, or internal test](<https://support.google.com/googleplay/android-developer/answer/3131213>).

### Use pre-launch reports to identify issues

When you upload an APK or app bundle to the open or closed track, you can identify issues for a wide range of devices running different versions of Android.

The pre-launch report on your Play Console helps you identify potential issues with the following:

- Stability
- Android compatibility
- Performance
- Accessibility
- Security vulnerabilities

After you upload your app bundle, test devices automatically launch and crawl your app for several minutes. The crawl performs basic actions every few seconds on your app, such as typing, tapping, and swiping.

After tests are complete, your results will be available in the **pre-launch report** section of your Play Console. To learn more, see the Play Console help topic about how to [Use pre-launch reports to identify issues](<https://support.google.com/googleplay/android-developer/answer/7002270>).

### Browse and download APKs for specific device configurations

When you upload your app bundle, the Play Console automatically generates split APKs and multi-APKs for all device configurations your app supports. In the Play Console, you can use the **Latest releases and bundles** to see all APK artifacts that Google Play generates, inspect data such as supported devices and your app's delivery configuration, and download the generated APKs to deploy and test locally.

To learn more, read the Play Console help topic about [Reviewing your app bundle details](<https://support.google.com/googleplay/android-developer/answer/9006925#review>).

## Test your app bundle with Firebase App Distribution

[Firebase App Distribution](<https://firebase.google.com/products/app-distribution>) lets you distribute pre-release versions of your app to trusted testers so you can get valuable feedback before launch.

App Distribution lets you manage all of your pre-release builds in a central hub, and it gives you the flexibility to distribute these builds right from the console or using the command-line tools that are already part of your workflow.

There are a few steps you need to take to enable your project for Firebase App Distribution. Check out the [Before you begin](<https://firebase.google.com/docs/app-distribution/android/distribute-console?apptype=aab#before_you_begin>) section of the Firebase documentation. After you've set up your project, choose how you want to integrate App Distribution with your workflow:

- [Using the command line](<https://firebase.google.com/docs/app-distribution/android/distribute-cli?apptype=aab>)
- [Using Gradle](<https://firebase.google.com/docs/app-distribution/android/distribute-gradle?apptype=aab>)
- [Using fastlane](<https://firebase.google.com/docs/app-distribution/android/distribute-fastlane?apptype=aab>)

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/app-bundle/test).
