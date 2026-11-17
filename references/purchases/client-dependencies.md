> **Note:** Before reading this document, make sure you've read through the [Play Console Help Center documentation](<https://support.google.com/googleplay/android-developer/topic/3450769>), which describes critical purchase-related concepts, as well as how to create and configure your products for sale. In addition, be sure you've set up your Google Play configuration beforehand by following the steps in [Getting ready](<https://developer.android.com/google/play/billing/getting-ready>).

This document describes how to integrate the Google Play Billing Library into your app to start selling products.

## Life of a purchase

Here's a typical purchase flow for a one-time purchase or a subscription.

1. Show the user what they can buy.
2. Launch the purchase flow for the user to accept the purchase.
3. Verify the purchase on your server.
4. Give content to the user.
5. Acknowledge delivery of the content. For consumable products, consume the purchase so that the user can buy the item again.

Subscriptions automatically renew until they are canceled. A subscription can go through the following states:

- **Active**: User is in good standing and has access to the subscription.
- **Cancelled**: User has cancelled but still has access until expiration.
- **In grace period**: User experienced a payment issue but still has access while Google is retrying the payment method.
- **On hold**: User experienced a payment issue and no longer has access while Google is retrying the payment method.
- **Paused**: User paused their access and does not have access until they resume.
- **Expired**: User has cancelled and lost access to the subscription. The user is considered *churned* at expiration.

## Initialize a connection to Google Play

The first step to integrate with Google Play's billing system is to add the Google Play Billing Library to your app and initialize a connection.

### Add the Google Play Billing Library dependency

> **Note:** If you've followed the [Getting ready](<https://developer.android.com/google/play/billing/getting-ready>) guide, then you've already added the necessary dependencies and can continue with [client initialization](client-connection.md).

Add the Google Play Billing Library dependency to your app's `build.gradle` file as shown:

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

If you're using Kotlin, the Google Play Billing Library KTX module contains Kotlin extensions and coroutines support that enable you to write idiomatic Kotlin when using the Google Play Billing Library. To include these extensions in your project, add the following dependency to your app's `build.gradle` file as shown:

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

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/integrate).
