> **Note:** Before reading this document, make sure you've read through the [Play Console Help Center documentation](<https://support.google.com/googleplay/android-developer/topic/3450769>), which describes critical purchase-related concepts, as well as how to create and configure your products for sale.

This document lists and describes the setup steps you need to take before you can sell products in your app. At a high level, this setup includes creating a developer account, creating and configuring the products you want to sell, and enabling and configuring the APIs that you use to sell and manage your products. This document also describes how to configure Real-time developer notifications to be notified whenever the status of a product changes.

## Set up a Google Play developer account

To publish your apps and games on Google Play, use the [Google Play Console](<https://developer.android.com/distribute/console>). You also use the Google Play Console to manage your billing-related products and settings.

To access the Google Play Console, you need to [set up a Google Play Developer Account](<https://support.google.com/googleplay/android-developer/answer/6112435>).

To sell paid apps and in-app purchases on Google Play, you must also set up a profile in the [Google Payments Center](<https://pay.google.com>) and then link that profile to your Google Play developer account. To learn how to link your profile to your account, or to learn how to check if you already have a linked account and profile, see [Link a Google Play developer account to your payments profile](<https://support.google.com/googleplay/android-developer/answer/3092739>).

## Enable billing-related features in the Google Play Console

Once you've set up a developer account, you must publish a version of your app that includes the Google Play Billing Library. This step is required to enable billing-related features in the Google Play Console, such as configuring the products you want to sell.

### Add library dependency

To integrate Google Play's billing system, first add a dependency to the Google Play Billing Library in your app. This library provides access to Android APIs that connect you to Google Play. From there, you can access purchase information, query for updates about purchases, prompt a user to make new purchases, and more.

The Google Play Billing Library is available from [Google's Maven repository](<https://developer.android.com/build/remote-repositories#google-maven>). Add the dependency to your app's `build.gradle` file as shown:

**Groovy**

```groovy
dependencies {
    def billing_version = "9.1.0"

    implementation "com.android.billingclient:billing:$billing_version"
}
```

**Kotlin**

```kotlin
dependencies {
    val billing_version = "9.1.0"

    implementation("com.android.billingclient:billing:$billing_version")
}
```

If you're using Kotlin, the Play Billing Library KTX module contains Kotlin extensions and coroutines support that enable you to write idiomatic Kotlin when using Google Play's billing system. To include these extensions in your project, add the following dependency to your app's `build.gradle` file as shown:

**Groovy**

```groovy
dependencies {
    def billing_version = "9.1.0"

    implementation "com.android.billingclient:billing-ktx:$billing_version"
}
```

**Kotlin**

```kotlin
dependencies {
    val billing_version = "9.1.0"

    implementation("com.android.billingclient:billing-ktx:$billing_version")
}
```

The Kotlin code examples found on this page leverage KTX where possible.

### Upload your app

Once you've added the library to your app, build and publish your app. For this step, [create your app](<https://support.google.com/googleplay/android-developer/answer/113469>) and then publish to any track, including the [internal test track](<https://support.google.com/googleplay/android-developer/answer/3131213>).

> **Note:** Purchases made in apps published to the internal test track or in the draft stage are subject to [spend limits](<https://developer.android.com/google/play/billing/test#spend-limits>).

## Create and configure your products

After enabling Google Play Billing features for your app, you need to configure products to sell.

The steps to create one-time products and subscriptions are similar. For each product, you need to provide a unique product ID, a title, a description, and pricing information. Subscriptions have additional required information, such as selecting whether it's an auto-renewing or prepaid renewal type for the base plan.

The Google Play Console provides a web interface that you can use to manage your products.

- To create and configure one-time products, see [Create a managed product](<https://support.google.com/googleplay/android-developer/answer/1153481>). Note that the Google Play Console refers to one-time products as *managed products*.
- To create and configure subscriptions, see [Create a subscription](<https://support.google.com/googleplay/android-developer/answer/140504>).

As an alternative to the web interface, you can also manage your products by using the [`inappproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts>) REST resource for in-app products and the [`monetization.subscriptions`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions>) REST resource for subscription products in the Google Play Developer API.

## Configure the Google Play Developer API

The Google Play Developer API is a server-to-server API that complements the Google Play Billing Library on Android. This API provides functionality not available in the Google Play Billing Library, such as securely verifying purchases and issuing refunds to your users.

As part of integrating Google Play's billing system into your app, you must configure access to the Google Play Developer API through the Google Play Console. For instructions, see [Getting Started with Google Play Developer API](<https://developers.google.com/android-publisher/getting_started>).

Once you've configured access to the Google Play Developer API, be sure that you've granted the **View financial data** permission, which is needed to access billing-related functionality. For information on best practices, along with more information on configuring permissions, see [Add developer account users and manage permissions](<https://support.google.com/googleplay/android-developer/answer/2528691>).

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/getting-ready).
