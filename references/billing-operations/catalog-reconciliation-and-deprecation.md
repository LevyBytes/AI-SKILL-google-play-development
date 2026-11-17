### Catalog reconciliation

Whether you choose to update your Google Play catalog every time your backend's catalog changes or periodically, if you have a catalog management system or a database outside of Google Play's catalog there could be situations where it falls out of sync with the catalog on your apps configuration on Play. This could be due to emergency manual catalog changes in the Console, an outage on your catalog management system or maybe if you lost your latest data.

You can build a catalog reconciliation process to avoid a prolonged discrepancy window.

#### Diff system consideration

We recommend building a diff system to detect inconsistencies and reconcile the two systems. Here are some things to consider when building a diff system to help keep your catalogs in sync:

- **Understand the data models:** The first step is to understand the data models of the developer CMS and the Google Play Developer API. This includes knowing the different types of data that are stored in each system, and how the different data elements map to each other.
- **Define the diff rules:** Once you understand the data models, you need to define the diff rules. These rules will determine how the data in the two systems are compared. For example, you may want to match product IDs and compare key attributes of the subscription and its associated base plans and offers.
- **Implement a diff algorithm:** Once you have defined the diff rules, you need to implement the diff algorithm. This algorithm will take the data from the two systems and compare it according to the rules you have defined. To get the catalog data from Google Play, you can use the [`monetization.onetimeproducts.list`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/list>), [`monetization.onetimeproducts.batchGet`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/batchGet>), [`inappproducts.list`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/list>), [`inappproducts.batchGet`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/batchGet>), [`monetization.subscriptions.list`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/list>) and [`monetization.subscriptions.batchGet`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/batchGet>) methods.
- **Generate diff reports:** The diff algorithm will generate a diff report. This report will show the differences between both systems.
- **Reconcile differences:** Once you have generated the diff report, you need to resolve the differences. This may involve updating the data in your CMS, or it may involve updating the data on Google Play's side using the Developer API catalog management endpoints, depending on how you normally update your catalog. To reconcile out of sync products, use the update endpoints as described in the Product updates section.

### Product deprecation

The Google Play Developer API provides the following methods to assist you in deprecating your products:

For one-time products:

- [`monetization.onetimeproducts.delete`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/delete>)
- [`monetization.onetimeproducts.batchDelete`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts/batchDelete>)
- [`inappproducts.delete`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/delete>)
- [`inappproducts.batchDelete`](<https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts/batchDelete>)

For subscription products:

- [`monetization.subscriptions.delete`](<https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.subscriptions/delete>) for subscriptions. A subscription cannot be removed once at least one base plan has been activated.

Deprecating a product might be necessary in various scenarios, such as:

- Creation by mistake.
- Discontinuing a feature or service.

We recommend incorporating product deprecation into your catalog management strategy.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/manage-catalog).
