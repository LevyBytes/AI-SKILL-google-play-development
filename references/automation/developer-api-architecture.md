## Overview

The Google Play Console provides a suite of REST-based web service APIs that let you perform publishing, reporting, and other app-management functions directly for your app.

Not all developers need to use these developer APIs; in most cases you can continue to manage your apps directly using the Google Play Console. However, if you have a large number of APKs to manage, or have to track user purchases and subscriptions, you might find these APIs to be useful.

### What's included

The Google Play Developer APIs let you focus on designing and developing your app, while spending less time and effort managing your releases, even as you grow to new markets.

The Google Play Console includes a suite of APIs that you can use to manage your app:

- The [Publishing API](<https://developer.android.com/google/play/developer-api?hl=en#publishing>) lets you upload and publish apps, and perform other publishing-related tasks.
- The [Subscriptions and In-App Purchases API](<https://developer.android.com/google/play/developer-api?hl=en#subscriptions>) lets you manage in-app purchases and subscriptions. (This was previously known as the "Purchase Status API".)
- The [Reporting API](<https://developer.android.com/google/play/developer-api?hl=en#reporting>) lets you retrieve information about your app's quality from Android vitals.
- The [Reply to Reviews API](<https://developer.android.com/google/play/developer-api?hl=en#reviews>) lets you retrieve and reply to reviews of your app.
- The [Permissions API](<https://developer.android.com/google/play/developer-api?hl=en#permissions>) lets you automate permission management within the Play Console.
- The [Play Games Services Management API](<https://developer.android.com/games/pgs/management/management>) lets you issue REST calls to programmatically control the metadata underlying the Google Play Games Services features.
- The [Voided Purchases API](<https://developer.android.com/google/play/developer-api?hl=en#voided-purchases>) provides a list of orders that are associated with purchases that a user has voided.

### Getting started

To get started with the Google Play Developer APIs, see the [getting started](<https://developers.google.com/android-publisher/getting_started>) documentation.

## Publishing API

The [Publishing API](<https://developers.google.com/android-publisher#publishing>) lets you automate frequent tasks related to app distribution. This provides functions similar to those available to a developer through the Play Console, such as:

- Uploading new versions of an app
- Releasing apps, by assigning APKs to various [tracks](<https://developers.google.com/android-publisher/tracks>) (alpha, beta, staged rollout, or production)
- Creating and modifying Google Play Store listings, including localized text and graphics and multidevice screenshots

Those tasks are performed using the [edits](<https://developers.google.com/android-publisher/edits>) functionality, which takes a transactional approach to making changes. This lets you bundle several changes into a single draft edit, then commit the changes all at once. (None of the changes take effect until the edit is committed.)

> **Note:** Not all developers need to use this API. All the functionality provided by the API is also available through the Google Play Console. However, this API lets you integrate your app and listing update process with your existing tools, which is useful for some developers. In particular, if you have a large number of APKs to manage, or localized listings in many different locales, you may find this API invaluable.

### Best practices

- Limit the number of app updates. Don't publish alpha or beta updates more frequently than once a day (production apps should be updated even less frequently than that). Every update costs your users time and possibly money. If you update too frequently, users might start ignoring updates, or even uninstall the product.

## Subscriptions and In-App Purchases API

The [Subscriptions and In-App Purchases API](<https://developers.google.com/android-publisher#subscriptions>) lets you manage your app's catalog of in-app products and subscriptions. In addition, with the Subscriptions and In-App Purchases API, you can quickly retrieve the details of any purchase using a standard `GET` request.

In the request, you supply information about the purchase: app package name, purchase or subscription ID, and the purchase token. The server responds with a JSON object describing the associated purchase details, order status, developer payload, and other information.

You can use this API in several ways, such as:

- Reporting and reconciling individual orders.
- Verifying purchases and subscription expirations.
- Learning about canceled orders and confirming whether in-app products have been consumed, including whether they were consumed before being canceled.

> **Note:** The Subscriptions and In-App Purchases API does not use the transactional "edits" functionality used by the [Publishing API](<https://developers.google.com/android-publisher#publishing>). Methods for the [Inappproducts](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts>) and [Purchases.subscriptions](<https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions>) resources take effect immediately. Each resource's API reference page notes specifically whether the methods for that resource use the "edits" model.

### Best practices

- Store subscription information on your server to avoid making unnecessary API calls. When your app needs to verify a subscription, you should rely on the cached information on your server instead of repeating the API call to Google.
- There are two scenarios in which your secure server should use the Google Play Developer API to get subscription information:

  - Your server receives a new purchase token that has not been seen before.
  - Your server receives a real-time developer notification (RTDN), which indicates that you need to use the purchase token to get the new subscription information.
- Don't poll the API for subscription status on a regular basis. For example, don't call the API daily to check each subscription.
- Since you receive an RTDN when the subscription expires or renews, you don't need to schedule an API call based on the scheduled expiry time.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/developer-api).
