This version-specific example depends on [the library 6 catalog and client migration](library-6-catalog-and-setup.md). Check [present eligibility](version-eligibility.md) before using an older library.

### Process the purchases

Processing purchases with Google Play Billing Library 6 remains similar to previous versions.

To pull all active purchases owned by the user and query for new purchases, do the following:

- Instead of passing a `BillingClient.SkuType` value to `queryPurchasesAsync()`, pass a `QueryPurchasesParams` object that contains a `BillingClient.ProductType` value.

> **Note:** If you're migrating from version 4, note that the previously deprecated `queryPurchases` method has been removed in Play Billing Library 6. Use [`queryPurchasesAsync`](<https://developer.android.com/reference/com/android/billingclient/api/BillingClient#queryPurchasesAsync(com.android.billingclient.api.QueryPurchasesParams,%20com.android.billingclient.api.PurchasesResponseListener)>) instead as shown below.

The following example shows how your app might look before and after making these changes:

**Before**

**Kotlin**

```kotlin
billingClient.queryPurchasesAsync(BillingClient.SkuType.SUBS) {
    billingResult,
    purchaseList -> {
        // Process the result
    }
}
```

**Java**

```java
billingClient.queryPurchasesAsync(
    BillingClient.SkuType.SUBS,
    new PurchasesResponseListener() {
        public void onQueryPurchasesResponse(
                BillingResult billingResult,
                List<Purchase> purchases) {
            // process the result
        }
    }
);
```

**After**

**Kotlin**

```kotlin
billingClient.queryPurchasesAsync(
    QueryPurchasesParams.newBuilder()
        .setProductType(BillingClient.ProductType.SUBS)
        .build()
) { billingResult, purchaseList ->
    // Process the result
}
```

**Java**

```java
billingClient.queryPurchasesAsync(
    QueryPurchasesParams.newBuilder().setProductType(ProductType.SUBS).build(),
    new PurchasesResponseListener() {
        public void onQueryPurchasesResponse(
                BillingResult billingResult,
                List<Purchase> purchases) {
            // Process the result
        }
    }
);
```

The steps to manage [out of app purchases](<https://developer.android.com/google/play/billing/integrate#ooap>) and [pending transactions](<https://developer.android.com/google/play/billing/integrate#pending>) haven't changed.

Adapted and reorganized from [Android Developers](https://developer.android.com/google/play/billing/migrate-gpblv6).
