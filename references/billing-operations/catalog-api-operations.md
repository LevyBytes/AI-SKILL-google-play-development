This guide explains how to use the Google Play Developer API to create and manage a product catalog for your Play app.

To sell products in your app through Google Play's billing system you need to set up a catalog with all the products you want to make available for purchase by your users. This can be done through the Play Console, or you can automate catalog management using the Google Play Developer API. Automation can help ensure your catalog is always up-to-date, and scale to large catalogs where manual coordination is impractical. In this guide you will see how to use the [Play Developer API](<https://developers.google.com/android-publisher#subscriptions>) to create and manage a product catalog for your Play app. Review our [Getting ready](<https://developer.android.com/google/play/billing/getting-ready#dev-api>) guide for instructions on how to set up the Google Play Developer API for your backend integration.

## Catalog Management APIs

To read about the different types of product you can sell with Google Play's billing system, read [Understand in-app product types and catalog considerations](<https://support.google.com/googleplay/android-developer/answer/14590082>). Google offers two main sets of APIs for catalog management on Play, corresponding to the two main product categories:

- One-time products
- Subscription products

### One-time products

The one-time products (previously referred to as in-app products) use the [one-time product object model](<https://support.google.com/googleplay/android-developer/answer/16430488>) which lets you configure multiple purchase options and offers for your one-time products. The one-time product object model provides you greater flexibility in how you sell products, and reduces the complexity of managing them. Your existing in-app products will be migrated to the one-time product object model. For more information see [Migration of in-app products](<https://support.google.com/googleplay/android-developer/answer/16430488>).

The [`monetization.onetimeproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts>) and the [`inappproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts>) endpoints let you manage one-time products from your backend. This includes creating, updating, and deleting products, and managing prices and availability. Depending on how you handle one-time product purchases, you will model consumable products (can be bought as many times as desired) or permanent entitlements (cannot be made twice by the same user). You can decide which one-time products should be consumable or not.

> **Note:** You can continue to use the [`inappproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts>) service to manage your existing in-app products. While Google Play maintains backward compatibility for in-app products created with the inappproducts service, it's recommended to migrate them to the [one-time product model](<https://support.google.com/googleplay/android-developer/answer/16430488>).

### Subscription products

The [`monetization.subscriptions`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions>) endpoint helps you manage subscription products from your developer backend. You can do things such as create, update, and delete subscriptions, or control their regional availability and pricing. In addition to the [`monetization.subscriptions`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions>) endpoint, we also provide [`monetization.subscriptions.basePlans`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans>) and [`monetization.subscriptions.basePlans.offers`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers>) to respectively manage subscriptions' base plans and offers.

> **Note:** When configuring regional pricing, ensure you use the **parent region code** for territories that are handled as location overrides. For example, United States (US) includes territories such as Puerto Rico (PR), Guam (GU), and the US Virgin Islands (VI). Prices for these territories cannot be set independently and must be managed using the parent region's configuration.

> **Note:** The `inappproducts` API contains legacy subscription-management features because Google Play products originally shared this endpoint. You should **no longer** use it to manage subscription products. [Migrate subscription publishing integrations](<https://developer.android.com/google/play/billing/migrate-gpblv5#manage-subscription-product-catalog>) to [`monetization.subscriptions`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions>). Check the [current catalog guidance](<https://developer.android.com/google/play/billing/manage-catalog>) for the documented deprecation context.

### Batch methods

The [`onetimeproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts>), [`inappproducts`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts>), and the [`monetization.subscriptions`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions>) endpoints provide a number of batch methods that allow retrieving or managing up to 100 entities under the same app at the same time.

Batch methods, when used with enabled latency tolerance, support higher throughput and are particularly useful for large-catalog developers for initial catalog creation or catalog reconciliation.

### Update propagation latency versus throughput

After a product creation or modification request is complete, changes may not be immediately visible to end users on their devices due to network or backend processing delays. By default, all product modification requests are latency-sensitive. This means they are optimized for fast propagation through backend systems, typically reflecting on end-user devices within minutes. However, there is an hourly limit on the number of such modification requests. For cases where you need to create or update many products (for example, during initial large catalog creation), you can use batch methods with the `latencyTolerance`field set to [`PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT`](<https://developers.google.com/android-publisher/api-ref/rest/v3/ProductUpdateLatencyTolerance>). This will significantly increase update throughput. Latency-tolerant updates will take up to 24 hours to propagate to end-user devices.

### Quota configuration

There are several quota limits you should be aware of when using Play Developer API to manage your product catalog:

1. The Google Play Developer APIs are organized into categories called buckets, where each bucket has its own per-minute quota limit. For more information, see [quotas](<https://developers.google.com/android-publisher/quotas>).
2. Product modification endpoints also enforce a limit of 7,200 queries per hour. This is a single limit across both one-time products and subscriptions and across all modification requests, including creation, update, activate, delete. Batch modification method calls count as one query for this quota, regardless of the number of individual requests included or their latency sensitivity.
3. Latency sensitive modifications also have a limit of 7,200 modifications per hour. For batch methods, every nested modification request counts separately for the purpose of this quota. This quota has practical implications only for the users of batch API performing latency sensitive updates, as in other cases quota 2 will be exhausted before or at the same time as this quota.

Here are several illustrative examples to understand the quota usage of different requests:

- A single `get` request to fetch one item will consume 1 token of quota 1 and no tokens of quota 2 and 3 (as they concern only modification endpoints).
- A batch `get` request to fetch up to 100 items will also consume 1 token of quota 1 and no tokens of quota 2 and 3.
- A single `modification` request for one item will consume 1 token of quota 1 , 1 token of quota 2. If the request is latency sensitive, it will also consume 1 token of quota 3. Because quota C has the same limit as quota 2, it has no practical implications for users using only single modification methods.
- A batch `modification` request for 100 latency tolerant items will consume 1 token of quota 1, 1 token of quota 2. This quota setup should allow for ample margin to keep your catalog updated, but if your algorithm is not conscious of this quota and goes beyond this rate you may get an error per additional call.
- A batch `modification` request for 100 latency sensitive items will consume 1 token of quota 1, 1 token of quota 2, and 100 tokens of quota 3.

### Catalog Management API usage recommendations

By adhering to these guidelines, you optimize your interactions with the API, ensuring a smooth and efficient catalog management experience.

#### Monitor your usage

You should be aware of heavy usage processes. For example, at the beginning of your integration your catalog management endpoints are more likely to consume more quota to create your full initial catalog and this could potentially affect production usage of other endpoints like the purchase status API if you are close to the overall usage limit. You need to monitor your quota consumption to make sure that you are not exceeding the API quotas. There are several ways to monitor usage. For example, you can use the Google Cloud APIs quota dashboard, or any other in-house or third party API monitoring tool of your choice.

#### Optimize API quota usage

Optimizing rate consumption is highly recommended to minimize the likelihood of API errors. To implement this effectively, we recommend that you:

- Choose the right catalog management strategy. Once you understand the API quota, you need to choose the right strategy for your application to achieve your catalog management goals efficiently.
- Only make the minimum amount of calls you need to reflect your changes.
- Don't send redundant or unnecessary modification calls to the APIs. This might require you to keep a changelog in your backend catalog.
- Stay under the product modification hourly limit of 7,200 queries. You may want to build sync processes that require you to make large numbers of product modifications in a short period of time (for example, an initial catalog creation). If you expect these processes to go over the hourly limit, implement waits as necessary to slow the usage to a safe level. Consider using batch methods with latency tolerant updates to achieve higher throughput.
- Proactively prepare to scale. As your application grows, you may need to scale up your usage of the API and the various endpoints. Read [the Google Play Developer API quotas documentation](<https://developers.google.com/android-publisher/quotas>) for details on how to increase your quota when you are getting close to the maximum usage.
- Strategically schedule heavy processes. Try to schedule your heavy catalog processes around critical usage peaks, for example you can avoid running a full catalog sync during your peak sales times of the week.

#### Add quota error handling logic

No matter how efficiently you build your catalog management logic, you should make it resilient to unexpected quota limits, given that the daily quota is shared by endpoints used in independent modules of your integration. Make sure you include quota throttling errors in your error handling, and implement the appropriate waits. Every call made to Google Play Developer APIs will generate a response. In the event of a call failure, you will receive a failure response that includes an HTTP response status code and an `errors` object, providing further details about the error domain and a debug message. For example, if you surpass your daily limit, you may encounter an error similar to the following:

```json
{
  "code" : 403,
  "errors" : [ {
    "domain" : "usageLimits",
    "message" : "Daily Limit Exceeded. The quota will be reset at midnight Pacific Time (PT). You may monitor your quota usage and adjust limits in the API
  Console: https://console.developers.google.com/apis/api/androidpublisher.googleapis.com/quotas?project=xxxxxxx",
  "reason" : "dailyLimitExceeded",
  "extendedHelp" : "https://console.developers.google.com/apis/api/androidpublisher.googleapis.com/quotas?project=xxxxxx"
  } ],
}
```

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/manage-catalog).
