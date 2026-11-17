## Catalog management implementation

Developers use the Google Play Developer API product publishing endpoints to keep their catalog synchronized between their backend and Google Play. Making sure your Google Play catalog is always up to date with your backend's catalog latest information has advantages to create a better user experience. For example:

- You will be able to consult the entire list of available offers, and manage offer and base plan tags to influence your own eligibility and offer surfacing logic.
- You can check the different price points and product details users are seeing across platforms, and make sure they are consistent.
- You will have product details at hand in your backend when processing new purchases, without the need to increase latency and risk of failure by making additional calls to the Google Play Developer API during user critical flows.

There are [certain limits and considerations](<https://support.google.com/googleplay/android-developer/answer/14590082>) you should keep in mind when creating your product catalog on Google Play. Once you understand these limits and you know how you want to structure your catalog, it's time to decide on your synchronization strategy.

### Catalog synchronization strategies

The Google Play Developer API publishing endpoints allow you to make updates to your catalog as changes occur. On occasion, you might need to take a periodic updates approach, where you send a battery of changes in the same process. Each approach requires different design choices. Each synchronization strategy will fit some use cases better than others, and you might have a set of needs that calls for both, depending on the situation.

Sometimes you may want to make an update to a product the moment you are aware of a new change, for example to process an urgent product update (i.e. a wrong price needs to be corrected as soon as possible). Other times you can use a periodic background sync to ensure your backend and Play catalogs are always consistent. Read some common use cases where you might want to implement these different catalog management strategies.

**When to send updates as your local catalog changes**

Ideally, updates should happen as soon as there is any change to your backend's product catalog, to minimize discrepancies.

This type of updates is a good option when:

- You must ensure that your products are always up-to-date.
- You need to make a few changes to your products each day.
- You need to update products that are already in production and being sold.

This approach is simpler to implement, and lets you keep your catalog in sync with the least amount discrepancy window.

**When to use periodic updates**

Periodic updates are run asynchronously to the product edition on your backend, and they are a good option when:

- You don't have to ensure your products are updated on a short notice.
- You need to plan bulk updates or conciliation processes.
- You already have a Content or Catalog Management System to handle your digital products, and that updates your catalog constantly

In case of large catalogs, consider using batch methods with latency tolerant updates to achieve maximum throughput.

> **Note:** While you may send updates to your Google Play product catalog immediately upon any changes, this does not necessarily mean the changes will be immediately available to your users in-app. There may still be some latency in the process due to network or backend processing delays. Similarly, while periodic updates are performed with some delay, they can still be designed to update your catalog frequently if needed, making your changes available to users with similar latency to on demand updates. Additionally, the `latencyTolerance` field in batch methods lets you choose between optimizing for fast update propagation or higher throughput. Ultimately, the choice between these two options should be based on your specific requirements and limitations.

### Create your product catalog

If you have a large catalog to upload to Google Play, you may want to automate the initial load. This type of heavy process works best if a periodic strategy combined with latency tolerant batch methods is followed.

#### Create one-time products

For initial one-time product catalog creation, we recommend using the [monetization.onetimeproducts.batchUpdate](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/batchUpdate>) or the [`inapp_products.insert`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/insert>) method with the `allowMissing` field set to `true` and the `latencyTolerance` field set to [`PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT`](<https://developers.google.com/android-publisher/api-ref/rest/v3/ProductUpdateLatencyTolerance>). This will minimize the time it takes to create the catalog within quota limits.

#### Create subscription products

For initial subscription large catalog creation, we recommend using the [`monetization.subscriptions.batchUpdate`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/batchUpdate>) method with the `allowMissing` field set to `true` and the `latencyTolerance`field set to [`PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT`](<https://developers.google.com/android-publisher/api-ref/rest/v3/ProductUpdateLatencyTolerance>). This will minimize the time it takes to create the catalog within quota limits.

For smaller subscription catalogs the Play Developer API provides the [`monetization.subscriptions.create`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/create>) method. Alternatively you can create subscriptions using [`monetization.subscriptions.patch`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/patch>) method with the `allowMissing` parameter as described in the Product updates section.

All of the earlier methods create subscriptions along with their base plans (supplied within the Subscription object). These base plans are initially inactive. To manage base plans' status, you can use the [`monetization.subscriptions.basePlans`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans>) endpoint, including activating a base plan to make it available for purchase. Additionally, the [`monetization.subscriptions.basePlans.offers`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers>) endpoint lets you create and manage offers.

### Product updates

The following methods enable you to efficiently modify your existing products, ensuring your offerings align with your latest adjustments.

#### Update one-time products

The following methods are available to you to help update existing one-time products.

- [monetization.onetimeproducts.batchUpdate](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/batchUpdate>)
- [`inappproducts.patch`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/patch>) : The patch endpoint is used to update a resource partially. This means you can update specific fields that you specify in the request body. The patch endpoint is typically used when you only need to update a few fields of a resource.
- [`inappproducts.update`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/update>) : The update endpoint is used to update a resource in its entirety. This means that you will need to send the entire resource object in the request body. The update endpoint is typically used when you need to update all fields in a resource. When the `allowMissing` parameter is set to `true` and the supplied product ID does not already exist, the endpoint will insert the product instead of failing.
- [`inappproducts.batchUpdate`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/batchUpdate>) : This is a batch version of the update endpoint, which lets you modify multiple products with a single query. Use it together with the `latencyTolerance` field set to [`PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT`](<https://developers.google.com/android-publisher/api-ref/rest/v3/ProductUpdateLatencyTolerance>) to achieve higher throughput.

#### Update subscription products

To update existing subscriptions, you can use the [`monetization.subscriptions.patch`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/patch>) method. This method takes the following required parameters:

- `packageName`: The package name of the app that the subscription belongs to.

  - `productId`: The subscription's unique product ID.
- `regionsVersion`: The [region configuration version](<https://developers.google.com/android-publisher/api-ref/rest/v3/RegionsVersion>).

Unless you are creating a new subscription by using the `allowMissing` parameter , you must provide the `updateMask` parameter. This parameter is a comma-separated list of fields that you want to update.

For example, if you only want to update a listing of a subscription product, you would specify the `listings` field to the `updateMask` parameter.

You can use [`monetization.subscriptions.batchUpdate`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/batchUpdate>) to update multiple subscriptions at the same time. Use it together with the `latencyTolerance` field set to [`PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT`](<https://developers.google.com/android-publisher/api-ref/rest/v3/ProductUpdateLatencyTolerance>) to achieve higher throughput.

To activate, deactivate, delete base plans or to migrate subscribers to the latest base plan price versions use the [`monetization.subscriptions.basePlans`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans>) endpoint.

Additionally, you can update your base plans' offers with the [`monetization.subscriptions.basePlans.offers.patch`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions.basePlans.offers/patch>) method.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/manage-catalog).
