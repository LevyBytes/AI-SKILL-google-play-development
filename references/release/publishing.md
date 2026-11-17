> **Important:** New apps on Google Play are required to use the [Android App Bundle](<https://developer.android.com/guide/app-bundle>). New apps larger than 200 MB are supported through [Play Feature Delivery](<https://developer.android.com/guide/app-bundle/dynamic-delivery>) or [Play Asset Delivery](<https://developer.android.com/guide/app-bundle/asset-delivery>). New and existing [TV apps must meet the App Bundle publishing requirement](<https://developer.android.com/docs/quality-guidelines/tv-app-quality#SC-E1>); check the current requirements and any applicable transition rules before release.

Publishing is the general process that makes your Android app available to users. When you publish an Android app, you do the following:

- **Prepare the app for release.**

  During the preparation step, you build a release version of your app.
- **Release the app to users.**

  During the release step, you publicize, sell, and distribute the release version of your app, which users can download and install on their Android-powered devices.

This page provides an overview of the process for preparing to publish your app. If you plan to publish on Google Play, read [Release with confidence](<https://developer.android.com/distribute/best-practices/launch/launch-checklist>).

If you use a Continuous Integration server, you can configure it to automate the steps outlined here. You can also configure it to push builds to your [internal test distribution channel](<https://developer.android.com/studio/publish/upload-bundle#test_with_play>).

## Prepare your app for release

Preparing your app for release is a multistep process involving the following tasks:

- **Configure your app for release.**

  At a minimum, you need to make sure that logging is disabled and removed and that your release variant has `debuggable false` for Groovy or `isDebuggable = false` for Kotlin script set. You should also [set your app's version information](<https://developer.android.com/studio/publish/versioning>).
- **Build and sign a release version of your app.**

  You can use the Gradle build files with the *release* build type to build and sign a release version of your app. For more information, see [Build and run your app](<https://developer.android.com/tools/building/building-studio>).
- **Test the release version of your app.**

  Before you distribute your app, you should thoroughly test the release version on at least one target handset device and one target tablet device. [Firebase Test Lab](<https://firebase.google.com/docs/test-lab/android/get-started>) is useful for testing across a variety of devices and configurations.
- **Update app resources for release.**

  Make sure that all app resources, such as multimedia files and graphics, are updated and included with your app or staged on the proper production servers.
- **Prepare remote servers and services that your app depends on.**

  If your app depends on external servers or services, make sure they are secure and production ready.

You might need to perform several other tasks as part of the preparation process. For example, you need to create an account on the app marketplace you want to use, if you don't already have one. You also need to create an icon for your app, and you might want to prepare an End User License Agreement (EULA) to protect yourself, your organization, and your intellectual property.

To learn how to prepare your app for release, see [Prepare for release](<https://developer.android.com/tools/publishing/preparing>) for step-by-step instructions for configuring and building a release version of your app.

When you are finished preparing your app for release, you have a signed APK file that you can distribute to users.

## Release your app to users

You can release your Android apps several ways. Typically, you release apps through an app marketplace such as [Google Play](<https://play.google.com>). You can also release apps on your own website or by sending an app directly to a user.

### Release through an app marketplace

If you want to distribute your apps to the broadest possible audience, release them through an app marketplace.

Google Play is the premier marketplace for Android apps and is particularly useful if you want to distribute your apps to a large global audience. However, you can distribute your apps through any app marketplace, and you can use multiple marketplaces.

#### Release your apps on Google Play

[Google Play](<https://play.google.com>) is a robust publishing platform that helps you publicize, sell, and distribute your Android apps to users around the world. When you release your apps through Google Play, you have access to a suite of developer tools that let you analyze your sales, identify market trends, and control who your apps are being distributed to.

Google Play also gives you access to several revenue-enhancing features such as [in-app billing](<https://developer.android.com/google/play/billing>) and [app licensing](<https://developer.android.com/google/play/licensing>). The rich array of tools and features, coupled with numerous end-user community features, makes Google Play the premier marketplace for selling and buying Android apps.

[Releasing your app on Google Play](<https://developer.android.com/distribute/googleplay>) is a simple process that involves three basic steps:

- **Prepare promotional materials.**

  To fully leverage the marketing and publicity capabilities of Google Play, you need to create promotional materials for your app such as screenshots, videos, graphics, and promotional text.
- **Configure options and uploading assets.**

  Google Play lets you target your app to a worldwide pool of users and devices. By configuring various Google Play settings, you can choose the countries you want to reach, the listing languages you want to use, and the price you want to charge in each country.

  You can also configure listing details such as the app type, category, and content rating. When you are done configuring options, you can upload your promotional materials and your app as a draft app.
- **Publish the release version of your app.**

  If you are satisfied that your publishing settings are correctly configured and your uploaded app is ready to be released to the public, click **Publish**. Once it has passed Google Play review, your app will be live and available for download around the world.

For more information, see [How Google Play works](<https://developer.android.com/distribute/googleplay>).

Adapted and reorganized from [Android Developers](https://developer.android.com/studio/publish).
