This guide contains instructions for developers to share app subscription and entitlement data with Google TV using [Engage SDK](<https://developer.android.com/guide/playcore/engage>). Users can find content they are entitled to and enable Google TV to deliver highly relevant content recommendations to users, directly within Google TV experiences on TV, mobile, and tablet.

## Prerequisites

> **Important:** [Express interest in developing with Engage](<http://g.co/tv/vda>).

Onboarding the media actions feed is required before you can use the device entitlement API. If you haven't already done so, complete the [media actions feed](<https://developers.google.com/actions/media>) onboarding process.

## Pre-work

Complete the [Pre-work](<https://developer.android.com/guide/playcore/engage/tv/getting-started#pre-work>) instructions in the Getting Started guide.

1. Publish subscription information on the following events:

   1. User logs in to your app.
   2. User switches between profiles (if profiles are supported).
   3. User purchases a new subscription.
   4. User upgrades an existing subscription.
   5. User subscription expires.

## Integration

This section provides the necessary code examples and instructions for implementing `SubscriptionEntity` to manage various subscription types.

### Common tier subscription

For users with basic subscriptions to media provider services, for example, a service that has one subscription tier that grants access to all the paid content, provide these essential details:

1. `SubscriptionType`: Clearly indicate the specific subscription plan the user has.

   - `SUBSCRIPTION_TYPE_ACTIVE`: User has an active paid subscription.
   - `SUBSCRIPTION_TYPE_ACTIVE_TRIAL`: User has a trial subscription.
   - `SUBSCRIPTION_TYPE_INACTIVE`: User has an account but no active subscription or trial.

   > **Important:** Only users with `SUBSCRIPTION_TYPE_ACTIVE` or `SUBSCRIPTION_TYPE_ACTIVE_TRIAL` are eligible for personalized content recommendations based on their subscription.
2. `ExpirationTimeMillis`: Optional time in milliseconds. Specify when the subscription is set to expire.
3. `ProviderPackageName`: Specify the package name of the app that handles the subscription.

Example for the sample media provider feed.

[Complete json example: Common tier subscription](<https://developer.android.com/guide/playcore/engage/tv/entitlements#common-tier>).

The following example creates a `SubscriptionEntity` for a user:

[Complete kotlin example: Common tier subscription](<https://developer.android.com/guide/playcore/engage/tv/entitlements#common-tier>).

### Premium subscription

If app offer multi-tiered premium subscription packages, which includes expanded content or features beyond the common tier, represent this by adding one or more entitlements to Subscription.

This entitlement has the following fields:

1. `Identifier`: Required identifier string for this entitlement. This must match one of the [entitlement identifiers](<https://developers.google.com/actions/media/concepts/access-requirements#entitlement-identifier>) (note that this isn't the ID field) provided in the media provider's feed published to Google TV.
2. `Name`: This is auxiliary information and is used for entitlement matching. While optional, providing a human readable entitlement name enhances understanding of user entitlements for both developers and support teams. For example: Sling Orange.
3. `ExpirationTimeMillis`: Optionally specify the expiration time in milliseconds for this entitlement, if it differs from the subscription expiration time. By default, the entitlement will expire with the expiry of subscription.

For the following sample media provider feed snippet:

[Complete json example: Premium subscription](<https://developer.android.com/guide/playcore/engage/tv/entitlements#premium-subscription>).

The following example creates a `SubscriptionEntity` for a subscribed user:

[Complete kotlin example: Premium subscription](<https://developer.android.com/guide/playcore/engage/tv/entitlements#premium-subscription>).

[Complete kotlin example: Premium subscription](<https://developer.android.com/guide/playcore/engage/tv/entitlements#premium-subscription>).

### Subscription for linked service package

While subscriptions typically belong to the originating app's media provider, a subscription can be attributed to a linked service package by specifying the linked service package name within the subscription.

Following code sample demonstrate how to create user subscription.

[Complete kotlin example: Subscription for linked service package](<https://developer.android.com/guide/playcore/engage/tv/entitlements#subscription>).

In addition, if the user has another subscription to a subsidiary service, add another subscription and set the linked service package name accordingly.

[Complete kotlin example: Subscription for linked service package](<https://developer.android.com/guide/playcore/engage/tv/entitlements#subscription>).

Optionally, add entitlements to a linked service subscription too.

Adapted and reorganized from [Android Developers](https://developer.android.com/guide/playcore/engage/tv/entitlements).
